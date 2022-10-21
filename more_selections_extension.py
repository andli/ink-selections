#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) [YEAR] [YOUR NAME], [YOUR EMAIL]
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""
This extension gives you more selection options.
"""

import inkex
from inkex.elements import *


class MoreSelectionsExtension(inkex.EffectExtension):
    """EffectExtension to select lines pointing up"""

    def add_arguments(self, pars):
        pars.add_argument("--found_layer", type=str, default="Found")  # inkex.Layer
        pars.add_argument("--select_option", type=str, default="horizontal")

    def effect(self):
        """
        Effect behaviour.
        Search for all paths that match condition
        """
        found_layer = self.options.found_layer
        selection_option = self.options.select_option
        print(found_layer)
        print(selection_option)

        for elem in self.svg.selection.filter(inkex.PathElement):
            elem.set("inkscape:modified_by_tutorial", "Yes")
            elem.style["stroke-width"] = 6.0
            self.svg.selection.add(elem)
            # selection.add(elem)


if __name__ == "__main__":
    MoreSelectionsExtension().run()
