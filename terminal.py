import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class terminalWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Terminal Overlay")
        self.set_border_width(10)
        hb = Gtk.HeaderBar(title="Terminal")

        self.set_titlebar(hb)
        closebutton = Gtk.Button()
        closebutton.set_relief(Gtk.ReliefStyle.NONE)
        img = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.MENU)
        closebutton.set_image(img)
        closebutton.connect("clicked", Gtk.main_quit)
        hb.pack_end(closebutton)

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(hbox)

        listbox = Gtk.ListBox()

        listbox.add(self.terminalW())
        hbox.pack_start(listbox, False, True, 0)

    def terminalW(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)


        entry1 = Gtk.Entry()
        entry1.set_text('[Destination Folder Path]> [Generated Files]')
        hbox.pack_start(entry1, False, True, 0)



        return row

window = terminalWindow()
window.show_all()
Gtk.main()