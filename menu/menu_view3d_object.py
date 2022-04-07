import bpy

from ..actions.images_change_alpha_mode import QUICKF_OT_images_change_alpha_mode
from ..actions.images_pack import QUICKF_OT_images_pack
from ..actions.images_unpack import QUICKF_OT_images_unpack

####################################################
# Menus
####################################################
class QUICKF_MT_view3d_object(bpy.types.Menu):
	bl_label = "QuickF"

	def draw(self, context):
		layout = self.layout
		self.layout.menu(QUICKF_MT_view3d_object_images.__name__)

	def menu_draw(self, context):
		self.layout.separator()
		self.layout.menu(QUICKF_MT_view3d_object.__name__)

class QUICKF_MT_view3d_object_images(bpy.types.Menu):
	bl_label = "Images"

	def draw(self, context):
		layout = self.layout
		layout.operator(QUICKF_OT_images_change_alpha_mode.bl_idname)
		layout.operator(QUICKF_OT_images_pack.bl_idname)
		layout.operator(QUICKF_OT_images_unpack.bl_idname)


	def menu_draw(self, context):
		self.layout.separator()
		self.layout.menu(QUICKF_MT_view3d_object.__name__)