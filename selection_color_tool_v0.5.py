# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>
#
bl_info = {
    "name": "Layer Color Selection",
    "author": "Timo Stampa",
    "version": (0, 5, 0),
    "blender": (2, 73, 0),
    "location": "Toolshelf > Layers Tab",
    "warning": "",
    "description": "Changes the selection color of an active object for specific layers. Optional Addon for Layer Manager",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/layer_manager",
    "category": "3D View",
}

import bpy
from bpy.app.handlers import persistent

defaultColors = {'color1': [1.0, 0.0, 0.05]
                , 'color2': [1.0, 0.5, 0.0]
                , 'color3': [0.7, 1.0, 0.0]
                , 'color4': [0.0, 1.0, 0.0]
                , 'color5': [0.0, 1.0, 0.7]
                , 'color6': [1.0, 0.0, 0.0]
                , 'color7': [1.0, 0.0, 1.0]
                , 'color8': [0.5, 0.5, 0.0]
                , 'color9': [0.5, 0.5, 0.0]
                , 'color10': [0.0, 0.5, 0.5]
                , 'color11': [1.0, 1.0, 0.5]
                , 'color12': [0.5, 1.0, 0.5]
                , 'color13': [0.5, 0.5, 1.0]
                , 'color14': [1.0, 0.5, 1.0]
                , 'color15': [1.0, 0.5, 0.5]
                , 'color16': [0.0, 0.0, 0.0]
                , 'color17': [0.0, 0.0, 0.0]
                , 'color18': [0.0, 0.0, 0.0]
                , 'color19': [0.0, 0.0, 0.0]
                , 'color20': [0.0, 0.0, 0.0]} 

class ModalLayerColor(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Modal Timer Operator"

    _timer = None

    def modal(self, context, event):
        themeOB = bpy.context.user_preferences.themes[0].view_3d
        
        try:
          ob = bpy.context.active_object
        except:
          ob = 0

        

        if event.type == 'TIMER':
              try:
                ob = bpy.context.active_object
                if ob.layers[0] == True:          
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color1
                    except:
                         wmc = defaultColors["color1"]
                         
                elif ob.layers[1] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color2
                    except:
                         wmc = defaultColors["color2"]
                         
                elif ob.layers[2] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color3
                    except:
                         wmc = defaultColors["color3"]
                         
                elif ob.layers[3] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color4
                    except:
                         wmc = defaultColors["color4"]
                         
                elif ob.layers[4] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color5
                    except:
                         wmc = defaultColors["color5"]
                         
                elif ob.layers[5] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color6
                    except:
                         wmc = defaultColors["color6"]
                         
                elif ob.layers[6] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color7
                    except:
                         wmc = defaultColors["color7"]
                    
                elif ob.layers[7] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color8
                    except:
                         wmc = defaultColors["color8"]
                         
                elif ob.layers[8] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color9
                    except:
                         wmc = defaultColors["color9"]
                         
                elif ob.layers[9] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color10
                    except:
                         wmc = defaultColors["color10"]
                         
                elif ob.layers[10] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color11
                    except:
                         wmc = defaultColors["color11"]
                         
                elif ob.layers[11] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color12
                    except:
                         wmc = defaultColors["color12"]
                         
                elif ob.layers[12] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color13
                    except:
                         wmc = defaultColors["color13"]
                         
                elif ob.layers[13] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color14
                    except:
                         wmc = defaultColors["color14"]
                         
                elif ob.layers[14] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color15
                    except:
                         wmc = defaultColors["color15"]
                         
                elif ob.layers[15] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color16
                    except:
                         wmc = defaultColors["color16"]
                         
                elif ob.layers[16] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color17
                    except:
                         wmc = defaultColors["color17"]
                         
                elif ob.layers[17] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color18
                    except:
                         wmc = defaultColors["color18"]
                         
                elif ob.layers[18] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color19
                    except:
                         wmc = defaultColors["color19"]
                         
                elif ob.layers[19] == True:
                    try:
                         wmc = bpy.data.window_managers["WinMan"].color.color20
                    except:
                         wmc = defaultColors["color20"]
                         
                    
                themeOB.object_active = wmc
                
              except:
                  ob = 0

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        
def init():
    # test call
    bpy.ops.wm.modal_timer_operator()

@persistent
def addon_handler(scene):
    bpy.ops.wm.modal_timer_operator()
    bpy.app.handlers.scene_update_post.remove(addon_handler)


def register():
    #bpy.utils.register_class(ModalLayerColor)
    bpy.utils.register_module(__name__)
    bpy.app.handlers.scene_update_post.append(addon_handler)


def unregister():
    #bpy.utils.unregister_class(ModalLayerColor)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()


    

