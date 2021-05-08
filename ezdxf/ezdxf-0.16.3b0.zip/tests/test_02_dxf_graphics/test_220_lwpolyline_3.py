#  Copyright (c) 2021, Manfred Moitzi
#  License: MIT License

import pytest

from ezdxf.entities import factory
from ezdxf.path import make_path


@pytest.fixture
def i329():
    e = factory.new(
        'LWPOLYLINE',
        dxfattribs={
            'layer': "0",
            'flags': 1,
            'const_width': 0.0,
        },
    )
    e.set_points([
        (65998.39650964737, 18466.88688385487, 0.0, 0.0, 0.0),
        (65977.89650949836, 18466.88688382506, 0.0, 0.0, 0.0),
        (65977.89650899172, 18669.88688378036, 0.0, 0.0, 0.0),
        (65998.39650905877, 18669.88688381016, 0.0, 0.0, 0.0),
        (65998.39650928229, 18585.08688393235, 0.0, 0.0, 0.414213562196322),
        (66008.59650930017, 18574.88688395917, 0.0, 0.0, -2.484539e-10),
        (66150.19650941342, 18574.8868842423, 0.0, 0.0, 0.4142135632974055),
        (66160.3965094015, 18585.08688431978, 0.0, 0.0, 0.0),
        (66160.39650917053, 18669.8868842423, 0.0, 0.0, 0.0),
        (66180.89650899917, 18669.886884287, 0.0, 0.0, 0.0),
        (66180.89650952816, 18466.8868843168, 0.0, 0.0, 0.0),
        (66160.39650961757, 18466.8868842423, 0.0, 0.0, 0.0),
        (66160.39650934935, 18551.68688428402, 0.0, 0.0, 0.4142135607378567),
        (66150.19650932401, 18561.8868842721, 0.0, 0.0, 0.0),
        (66008.59650933743, 18561.88688386977, 0.0, 0.0, 0.4179324604143259),
        (65998.39650934935, 18551.68688383698, 0.0, 0.0, 0.0),
        (65998.39650964737, 18466.88688385487, 0.0, 0.0, 0.0),
    ])
    return e


def test_lwpolyline_to_path(i329):
    p = make_path(i329)
    assert len(p) == 18

    vertices = list(p.flattening(0.01))
    assert len(vertices) == 141


if __name__ == '__main__':
    pytest.main([__file__])
