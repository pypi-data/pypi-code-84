#  Copyright (c) 2021, Manfred Moitzi
#  License: MIT License

import pytest
import ezdxf
from ezdxf.disassemble import recursive_decompose


@pytest.fixture(scope='module')
def doc():
    d = ezdxf.new()
    l0 = d.blocks.new('L0')
    build_level_0(l0)
    l1 = d.blocks.new('L1')
    build_nesting_level_1(l1)
    return d


def build_level_0(l0):
    # Block of 4 lines in 4 different colors
    l0.add_line((1, -1), (1, 1), dxfattribs={'color': 1})
    l0.add_line((1, 1), (-1, 1), dxfattribs={'color': 2})
    l0.add_line((-1, 1), (-1, -1), dxfattribs={'color': 3})
    l0.add_line((-1, -1), (1, -1), dxfattribs={'color': 4})


def scale(sx, sy, sz):
    return {
        'xscale': sx,
        'yscale': sy,
        'zscale': sz,
    }


def build_nesting_level_1(l1, name='L0'):
    l1.add_blockref(name, (0, 0), dxfattribs=scale(1, 1, 1))
    l1.add_blockref(name, (3, 0), dxfattribs=scale(-1, 1, 1))
    l1.add_blockref(name, (6, 0), dxfattribs=scale(1, -1, 1))
    l1.add_blockref(name, (9, 0), dxfattribs=scale(-1, -1, 1))
    l1.add_blockref(name, (0, 3), dxfattribs=scale(1, 1, -1))
    l1.add_blockref(name, (3, 3), dxfattribs=scale(-1, 1, -1))
    l1.add_blockref(name, (6, 3), dxfattribs=scale(1, -1, -1))
    l1.add_blockref(name, (9, 3), dxfattribs=scale(-1, -1, -1))


def count(doc, block_names) -> int:
    count = 1
    for name in block_names:
        block = doc.blocks.get(name)
        count *= len(block)
    return count


def test_decompose_block_level_0(doc):
    l0 = doc.blocks.get('L0')
    result = list(recursive_decompose(l0))
    assert len(result) == count(doc, ['L0'])


REFLECTIONS = [(1, 1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]
NAMES = ["normal", "reflect-x", "reflect-y", "reflect-z", ]


@pytest.mark.parametrize("sx,sy,sz", REFLECTIONS, ids=NAMES)
def test_decompose_block_reference_level_0(doc, sx, sy, sz):
    msp = doc.modelspace()
    msp.delete_all_entities()
    msp.add_blockref('L0', (0, 0), dxfattribs=scale(sx, sy, sz))
    result = list(recursive_decompose(msp))
    assert len(result) == count(doc, ['L0'])


def test_decompose_block_level_1(doc):
    l1 = doc.blocks.get('L1')
    types = [e.dxftype() for e in recursive_decompose(l1)]
    assert len(types) == count(doc, ['L0', 'L1'])
    assert set(types) == {'LINE'}, "expected only LINES"


@pytest.mark.parametrize("sx,sy,sz", REFLECTIONS, ids=NAMES)
def test_decompose_block_reference_level_1(doc, sx, sy, sz):
    msp = doc.modelspace()
    msp.delete_all_entities()
    msp.add_blockref('L1', (0, 0), dxfattribs=scale(sx, sy, sz))
    types = [e.dxftype() for e in recursive_decompose(msp)]
    assert len(types) == count(doc, ['L0', 'L1'])
    assert set(types) == {'LINE'}, "expected only LINES"


def test_decompose_minsert_level_1(doc):
    nrows = 2
    ncols = 2
    expected_count = count(doc, ['L0', 'L1']) * nrows * ncols

    msp = doc.modelspace()
    msp.delete_all_entities()
    msp.add_blockref('L1', (0, 0), dxfattribs={
        'row_count': nrows,
        'row_spacing': 5,
        'column_count': ncols,
        'column_spacing': 5,
    })
    types = [e.dxftype() for e in recursive_decompose(msp)]
    assert len(types) == expected_count
    assert set(types) == {'LINE'}, "expected only LINES"


if __name__ == '__main__':
    pytest.main([__file__])
