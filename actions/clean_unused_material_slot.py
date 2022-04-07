import bpy

from ..utilities.utilities import get_all_objects, show_message_box

#################################################################################
# Operator
#################################################################################
class QUICKF_OT_clean_unused_material_slot(bpy.types.Operator):
	'''Remove all unused material slot in the file'''
	bl_idname = "quickf.clean_unused_material_slot"
	bl_label = "Unused Materials slot"
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		_clean_unused_slot(get_all_objects())
		return {'FINISHED'}

#################################################################################
# Functions
#################################################################################
def _clean_unused_slot(objects):
	ob: bpy.types.Object
	for ob in objects:
		if not ob.material_slots:
			continue
		
		if ob.visible_get():
			bpy.ops.object.material_slot_remove_unused({"object" : ob})
	
	show_message_box("Removed unused material slot", title="Result")