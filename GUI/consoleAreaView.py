import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class consoleAreaWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Terminal Overlay")
        self.set_border_width(10)
        hb = Gtk.HeaderBar(title="Terminal")

        self.connect("destroy", Gtk.main_quit)

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(hbox)

        listbox = Gtk.ListBox()

        listbox.add(self.consoleW())
        hbox.pack_start(listbox, False, True, 0)

    def consoleW(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)

        label2 = Gtk.Label()
        label2.set_markup("No error message to show")
        hbox.pack_start(label2, False, True, 0)



        return row

window = consoleAreaWindow()
window.show_all()
Gtk.main()