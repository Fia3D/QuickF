# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
	"name" : "QuickF",
	"description" : "Quick clean and change operations in the file",
	"author" : "Fia",
	"version" : (0, 1, 0),
	"blender" : (3, 1, 0),
	"location" : "Editor > QuickF",
	"support" : "COMMUNITY",
	"category" : "Utility"
}

import bpy

from .menu.menu_editor import QUICKF_MT_editor, QUICKF_MT_editor_clean, QUICKF_MT_editor_rename, QUICKF_MT_editor_rename_images, QUICKF_MT_editor_rename_objects
from .menu.menu_view3d_object import QUICKF_MT_view3d_object, QUICKF_MT_view3d_object_images

from .actions.open_asset_browser import QUICKF_OT_open_asset_browser
from .actions.clean_unused_material_slot import QUICKF_OT_clean_unused_material_slot
from .actions.rename_data_by_object_name import QUICKF_OT_rename_data_by_object_name
from .actions.rename_images_extension import QUICKF_OT_rename_images_extension_exr_to_png, QUICKF_OT_rename_images_extension_tga_to_png, QUICKF_OT_rename_images_extension_dds_to_png
from .actions.clean_duplicated_textures import QUICKF_OT_clean_duplicated_texture
from .actions.rename_images_by_filename import QUICKF_OT_rename_images_by_filename

from .actions.images_change_alpha_mode import QUICKF_OT_images_change_alpha_mode
from .actions.images_pack import QUICKF_OT_images_pack
from .actions.images_unpack import QUICKF_OT_images_unpack

####################################################
# Register
####################################################
classes = [
	# MENU EDITOR
	QUICKF_MT_editor, 
	QUICKF_MT_editor_clean,
	QUICKF_MT_editor_rename,
	QUICKF_MT_editor_rename_images,
	QUICKF_MT_editor_rename_objects,

	# EDITOR open_asset_browser
	QUICKF_OT_open_asset_browser,

	# REMOVE 
	QUICKF_OT_clean_unused_material_slot,
	QUICKF_OT_clean_duplicated_texture,

	# RENAME OBJECTS
	QUICKF_OT_rename_data_by_object_name,

	# RENAME IMAGES
	QUICKF_OT_rename_images_by_filename,
	QUICKF_OT_rename_images_extension_tga_to_png,
	QUICKF_OT_rename_images_extension_dds_to_png,
	QUICKF_OT_rename_images_extension_exr_to_png,

	#############################################
	
	# MENU VIEW3D OBJECT
	QUICKF_MT_view3d_object,
	QUICKF_MT_view3d_object_images,

	# IMAGES
	QUICKF_OT_images_change_alpha_mode,
	QUICKF_OT_images_pack,
	QUICKF_OT_images_unpack
]

def register():
	for c in classes:
		bpy.utils.register_class(c)
	
	bpy.types.TOPBAR_MT_editor_menus.append(QUICKF_MT_editor.menu_draw)
	bpy.types.VIEW3D_MT_object.append(QUICKF_MT_view3d_object.menu_draw)
	bpy.types.VIEW3D_MT_object_context_menu.append(QUICKF_MT_view3d_object.menu_draw)
	
def unregister():
	bpy.types.VIEW3D_MT_object_context_menu.remove(QUICKF_MT_view3d_object.menu_draw)
	bpy.types.VIEW3D_MT_object.remove(QUICKF_MT_view3d_object.menu_draw)
	bpy.types.TOPBAR_MT_editor_menus.remove(QUICKF_MT_editor.menu_draw)

	for c in classes:
		bpy.utils.unregister_class(c)

if __name__ == '__main__':
	register()