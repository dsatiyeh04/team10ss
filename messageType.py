import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf

class messageTypeWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title= "Message Type")
        self.set_border_width(10)
        hb = Gtk.HeaderBar(title="Message Type Area")

        self.set_titlebar(hb)
        closebutton = Gtk.Button()
        closebutton.set_relief(Gtk.ReliefStyle.NONE)
        img = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.MENU)
        closebutton.set_image(img)
        closebutton.connect("clicked", Gtk.main_quit)
        hb.pack_end(closebutton)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        #New/Modify Tab
        self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label('To create a new message type, please enter a \nmessage type name and select message type field \nvalue pair(s). To update/delete an existing \nmessage type, please select from the existing \nmessage type first and the previously selected \nname and field value pairs(s) will be pre-populated.'))
        listbox = Gtk.ListBox()
        self.page1.add(listbox)
        listbox.add(self.newModifyWin())
        self.notebook.append_page(self.page1, Gtk.Label('New/Modify'))

        #Dependency Tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('A page with an image for a Title.'))
        self.notebook.append_page(self.page2, Gtk.Label('Dependency'))

        #Template Tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('A page with an image for a Title.'))
        self.notebook.append_page(self.page2, Gtk.Label('Template'))

        #Equivalency Tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('A page with an image for a Title.'))
        self.notebook.append_page(self.page2, Gtk.Label('Equivalency'))

        #Generation Tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('A page with an image for a Title.'))
        self.notebook.append_page(self.page2, Gtk.Label('Generation'))


    def newModifyWin(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Existing Message Type")
        vbox.pack_start(label2,False,True,0)

        messageT = ["Hi", "this", "are", "message types"]
        messageT_combo = Gtk.ComboBoxText()
        messageT_combo.set_entry_text_column(0)
        messageT_combo.connect("changed", self.on_messageT_combo_changed)
        for message in messageT:
            messageT_combo.append_text(message)

        hbox.pack_start(messageT_combo, False, True, 0)

        return row

    def on_messageT_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
	           print("Selected: currency=%s" % text)

window = messageTypeWindow()
window.show_all()
Gtk.main()
