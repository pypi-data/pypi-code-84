#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import print_function
import os
import numpy as np
import pandas as pd
from matplotlib.pylab import plt #load plot library
from matplotlib import rc
import seaborn as sns
from natf import utils

# set color and markers
sns.set_palette(sns.color_palette("hls", 10))
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
markers = ['o', 's', 'v', '^', 'P', '*', 'X', 'd', 'x', 'D', 'H']

def get_labels(items, filename=None):
    """
    Get the labesl for all the parts.
    """
    if filename is not None and items == ['All']:
        # part with multiple nuc 'All'
        df = pd.read_csv(filename)
        items = list(df.columns)[1:]
    labels = []
    for i, p in enumerate(items):
        if p == 'CP':
            labels.append('CP')
        elif p in ['']:
            labels.append('PFC')
        elif p in ['Divertor_W_layer']:
            labels.append('Divertor W layer')
        elif p == 'Divertor_structure':
            labels.append("Divertor structure using SS316")
        elif p == 'Divertor_structure_eurofer':
            labels.append("Divertor structure using Eurofer")
        elif p == 'FirstWall':
            labels.append('FW')
        elif p == 'Be_U_0':
            labels.append('Be w/o U')
        elif p.upper() == 'BLK':
            labels.append('BLK')
        elif p.upper() == 'DIV':
            labels.append('DIV')
        elif p.upper() == 'VV':
            labels.append('VV')
        elif p.upper() == 'PF':
            labels.append('PFC')
        elif p.upper() == 'TF':
            labels.append('TFC')
        elif p.upper() == 'CS':
            labels.append('CS')
        elif p.upper() == 'TS':
            labels.append('TS')
        elif p.upper() == 'CRYOSTAT':
            labels.append('cryostat')
        elif p.upper() == 'ALL':
            labels.append('Overall')
        else:
            labels.append(p)
    return labels


def get_part_flux(filename, n_group_size=175):
    """
    Read the neutron flux of a part.
    """
    flux = np.zeros(n_group_size, dtype=np.float)
    with open(filename, 'r') as fin:
        count = 0
        while True:
            line = fin.readline()
            if line == '':
                break
            flux[count] = float(line.strip().split()[0])
            count += 1
    if count != n_group_size:
        raise ValueError(f"flux group size wrong")
    return flux
    


def get_filename(part, key, work_dir=None):
    """
    Get the filename for specific part and key.
    Eg. Get the act of A -> A.act
    """
    filename = os.path.join(work_dir, part, part + '.' + key)
    return filename

def get_value(filename, nucs=None, item=None):
    """
    Get the value for specific file.
    """
    df = pd.read_csv(filename)
    if nucs == ['All']:
        nucs = list(df.columns)[1:]
    if item is not None:
        # return specific item but not all
        idx = list(df['Nuclide']).index(item)
        value = np.array(df[nucs]).flatten()[idx]
    else:
        value = df[nucs]
    return value

def get_cooling_times(filename):
    "Get the cooling time."
    df = pd.read_csv(filename)
    value = df['Cooling_time(s)']
    return value

def get_values(parts, key, item=None, nucs=None, work_dir=None):
    """
    Get the value of parts for given key.
    The key could be 'act', 'acts', 'ci', ...

    Parameters:
    nucs: list
        If nucs is ['Total'], then get total value.
        If nucs is a list of specific nuc, then them.
        if nucs is ['all'], then get all the nucs
    """
    if len(parts) > 1 and len(nucs) > 1:
        raise ValueError("Multiple nucs and multiple parts mode is not supported")
    values = []
    cooling_times = []
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir=work_dir)
        value = get_value(filename, nucs=nucs, item=item)
        if item is None:
            if i == 0:
                cooling_times = get_cooling_times(filename)
        values.append(value)
    return values, cooling_times

def plot_example():
    """
    Example.
    """
    # create figure
    fig, ax = plt.subplots(figsize=(8,6))
    # example data
    a = np.arange(1,5)
    b = a**2
    c = a**3
    ax.plot(a, b)
    ax.plot(a, c)
    ax.legend()
    # show figure
    # save figure
    fig.savefig(fname="example.png",dpi=300)

def get_ylabel(key):
    """
    Set ylabel according to key.
    """
    if key in ['act']:
        return 'Total activity (Bq)'
    if key in ['act_st_t']:
        return 'Specific activity (Bq/kg)'
    if key in ['cdt']:
        return 'Contact dose rate (Sv/h)'
    if key == 'flx':
        return r'Nuetron flux (n/cm$^2 \cdot s$)'

