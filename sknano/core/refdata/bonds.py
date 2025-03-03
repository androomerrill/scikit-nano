# -*- coding: utf-8 -*-
"""
=========================================================
Reference bond data (:mod:`sknano.core.refdata.bonds`)
=========================================================

.. currentmodule:: sknano.core.refdata.bonds

"""
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import os

# from sknano.core.atoms.mixins import Bond
from sknano.core import dumpobj, loadobj

aCC = C_C = CCbond = 1.42  # angstroms
C_H = CHbond = 1.09  # angstroms

__all__ = ['dump_bond_data', 'load_bond_data',
           'aCC', 'C_C', 'CCbond', 'C_H', 'CHbond']

_bond_file = os.path.join(os.path.dirname(__file__), 'bonds.yaml')


def dump_bond_data(data):
    """dump bond data"""
    dumpobj(data, _bond_file)


def load_bond_data():
    """load bond data"""
    return loadobj(_bond_file)
