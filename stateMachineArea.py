import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class stateMachineWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="State Machine Overlay")
        self.set_border_width(10)
        hb = Gtk.HeaderBar(title="State Machine Area")

        self.set_titlebar(hb)
        closebutton = Gtk.Button()
        closebutton.set_relief(Gtk.ReliefStyle.NONE)
        img = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.MENU)
        closebutton.set_image(img)
        closebutton.connect("clicked", Gtk.main_quit)
        hb.pack_end(closebutton)

        self.state = Gtk.DrawingArea()
        self.add(self.state)


window = stateMachineWindow()
window.show_all()
Gtk.main()
