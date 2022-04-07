import bpy

####################################################
# Operators
####################################################
class QUICKF_OT_open_asset_browser(bpy.types.Operator):
	""" Open Asset Browser in a new window """
	bl_idname = "quickf.open_window_asset_browser"
	bl_label = "Open Asset Browser"
	bl_options = {"REGISTER"}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		_open_asset_browser()
		return {'FINISHED'}

####################################################
# Functions
####################################################
def _open_asset_browser():
	bpy.ops.screen.userpref_show('INVOKE_DEFAULT')
	screen = bpy.context.window_manager.windows[-1].screen
	screen.areas[0].ui_type = 'ASSETS'