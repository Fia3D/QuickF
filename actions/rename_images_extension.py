import bpy

from .clean_unused_material_slot import show_message_box

#################################################################################
# Operator
#################################################################################
class QUICKF_OT_rename_images_extension_tga_to_png(bpy.types.Operator):
	''' Rename images extension from .tga to .png '''
	bl_idname = "quickf.rename_images_extension_tga_to_png"
	bl_label = ".TGA to .PNG"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		_rename_images_extension("tga", "png", bpy.data.images)
		return {'FINISHED'}

class QUICKF_OT_rename_images_extension_dds_to_png(bpy.types.Operator):
	''' Rename images extension from .dds to .png '''
	bl_idname = "quickf.rename_images_extension_dds_to_png"
	bl_label = ".DDS to .PNG"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		_rename_images_extension("dds", "png", bpy.data.images)
		return {'FINISHED'}

class QUICKF_OT_rename_images_extension_exr_to_png(bpy.types.Operator):
	''' Rename images extension from .exr to .png '''
	bl_idname = "quickf.rename_images_extension_exr_to_png"
	bl_label = ".EXR to .PNG"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		_rename_images_extension("exr", "png", bpy.data.images)
		return {'FINISHED'}

#################################################################################
# Functions
#################################################################################
def _rename_images_extension(old_extension, new_extension, images):
	counter = 0
	for image in images:
		if old_extension not in image.filepath:
			continue
		image.filepath = image.filepath.replace(old_extension, new_extension)
		counter+=1
		image.reload()
	show_message_box("Renamed {} images".format(counter), title="Result")