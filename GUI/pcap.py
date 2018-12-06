import gi
import sys
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename

sys.path.append('/root/Documents/team10ss/backend/')
from PDMLConverter import PDMLConverter

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf

sys.path.append('/root/Documents/team10ss/')
from controller import Controller

class pcapWindow(Gtk.Window):

    pcapFile = ''

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
        label2.set_markup("PCAP File")
        vbox.pack_start(label2, False, True, 0)

        entry1 = Gtk.Entry()
        # entry1.set_text('Project Name')
        vbox.pack_start(entry1, False, True, 0)

        browse1 = Gtk.Button.new_with_label("Browse")
        browse1.connect("clicked", self.browse_clicked, entry1)
        vbox.pack_start(browse1, False, True, 0)

        return row
    def browse_clicked(self, button, *data):
        Tk().withdraw()
        filename = askopenfilename()
        name = filename.split('/')
        data[0].set_text(name[-1])
        global pcapFile
        pcapFile = filename
        self.connect("destroy", Gtk.main_quit)


    def dissName(self):
        row = Gtk.ListBox()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        hbox.pack_start(vbox, False, True, 0)

        label2 = Gtk.Label()
        label2.set_markup("Disssector Name")
        vbox.pack_start(label2, False, True, 0)

        entry2 = Gtk.Entry()
        entry2.set_text('Optional Dissector')
        vbox.pack_start(entry2, False, True, 0)

        browse2 = Gtk.Button.new_with_label("Browse")
        browse2.connect("clicked", self.browse_clicked, entry2)
        vbox.pack_start(browse2, False, True, 0)

        return row

    def bottomBttn(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)

        btn = Gtk.Button.new_with_label("Convert to PDML")
        btn.connect("clicked", self.convert_btn_clicked)
        hbox.pack_start(btn, True, True, 0)

        btn = Gtk.Button.new_with_label("Cancel")
        hbox.pack_start(btn, True, True, 0)

        return row
    # Method to call controller 
    def convert_btn_clicked(self, button):
        foo = Controller()
        foo.convertPCAP(pcapFile)





window = pcapWindow()
window.show_all()
Gtk.main()