def plot_parts_flux(parts, work_dir=None, figname="example.png", dpi=600,
    multiplier=1.0):
    """
    Plot the fluxes of parts.
    """
    # label and value 
    key = 'flx'
    labels = get_labels(parts)
    ylabel = get_ylabel(key='flx')
    # plots
    fig, ax = plt.subplots()
    for i, p in enumerate(parts):
        filename = get_filename(p, work_dir=work_dir, key=key)
        flux = get_part_flux(filename)
        flux = np.multiply(flux, multiplier)
        ax.step(utils.get_energy_group(175), flux, label=labels[i], color=colors[i], marker=None)
    ax.legend()
    # style difinition
    rc('text', usetex=True)
    rc('font', family='serif')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(xlabel='Neutron energy (MeV)', fontsize='x-large')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    # save file
    fig.savefig(fname=figname, dpi=dpi)


def plot_parts(parts, key=None, nucs=None, work_dir=None,
        figname='example.png', dpi=600, figtitle=None,
        xlabel='Time after shutdown (a)', ylabel=None, labels=None):
    """
    Plot specific act of given parts.
    """
    # label and value
    if labels is None:
        labels = get_labels(parts)
    if ylabel is None:
        ylabel = get_ylabel(key)
    values, cooling_times = get_values(parts, key=key, nucs=nucs, work_dir=work_dir)
    # convert time from sec to year.
    for i, ct in enumerate(cooling_times):
        cooling_times[i] = utils.time_sec_to_unit(ct, 'a')
    # plots parts
    fig, ax = plt.subplots()
    for i, p in enumerate(parts):
        ax.plot(cooling_times, values[i], label=labels[i], color=colors[i], marker=markers[i])
    ax.legend()
    # style difinition
    rc('text', usetex=True)
    rc('font', family='serif')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(xlabel=xlabel, fontsize='x-large')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    # save file
    fig.savefig(fname=figname, dpi=dpi)

def plot_wap_distribute(parts, key=None, nucs=None, work_dir=None,
        figname='example.png', dpi=600, figtitle=None,
        xlabel='Distance from BLK to PHTS components (m)', ylabel=r'Sepcific Activity (Bq/kg$_{H2O}$)',
        x_values=None):
    """
    Plot specific activity of given nuclide in PHTS.
    """
    # label and value
    labels = get_labels(parts)
    # plots parts
    fig, ax = plt.subplots()
    if x_values is None:
        x_values = range(0, len(parts))
    for i, nuc in enumerate(nucs):
        values, cooling_times = get_values(parts, key=key, nucs=[nucs[i]], work_dir=work_dir, item='Specific act (Bq/kg)')
        ax.plot(x_values, values, label=nuc, color=colors[i], marker=markers[i])
    ax.legend()
    # style difinition
    rc('text', usetex=True)
    rc('font', family='serif')
    ax.set_xlim([20, 200])
    ax.set_xscale('linear')
    ax.set_yscale('log')
    ax.set_xlabel(xlabel=xlabel, fontsize='x-large')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    ax.set_xticks(x_values)
    ax.set_xticklabels(parts, rotation = 75)
    ax2=ax.twiny()
    ax2.set_xlim([20, 200])
    ax2.set_xticks(x_values)
    ax2.set_xticklabels(x_values, rotation=75)
    plt.tight_layout()
    # save file
    fig.savefig(fname=figname, dpi=dpi)

def plot_wap_power_cmp(powers, cs, parts, key=None, nucs=None, work_dir=None,
        figname='example.png', dpi=600, figtitle=None,
        xlabel='Distance from BLK to PHTS components (m)', ylabel=r'Sepcific Activity (Bq/kg$_{H2O}$)',
        x_values=None):
    """
    Plot specific activity of given nuclide in PHTS.
    Only one nuc is allowed.
    """
    # label and value
    labels = get_labels(parts)
    # plots parts
    fig, ax = plt.subplots()
    if x_values is None:
        x_values = range(0, len(parts))
    for i, power in enumerate(powers):
        folder_name = os.path.join(work_dir, 'natf_coolant_' + cs + '_' + power)
        values, cooling_times = get_values(parts, key=key, nucs=nucs, work_dir=folder_name, item='Specific act (Bq/kg)')
        ax.plot(x_values, values, label=power, color=colors[i], marker=markers[i])
    ax.legend()
    # style difinition
    rc('text', usetex=True)
    rc('font', family='serif')
    ax.set_xlim([20, 200])
    ax.set_xscale('linear')
    ax.set_yscale('log')
    ax.set_xlabel(xlabel=xlabel, fontsize='x-large')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    ax.set_xticks(x_values)
    ax.set_xticklabels(parts, rotation = 75)
    ax2=ax.twiny()
    ax2.set_xlim([20, 200])
    ax2.set_xticks(x_values)
    ax2.set_xticklabels(x_values, rotation=75)
    plt.tight_layout()
    # save file
    fig.savefig(fname=figname, dpi=dpi)


