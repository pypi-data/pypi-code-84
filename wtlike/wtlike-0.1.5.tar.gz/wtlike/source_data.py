# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_source_data.ipynb (unless otherwise specified).

__all__ = ['contiguous_bins', 'time_bin_edges', 'binned_exposure', 'SourceData']

# Cell
import os, sys
import numpy as np
import pandas as pd
import healpy
import pickle
from pathlib import Path

from .config import *
from .data_man import *
from .effective_area import *
from .weights import *

# Cell
def _exposure(config,  livetime, pcosine):
    """return exposure calculated for each pair in livetime and cosines arrays

    uses effective area
    """
    from scipy.integrate import simps
    assert len(livetime)==len(pcosine), 'expect equal-length arrays'

    # get a set of energies and associated weights from a trial spectrum

    emin,emax = config.energy_range
    loge1=np.log10(emin); loge2=np.log10(emax)

    edom=np.logspace(loge1, loge2, int((loge2-loge1)*config.bins_per_decade+1))
    if config.verbose>1:
        print(f'Calculate exposure using the energy domain'\
              f' {emin}-{emax} {config.bins_per_decade} bins/decade' )
    base_spectrum = eval(config.base_spectrum) #lambda E: (E/1000)**-2.1
    assert base_spectrum(1000)==1.
    wts = base_spectrum(edom)

    # effectivee area function from
    ea = EffectiveArea(file_path=config.wtlike_data/'aeff_files')

    # a table of the weighted for each pair in livetime and pcosine arrays
    rvals = np.empty([len(wts),len(pcosine)])
    for i,(en,wt) in enumerate(zip(edom,wts)):
        faeff,baeff = ea([en],pcosine)
        rvals[i] = (faeff+baeff)*wt

    aeff = simps(rvals,edom,axis=0)/simps(wts,edom)
    return (aeff*livetime)

def _calculate_exposure_for_source(config, source, week):
    """
    Calcualate the exposure for the source during the given week
    """
    df = week['sc_data']

    # calculate cosines with respect to sky direction
    sc = source
    ra_r,dec_r = np.radians(sc.ra), np.radians(sc.dec)
    sdec, cdec = np.sin(dec_r), np.cos(dec_r)

    def cosines( ra2, dec2):
        ra2_r =  np.radians(ra2.values)
        dec2_r = np.radians(dec2.values)
        return np.cos(dec2_r)*cdec*np.cos(ra_r-ra2_r) + np.sin(dec2_r)*sdec

    pcosines = cosines(df.ra_scz,    df.dec_scz)
    zcosines = cosines(df.ra_zenith, df.dec_zenith)
    # mask out entries too close to zenith, or too far away from ROI center
    mask =   (pcosines >= config.cos_theta_max) & (zcosines>=np.cos(np.radians(config.z_max)))
    if config.verbose>1:
        print(f'\tFound {len(mask):,} S/C entries:  {sum(mask):,} remain after zenith and theta cuts')
    dfm = df.loc[mask,:]
    livetime = dfm.livetime.values

    return  pd.DataFrame(
        dict(
            start=df.start[mask],
            stop=df.stop[mask],
            exp=_exposure(config, livetime, pcosines[mask]),
            cos_theta=pcosines[mask],
        ))




# Cell

def _get_photons_near_source(config, source, week): #tzero, photon_df):
    """
    Select the photons near a source

    - source : a PointSource object
    - week : dict with
        - tzero : start time for the photon
        - photon_df : DataFrame with photon data

    Returns a DF with
    - `band` index,
    - `time` in MJD (added tstart and converted from MET)
    - `pixel` index, nest indexing
    - `radius` distance in deg from source direction
    """

    def _cone(config, source, nest=True):
        # cone geometry stuff: get corresponding pixels and center vector
        l,b,radius = source.l, source.b, config.radius
        cart = lambda l,b: healpy.dir2vec(l,b, lonlat=True)
        conepix = healpy.query_disc(config.nside, cart(l,b), np.radians(radius), nest=nest)
        center = healpy.dir2vec(l,b, lonlat=True)
        return center, conepix

    center, conepix = _cone(config,source)

    df = week['photons']
    tstart = week['tstart']
    allpix = df.nest_index.values

    # select by comparing high-order pixels (faster)
    shift=11
    a = np.right_shift(allpix, shift)
    c = np.unique(np.right_shift(conepix, shift))
    incone = np.isin(a,c)

    if sum(incone)<2:
        if config.verbose>1:
            print(f'\nWeek at {UTC(MJD(tstart))} has 0 or 1 photons')
        return

    if config.verbose>2:
        a, b = sum(incone), len(allpix)
        print(f'Select photons for source {source.name}:\n\tPixel cone cut: select {a} from {b} ({100*a/b:.1f}%)')

    # cut df to entries in the cone
    dfc = df[incone]

    # distance from center for all accepted photons
    ll,bb = healpy.pix2ang(config.nside, dfc.nest_index,  nest=True, lonlat=True)
    cart = lambda l,b: healpy.dir2vec(l,b, lonlat=True)
    t2 = np.degrees(np.array(np.sqrt((1.-np.dot(center, cart(ll,bb)))*2), np.float32))
    in_cone = t2<config.radius

    if config.verbose>2:
        print(f'\tGeometric cone cut: select {sum(in_cone)}')
    # assume all in the GTI (should check)

    # times: convert to float, add tstart, convert to MJD
    time = MJD(np.array(dfc.time, float)+tstart)

    # assemble the DataFrame, remove those outside the radius
    out_df = pd.DataFrame(np.rec.fromarrays(
        [np.array(dfc.band), time, dfc.nest_index, np.atleast_1d(t2)],
        names='band time pixel radius'.split()))[in_cone]

    # make sure times are monotonic by sorting (needed for most weeks after March 2018)
    out_df = out_df.sort_values(by='time')

    return out_df

