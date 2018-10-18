import gi
#import workspaceLauncher
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
        listbox.add(self.existingMessageType())
        listbox.add(self.messageTypeName())
        listbox.add(self.messageTypeFVP())
        listbox.add(self.checkBtnRow())
        listbox.add(self.btnRow())
        self.notebook.append_page(self.page1, Gtk.Label('New/Modify'))

        #Dependency Tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        listbox = Gtk.ListBox()
        self.page2.add(listbox)
        listbox.add(self.existingMessageType())
        listbox.add(self.cycleBtn())
        listbox.add(self.sizeField())
        listbox.add(self.sizePacket())
        listbox.add(self.checksum())
        listbox.add(self.btnRow2())
        self.notebook.append_page(self.page2, Gtk.Label('Dependency'))

        #Template Tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        listbox = Gtk.ListBox()
        self.page2.add(listbox)
        listbox.add(self.existingMessageType())
        listbox.add(self.cycleBtn())
        listbox.add(self.messageTypeTemplate())
        listbox.add(self.btnRow2())
        self.notebook.append_page(self.page2, Gtk.Label('Template'))

        #Equivalency Tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        listbox = Gtk.ListBox()
        self.page2.add(listbox)
        listbox.add(self.fieldEq())
        listbox.add(self.fieldEq2())
        self.notebook.append_page(self.page2, Gtk.Label('Equivalency'))

        #Generation Tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        listbox = Gtk.ListBox()
        self.page2.add(listbox)
        listbox.add(self.existingMessageType())
        listbox.add(self.msgTemplateOutput())
        listbox.add(self.messageTempName())
        listbox.add(self.btnRow3())
        self.notebook.append_page(self.page2, Gtk.Label('Generation'))

    #------------------New/Modify Tab Rows-------------------------------------
    def existingMessageType(self):
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


    def messageTypeName(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Message Type Name")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Message Type Names')

        hbox.pack_start(self.entry, False, True, 0)

        return row

    def messageTypeFVP(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Message Type Field\n Value Pair(s)")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Field Value Pair(s)')

        hbox.pack_start(self.entry, False, True, 0)

        return row

    def checkBtnRow(self):
        row = Gtk.ListBoxRow()
        #hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        #hbox.pack_start(vbox, False, True, 0)
        row.add(vbox)
        check1 = Gtk.CheckButton("Select both field name and value")
        vbox.pack_start(check1, False, True, 0)

        check2 = Gtk.CheckButton("Select field name only")
        vbox.pack_start(check2, False, True, 0)

        return row

    def btnRow(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)

        btn = Gtk.Button.new_with_label("Save")
        hbox.pack_start(btn, True, True, 0)

        btn = Gtk.Button.new_with_label("Delete")
        hbox.pack_start(btn, True, True, 0)

        btn = Gtk.Button.new_with_label("Clear")
        hbox.pack_start(btn, True, True, 0)
        return row

    #--------------------------------------------------------------------------
    #---------------Dependency Tab Rows----------------------------------------

    def cycleBtn(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)

        btn = Gtk.Button.new_with_label("Cycle Through Packets")
        hbox.pack_start(btn, True, True, 0)
        return row

    def sizeField(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Size of Field")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Field Name')
        hbox.pack_start(self.entry, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Depends \non")
        hbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Field Name')
        hbox.pack_start(self.entry, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("+")
        hbox.pack_start(label2,False,True,0)

        return row


    def sizePacket(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Size of Packet")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Packet')
        hbox.pack_start(self.entry, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Depends \non")
        hbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Field Name')
        hbox.pack_start(self.entry, False, True, 0)

        return row

    def checksum(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Checksum")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Packet')
        hbox.pack_start(self.entry, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Depends \non")
        hbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('List of Field Names')
        hbox.pack_start(self.entry, False, True, 0)

        return row

    def btnRow2(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)

        btn = Gtk.Button.new_with_label("Save")
        hbox.pack_start(btn, True, True, 0)

        btn = Gtk.Button.new_with_label("Clear")
        hbox.pack_start(btn, True, True, 0)
        return row
    #---------------------------------------------------------------------------

    #----------------------Template Tab-----------------------------------------

    def messageTypeTemplate(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Message Type \nTemplate Field Value \nPair(s)")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('List of Field Value Pair(s)')

        hbox.pack_start(self.entry, False, True, 0)

        return row
    #---------------------------------------------------------------------------

    #-----------------Equivalency Tab-------------------------------------------

    def fieldEq(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Field Equivalency")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Field Name')
        hbox.pack_start(self.entry, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Of")
        hbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Message Type')
        hbox.pack_start(self.entry, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("=")
        hbox.pack_start(label2,False,True,0)

        return row

    def fieldEq2(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("                                   ")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Field Name')
        hbox.pack_start(self.entry, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Depends \non")
        hbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Field Name')
        hbox.pack_start(self.entry, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("+")
        hbox.pack_start(label2,False,True,0)

        return row

    #---------------------------------------------------------------------------

    #-----------------------Generation Tab--------------------------------------
    def msgTemplateOutput(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Message Template \nOutput Format")
        vbox.pack_start(label2,False,True,0)

        messageT = ["Hi", "this", "are", "message types"]
        messageT_combo = Gtk.ComboBoxText()
        messageT_combo.set_entry_text_column(0)
        messageT_combo.connect("changed", self.on_messageT_combo_changed)
        for message in messageT:
            messageT_combo.append_text(message)

        hbox.pack_start(messageT_combo, False, True, 0)

        return row


    def messageTempName(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, False, True, 0)

        label2 =Gtk.Label()
        label2.set_markup("Message Template \nName")
        vbox.pack_start(label2,False,True,0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Message Template Name')

        hbox.pack_start(self.entry, False, True, 0)

        return row

    def btnRow3(self):
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)

        btn = Gtk.Button.new_with_label("Generate")
        hbox.pack_start(btn, True, True, 0)

        btn = Gtk.Button.new_with_label("Clear")
        hbox.pack_start(btn, True, True, 0)

        btn.connect("clicked", self.btn_click)
        return row

    #---------------------------------------------------------------------------

    def btn_click(self, widget):
        from workspaceLauncher import workspaceLauncherWindow
        window.destroy()
        var1 = workspaceLauncherWindow()
        var1.show()

window = messageTypeWindow()
window.show_all()
Gtk.main()