def plot_nucs(parts, key, nucs, labels=None, work_dir=None,
        figname='example.png', dpi=600, figtitle=None,
        xlabel='Time after shutdown (a)', ylabel=None, yscale='log'):
    """
    Plot the different nucs or item in the same part.
    """
    filename = get_filename(part=parts[0], key=key, work_dir=work_dir)
    # label and value
    if labels is None:
        labels = get_labels(nucs, filename=filename)
    if ylabel is None:
        ylabel = get_ylabel(key)
    values, cooling_times = get_values(parts, key=key, nucs=nucs, work_dir=work_dir)
    # convert time from sec to year.
    for i, ct in enumerate(cooling_times):
        cooling_times[i] = utils.time_sec_to_unit(ct, 'a')
    # plots parts
    ratio_fix = 0
    if 'ratio' in key:
        ratio_fix = 1
    fig, ax = plt.subplots()
    for i, item in enumerate(labels):
        ax.plot(cooling_times, values[0][item], label=labels[i], color=colors[i+ratio_fix], marker=markers[i+ratio_fix])
    ax.legend()
    # style difinition
    rc('text', usetex=True)
    rc('font', family='serif')
    ax.set_xscale('log')
    ax.set_yscale(yscale)
    ax.set_xlabel(xlabel=xlabel, fontsize='x-large')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    # save file
    fig.savefig(fname=figname, dpi=dpi)
    plt.close()

def get_part_mass(part, work_dir=None):
    """
    Get part mass from part name.
    """
    key = 'basicinfo'
    filename = get_filename(part, key, work_dir=work_dir)
    df = pd.read_csv(filename)
    mass_info = np.array(df.loc[df[part] == 'mass(g)']).flatten()
    return float(mass_info[1])

def get_part_vol(part, work_dir=None):
    """
    Get part volume from part name.
    """
    key = 'basicinfo'
    filename = get_filename(part, key, work_dir=work_dir)
    df = pd.read_csv(filename)
    vol_info = np.array(df.loc[df[part] == 'volume(cm3)']).flatten()
    return float(vol_info[1])

def write_part_basicinfo(parts, work_dir=None, ofname='cfetr_parts_vol_mass.csv'):
    """
    Write part basic information as a csv table.
    """
    vols = [0.0]*len(parts)
    masses = [0.0]*len(parts)
    for i, p in enumerate(parts):
        vols[i] = get_part_vol(p, work_dir=work_dir)
        masses[i] = get_part_mass(p, work_dir=work_dir)
    # save the ctrs into csv
    fo = open(ofname, 'w')
    title_line = utils.data_to_line_1d(key='Components', value=['Volumes (m3)', 'Masses (ton)'])
    fo.write(title_line)
    for i, p in enumerate(parts):
        line = utils.data_to_line_1d(key=p, value=[vols[i]/1e6, masses[i]/1e6], decimals=1)
        fo.write(line)
    fo.close()

def calc_rwcs_masses(parts, key, cooling_time_s, work_dir=None):
    """
    Calcualte the mass of HLW, ILW and LLW.
    """
    rwc_dict = {'Clearance':0, 'VLLW':0, 'LLW':1, 
                'LLWC':1, 'LLWB':1, 'LLWA':1,
                'ILW':2, 'HLW':3}
    masses = np.array([0.0, 0.0, 0.0, 0.0])
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir=work_dir)
        rwc = get_rwc(filename, cooling_time_s=cooling_time_s) 
        masses[rwc_dict[rwc]] += get_part_mass(p, work_dir=work_dir)
    return masses

