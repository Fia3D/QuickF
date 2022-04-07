import bpy

from ..utilities.utilities import get_all_materials, show_message_box

#################################################################################
# Operator
#################################################################################
class QUICKF_OT_clean_duplicated_texture(bpy.types.Operator):
	'''Remove all duplicated texture using the same image and reasign properly Users'''
	bl_idname = "quickf.clean_duplicated_texture"
	bl_label = "Duplicated textures"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		_clean_duplicated_textures(get_all_materials())
		return {'FINISHED'}

#################################################################################
# Functions
#################################################################################
def _clean_duplicated_textures(mats):
	counter = 0
	for mat in mats:
		if mat.node_tree:
			for n in mat.node_tree.nodes:
				if n.type == 'TEX_IMAGE':
					if n.image is None:
						continue
					elif n.image.name[-3:].isdigit():
						name = n.image.name[:-4]
						exists = False
						for img in bpy.data.images:
							if img.name in name:
								exists = True
						if exists:
							n.image = bpy.data.images[name]
							counter+=1
						else:
							n.image.name = name
	show_message_box("Removed {} duplicated textures".format(counter), title="Result")