import bpy

from .clean_unused_material_slot import show_message_box

#################################################################################
# Operator
#################################################################################
class QUICKF_OT_rename_images_by_filename(bpy.types.Operator):
	''' Rename images by filename '''
	bl_idname = "quickf.rename_images_by_filename"
	bl_label = "By Filename"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		_rename_images_by_filename(bpy.data.images)
		return {'FINISHED'}

#################################################################################
# Functions
#################################################################################
def _rename_images_by_filename(images):
	counter = 0
	for image in images:
		filename = bpy.path.basename(image.filepath)
		if image.name == filename or image == "":
			continue

		image.name = filename
		counter+=1

	show_message_box("Renamed {} images".format(counter), title="Result")