def plot_rwcs_compare(parts, keys=['rwc_chn2018', 'rwc_usnrc', 'rwc_usnrc_fetter', 'rwc_uk'],
        cooling_time_s='1 s', work_dir=None, ofname='rwc_compare_1s.png'):
    """
    Plot the compare result of different radwaste standards.

    Parameters:
    -----------
    parts: list
        List of part names.
    keys: list
        List of keys. Eg. ['rwc_chn2018', 'rwc_usnrc']
    cooling_time: string
        The cooling time to plot.
    work_dir: string
        The working directory.
    ofname: string
        Output figure name.
    """
    rwcs_masses = np.zeros(shape=(len(keys), 4), dtype=float)
    for i, key in enumerate(keys):
        # get mass of Clearance/VLLW, LLW, ILW and HLW
        rwcs_masses[i][:] = calc_rwcs_masses(parts, key, cooling_time_s, work_dir=work_dir)
    # convert to unit t
    rwcs_masses = np.divide(rwcs_masses, 1.0e6)
    # plot
    labels = ['VLLW', 'LLW', 'ILW', 'HLW']
    x = np.arange(len(labels)) * 2
    witdh = 0.35
    fig, ax = plt.subplots()
    rects0 = ax.bar(x - 1.5 * witdh, rwcs_masses[:][0], witdh, label='CHN2018', color=colors[0], hatch='//')
    rects1 = ax.bar(x - 0.5 * witdh, rwcs_masses[:][1], witdh, label='USNRC', color=colors[1], hatch='--')
    rects2 = ax.bar(x + 0.5 * witdh, rwcs_masses[:][2], witdh, label='USNRC_FETTER', color=colors[2], hatch='xx')
    rects3 = ax.bar(x + 1.5 * witdh, rwcs_masses[:][3], witdh, label='UK', color=colors[3], hatch='++')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Mass (t)')
    ax.set_xlabel('Radioactive levels')
#    ax.set_title('')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc='best')

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(round(height, 1)),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', size=5)
    
    autolabel(rects0)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    fig.tight_layout()
    fig.savefig(fname=ofname,dpi=600)
    
def calc_rwc_cooling_requirement(parts, key, classes, standard='CHN2018', work_dir=None, out_unit='a', ofname=None):
    """
    Calculate the cooling time requirement for specific classes.
    """
    ctrs = []
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir)
        cooling_times = get_cooling_times(filename)
        rwcs = list(get_value(filename, nucs='Radwaste_Class'))
        ctr = utils.calc_ctr(cooling_times, rwcs, classes, out_unit=out_unit, standard=standard)
        ctrs.append(ctr)
    # save the ctrs into csv
    if ofname is not None:
        fo = open(ofname, 'w')
        title_line = utils.data_to_line_1d(key='Components', value=list(c + ' (' +out_unit+')' for c in classes))
        fo.write(title_line)
        for i, p in enumerate(parts):
            line = utils.data_to_line_1d(key=p, value=ctrs[i])
            fo.write(line)
        fo.close()
    return ctrs


def get_rwc(filename, cooling_time_s=None, cooling_time=None):
    """
    Get the rwc from specific filename and cooling time.
    """
    if cooling_time_s is not None and cooling_time is not None:
        raise ValueError("only one cooling time input is supported")
    if cooling_time_s is not None:
        tokens = cooling_time_s.strip().split()
        value = tokens[0]
        unit = tokens[1]
        ct = utils.cooling_time_sec(value, unit)
    if cooling_time is not None:
        ct = cooling_time
    df = pd.read_csv(filename)
    cooling_times = np.array(df['Cooling_time(s)']).flatten()
    index = utils.get_ct_index(ct, cooling_times)
    rwc = np.array(df['Radwaste_Class']).flatten()[index]
    return rwc


def get_rwcs_by_cooling_times(parts, cooling_times_s=['1 s', '1 a', '10 a', '100 a'],
        cooling_times=[], key='rwc_chn2018', work_dir=None, ofname='cfetr_all_rwc_chn2018.csv'):
    """
    Get the radwaste classification of different cooling times.

    Parameters:
    -----------
    parts: list of string
        List of part names.
    cooling_times_s: list of string
        List of cooling times.
    cooling_times: list of float
    key: string
        Standard name. Supported standards: 'rwc_chn2018', 'usnrc', 'usnrc_fetter', 'uk'
    work_dir: string
        Working directory.
    ofname: string
        Output csv file name.
    """
    
    if len(cooling_times) == 0:
        cooling_times = [0.0] * len(cooling_times_s)
        # convert cooling_times from string to float
        for i, ct in enumerate(cooling_times_s):
            tokens = ct.strip().split()
            value = tokens[0]
            unit = tokens[1]
            cooling_times[i] = utils.cooling_time_sec(value, unit)

    rwcs = np.array([['']*len(cooling_times)]*len(parts), dtype='<U16')
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir=work_dir)
        df = pd.read_csv(filename)
        cts = np.array(df['Cooling_time(s)']).flatten()
        for j, ct in enumerate(cooling_times):
            rwc = get_rwc(filename, cooling_time = ct)
            rwcs[i][j] = rwc

    if ofname is not None:
        # save the rwcs into csv
        fo = open(ofname, 'w')
        title_line = utils.data_to_line_1d(key='Components', value=cooling_times_s)
        fo.write(title_line)
        for i, p in enumerate(parts):
            line = utils.data_to_line_1d(key=p, value=rwcs[i])
            fo.write(line)
        fo.close()
    return rwcs

