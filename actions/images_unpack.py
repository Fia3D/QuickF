import bpy

from ..utilities.utilities import get_all_materials_in_selected_objects, show_message_box

#################################################################################
# Operator
#################################################################################
class QUICKF_OT_images_unpack(bpy.types.Operator):
	'''Unpack Images from Objects'''
	bl_idname = "quickf.images_unpack"
	bl_label = "Unpack"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def menu_draw(self, context):
		self.layout.operator(QUICKF_OT_images_unpack.bl_idname)

	def execute(self, context):
		_image_unpack_in_materials(get_all_materials_in_selected_objects())
		return {'FINISHED'}

#################################################################################
# Functions
#################################################################################
def _image_unpack_in_materials(mats):
	images = set()

	mat : bpy.types.Material
	for mat in mats:
		if mat.name != "Dots Stroke":
			
			node : bpy.types.ShaderNode
			for node in mat.node_tree.nodes:
				if node.type != "TEX_IMAGE":
					continue
				
				node : bpy.types.ShaderNodeTexImage
				
				if node.image in images:
					continue
				if node.image.packed_file is None:
					continue
				
				images.add(node.image)
				node.image.unpack()
	
	show_message_box("Unpacked {} image(s)".format(len(images)), title="Result")