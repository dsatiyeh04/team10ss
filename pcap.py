import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class pcapWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PCAP Overlay")
        self.set_border_width(10)
        hb = Gtk.HeaderBar(title="PCAP")

        self.connect("destroy", Gtk.main_quit)

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(hbox)

        listbox = Gtk.ListBox()

        listbox.add(Gtk.Label('                Open a PCAP file                '))
        listbox.add(self.pcapName())
        listbox.add(self.dissName())
        listbox.add(self.bottomBttn())
        hbox.pack_start(listbox, False, True, 0)

    def pcapName(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Session Name")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        entry1.set_text('Project Name')
        vbox.pack_start(entry1, False, True, 0)

        browse1 = Gtk.Button.new_with_label("Browse")
        vbox.pack_start(browse1, False, True, 0)

        return row

    def dissName(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Description")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        entry1.set_text('Description of Project')
        vbox.pack_start(entry1, False, True, 0)

        browse1 = Gtk.Button.new_with_label("Browse")
        vbox.pack_start(browse1, False, True, 0)

        return row

    def bottomBttn(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)

        btn = Gtk.Button.new_with_label("Convert to PDML")
        hbox.pack_start(btn, True, True, 0)

        btn = Gtk.Button.new_with_label("Cancel")
        hbox.pack_start(btn, True, True, 0)

        return row




window = pcapWindow()
window.show_all()
Gtk.main()