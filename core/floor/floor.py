import bpy
import bmesh
from .floor_types import flr_multistorey

from ...utils import (
    get_edit_mesh,
    kwargs_from_props
    )


class Floor:

    @classmethod
    def build(cls, context, props):
        """ Build floorplan geomerty from properties """

        # -- ensure that the mesh is a valid floorplan - (planar)
        if not cls.check_planar():
            return

        kwargs = kwargs_from_props(props)
        flr_multistorey(**kwargs)

    @classmethod
    def check_planar(cls):
        """ Check to see in active mesh is planar """

        # -- get current object bmesh
        me = get_edit_mesh()
        bm = bmesh.from_edit_mesh(me)

        # -- check that all verts are on same z coordinate
        if len(set([v.co.z for v in bm.verts])) == 1:
            return True
        return False
