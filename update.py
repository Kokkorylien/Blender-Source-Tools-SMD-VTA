#  Copyright (c) 2014 Tom Edwards contact@steamreview.org
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Modified by Kokkorylien, 2026-10-25: open this edition's releases
# instead of downloading and installing the upstream package.

import bpy
from .utils import get_id

RELEASES_URL = "https://github.com/Kokkorylien/Blender-Source-Tools-SMD-VTA/releases"

class SmdToolsUpdate(bpy.types.Operator):
	bl_idname = "script.update_smd"
	bl_label = get_id("updater_title")
	bl_description = get_id("updater_title_tip")

	def execute(self, _):
		return bpy.ops.wm.url_open(url=RELEASES_URL)
