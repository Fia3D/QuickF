import bpy

from ..utilities.utilities import get_all_objects, show_message_box

#################################################################################
# Operator
#################################################################################
class QUICKF_OT_rename_data_by_object_name(bpy.types.Operator):
	''' Rename all objects data with the name of the Object holding it (if it has only one) '''
	bl_idname = "quickf.rename_data_by_object_name"
	bl_label = "By their Object name"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		_rename_data_by_object_name(get_all_objects())
		return {'FINISHED'}

#################################################################################
# Functions
#################################################################################
def _rename_data_by_object_name(objects):
	counter = 0
	
	for obj in objects:
		if obj.data and obj.data.users == 1 and obj.data.name != obj.name:
			obj.data.name = obj.name
			counter+=1

	show_message_box("Renamed {} object data".format(counter), title="Result")