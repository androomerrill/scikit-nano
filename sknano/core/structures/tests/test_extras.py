# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import nose
from nose.tools import assert_equal
from sknano.core.structures import filter_Ch_list, generate_Ch_list, \
    generate_Ch_property_grid, get_chiral_type


def test1():
    Ch_list = generate_Ch_list(ni=5, nf=20, mi=0, mf=20, handedness='right')
    Ch_list = filter_Ch_list(Ch_list)
    assert_equal(len(Ch_list), 216)


def test2():
    list1 = generate_Ch_list(ni=5, nf=20, mi=0, mf=20, handedness='right')
    list2 = generate_Ch_list(ni=5, imax=20, handedness='right')
    assert_equal(len(list1), 216)
    assert_equal(list1, list2)


def test3():
    Ch_grid = generate_Ch_property_grid(compute='compute_dt', imax=20)
    assert_equal(Ch_grid.shape, (21, 21))


def test4():
    Ch_list = generate_Ch_list(ni=5, nf=20, mi=0, mf=20,
                               chiral_types='achiral')
    assert_equal(len(Ch_list), 3 * 16)
    chiral_types = [get_chiral_type(Ch) for Ch in Ch_list]
    assert_equal(set(chiral_types), {'armchair', 'zigzag'})


def test5():
    Ch_list = generate_Ch_list(ni=2, nf=5, mi=0, mf=4, handedness='right')
    Ch_list = filter_Ch_list(Ch_list, property_filters=[('n', '<=', 4)])
    assert_equal(Ch_list, generate_Ch_list(ni=2, nf=4, mi=0, mf=4,
                                           handedness='right'))

if __name__ == '__main__':
    nose.runmodule()
