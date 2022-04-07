import bpy

from ..actions.open_asset_browser import QUICKF_OT_open_asset_browser
from ..actions.clean_unused_material_slot import QUICKF_OT_clean_unused_material_slot
from ..actions.rename_data_by_object_name import QUICKF_OT_rename_data_by_object_name
from ..actions.rename_images_extension import QUICKF_OT_rename_images_extension_exr_to_png, QUICKF_OT_rename_images_extension_tga_to_png, QUICKF_OT_rename_images_extension_dds_to_png
from ..actions.clean_duplicated_textures import QUICKF_OT_clean_duplicated_texture
from ..actions.rename_images_by_filename import QUICKF_OT_rename_images_by_filename

####################################################
# Menus
####################################################
class QUICKF_MT_editor(bpy.types.Menu):
	bl_label = "QuickF"

	def draw(self, context):
		layout = self.layout
		layout.operator(QUICKF_OT_open_asset_browser.bl_idname)
		layout.menu(QUICKF_MT_editor_clean.__name__)
		layout.menu(QUICKF_MT_editor_rename.__name__)

	def menu_draw(self, context):
		self.layout.menu(QUICKF_MT_editor.__name__)

class QUICKF_MT_editor_clean(bpy.types.Menu):
	bl_label = "Clean"

	def draw(self, context):
		layout = self.layout
		layout.operator(QUICKF_OT_clean_unused_material_slot.bl_idname)
		layout.operator(QUICKF_OT_clean_duplicated_texture.bl_idname)


class QUICKF_MT_editor_rename(bpy.types.Menu):
	bl_label = "Rename"

	def draw(self, context):
		layout = self.layout
		layout.menu(QUICKF_MT_editor_rename_images.__name__)
		layout.menu(QUICKF_MT_editor_rename_objects.__name__)

class QUICKF_MT_editor_rename_images(bpy.types.Menu):
	bl_label = "Images"

	def draw(self, context):
		layout = self.layout
		layout.operator(QUICKF_OT_rename_images_by_filename.bl_idname)
		layout.separator()
		layout.operator(QUICKF_OT_rename_images_extension_tga_to_png.bl_idname)
		layout.operator(QUICKF_OT_rename_images_extension_dds_to_png.bl_idname)
		layout.operator(QUICKF_OT_rename_images_extension_exr_to_png.bl_idname)

class QUICKF_MT_editor_rename_objects(bpy.types.Menu):
	bl_label = "Datas"

	def draw(self, context):
		layout = self.layout
		layout.operator(QUICKF_OT_rename_data_by_object_name.bl_idname)