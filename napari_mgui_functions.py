"""
Make changes here while Napari is running and press reload.
"""

from magicgui import widgets
from napari import Viewer
from napari.utils.events import Event

class my_Viewer():
    """
    Hold the viewer instance
    """
    viewer: Viewer = None

# Some test button to play around with getting the extent of
nap_dock_widget = widgets.Container(widgets=[
    widgets.PushButton(text='Get Ext', name='get_ext'),
    # widgets.PushButton(text='Reduce', name='reduce') # --> uncomment to add something
    ],
    layout='vertical')

# --> uncomment subsequent block to have a function to act on Reduce
# @nap_dock_widget.reduce.clicked.connect
# def reduce():
#     viewer = my_Viewer.viewer
#     viewer.layers.selection.active.scale = [0.5, 0.5]


@nap_dock_widget.get_ext.clicked.connect
def get_ext():
    """
    Example function showing the extent of the selected layer.
    :return:
    """
    layers = my_Viewer.viewer.layers
    if len(layers) > 0:
        print(my_Viewer.viewer.layers.selection.active.extent)


def my_event_handler(event: Event):
    """
    Some test function to show capturing Napari events.
    :param event:
    :return:
    """
    print(f'my_event_handler {event.source.point} {event.source.point[event.source.order[0]]}')

def create_nap_doc(viewer_p, prev_functions):
    """
    Create the magicgui that can be docked into Napari.
    :param viewer_p:
    :param prev_functions:
    :return:
    """
    viewer = viewer_p
    my_Viewer.viewer = viewer_p
    if not prev_functions is None:
        viewer_p.dims.events.current_step.disconnect(prev_functions)
    viewer.dims.events.current_step.connect(my_event_handler)
    return nap_dock_widget, prev_functions

