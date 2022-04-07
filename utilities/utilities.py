import bpy

############################################
# Get Materials
############################################
def get_all_materials():
	mats = set()    
	for mat in bpy.data.materials:
		if mat.name != "Dots Stroke":
			mats.add(mat)
	return mats

def get_all_materials_in_selected_objects():
	mats = set()
	objects = get_selected_objects()
	for object in objects:
		for slot in object.material_slots:
			mats.add(slot.material)
	return mats

def get_all_materials_in_active_object():
    mats = set()
    obj=bpy.context.active_object
    for slot in obj.material_slots:
        mats.add(slot.material)
    return mats

############################################
# Get Objects
############################################
def get_all_objects():
	return bpy.data.objects

def get_selected_objects():
	objects = set()
	for object in bpy.context.selected_objects:
		objects.add(object)
	return objects

def get_scene_object(scene: bpy.types.Scene):
	return scene.objects

def show_message_box(message = "", title = "Info", icon = 'INFO'):
	def draw(self, context):
		self.layout.label(text=message)

	bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)
	
	print("[" + title + "] : " + message)