# Cell
def contiguous_bins(exposure, min_gap=20, min_duration=600):

    """ return a dataframe with start and stop columns that
    denote contiguous intervals

    """

    stop = exposure.stop.values
    start = exposure.start.values

    # interleave  the starts ane stops
    ssint = np.empty(2*len(start))
    ssint[0::2] = start
    ssint[1::2] = stop

    # Tag the (stpp,start) pairs < 10 sec as  not adjacent
    not_adjacent = np.diff(ssint)[1::2] > min_gap/(24*3600) ;
    #print(f'{sum(not_adjacent)} (start,stop) pairs are not closer than {min_gap} s')

    # make a mask, keep ends
    mask = np.empty(2*len(start), bool)
    mask[0] = mask[-1] = True
    #

    # insert into mask -- keep only the (stop,start) pairs  which are not adjacent
    mask[1:-2:2] = not_adjacent
    mask[2:-1:2] = not_adjacent

    # apply mask, split into start and stop
    keep = ssint[mask]
    return keep
#     gstart, gstop = keep[0::2], keep[1::2]
#     df =  pd.DataFrame.from_dict(dict(start=gstart, stop=gstop))

#     # add column with duration in sec
#     df.loc[:,'duration'] = (df.stop-df.start)*24*3600
#     return df.query(f'duration>{min_duration}')

def time_bin_edges(config, exposure, tbin=None):
    """Return an interleaved array of start/stop values

    tbin: an array (a,b,d), default config.time_bins

    interpretation of a, b:

        if > 5000, interpret as MJD
        if <0, back from stop
        otherwise, offset from start

    d : if positive, the day bin size
        if 0; return contiguous bins


    """
    # nominal total range, MJD edges
    start = np.round(exposure.start.values[0])
    stop =  np.round(exposure.stop.values[-1])

    a, b, step = tbin if tbin is not None else config.time_bins


    if a>50000: start=a
    elif a<0: start = stop+a
    else : start += a


    if b>5000: stop=b
    elif b>0: stop = start+b
    else: stop += b

    if step<=0:
        return contiguous_bins(exposure.query(f'{start}<start<{stop}'),)

    # adjust stop
    nbins = int((stop-start)/step)
    assert nbins>1, 'Bad binning: no bins'
    stop = start+(nbins)*step
    u =  np.linspace(start,stop, nbins+1 )

    # make an interleaved start/stop array
    v = np.empty(2*nbins, float)
    v[0::2] = u[:-1]
    v[1::2] = u[1:]
    return v

# Cell
def binned_exposure(config, exposure, time_edges):
    """Bin the exposure

    - time_bins: list of edges, as an interleaved start/stop array


    returns  array of exposure integrated over each time bin, times 1e-9
    it is interleaved, client must apply [0::2] selection.

    """

    # get exposure calculation
    exp   =exposure.exp.values
    estart= exposure.start.values
    estop = exposure.stop.values

    # determine bins,

    #use cumulative exposure to integrate over larger periods
    cumexp = np.concatenate(([0],np.cumsum(exp)) )

    # get index into tstop array of the bin edges
    edge_index = np.searchsorted(estop, time_edges)

    # return the exposure integrated over the intervals
    cum = cumexp[edge_index]

    # difference is exposure per interval: normalize it here
    bexp = np.diff(cum)
#     if config.verbose>1:
#         print(f'Relative exposure per bin:\n{pd.Series(bexp).describe(percentiles=[])}')
    return bexp

# Cell

def _load_from_weekly_data(config, source, week_range=None):
    """
    Generate combinded DataFrames from a list of pickled files
    Either weekly or monthly

    kwargs:
    - week_range
    """

    # check weights
    weight_file =  check_weights(config,  source)
    assert weight_file is not None

    data_folder = config.wtlike_data/'data_files'
    data_files = sorted(list(data_folder.glob('*.pkl')))
    iname = data_folder.name

    if config.verbose>0:
        print(f"\tAssembling photon data and exposure for source {source.name} from"\
              f' folder "{data_folder}",\n\t with {len(data_files)} files,'\
              f' last file:  {data_files[-1].name}: ', end='')

    w1,w2 = week_range or  config.week_range
    if w1 is not None or w2 is not None:
        if config.verbose>0:
            print(f'\tLoading weeks {t}')
        data_files= data_files[w1:w2]
    else:
        if config.verbose>0: print('loading all files')



    verbose, config.verbose=config.verbose, 0
    # list of data framees
    pp = []
    ee = []
    for f in data_files:
        print('.', end='')
        with open(f, 'rb') as inp:
            week = pickle.load(inp)

        photons = _get_photons_near_source(config, source, week )
        if photons is not None:
            pp.append(photons)
        ee.append(_calculate_exposure_for_source(config, source, week ))
    print('');
    config.verbose=verbose
    # concatenate the two lists of DataFrames
    p_df = pd.concat(pp, ignore_index=True)
    e_df = pd.concat(ee, ignore_index=True)

    if config.verbose>1:
        times = p_df.time.values
        print(f'Loaded {len(p_df):,} photons from {UTC(times[0])} to  {UTC(times[-1])} ')
        print(f'Calculated {len(e_df):,} exposure entries')

    # add weights to photon data
    add_weights(config, p_df, source)

    return p_df, e_df

