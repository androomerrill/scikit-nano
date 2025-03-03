#! /usr/bin/env python

from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

# from pkg_resources import resource_filename

import nose
from nose.tools import assert_equal, assert_false, assert_true

import numpy as np

# from sknano.core import dedupe
# import sknano.core.atoms
# from sknano.core.atoms import StructureAtom, StructureAtoms
from sknano.generators import SWNTGenerator
# from sknano.io import DATAReader
# from sknano.core.structures import compute_Natoms
# from sknano.core.atoms import SelectionParser
from sknano.core.geometric_regions import Cylinder
from sknano.testing import AtomsTestFixture


class SelectionTestFixture(AtomsTestFixture):

    @AtomsTestFixture.atoms.getter
    def atoms(self):
        atoms = super().atoms
        atoms.center_centroid()
        return atoms

    @property
    def BNatoms(self):
        BNatoms = SWNTGenerator((10, 5), basis=['B', 'N']).atoms
        BNatoms.assign_unique_types()
        BNatoms.assign_unique_ids()
        BNatoms.center_centroid()
        return BNatoms


class Tests(SelectionTestFixture):

    def test1(self):
        atoms = self.atoms
        # atoms.update_attrs()
        atoms = atoms.select("id 1 2 3 4 5")
        assert_true(np.allclose(atoms.ids, [1, 2, 3, 4, 5]))

    def test2(self):
        atoms = self.atoms
        Natoms = atoms.Natoms
        atoms = atoms.select("not id 1 2 3 4 5")
        assert_true(np.allclose(atoms.ids, list(range(6, Natoms + 1))))

    def test3(self):
        atoms = self.atoms
        atoms = atoms.select("(id 1 2 3 4 5) or (id 99 100)")
        print(atoms.ids)
        assert_true(np.allclose(atoms.ids, [1, 2, 3, 4, 5, 99, 100]))

    def test4(self):
        atoms = self.atoms
        assert_false(all([atom.z >= 0 for atom in atoms]))
        atoms = atoms.select("z >= 0")
        assert_true(all([atom.z >= 0 for atom in atoms]))

    def test5(self):
        atoms = self.atoms
        assert_false(all([atom.z >= 0 for atom in atoms]))
        atoms = atoms.select("z >= 0 and x >= 0")
        assert_true(all([atom.z >= 0 for atom in atoms]))
        assert_true(all([atom.x >= 0 for atom in atoms]))

    def test6(self):
        atoms = self.BNatoms
        atoms = atoms.select("type 2")
        assert_true(all([atom.type == 2 for atom in atoms]))

    def test7(self):
        atoms = self.BNatoms
        Natoms = atoms.Natoms
        atoms = atoms.select("element B")
        assert_true(all([atom.element == 'B' for atom in atoms]))
        assert_equal(atoms.Natoms, Natoms / 2)

    def test8(self):
        atoms = self.BNatoms
        atoms = atoms.select("element B and z >= 0")
        assert_true(all([atom.element == 'B' for atom in atoms]))

    def test9(self):
        atoms = self.atoms
        atoms = atoms.select("within 1.5 of id 4 5 6 9")
        print(atoms.ids)
        assert_true(all([id in atoms.ids for id in (4, 5, 6, 9)]))

    def test10(self):
        atoms = self.atoms
        atoms = atoms.select("exwithin 1.5 of id 4 5 6 9")
        assert_true(all([id not in atoms.ids for id in (4, 5, 6, 9)]))

    def test11(self):
        atoms = self.atoms
        selstr1 = "within 1.5 of id 4 5 6 9"
        selstr2 = "not within 1.5 of id 4 5 6 9"

        sel1 = atoms.select(selstr1)
        sel2 = atoms.select(selstr2)
        print('atoms.select(selstr1={!r}).Natoms: {}'.format(
              selstr1, sel1.Natoms))
        print('atoms.select(selstr2={!r}).Natoms: {}'.format(
              selstr2, sel2.Natoms))

    def test12(self):
        atoms = self.atoms
        sel = atoms.select("all")
        assert_equal(atoms.Natoms, sel.Natoms)

    def test13(self):
        atoms = self.BNatoms
        selstr = "element B and y >= 0 and (not within 1.5 of id 4 5 6 9)"
        atoms = atoms.select(selstr)
        # atoms = atoms.select("within Sphere(r=1.0)")

    def test14(self):
        atoms = self.BNatoms
        selstr1 = "element B and y >= 0"
        selstr2 = "not within 1.5 of id 4 5 6 9"
        sel1 = atoms.select(selstr1)
        sel2 = atoms.select(selstr2)
        print('atoms.select(selstr1={!r}).Natoms: {}'.format(
              selstr1, sel1.Natoms))
        print('atoms.select(selstr2={!r}).Natoms: {}'.format(
              selstr2, sel2.Natoms))
        print('atoms.select(selstr1={!r}).ids: {}'.format(selstr1, sel1.ids))
        print('atoms.select(selstr2={!r}).ids: {}'.format(selstr2, sel2.ids))

        and_selection = atoms.select(' and '.join((selstr1, selstr2)))
        or_selection = atoms.select(' or '.join((selstr1, selstr2)))
        print('and_selection.Natoms: {}'.format(and_selection.Natoms))
        print('or_selection.Natoms: {}'.format(or_selection.Natoms))
        print('and_selection.ids: {}'.format(and_selection.ids))
        print('or_selection.ids: {}'.format(or_selection.ids))
        assert_equal(sorted(list(set(sel1.ids) & set(sel2.ids))),
                     sorted(and_selection.ids.tolist()))
        assert_equal(sorted(list(set(sel1.ids) | set(sel2.ids))),
                     sorted(or_selection.ids.tolist()))

    def test15(self):
        atoms = self.BNatoms
        print(atoms.bounds)

        print(atoms.Natoms)
        parallelepiped = \
            atoms.select("within Parallelepiped(o=[0, -5.2, 0])")
        print(parallelepiped.Natoms)
        sphere = atoms.select("within Sphere(r=6)", verbose=True)
        print(sphere.Natoms)

    def test16(self):
        atoms = self.dumpdata1.trajectory[-1].atoms
        atoms = atoms.select("within Cylinder(p1=[0,-15,0], p2=[0,25,0], r=15)")
        print(atoms.bounding_box)
        atoms = atoms.select("molid 1 2 3 4 5")
        mol_ids = list(set(atoms.mol_ids))
        print(mol_ids)
        assert_true(np.allclose(mol_ids, [1, 2, 3, 4, 5]))
        # selection_list = []
        # for i in range(1, 9):
        #     selection_list.append(atoms.select('mol_id {}'.format(i)))


if __name__ == '__main__':
    nose.runmodule()
