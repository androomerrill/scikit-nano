# -*- coding: utf-8 -*-
"""
===============================================================================
Atom class for MD trajectory analysis (:mod:`sknano.core.atoms._md_atom`)
===============================================================================

An `Atom` class for molecular dynamics trajectory analysis.

.. currentmodule:: sknano.core.atoms._md_atom

"""
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals
__docformat__ = 'restructuredtext en'

import numpy as np

import sknano.core.atoms

from . import StructureAtom as Atom

__all__ = ['MDAtom']


class MDAtom(Atom):
    """An `Atom` class for molecular dynamics trajectory analysis.

    """
    def __init__(self, *args, reference_atom=None, t0_atom=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.reference_atom = reference_atom
        self.t0_atom = t0_atom
        try:
            self.r0 = t0_atom.r
        except AttributeError:
            pass

    @property
    def NN(self):
        return super().NN

    @NN.setter
    def NN(self, value):
        """Set nearest-neighbor `Atoms`."""
        # if self.reference_atom is not None:
        try:
            value = sknano.core.atoms.MDAtoms(
                atoms=[value[value.ids.tolist().index(atom.id)]
                       if atom.id in value.ids else
                       self.__class__(reference_atom=atom.reference_atom,
                                      element=atom.element, id=atom.id,
                                      mol=atom.mol, type=atom.type,
                                      mass=atom.mass, q=atom.q,
                                      x=np.inf, y=np.inf, z=np.inf,
                                      CN=atom.CN, NN=atom.NN)
                       for atom in self.reference_atom.NN])
        except AttributeError:
            pass
        super(MDAtom, MDAtom).NN.__set__(self, value)

    @NN.deleter
    def NN(self):
        super(MDAtom, MDAtom).NN.__delete__(self)

    def todict(self):
        super_dict = super().todict()
        super_dict.update(dict(reference_atom=self.reference_atom,
                               NN=self.NN))
        return super_dict