# Cell
class SourceData(object):
    """ Load the photon data near the source and associated exposure.

    Either from:
      1. `config.wtlike_data/'data_files'`, the Path to folder with list of pickle files
      2. the cache, with key `{source.name}_data`

    * source_name : if specified, create a PointSource object
    * `config` : basic configuration
    * `source` : PointSource object if specified
    * `clear` : if set, overwrite the cached results

    Calculate the values for

    * S, B : sums of w and 1-w
    * exptot : total associated exposure
    """

    def __init__(self, source_name, config=None, source=None, clear=False,
                 week_range=None, key=''):
        """

        """

        self.config = config if config else Config()
        if not (source_name or source):
            print('Must specify either the source name or a PointSource object', file=sys.stderr)
            return

        try:
            self.source = PointSource(source_name) if source_name else source
        except Exception as e:
            print(f'{e}', file=sys.stderr)
            return

        self.source_name = self.source.name
        self.verbose = self.config.verbose

        key = f'{self.source.name}_data' if key=='' else key
        self.source.data_key = key

        if self.config.wtlike_data/'data_files' is None and key not in config.cache:
            raise Exception(f'Data for {source.name} is not cached, and config.wtlike_data/"data_files" is not set')

        photons, self.exposure = self.config.cache(key,
                        _load_from_weekly_data, self.config, self.source, week_range,
                        overwrite=clear,
                        description=f'SourceData: photons and exposure for {self.source.name}')

        # get the photon data with good weights, not NaN (maybe remove small weigts, too)
        w = photons.weight
        good = np.logical_not(np.isnan(w))
        self.p_df = self.photons = photons.loc[good]
        self.exptot = self.exposure.exp.sum()

        # estimates for signal and background counts in toteal exposure
        self.S = np.sum(w)
        self.B = np.sum(1-w)

        # normailze to exposure
#         self.exptot = sum(self.e_df.exp)
#         self.S_exp = self.S/self.exptot
#         self.B_exp = self.B/self.exptot

        if self.verbose>0:
            print(SourceData.__repr__(self))


    def __repr__(self):
        time = self.photons.time.values
        r = f'{self.__class__.__name__}: Source {self.source.name} with:'\
            f'\n\t data:     {len(self.photons):9,} photons from   {UTC(time[0])[:10]} to {UTC(time[-1])[:10]}'\
            f'\n\t exposure: {len(self.exposure):9,} intervals from {UTC(self.exposure.iloc[0].start)[:10]}'\
            f' to {UTC(self.exposure.iloc[-1].stop)[:10]}'
        return r

    def binned_exposure(self, time_edges):
        """Bin the exposure

        - time_bins: list of edges.
        """
        return binned_exposure(self.config, self.exposure,  time_edges)

    def binned_cos_theta(self, time_bins=None):
        """ Calculate average cosine of angle with respect to bore axis, per time bin
        """
        if time_bins is None:
            time_bins = get_default_bins(self.config, self.exposure)
        df = self.exposure.copy()
        estop =df.stop.values
        df.loc[:,'tbin'] =np.digitize(estop, time_bins)
        ct = df.groupby('tbin').mean()['cos_theta']
        return ct, time_bins

    def weight_histogram(self, nbins=1000, key=''):
        """ return a weight distribution
        """
        def doit(nbins):
            return np.histogram(self.p_df.weight.values, np.linspace(0,1,nbins+1))[0]

        key = f'{self.source.name}_weight_hist' if key=='' else key
        description = f'Weight histogram for {self.source.name}' if self.config.verbose>0 else ''
        return self.config.cache(key, doit, nbins, description=description)

    def plot_data(self):
        import matplotlib.pyplot as plt
        fig, (ax1,ax2, ax3,ax4) = plt.subplots(1,4, figsize=(15,4))
        ax1.hist(self.p_df.time.values, 500, histtype='step');
        ax1.set(xlabel='Time (MJD)')
        ax2.hist(self.p_df.radius.values, 500, histtype='step');
        ax2.set(xlabel='Radius (deg)');

        ax3.hist(self.p_df.band, 32, histtype='step', log=True);
        ax3.set(xlabel='Band index')
        ax4.hist(self.p_df.weight, 100, histtype='step')
        ax4.set(xlabel='weight');