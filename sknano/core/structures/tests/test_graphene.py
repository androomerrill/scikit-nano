# -*- coding: utf-8 -*-
#
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import warnings
warnings.simplefilter('always')

import nose
from nose.tools import assert_equal, assert_true

import numpy as np

from sknano.core.structures import Graphene, PrimitiveCellGraphene, \
    ConventionalCellGraphene, GraphenePrimitiveCell, \
    GrapheneConventionalCell, BilayerGraphene


def test1():
    s = Graphene(armchair_edge_length=10, zigzag_edge_length=10)
    assert_equal(s.zigzag_edge_length, 10)
    assert_equal(s.armchair_edge_length, 10)
    assert_true(isinstance(s, ConventionalCellGraphene))
    assert_true(isinstance(s.unit_cell, GrapheneConventionalCell))
    assert_equal(s.unit_cell.basis.Natoms, 4)
    assert_true(np.allclose(s.unit_cell.lattice.angles, 3 * [90.0]))


def test2():
    s = PrimitiveCellGraphene(edge_length=10)
    assert_equal(s.edge_length, 10)
    assert_true(isinstance(s, PrimitiveCellGraphene))
    assert_true(isinstance(s.unit_cell, GraphenePrimitiveCell))
    assert_true(np.allclose(np.degrees(s.r1.angle(s.r2)), 60.0))
    assert_equal(s.unit_cell.basis.Natoms, 2)
    print(s)


def test3():
    s = ConventionalCellGraphene(armchair_edge_length=10,
                                 zigzag_edge_length=10)
    assert_equal(s.l1, 10)
    assert_equal(s.l2, 10)
    assert_true(isinstance(s, ConventionalCellGraphene))
    assert_true(isinstance(s.unit_cell, GrapheneConventionalCell))
    print(s.unit_cell)
    print(s.area)
    print(s)


def test4():
    s = Graphene.from_conventional_cell(armchair_edge_length=10,
                                        zigzag_edge_length=10)
    assert_equal(s.zigzag_edge_length, 10)
    assert_equal(s.armchair_edge_length, 10)
    assert_true(isinstance(s.unit_cell, GrapheneConventionalCell))
    # print(s.unit_cell)
    assert_true(isinstance(s, ConventionalCellGraphene))


def test5():
    s = Graphene.from_primitive_cell(edge_length=10)
    assert_true(isinstance(s, PrimitiveCellGraphene))
    assert_true(isinstance(s.unit_cell, GraphenePrimitiveCell))


def test6():
    blg = BilayerGraphene(armchair_edge_length=10, zigzag_edge_length=10,
                          layer_rotation_increment=45, degrees=True)
    assert_equal(blg.nlayers, 2)
    assert_equal(blg.layer_rotation_angles[-1], np.pi/4)

if __name__ == '__main__':
    nose.runmodule()
