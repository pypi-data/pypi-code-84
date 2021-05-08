#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class SourceParticle(object):
    ''' class Source particle'''

    def __init__(self):
        self._xxx = -1.0
        self._yyy = -1.0
        self._zzz = -1.0
        self._cell_id = -1
        self._mat_id = -1
        self._mesh_id = -1

    @property
    def xxx(self):
        return self._xxx

    @xxx.setter
    def xxx(self, value):
        if not isinstance(value, float):
            raise ValueError('xxx must be float')
        self._xxx = value

    @property
    def yyy(self):
        return self._yyy

    @yyy.setter
    def yyy(self, value):
        if not isinstance(value, float):
            raise ValueError('yyy must be float')
        self._yyy = value

    @property
    def zzz(self):
        return self._zzz

    @zzz.setter
    def zzz(self, value):
        if not isinstance(value, float):
            raise ValueError('zzz must be float')
        self._zzz = value

    @property
    def cell_id(self):
        return self._cell_id

    @cell_id.setter
    def cell_id(self, value):
        if not isinstance(value, int):
            raise ValueError('cell_id of source particle must be int')
        if value > 100000 or value < 1:
            raise ValueError(
                'cell_id of source particle must in the range of 1 ~ 100000')
        self._cell_id = value

    @property
    def mat_id(self):
        return self._mat_id

    @mat_id.setter
    def mat_id(self, value):
        if not isinstance(value, int):
            raise ValueError('mat_id of source particle must be integer')
        if value > 100000 or value < 0:
            raise ValueError(
                'mat_id of source particle must in the range of 0 ~ 100000')
        self._mat_id = value

    @property
    def mesh_id(self):
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, value):
        if not isinstance(value, int):
            raise ValueError('mesh_id of source particle must be integer')
        if value != -1 and value < 0:
            raise ValueError(
                'mesh_id of source particle must no smaller than 0 (except -1)')
        self._mesh_id = value


######################################################################
######################################################################
def get_source_particles(MCNP_PTRAC):
    """get source particle information form ptrac file
    input: MCNP_PTRAC, this is the file name of the patrc.
    return: SourceParticles, this is a list of SourceParticle"""

    SourceParticles = []
    # open the ptrac file
    fin = open(MCNP_PTRAC)
    for line in fin:
        line_ele = line.split()
        temp_s = SourceParticle()
        if len(line_ele) == 6:
            temp_s.cell_id = int(line_ele[3])
            temp_s.mat_id = int(line_ele[4])
            SourceParticles.append(temp_s)
        if len(line_ele) == 9:
            SourceParticles[-1].xxx = float(line_ele[0])
            SourceParticles[-1].yyy = float(line_ele[1])
            SourceParticles[-1].zzz = float(line_ele[2])

    fin.close()
    return SourceParticles


