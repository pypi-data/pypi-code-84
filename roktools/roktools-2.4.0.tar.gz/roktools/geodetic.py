#!/usr/bin/env python
"""
Module with several geodetic related methods
"""
# import math
# import sys
import collections
import math
import typing

import numpy as np

import roktools.logger

# WGS84 constants
WGS84_A = 6378137.0
WGS84_E = 8.1819190842622e-2

DMS = collections.namedtuple('DMS', 'degrees minutes seconds')
LLA = collections.namedtuple('LLA', 'longitude latitude altitude')
XYZ = collections.namedtuple('XYZ', 'x y z')
ENU = collections.namedtuple('ENU', 'east north up')
ElAz = collections.namedtuple('ElAz', 'elevation azimuth')

class Coordinates(object):
    """
    Class to store coordinates and transform among various coordinate systems
    (cartesian and geodetic)
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        self.point = XYZ(x, y, z)

    def is_valid(self) -> bool:
        """
        >>> coordinates = Coordinates(0, 0, 0)
        >>> coordinates.is_valid()
        False
        """
        return valid_coordinates(xyz=self.xyz())

    def xyz(self) -> XYZ:
        """
        >>> coordinates = Coordinates(4889803.653, 170755.706, 4078049.851)
        >>> coordinates.xyz()
        XYZ(x=4889803.653, y=170755.706, z=4078049.851)
        """
        return self.point

    def lla(self, radians: bool = False, a: float = WGS84_A, e: float = WGS84_E) -> LLA:
        """
        >>> coordinates = Coordinates(4889803.653, 170755.706, 4078049.851)
        >>> "lon: {:.0f} lat: {:.0f} height: {:.0f}".format(*coordinates.lla())
        'lon: 2 lat: 40 height: 100'
        """
        return LLA(*xyz_to_lla(*self.point, radians=radians, a=a, e=e))

    def dms(self, radians: bool = False, a: float = WGS84_A, e: float = WGS84_E) -> LLA:
        """
        >>> coordinates = Coordinates(4889803.653, 170755.706, 4078049.851)
        >>> coord = coordinates.dms()
        >>> coord.longitude.degrees
        1
        >>> coord.longitude.minutes
        59
        """
        lla = self.lla(radians=radians, a=a, e=e)

        longitude = convert_decimal_units_to_dms(lla.longitude)
        latitude = convert_decimal_units_to_dms(lla.latitude)

        return LLA(longitude, latitude, lla.altitude)

    def __repr__(self) -> str:
        """
        >>> Coordinates(4889803.653, 170755.706, 4078049.851)
        4889803.653 170755.706 4078049.851
        """
        return f'{self.point.x:.3f} {self.point.y:.3f} {self.point.z:.3f}'


    def __sub__(self, other) -> XYZ:
        """
        >>> dest_position = Coordinates(4889804, 170755, 4078049)
        >>> orig_position = Coordinates(4889803, 170757, 4078049)
        >>> dest_position - orig_position
        XYZ(x=1, y=-2, z=0)
        """

        xyz_self = self.xyz()
        xyz_other = other.xyz()

        return XYZ(x=xyz_self.x-xyz_other.x, y=xyz_self.y-xyz_other.y, z=xyz_self.z-xyz_other.z)

    @staticmethod
    def from_lla(longitude_deg: float, latitude_deg: float, height_m: float,
                 a: float = WGS84_A, e: float = WGS84_E) -> 'Coordinates':
        """
        >>> coordinates = Coordinates.from_lla(2, 40, 100)
        >>> coordinates.is_valid()
        True
        """

        xyz = lla_to_xyz(longitude_deg, latitude_deg, height_m, a=a, e=e)

        return Coordinates(*xyz)

    @staticmethod
    def from_xyz(x: float, y: float, z: float) -> 'Coordinates':
        """
        >>> coordinates = Coordinates.from_lla(4889803.653, 170755.706, 4078049.851)
        >>> coordinates.is_valid()
        True
        """

        return Coordinates(x, y, z)

# ------------------------------------------------------------------------------

class CoordinatesDisplacement(object):
    """
    Representation of a displacement relative to a certain point (Coordinates).
    Use this class to represent deviations such as error vector, lever arms, ...
    """

    def __init__(self, xyz: XYZ = None, enu: ENU = None, ref_position: Coordinates = None):
        """
        >>> c = CoordinatesDisplacement(xyz=XYZ(0.1, 0.1, 0.1))
        >>> c.is_valid()
        True
        """
        self.xyz = xyz
        self.enu = enu
        self.ref_lla = None
        
        if ref_position:
            self.set_reference_position(ref_position)

    def set_reference_position(self, position: Coordinates) -> None:

        if not position:
            raise ValueError("Invalid reference position")

        self.ref_lla = position.lla(radians=True)

    def is_valid(self) -> bool:
        """
        >>> c = CoordinatesDisplacement()
        >>> c.is_valid()
        False
        """
        return self.xyz is not None or self.enu is not None

    def check_validity(self) -> None:
        if not self.is_valid():
            raise ValueError("CoordinatesDisplacement object is not valid")

    def get_xyz(self) -> XYZ:
        """
        >>> enu = ENU(-0.416, 5.664, -0.081)
        >>> reference_position = Coordinates.from_lla(1.52160871, 41.26531742, 127.0)
        >>> c = CoordinatesDisplacement(enu=enu)
        >>> c.set_reference_position(reference_position)
        >>> xyz = c.get_xyz()
        >>> '{:.03f} {:.03f} {:.03f}'.format(*xyz)
        '-3.784 -0.517 4.204'
        """

        self.check_validity()

        if not self.xyz:
            if not self.ref_lla:
                raise ValueError("Missing reference position in CoordinatesDisplacement to convert frame (ENU to XYZ)")
            xyz_list = enu_to_ecef(self.ref_lla.longitude, self.ref_lla.latitude, *self.enu, radians=True)
            self.xyz = XYZ(*xyz_list)
            
        return self.xyz 

    def get_enu(self) -> ENU:
        """
        >>> xyz = XYZ(0.1, 0.1, 0.1)
        >>> ref_position = Coordinates(4889803.653, 170755.706, 4078049.851)
        >>> c = CoordinatesDisplacement(xyz=xyz, ref_position=ref_position)
        >>> enu = c.get_enu()
        >>> '{:.03f} {:.03f} {:.03f}'.format(*enu)
        '0.096 0.010 0.144'
        """

        self.check_validity()

        if not self.enu:
            if not self.ref_lla:
                raise ValueError("Missing reference position in CoordinatesDisplacement to convert frame (XYZ to ENU)")
            enu_list = ecef_to_enu(self.ref_lla.longitude, self.ref_lla.latitude, *self.xyz, radians=True)
            self.enu = ENU(*enu_list)
            
        return self.enu

    def __abs__(self):
        """
        >>> c = CoordinatesDisplacement.from_xyz(0.1, 0.1, 0.1)
        >>> f'{abs(c):.4f}'
        '0.1732'
        """

        if not self.is_valid():
            raise ValueError("Cannot compute the magnitude of an empty array")

        vector = self.xyz or self.enu

        return math.sqrt(sum([v * v for v in vector]))


    @staticmethod
    def from_xyz(x: float, y: float, z: float):
        """
        >>> c = CoordinatesDisplacement.from_xyz(0.1, 0.1, 0.1)
        >>> c.is_valid()
        True
        """
        return CoordinatesDisplacement(xyz=XYZ(x, y, z))

    @staticmethod
    def from_enu(e: float, n: float, u: float):
        """
        >>> c = CoordinatesDisplacement.from_enu(0.1, 0.1, 0.1)
        >>> c.is_valid()
        True
        """
        return CoordinatesDisplacement(enu=ENU(e, n, u))

# ------------------------------------------------------------------------------

def valid_coordinates(lla=None, xyz=None):
    """
    Check wether the input geographic coordinates are valid or not (in terms
    of being on the Earth's surface)

    >>> valid_coordinates(lla=[0, 0, -6378137])
    False
    >>> valid_coordinates(xyz=[0, 0, 0])
    False
    """

    ALT_THRESHOLD = 10.0e3 # meters above/under surface level

    if lla is not None and (lla[2] > ALT_THRESHOLD or lla[2] < -ALT_THRESHOLD):
        return False

    EPS_THRESHOLD = 1.0e-3

    if xyz is not None and np.sum(np.square(xyz)) < EPS_THRESHOLD:
        return False

    return True
    

#-------------------------------------------------------------------------------

def lla_to_xyz(longitude, latitude, height, a=WGS84_A, e=WGS84_E, radians=False):
    """
    Convert from geodetic coordinates (relative to a reference ellipsoid which
    defaults to WGS84) to Cartesian XYZ-ECEF coordinates.

    Longitude and latitude can be expressed in degrees (radians=False) or
    radians (radians=True)

    The longitude, latitude and height values can be vectors

    >>> xyz = lla_to_xyz(9.323302567, 48.685064919, 373.2428)
    >>> [float('{0:.3f}'.format(v)) for v in xyz]
    [4163316.145, 683507.935, 4767789.479]

    >>> import numpy as np
    >>> lons = np.array([9.323302567, 9.323335545, 9.323368065])
    >>> lats = np.array([48.685064919, 48.685050295, 48.685036011])
    >>> hgts = np.array([373.2428, 373.2277, 373.2078])
    >>> x, y, z = lla_to_xyz(lons, lats, hgts)
    >>> "{0:.6f}".format(x[0])
    '4163316.144693'
    >>> "{0:.6f}".format(x[1])
    '4163316.946837'
    >>> "{0:.6f}".format(x[2])
    '4163317.723291'
    >>> "{0:.6f}".format(y[0])
    '683507.934738'
    >>> "{0:.6f}".format(y[1])
    '683510.527317'
    >>> "{0:.6f}".format(y[2])
    '683513.081502'
    >>> "{0:.6f}".format(z[0])
    '4767789.478699'
    >>> "{0:.6f}".format(z[1])
    '4767788.393654'
    >>> "{0:.6f}".format(z[2])
    '4767787.329966'
    """

    # Convert from degrees to radians if necessary
    lon = longitude if radians else np.deg2rad(longitude)
    lat = latitude if radians else np.deg2rad(latitude)

    sinlat = np.sin(lat)
    coslat = np.cos(lat)
    sinlon = np.sin(lon)
    coslon = np.cos(lon)
    e2 = e * e

    # Intermediate calculation (prime vertical radius of curvature)
    N = a / np.sqrt(1.0 - e2 * sinlat * sinlat)
    nalt = N + height

    x = nalt * coslat * coslon
    y = nalt * coslat * sinlon
    z = ((1.0-e2) * N + height) * sinlat

    return (x, y, z)


def convert_decimal_units_to_dms(value:float) -> DMS:
    """
    Convert from longitude/latitude to Degrees, minutes and seconds
    >>> latitude_deg = 41.528442316
    >>> dms = convert_decimal_units_to_dms(latitude_deg)
    >>> "{:.0f} {:.0f} {:.7f}".format(*dms)
    '41 31 42.3923376'
    >>> longitude_deg = 2.434318900
    >>> dms = convert_decimal_units_to_dms(longitude_deg)
    >>> "{:.0f} {:.0f} {:.7f}".format(*dms)
    '2 26 3.5480400'
    """

    degrees = (int)(value)
    minutes_float = (value - degrees) * 60
    minutes = (int)(minutes_float)
    seconds = (minutes_float - minutes) * 60

    return DMS(degrees, minutes, seconds)


#-------------------------------------------------------------------------------

def xyz_to_lla(x, y, z, radians=False, a=WGS84_A, e=WGS84_E):
    """
    Convert from Cartesian XYZ-ECEF coordinates to geodetic coordinates
    (relative to a reference ellipsoid which defaults to WGS84).

    Output longitude and latitude are expressed in degrees (radians=False) or
    radians (radians=True)

    The x, y and z values can be vectors

    >>> xyz_to_lla(4807314.3520, 98057.0330, 4176767.6160)
    (1.1685266980613551, 41.170001652314625, 173.4421242615208)

    >>> import numpy as np
    >>> xs = np.array([4807314.3520, 4807315.3520, 4807316.3520])
    >>> ys = np.array([98057.0330, 98058.0330, 98059.0330])
    >>> zs = np.array([4176767.6160, 4176768.6160, 4176769.6160])
    >>> lon, lat, height = xyz_to_lla(xs, ys, zs)
    >>> "{0:.7f}".format(lon[0])
    '1.1685267'
    >>> "{0:.7f}".format(lon[1])
    '1.1685384'
    >>> "{0:.7f}".format(lon[2])
    '1.1685500'
    >>> "{0:.7f}".format(lat[0])
    '41.1700017'
    >>> "{0:.7f}".format(lat[1])
    '41.1700024'
    >>> "{0:.7f}".format(lat[2])
    '41.1700031'
    >>> "{0:.7f}".format(height[0])
    '173.4421243'
    >>> "{0:.7f}".format(height[1])
    '174.8683741'
    >>> "{0:.7f}".format(height[2])
    '176.2946241'
    """

    a2 = a ** 2     # Squared of radius, for convenience
    e2 = e ** 2     # Squared of eccentricity, for convenience

    b = np.sqrt(a2 * (1 - e2))
    b2 = b ** 2

    ep = np.sqrt((a2 - b2) / b2)

    p = np.sqrt(x ** 2 + y ** 2)
    th = np.arctan2(a * z, b * p)

    lon = np.arctan2(y, x)
    lon = np.fmod(lon, 2 * np.pi)

    sinth = np.sin(th)
    costh = np.cos(th)

    lat = np.arctan2((z + b * (ep ** 2) * (sinth ** 3)), (p - e2 * a * costh ** 3))
    sinlat = np.sin(lat)

    N = a / np.sqrt(1 - e2 * (sinlat ** 2))
    alt = p / np.cos(lat) - N

    if radians:
        return (lon, lat, alt)
    else:
        return (lon * 180 / np.pi, lat * 180 / np.pi, alt)



# #-------------------------------------------------------------------------------
#
# def body2enu_matrix(yaw, pitch, roll, radians=False):
#     """
#     Computes the matrix that transforms from Body frame to ENU
#
#     This accepts scalars or vector of scalars.
#
#     Also, the yaw, pitch and roll can be expressed as radians (radians=True)
#     or degrees (radians=False)
#     """
#
#     # Convert from degrees to radians if necessary
#     ya = yaw if radians else np.deg2rad(yaw)
#     pi = pitch if radians else np.deg2rad(pitch)
#     ro = roll if radians else np.deg2rad(roll)
#
#     # Compute the sines and cosines, used later to compute the elements
#     # of the transformation matrix
#     siny = np.sin(ya)
#     cosy = np.cos(ya)
#     sinp = np.sin(pi)
#     cosp = np.cos(pi)
#     sinr = np.sin(ro)
#     cosr = np.cos(ro)
#
#     cosy_cosr = cosy * cosr
#     siny_cosr = siny * cosr
#     sinp_sinr = sinp * sinr
#     sinr_siny = sinr * siny
#
#     # Compute the matrix coefficients
#     m = np.zeros((3, 3), dtype=object)
#
#     m[0,0] = cosp * cosy
#     m[0,1] = sinp_sinr * cosy - siny_cosr
#     m[0,2] = cosy_cosr * sinp + sinr_siny
#
#     m[1,0] =  cosp * siny
#     m[1,1] =  sinp_sinr * siny + cosr * cosy
#     m[1,2] =  siny_cosr * sinp - sinr * cosy
#
#     m[2,0] = - sinp
#     m[2,1] = sinr * cosp
#     m[2,2] = cosr * cosp
#
#     return m
#
#
# #-------------------------------------------------------------------------------
#
# def body2enu(yaw, pitch, roll, x, y, z, radians=False, matrix=None):
#     """
#     Converts from Body reference frame to ENU reference point.
#
#     This accepts scalars or vector of scalars.
#
#     Also, the yaw, pitch and roll can be expressed as radians (radians=True)
#     or degrees (radians=False)
#
#     TEST RATIONALE HAS TO BE CHANGED ACCORDING TO THE CHANGE IN THE BODY2ENU_MATRIX RESULT INTERPRETATION:
#     BODY2ENU_MATRIX IS ACTUALLY IMPLEMENTING BODY2NED_MATRIX!!!!!!
#
#     >>> body2enu(0, 0, 0, 1, 1, 1)
#     (1.0, 1.0, -1.0)
#
#     >>> import numpy as np
#
#     >>> enu = body2enu(90, 0, 0, 1, 1, 1)
#     >>> np.round(enu)
#     array([ 1., -1., -1.])
#
#     >>> enu = body2enu(0, 90, 0, 1, 1, 1)
#     >>> np.round(enu)
#     array([1., 1., 1.])
#
#     >>> enu = body2enu(0, 0, 90, 1, 1, 1)
#     >>> np.round(enu)
#     array([-1.,  1., -1.])
#
#     >>> yaws = [0] * 3; pitches = [0] * 3; rolls = [0] * 3
#     >>> xs = [1] * 3; ys = [1] * 3; zs = [1]*3
#     >>> es, ns, us = body2enu(yaws, pitches, rolls, xs, ys, zs)
#     >>> es
#     array([1., 1., 1.])
#     >>> ns
#     array([1., 1., 1.])
#     >>> us
#     array([-1., -1., -1.])
#     """
#
#     if matrix is None:
#         m = body2enu_matrix(yaw, pitch, roll, radians=radians)
#
#     n = m[0,0] * x + m[0,1] * y + m[0,2] * z
#     e = m[1,0] * x + m[1,1] * y + m[1,2] * z
#     d = m[2,0] * x + m[2,1] * y + m[2,2] * z
#
#     return (e, n, -d)
#
# #-------------------------------------------------------------------------------
#
# def enu2body(yaw, pitch, roll, e, n, u, radians=False, matrix=None):
#     """
#     Converts from ENU to XYZ Body reference frame
#
#     This accepts scalars or vector of scalars.
#
#     Also, the yaw, pitch and roll can be expressed as radians (radians=True)
#     or degrees (radians=False)
#
#
#     >>> np.round(enu2body(0, 0, 0, *body2enu(0, 0, 0, 0.2, 0.2, 1.5)), decimals=1)
#     array([0.2, 0.2, 1.5])
#     """
#
#     if matrix is None:
#         m = body2enu_matrix(yaw, pitch, roll, radians=radians)
#
#     x = m[0,0] * n + m[1,0] * e + m[2,0] * -u
#     y = m[0,1] * n + m[1,1] * e + m[2,1] * -u
#     z = m[0,2] * n + m[1,2] * e + m[2,2] * -u
#
#     return (x, y, z)
#
#
#
# -------------------------------------------------------------------------------

def enu_to_ecef_matrix(longitude, latitude, radians=False):
    """
    Computes the transformation matrix from ENU to XYZ (ECEF) and returns
    the matrix coefficients stored as a a numpy two-dimensional array

    This accepts scalars or vector of scalars.

    The latitude and longitude can be expressed either in radians (radians=True)
    or degrees (radians = True)
    """

    n_samples = np.size(longitude)

    # Convert from degrees to radians if necessary
    lon = longitude if radians else np.deg2rad(longitude)
    lat = latitude if radians else np.deg2rad(latitude)

    # Compute the sine and cos to avoid recalculations
    sinlon = np.sin(lon)
    coslon = np.cos(lon)
    sinlat = np.sin(lat)
    coslat = np.cos(lat)

    m = np.zeros((3, 3), dtype=object)

    # Compute the elemnts of the matrix

    m[0, 0] = -sinlon
    m[1, 0] = coslon
    m[2, 0] = 0 if n_samples == 1 else np.zeros(n_samples)

    m[0, 1] = -sinlat * coslon
    m[1, 1] = -sinlat * sinlon
    m[2, 1] = coslat

    m[0, 2] = coslat * coslon
    m[1, 2] = coslat * sinlon
    m[2, 2] = sinlat

    return m

# -------------------------------------------------------------------------------

def enu_to_ecef(longitude, latitude, e, n, u, radians=False, matrix=None):
    """
    Converts from East North and Up to Cartesian XYZ ECEF

    This accepts scalars or vector of scalars.

    The latitude and longitude can be expressed either in radians (radians=True)
    or degrees (radians = True)

    >>> enu = (0.5, 0.5, 1.0)
    >>> enu_to_ecef(0, 0, *enu)
    (1.0, 0.5, 0.5)

    >>> enu = (0.0, 0.0, 1.0)
    >>> enu_to_ecef(0, 0, *enu)
    (1.0, 0.0, 0.0)

    >>> lons = [90, 180, 270]
    >>> lats = [0, 0, 0]
    >>> es = [-1, -1, +1]
    >>> ns = [1, 1, 1]
    >>> us = [1, -1, -1]
    >>> dxyz = enu_to_ecef(lons, lats, es, ns, us)
    >>> round(dxyz[0][0], 8)
    1.0
    >>> round(dxyz[0][1], 8)
    1.0
    >>> round(dxyz[0][2], 8)
    1.0
    >>> round(dxyz[1][0], 8)
    1.0
    >>> round(dxyz[1][1], 8)
    1.0
    >>> round(dxyz[1][2], 8)
    1.0
    >>> round(dxyz[2][0], 8)
    1.0
    >>> round(dxyz[2][1], 8)
    1.0
    >>> round(dxyz[2][2], 8)
    1.0
    """

    if matrix is None:
        m = enu_to_ecef_matrix(longitude, latitude, radians=radians)


    x = m[0, 0] * e + m[0, 1] * n + m[0, 2] * u
    y = m[1, 0] * e + m[1, 1] * n + m[1, 2] * u
    z = m[2, 0] * e + m[2, 1] * n + m[2, 2] * u

    return (x, y, z)

# -------------------------------------------------------------------------------

def xyz_to_enu(ref_pos, x, y, z, a=WGS84_A, e=WGS84_E):
    """
    Converts from Cartesian XYZ ECEF to East North and Up given a reference
    position in Cartesian absolute XYZ ECEF.

    >>> xyz = [WGS84_A, 0.0, 0.0]   # Reference position
    >>> dxyz = (1.0, 0.0, 0.0)      # Deviation relative to reference position
    >>> enu = xyz_to_enu(xyz, *dxyz)  # Conversion to ENU at reference position
    >>> enu
    (0.0, 0.0, 1.0)

    >>> enu = (0.5, 0.5, 1.0)
    >>> dxyz = enu_to_ecef(0, 0, *enu)
    >>> dxyz
    (1.0, 0.5, 0.5)
    >>> xyz_to_enu(xyz, *dxyz) == enu
    True
    """

    lla = xyz_to_lla(*ref_pos, radians=True, a=a, e=e)

    return ecef_to_enu(lla[0], lla[1], x, y, z, radians=True)

# -------------------------------------------------------------------------------

def ecef_to_enu(longitude, latitude, x, y, z, radians=False, matrix=None):
    """
    Converts from Cartesian XYZ ECEF to East North and Up

    This accepts scalars or vector of scalars.

    The latitude and longitude can be expressed either in radians (radians=True)
    or degrees (radians = True)

    >>> dxyz = (1, 0, 0)
    >>> ecef_to_enu(0, 0, *dxyz)
    (0.0, 0.0, 1.0)

    >>> dxyz = (1, 0.5, 0.5)
    >>> ecef_to_enu(0, 0, *dxyz)
    (0.5, 0.5, 1.0)

    >>> enu = (0.5, 0.5, 1)
    >>> dxyz = enu_to_ecef(0, 0, *enu)
    >>> dxyz
    (1.0, 0.5, 0.5)
    >>> ecef_to_enu(0, 0, *dxyz) == enu
    True
    """

    if matrix is None:
        m = enu_to_ecef_matrix(longitude, latitude, radians=radians)

    e = m[0, 0] * x + m[1, 0] * y + m[2, 0] * z
    n = m[0, 1] * x + m[1, 1] * y + m[2, 1] * z
    u = m[0, 2] * x + m[1, 2] * y + m[2, 2] * z

    return (e, n, u)

# #-------------------------------------------------------------------------------
# 
# def body2ecef(longitude, latitude, yaw, pitch, roll, x, y, z, radians=False):
#     """
#     Transform from body fixed reference frame to Cartesian XYZ-ECEF
#     """
# 
#     enu = body2enu(yaw, pitch, roll, x, y, z, radians=radians)
# 
#     return enu2ecef(longitude, latitude, *enu, radians=radians)
# 
# 
# #-------------------------------------------------------------------------------
# 
# 
# def transposePosGeodetic(longitude, latitude, height, yaw, pitch, roll, lx, ly, lz, radians=False):
#     """
#     Apply lever arm (l=[lx,ly,lz]) to position (longitude,latitude, height) according to rover attitude (yaw,pitch,roll)
#     """
# 
#     leverArmEnu = body2enu(yaw, pitch, roll, lx,ly, lz, radians=radians)
#     leverArmNed = (leverArmEnu[1],leverArmEnu[0],-1*leverArmEnu[2])
# 
#     deltaPos =  smallPerturbationCart2Geodetic(leverArmNed[0],leverArmNed[1],leverArmNed[2],latitude,height,radians=radians)
# 
#     return (latitude + deltaPos[0], longitude + deltaPos[1], height + deltaPos[2])
# 
# 
# #-------------------------------------------------------------------------------
# 
# def smallPerturbationCart2Geodetic(n, e, d ,lat, h, radians):
#     """
#     Transform small perturbations from cartesian (in local navigation frame NED)  to geodetic, small angle
#     aproximation has to apply, which means norm(n,e,d) <<< Earth Radius
#     """
#     if not radians :
#         lat = lat * np.pi / 180
# 
#     RE = WGS84_A / np.sqrt((1-(np.sin(lat)**2)*(WGS84_E**2))**3)
#     RN = WGS84_A*(1-WGS84_E**2) / np.sqrt(1-(np.sin(lat)**2)*(WGS84_E**2))
# 
#     deltaLat = n / (RN+h)
#     deltaLon = e / ((RE+h)*np.cos(lat))
#     deltaH = -1*d
# 
#     if radians:
#         return (deltaLat, deltaLon, deltaH)
#     else:
#         return ((deltaLat * 180 / np.pi, deltaLon * 180 / np.pi, deltaH))
# 
# #-------------------------------------------------------------------------------
# 
# def haversine(lon1, lat1, lon2, lat2, r=6371):
#     """
#     Calculate the great circle distance between two points
#     on the earth (specified in decimal degrees) using the Haversine formula
# 
#     Return units: kilometers
# 
#     Extracted from http://stackoverflow.com/questions/4913349
# 
#     >>> haversine(0, 0, 0, 0)
#     0.0
# 
#     Example extracted from https://rosettacode.org/wiki/Haversine_formula
# 
#     >>> haversine(-86.67, 36.12, -118.40, 33.94, r=6372.8)
#     2887.259950607111
#     """
#     # convert decimal degrees to radians
#     lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
# 
#     # haversine formula
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
#     c = 2 * math.asin(math.sqrt(a))
# 
#     return c * r
# 
# #-------------------------------------------------------------------------------
# 
# 
# def area_triangle_in_sphere(coords, r=6371):
#     """
# 
#     Area = pi*R^2*E/180
# 
#     R = radius of sphere
#     E = spherical excess of triangle, E = A + B + C - 180
#     A, B, C = angles of spherical triangle in degrees
# 
#     tan(E/4) = sqrt(tan(s/2)*tan((s-a)/2)*tan((s-b)/2)*tan((s-c)/2))
# 
#     where
# 
#     a, b, c = sides of spherical triangle
#     s = (a + b + c)/2
# 
#     http://mathforum.org/library/drmath/view/65316.html
# 
#     # Compute approximate area of India (3287263 km2)
#     >>> pWest = (68.752441, 23.483401)
#     >>> pEast = (90.153809, 22.87744)
#     >>> pNorth = (76.723022, 32.87036)
#     >>> pSouth = (77.45636, 8.119053)
#     >>> triangle1 = (pWest,pEast,pNorth)
#     >>> triangle2 = (pWest,pEast,pSouth)
#     >>> area_triangle_in_sphere(triangle1) + area_triangle_in_sphere(triangle2)
#     3028215.293314756
#     """
# 
#     # Compute the spherical areas using the haversine method
#     a = haversine(coords[0][0], coords[0][1], coords[1][0], coords[1][1], r=1)
#     b = haversine(coords[1][0], coords[1][1], coords[2][0], coords[2][1], r=1)
#     c = haversine(coords[0][0], coords[0][1], coords[2][0], coords[2][1], r=1)
# 
#     s = (a + b + c) / 2.0
# 
#     tanE = math.sqrt(math.tan(s/2)*math.tan((s-a)/2)*math.tan((s-b)/2)*math.tan((s-c)/2))
# 
#     E = math.atan(tanE * 4.0)
# 
#     area = r*r*E
# 
#     return area
# 
# #-------------------------------------------------------------------------------


class Dop(object):
    """
    Class that implements computation of Dilution of Precision (DOP)
    

    Check that dop from NMEA GPGSV is the same as the one in NMEA GPGSA message
    (further investigations need to be conducted if NMEA generated by u-blox NEO 6P,
    discrepancies have been found)

    $GPGSA,A,3,10,07,05,02,29,04,08,13,,,,,1.72,1.03,1.38*0A
    $GPGSV,3,1,11,10,63,137,17,07,61,098,15,05,59,290,20,08,54,157,30*70
    $GPGSV,3,2,11,02,39,223,19,13,28,070,17,26,23,252,,04,14,186,14*79
    $GPGSV,3,3,11,29,09,301,24,16,09,020,,36,,,*76

    >>> elAz = [[63,137],
    ...         [61, 98],
    ...         [59,290],
    ...         [39,223],
    ...         [ 9,301],
    ...         [14,186],
    ...         [54,157],
    ...         [28, 70]]
    >>> dop = Dop(elAz)
    >>> f'{dop.pdop():.2f}'
    '1.72'
    >>> f'{dop.vdop():.2f}'
    '1.38'
    >>> f'{dop.hdop():.2f}'
    '1.04'


    Verification through the example of DOP computation proposed
    in Exercise 6-5 (page 228) of:

    Misra, P., Enge, P., "Global Positioning System: Signals, 
    Measurements and Performance", 2nd Edition. 2006

    Increasing 30 degrees the azimuth position of 3 sats (+ one in zenith), doubles the vdop value
    leaving pdop approximately constant

    >>> el_az_list = [[ 0,   0],
    ...               [ 0, 120],
    ...               [ 0, 240],
    ...               [90,   0]]
    >>> dop = Dop(el_az_list)
    >>> f'{dop.vdop():.2f}'
    '1.15'
    >>> f'{dop.hdop():.2f}'
    '1.15'

    >>> el_az_list = [[30,   0],
    ...               [30, 120],
    ...               [30, 240],
    ...               [90,  0]]
    >>> dop = Dop(el_az_list)
    >>> f'{dop.vdop():.2f}'
    '2.31'
    >>> f'{dop.hdop():.2f}'
    '1.33'
    """
    
    def __init__(self, el_az_list:typing.List[ElAz], angles_in_degrees:bool=True) -> None:
        
        self.el_az_list = el_az_list   
        self.angles_in_degrees = angles_in_degrees 
        self.__G()  # generate G matrix
        self.__Q()  # generate Q matrix


    def __G(self) -> None:
        """ 
        Construct geometry matrix G
        """

        elevations = [v[0] for v in self.el_az_list]
        azimuths = [v[1] for v in self.el_az_list]
        if self.angles_in_degrees:
            elevations = np.radians(elevations)
            azimuths = np.radians(azimuths)

        n_satellites = len(self.el_az_list)
        
        gx = np.cos(elevations) * np.sin(azimuths)
        gy = np.cos(elevations) * np.cos(azimuths)
        gz = np.sin(elevations)

        rows = list(zip(gx, gy, gz, [1]*n_satellites))

        self.G = np.array(rows)


    def __Q(self) -> None:
        """
        Construct co-factor matrix
        """
        try:
            self.Q = np.linalg.inv(np.dot(np.matrix.transpose(self.G), self.G))
        except np.linalg.linalg.LinAlgError as e:   
            self.Q = np.full([4, 4], np.nan)
            roktools.logger.warning("Could not compute DOP. Reason {}".format(e))

    def gdop(self) -> float:
        """
        Geometric DOP
        """

        return np.sqrt(self.Q[0, 0] + self.Q[1, 1] + self.Q[2, 2] + self.Q[3, 3])


    def pdop(self) -> float:
        """
        Position DOP
        """

        return np.sqrt(self.Q[0, 0] + self.Q[1, 1] + self.Q[2, 2])


    def tdop(self) -> float:
        """
        Time DOP
        """

        return np.sqrt(self.Q[3, 3])
        

    def vdop(self) -> float:
        """
        Vertical DOP
        """

        return np.sqrt(self.Q[2, 2])


    def hdop(self) -> float:
        """
        Horizontal DOP
        """

        return np.sqrt(self.Q[0, 0] + self.Q[1, 1])


if __name__ == "__main__":
    import doctest
    doctest.testmod(raise_on_error=True)
