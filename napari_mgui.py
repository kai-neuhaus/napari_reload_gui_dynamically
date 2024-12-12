'''
Allow reloading changes without restarting Napari.
Create a folder Napari_functions and import napari_mgui_functions, or chose your desired folder and file names!

Select the folder at sys.path.append for your functions (see below around line 18)

You must set the absolute path on your system!

Author: Kai Neuhaus
Date: 12/11/2024
'''

import sys
import importlib
import pathlib

# --> set the path to the folder on your system
sys.path.append(pathlib.Path('/your-path-here/Napari_functions/').as_posix())

# Import functions we want to edit and reload pressing the reload-button.
import napari_mgui_functions

import napari
from magicgui import widgets

class ReloadModItems():
    """
    Hold the previous instance to remove it from the event handler.
    """
    prev_functions = None

# Create an initial reload button.
reload_PB = widgets.PushButton( text = 'Reload Functions', name = 'reload_PB')
nap_dock_widget = widgets.Container(widgets=[reload_PB], name='nap_dock_widget')

@reload_PB.clicked.connect
def pb1_clicked():
    """
    Load or reload functions into running Napari.
    :return:
    """
    importlib.reload(napari_mgui_functions)
    napDock, prev_functions = napari_mgui_functions.create_nap_doc(viewer, ReloadModItems.prev_functions)
    ReloadModItems.prev_functions = prev_functions
    viewer.window.add_dock_widget(napDock)



if __name__ == '__main__':
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(nap_dock_widget,name = 'My Widget')
    napari.run()