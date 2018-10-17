import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class workspaceLauncherWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher Window")
        self.set_border_width(10)
        hb = Gtk.HeaderBar(title="Workspace Launcher")

        self.connect("destroy", Gtk.main_quit)

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(hbox)

        listbox = Gtk.ListBox()

        listbox.add(Gtk.Label(
            "Select a directory as workspcare: NTBSG uses the workspace\n                                 directory to store "
            "sessions."))
        listbox.add(self.workspaceDir())
        listbox.add(self.destFolderName())
        listbox.add(self.destFolderPath())
        listbox.add(self.bottomBttn())
        hbox.pack_start(listbox, False, True, 0)

    def workspaceDir(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=28)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Workspace")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        entry1.set_text('Workspace Directory Path')
        vbox.pack_start(entry1, False, True, 0)

        browse1 = Gtk.Button.new_with_label("Browse")
        vbox.pack_start(browse1, False, True, 0)

        return row

    def destFolderName(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Destination\nFolder Name")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        entry1.set_text('Destination Folder Name')
        vbox.pack_start(entry1, False, True, 0)

        return row

    def destFolderPath(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=25)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Destination\nFolder Path")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        entry1.set_text('Destination Folder Path')
        vbox.pack_start(entry1, False, True, 0)

        browse1 = Gtk.Button.new_with_label("Browse")
        vbox.pack_start(browse1, False, True, 0)

        return row

    def bottomBttn(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)

        btn = Gtk.Button.new_with_label("Launch")
        hbox.pack_start(btn, True, True, 0)

        btn = Gtk.Button.new_with_label("Cancel")
        hbox.pack_start(btn, True, True, 0)

        return row


window = workspaceLauncherWindow()
window.show_all()
Gtk.main()
