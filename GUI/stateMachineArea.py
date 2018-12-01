import math

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class stateMachineWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="State Machine Area")
        self.set_size_request(390, 240)
        #self.set_position(Gtk.WIN_POS_CENTER)

        self.connect("destroy", Gtk.main_quit)

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.expose)
        self.add(darea)

        self.show_all()

    def expose(self, widget, event):
        cr = widget.get_property('window').cairo_create()
        cr.set_source_rgb(0.6, 0.6, 0.6)

        #cr.rectangle(20, 20, 120, 80)
        cr.rectangle(180, 20, 80, 80)
        cr.fill()

window = stateMachineWindow()
window.show_all()
Gtk.main()
