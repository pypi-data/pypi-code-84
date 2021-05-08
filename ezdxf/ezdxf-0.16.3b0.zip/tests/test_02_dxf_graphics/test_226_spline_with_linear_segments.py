#  Copyright (c) 2021, Manfred Moitzi
#  License: MIT License

import pytest
from ezdxf.entities import Spline
import ezdxf.path


def test_flatten_spline():
    spline = make_spline_with_linear_segments()
    points = list(spline.flattening(0.01))
    assert len(points) == 161


def test_make_path():
    spline = make_spline_with_linear_segments()
    path = ezdxf.path.make_path(spline)
    assert len(path) == 22
    assert linear_segments(path) == 12


def linear_segments(path: ezdxf.path.Path):
    cmd = ezdxf.path.Command
    return sum(1 for curve in path if curve.type == cmd.LINE_TO)


def make_spline_with_linear_segments():
    s = Spline()
    s.dxf.degree = 3
    s.control_points = [
        (56.22273085144742, -52.38516304166649, 0.0),
        (56.22273085144742, -52.38516304166649, 0.0),
        (239.1976236415998, -52.38516304166649, 0.0),
        (239.1976236415998, -52.38516304166649, 0.0),
        (240.3021931409851, -52.38516304166649, 0.0),
        (241.1976236410993, -53.28059354178134, 0.0),
        (241.1976236410993, -54.38516304116636, 0.0),
        (241.1976236410993, -54.38516304116636, 0.0),
        (241.1976236410993, -62.34529113912412, 0.0),
        (241.1976236410993, -62.34529113912412, 0.0),
        (241.1976236410993, -62.34529113912412, 0.0),
        (241.1976236410993, -77.39045415751698, 0.0),
        (241.1976236410993, -77.39045415751698, 0.0),
        (241.1976236410993, -78.49328674892469, 0.0),
        (240.3049021562092, -79.38799615050624, 0.0),
        (239.2020722930055, -79.39044920938571, 0.0),
        (239.2020722930055, -79.39044920938571, 0.0),
        (233.6681749915751, -79.40275842984373, 0.0),
        (233.6681749915751, -79.40275842984373, 0.0),
        (232.5653451283714, -79.40521148872287, 0.0),
        (231.6726236434806, -80.29992089030473, 0.0),
        (231.6726236434806, -81.40275348171245, 0.0),
        (231.6726236434806, -81.40275348171245, 0.0),
        (231.6726236434806, -96.45719719271867, 0.0),
        (231.6726236434806, -96.45719719271867, 0.0),
        (231.6726236434806, -97.561766692104, 0.0),
        (232.5680541435954, -98.4571971922182, 0.0),
        (233.6726236429801, -98.4571971922182, 0.0),
        (233.6726236429801, -98.4571971922182, 0.0),
        (234.4351236427904, -98.4571971922182, 0.0),
        (234.4351236427904, -98.4571971922182, 0.0),
        (235.5396931421758, -98.4571971922182, 0.0),
        (236.43512364229, -99.35262769233242, 0.0),
        (236.43512364229, -100.4571971917187, 0.0),
        (236.43512364229, -100.4571971917187, 0.0),
        (236.43512364229, -115.5181506304424, 0.0),
        (236.43512364229, -115.5181506304424, 0.0),
        (236.43512364229, -116.6184332447135, 0.0),
        (237.3238741828279, -117.512078028625, 0.0),
        (238.4241402052798, -117.5181204707455, 0.0),
        (238.4241402052798, -117.5181204707455, 0.0),
        (243.9709633052181, -117.5485825197861, 0.0),
        (243.9709633052181, -117.5485825197861, 0.0),
        (245.07122932767, -117.5546249619067, 0.0),
        (245.9599798682079, -118.4482697458182, 0.0),
        (245.9599798682079, -119.5485523600892, 0.0),
        (245.9599798682079, -119.5485523600892, 0.0),
        (245.9599798682079, -161.5989385369997, 0.0),
        (245.9599798682079, -161.5989385369997, 0.0),
        (245.9599798682079, -162.7033810946488, 0.0),
        (245.0647474718881, -163.5987590049695, 0.0),
        (243.9603049288262, -163.5989385100843, 0.0),
        (243.9603049288262, -163.5989385100843, 0.0),
        (56.22327959401533, -163.6294514203422, 0.0),
        (56.22327959401533, -163.6294514203422, 0.0),
        (54.01388681794636, -163.6298105130854, 0.0),
        (52.22262959575984, -161.838844498455, 0.0),
        (52.2226294747784, -159.6294516932054, 0.0),
        (52.2226294747784, -159.6294516932054, 0.0),
        (52.22262382108676, -56.3802148685014, 0.0),
        (52.22262382108676, -56.3802148685014, 0.0),
        (52.22262372278778, -54.17103400176151, 0.0),
        (54.01354998549841, -52.38015558004202, 0.0),
        (56.22273085144742, -52.38021469295069, 0.0),
        (56.22273085144742, -52.38021469295069, 0.0),
        (56.22273085144742, -52.38516304166649, 0.0),
        (56.22273085144742, -52.38516304166649, 0.0),
    ]
    s.knots = [
        0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0,
        4.0, 4.0, 5.0, 5.0, 5.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 8.0, 8.0, 8.0,
        9.0, 9.0, 9.0, 10.0, 10.0, 10.0, 11.0, 11.0, 11.0, 12.0, 12.0, 12.0,
        13.0, 13.0, 13.0, 14.0, 14.0, 14.0, 15.0, 15.0, 15.0, 16.0, 16.0, 16.0,
        17.0, 17.0, 17.0, 18.0, 18.0, 18.0, 19.0, 19.0, 19.0, 20.0, 20.0, 20.0,
        21.0, 21.0, 21.0, 22.0, 22.0, 22.0, 22.0,
    ]
    return s


if __name__ == '__main__':
    pytest.main([__file__])
