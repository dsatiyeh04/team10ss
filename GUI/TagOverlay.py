import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class tagOverlay(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Tag Overlay")
        self.set_border_width(10)
        hb = Gtk.HeaderBar(title="Tag Overlay")

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

        listbox.add(self.tagName())
        listbox.add(self.taggedField())
        listbox.add(self.tagDescription())
        listbox.add(self.bottomBttn())
        hbox.pack_start(listbox, False, True, 0)

    def tagName(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Tag Name")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        entry1.set_text('Tag Name')
        vbox.pack_start(entry1, False, True, 0)

        return row

    def taggedField(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Tagged Field")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        entry1.set_text('Tagged Field Name')
        vbox.pack_start(entry1, False, True, 0)

        return row

    def tagDescription(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Tag Description")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        entry1.set_text('Tag Description')
        vbox.pack_start(entry1, False, True, 0)

        return row

    def bottomBttn(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        row.add(hbox)

        btn = Gtk.Button.new_with_label("Save")
        hbox.pack_start(btn, True, True, 0)

        btn = Gtk.Button.new_with_label("Cancel")
        hbox.pack_start(btn, True, True, 0)

        return row


window = tagOverlay()
window.show_all()
Gtk.main()
