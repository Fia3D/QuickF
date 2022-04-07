import bpy

from ..utilities.utilities import get_all_materials_in_selected_objects, show_message_box

#################################################################################
# Operator
#################################################################################
class QUICKF_OT_images_change_alpha_mode(bpy.types.Operator):
	''' Change Images Alpha Mode '''
	bl_idname = "quickf.images_change_alpha_mode"
	bl_label = "Change Alpha Mode"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def menu_draw(self, context):
		self.layout.operator(QUICKF_OT_images_change_alpha_mode.bl_idname)

	def execute(self, context):
		_change_alpha_mode_image_in_materials(get_all_materials_in_selected_objects(), "CHANNEL_PACKED")
		return {'FINISHED'}

#################################################################################
# Functions
#################################################################################
def _change_alpha_mode_image_in_materials(mats, mode):
	images = set()
	for mat in mats:
		if mat.name != "Dots Stroke":
			for node in mat.node_tree.nodes:
				if node.type != "TEX_IMAGE":
					continue
				if node.image in images:
					continue
				if node.image.alpha_mode == mode:
					continue

				images.add(node.image)
				node.image.alpha_mode=mode
	
	show_message_box("Changed {} image(s) alpha mode".format(len(images)), title="Result")