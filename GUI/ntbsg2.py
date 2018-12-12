#  _    _  _  _      _              _
# | |  | |(_)| |    | |            | |
# | |  | | _ | |  __| |  ___  __ _ | |_  ___
# | |/\| || || | / _` | / __|/ _` || __|/ __|
# \  /\  /| || || (_| || (__| (_| || |_ \__ \
#  \/  \/ |_||_| \__,_| \___|\__,_| \__||___/



import gi
import sys
import xml.etree.ElementTree as et
import xml.dom.minidom as dom

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf

sys.path.append('/root/Documents/team10ss')
from controller import Controller

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from PDML_Manager import PDML

sys.path.append('/root/Documents/team10ss/backend/Analysis/Field')
from Field_Manager import Field

controller = Controller()
pdml = PDML()
field = Field()

pdmlFile = pdml.getLatest()
# # print pdmlFile

class mainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title= "Network Traffic Based Software Generation")
		self.set_border_width(10) #border around window
		#self.set_default_size(300,200)

		hb = Gtk.HeaderBar(title= "Network Traffic Based Software Generation")
		#hb.set_show_close_button(False)

		# hb.props.title = "Network Traffic Based Software Generation"
		self.set_titlebar(hb)

		closebutton = Gtk.Button(label="X")
		closebutton.set_relief(Gtk.ReliefStyle.NONE)
		img = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.MENU)
		closebutton.set_image(img)
		closebutton.connect("clicked", Gtk.main_quit)
		hb.pack_end(closebutton)

		createSession = Gtk.Button(label="Create Session")
		openSession = Gtk.Button(label="Open Session")
		closeSession = Gtk.Button(label="Close Session")
		switchWorkspace = Gtk.Button(label="Switch Workspace")
		openPCAP = Gtk.Button(label="Open PCAP")
		terminal =Gtk.Button(label="Terminal")

		switchWorkspace.connect("clicked", self.workspaceLauncherClick)
		createSession.connect("clicked", self.newSessionClick)
		openSession.connect("clicked", self.openSessionClick)
		openPCAP.connect("clicked", self.pcapClick)
		terminal.connect("clicked", self.terminalClick)


		hb.pack_end(terminal)
		hb.pack_end(openPCAP)
		hb.pack_end(switchWorkspace)
		hb.pack_end(closeSession)
		hb.pack_end(openSession)
		hb.pack_end(createSession)
		# window = messageTypeWindow()
		# window.show_all()

		#stageboxes

		mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(mainbox)

		mainbox.add(self.stagesrow())

		mainListbox = Gtk.ListBox()
		mainListbox.set_selection_mode(Gtk.SelectionMode.NONE)
		mainbox.pack_start(mainListbox, False, False, 0) # box, cihld, expand ,fill, padding
		mainListbox.add(self.mainListBox())

	def terminalClick(self, widget):
		from terminal import terminalWindow
		#var1 = terminalWindow()
		#var1.show()

	def pcapClick(self, widget):
		from pcap import pcapWindow
		#var1 = pcapWindow()
		#var1.show()

	def openSessionClick(self, widget):
		from openSession import openSessionWindow
		#var1 = openSessionWindow()
		#var1.show()

	def newSessionClick(self, widget):
		from newSession import newSessionWindow
		#var1 = newSessionWindow()
		#var1.show()

	def workspaceLauncherClick(self, widget):
		from workspaceLauncher import workspaceLauncherWindow
		#var1 = workspaceLauncherWindow()
		#var1.show()

	def mainListBox(self):
		mainListBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

		listbox = Gtk.ListBox()
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		mainListBox.pack_start(listbox, False, False, 0)

		listbox.add(self.sessionviewCol())

		listbox_2 = Gtk.ListBox()
		listbox_2.set_selection_mode(Gtk.SelectionMode.NONE)
		mainListBox.pack_start(listbox_2,False, False, 0)

		listbox_2.add(self.pdmlviewCol())

		return mainListBox



	def sessionviewCol(self):
		sessionbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

		listbox = Gtk.ListBox()
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox, False, False, 0)

		listbox.add(self.stageviewrow())
		listbox.add(self.folderviewrow())
		listbox.add(self.folderviewrow())
		listbox.add(self.folderviewrow())

		listbox_2 = Gtk.ListBox()
		listbox_2.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox_2,False, False, 0)

		listbox_2.add(self.tagarearow())
		# listbox_2.add(self.nametagarea())
		listbox_2.add(self.tagname())


		return sessionbox

	def stageviewrow(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, True, True, 0)

		label1 = Gtk.Label()
		label1.set_markup("<big><b>Session View</b></big> ")
		label1.set_line_wrap(True)

		label2 = Gtk.Label()
		label2.set_markup("<big>Workspace X</big> ")

		vbox.pack_start(label1, True, True, 0)
		vbox.pack_start(label2, True, True, 0)

		return row

	def folderviewrow(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, False, False, 0)

		foleder1button =Gtk.Button(label="FOLDERICON")
		folderLabel = Gtk.Label()
		folderLabel.set_markup("Sessions A")

		vbox.pack_start(foleder1button, False,False , 0)
		hbox.pack_start(folderLabel,False, False, 0)

		return row

	def tagarearow(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, True, True, 0)

		label1 = Gtk.Label()
		label1.set_markup("<u>Tag Area</u> ")
		vbox.pack_start(label1, True, True, 0)


		return row

	def nametagarea(self):


		return row

	def on_currency_combo_changed(self, combo):
		text = combo.get_active_text()
		if text is not None:
			print("Selected: currency=%s" % text)

	def tagname(self):
		# TAG NAME
		box = Gtk.ListBox()
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, False, True, 0)

		label2 =Gtk.Label()
		label2.set_markup("Tag \n Name")
		vbox.pack_start(label2,False,True,0)

		tagnameEntry = Gtk.Entry()
		tagnameEntry.set_text('Tag Name')

		hbox.pack_start(tagnameEntry, False, True, 0)

		# TAG DESCRIPTION
		row1 = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row1.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, False, True, 0)
		label2 =Gtk.Label()
		label2.set_markup("Tagged \n Description")
		vbox.pack_start(label2,False ,True,0)

		tagDescriptionEntry = Gtk.Entry()
		tagDescriptionEntry.set_text('Tagged Description')

		hbox.pack_start(tagDescriptionEntry, False, True, 0)



		# THIS IS FIELD NAME
		row3 = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row3.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, False, True, 0)

		label2 =Gtk.Label()
		label2.set_markup("Field Names")
		vbox.pack_start(label2,False,True,0)

		currencies = field.getFields()
		currency_combo = Gtk.ComboBoxText()
		currency_combo.set_entry_text_column(0)
		currency_combo.connect("changed", self.on_currency_combo_changed)
		for currency in currencies:
			currency_combo.append_text(currency)

		hbox.pack_start(currency_combo, False, True, 0)

		# BUTTONS
		row2 = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		row2.add(hbox)

		update = Gtk.Button(label = "Update")
		cancel = Gtk.Button(label = "Cancel")

		hbox.add(update)
		hbox.add(cancel)
		# BUTTONS
		row2 = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		row2.add(hbox)
		update = Gtk.Button(label = "Update")
		cancel = Gtk.Button(label = "Cancel")
		update.connect("clicked", self.updateTag_clicked, currency_combo, tagnameEntry, tagDescriptionEntry)
		hbox.add(update)
		hbox.add(cancel)

		box.add(row3)
		box.add(row)
		box.add(row1)
		box.add(row2)
		return box


	def updateTag_clicked(self, button, *data):
		controller.tagFields(data[0].get_active_text(), data[1].get_text().lower().replace(" ", ""), data[2].get_text().lower().replace(" ", ""))
		self.destroy()
		win = mainWindow()
		win.show_all()
		Gtk.main()


	def pdmlviewCol(self):
		sessionbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

		listbox = Gtk.ListBox()
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox, False, False, 0)

		listbox.add(self.pdmlviewrow())
		listbox.add(self.pdmlsaving())
		#listbox.add(self.filterArea())

		listbox_2 = Gtk.ListBox()
		listbox_2.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox_2,False, False, 0)

		listbox_2.add(self.filterAreaName())
		listbox_2.add(self.filterAreaSaving())

		listbox_3 = Gtk.ListBox()
		listbox_3.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox_3,False,False,0)

		listbox_3.add(self.packetAreaName())
		listbox_3.add(self.treeFrame())

		listbox_4 = Gtk.ListBox()
		listbox_4.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox_4,False,False,0)

		listbox_4.add(self.bottomarea())

		return sessionbox

	def pdmlviewrow(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, True, True, 0)

		label1 = Gtk.Label()
		label1.set_markup("<big><b>PDML View</b></big> ")
		label1.set_line_wrap(True)

		vbox.pack_start(label1, True, True, 0)

		return row

	def pdmlsaving(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, False, False, 0)

		self.entry = Gtk.Entry()
		self.entry.set_text('New PDML State Name')
		hbox.pack_start(self.entry, False, False, 0)

		saveBtn =Gtk.Button(label = "Save as New \n PDML State")
		hbox.pack_start(saveBtn,False,False,0)
		saveBtn.connect("clicked", self.saved_clicked)

		closecurrButton =Gtk.Button(label = "Close Current \n PDML State")
		hbox.pack_start(closecurrButton,False,False,0)

		deletecurrButton =Gtk.Button(label = "Delete Current \n PDML State")
		hbox.pack_start(deletecurrButton,False,False,0)

		self.entry = Gtk.Entry()
		self.entry.set_text('Rename Current PDML State Name')
		hbox.pack_start(self.entry, False,False, 0)

		renamecurrButton =Gtk.Button(label = "Rename Current \n PDML State")
		hbox.pack_start(renamecurrButton,False,False,0)


		return row

	def saved_clicked(self, button):
		print "Clicked"


	def filterAreaName(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)

		label1 = Gtk.Label()
		label1.set_markup("<u>Filter Area</u> ")
		hbox.pack_start(label1, False, True, 0)


		return row

	def filterAreaSaving(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		row.add(hbox)

		label1 = Gtk.Label()
		label1.set_markup("<b>Filter Area</b> ")
		hbox.pack_start(label1, False, True, 0)

		#
		filter = Gtk.Entry()
		# self.entry.set_text('Filter Expression')
		hbox.pack_start(filter, False, False, 0)
		filter.set_editable(False)

		label2 =Gtk.Button(label = "Apply")
		hbox.pack_start(label2,False,False,0)

		savecurrButton =Gtk.Button(label = "Clear")
		hbox.pack_start(savecurrButton,False,False,0)

		closecurrButton =Gtk.Button(label = "Save")
		hbox.pack_start(closecurrButton,False,False,0)

		savefilterlabel = Gtk.Label()
		savefilterlabel.set_markup("<b>Saved Filter</b> ")
		hbox.pack_start(savefilterlabel, False, True, 0)

		currencies = ["icmp","tcp","dns"]
		currency_combo = Gtk.ComboBoxText()
		currency_combo.set_entry_text_column(0)
		currency_combo.connect("changed", self.on_savedfiltercombo)
		for currency in currencies:
			currency_combo.append_text(currency)

		hbox.pack_start(currency_combo, False, True, 0)

		applybutton =Gtk.Button(label = "Apply")
		hbox.pack_start(applybutton,False,False,0)
		applybutton.connect("clicked", self.apply_clicked, currency_combo)


		return row

	def apply_clicked(self, button, *data):
		controller.filterPDML(data[0].get_active_text())
		print "DATA: " + data[0].get_active_text()

	def on_savedfiltercombo(self, combo):
		text = combo.get_active_text()
		if text is not None:
			print("Selected: currency=%s" % text)

	def packetAreaName(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)

		label1 = Gtk.Label()
		label1.set_markup("<u>Packet Area</u> ")
		hbox.pack_start(label1, False, True, 0)


		return row

	def createTree(self, pdmlFile):
		self.model =Gtk.TreeStore(str)
		pdmlFile = pdml.getLatest()
		doc =dom.parse(pdmlFile)

		self.addtotree(doc.childNodes[0],None)
		#treeview
		treeview = Gtk.TreeView(self.model)
		#colums
		col0 =Gtk.TreeViewColumn("Name")
		self.cell0 = Gtk.CellRendererText()
		# first column
		treeview.append_column( col0)
		col0.pack_start( self.cell0,True)
		col0.set_attributes( self.cell0, text=0)
		col0.set_sort_column_id( 0) # make column sortable using column 0 data

		return treeview

	def treeFrame(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)

		# self.model =Gtk.TreeStore(str)
		# pdmlFile = pdml.getFilename()
		# doc =dom.parse(pdmlFile)
		#
		# self.addtotree(doc.childNodes[0],None)
		# #treeview
		# global pdmlFile
		# pdmlFile = pdml.getFilename()
		treeview = self.createTree(pdmlFile)
		# #colums
		# col0 =Gtk.TreeViewColumn("Name")
		# self.cell0 = Gtk.CellRendererText()
		# # first column
		# treeview.append_column( col0)
		# col0.pack_start( self.cell0,True)
		# col0.set_attributes( self.cell0, text=0)
		# col0.set_sort_column_id( 0) # make column sortable using column 0 data
		# add the treeview to the parent and show it
		hbox.add( treeview)
		treeview.show()


		hbox.add(self.removalclearbutt())


		return row

	def nodeToText(self, node):
		text = []
		text.append("<{}".format(node.nodeName))

		if node.hasAttributes():
			for k, v in node.attributes.items():
				text.append("{}=\"{}\"".format(k, v))

		text.append(">")
		return ' '.join(text)

	def addtotree(self, e, parent):
		if isinstance(e, dom.Element):
			me = self.model.append(parent, [self.nodeToText(e)])
			for child in e.childNodes:
				self.addtotree(child, me)

	def removalclearbutt(self):
			row = Gtk.ListBoxRow()
			vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
			row.add(vbox)
			remove = Gtk.Button(label = "Remove")
			clear = Gtk.Button(label = "Clear")
			vbox.add(remove)
			vbox.add(clear)
			return row

	def bottomarea(self):
		bottomrow = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		bottomrow.add(hbox)

		hbox.pack_start(self.fieldarea(),True,True,0)
		hbox.add(self.masomenos())
		message =Gtk.Button(label="Message Type")

		hbox.pack_end(self.messagetypearea(),True,True,0)
		hbox.pack_end(self.existingMessageType(),True,True,0)

		return bottomrow

	def fieldarea(self):
		bigboxfieldarea = Gtk.ListBoxRow()
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		bigboxfieldarea.add(vbox)


		buttonslane = Gtk.Button(label = "Clear") #at the end subtitles

		vbox.add(self.fieldAreaName())
		vbox.add(self.fieldattributes())#the tree view
		vbox.add(self.fieldareainstructions())




		return bigboxfieldarea

	def fieldAreaName(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)

		label1 = Gtk.Label()
		label1.set_markup("<u>Field Area</u> ")
		hbox.pack_start(label1, False, True, 0)


		return row

	def masomenos(self):
		buttonbox = Gtk.ListBoxRow()
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
		buttonbox.add(vbox)

		mas = Gtk.Button(label = "+") #the label
		menos = Gtk.Button(label = "-") # teh actual excel looking sheet

		vbox.add(mas)
		vbox.add(menos)

		return buttonbox


	def messagetypearea(self):
		bigboxmessagetypearea = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		bigboxmessagetypearea.add(hbox)


		##import messageType
		##var1 = messageType()
		##var1.show()


		return bigboxmessagetypearea


	def existingMessageType(self):
		bigboxmessagetypearea = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		bigboxmessagetypearea.add(hbox)

		label1 = Gtk.Label()
		label1.set_markup("<u>Message Type</u> ")
		hbox.pack_start(label1, False, True, 0)



		return bigboxmessagetypearea


	def fieldattributes(self):
		scrollwindow=Gtk.ScrolledWindow(hadjustment=None, vadjustment=None)
		bigboxfieldatt = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		bigboxfieldatt.add(hbox)

		columns = ["Field Name","Show Name","Size", "Position", "Show", "Value", "Entropy"]

		fieldnameatt = [["icmp.type", "Type 8[Echo(ping)request]", "1","34", "8","08","2"],
		["icmp.code", "Code 0", "1","35", "0x00","00","2"],
		["icmp.checksum", "Checksum:0x6891(correct)", "0x00","36", "0x6861","6861","0"],
		["icmp.Ident", "Identifier:0x809e", "2","38", "0x809e","809e","2"],
		["icmp.seq", "Sequence number:0x0f00", "2","40", "0x0f00","0f00","2"]]

		# the data in the model (three strings for each row, one for each column)
		listmodel = Gtk.ListStore(str, str, str, str, str, str, str)
		# append the values in the model
		for i in range(len(fieldnameatt)):
			listmodel.append(fieldnameatt[i])

		# a treeview to see the data stored in the model
		view = Gtk.TreeView(model=listmodel)
		# for each column
		cell1= Gtk.CellRendererToggle()
		col1=Gtk.TreeViewColumn("",cell1, active =1)
		view.append_column(col1)

		for i, column in enumerate(columns):
			# cellrenderer to render the text
			cell = Gtk.CellRendererText()
			# the text in the first column should be in boldface
			if i == 0:
				cell.props.weight_set = True
				# cell.props.weight = Pango.Weight.BOLD
			# the column is created
			col = Gtk.TreeViewColumn(column, cell, text=i)
			# and it is appended to the treevie
			view.append_column(col)

		# when a row is selected, it emits a signal
		view.get_selection().connect("changed", self.on_changed)

		# # the label we use to show the selection
		# self.label = Gtk.Label()
		# self.label.set_text("")

		# a grid to attach the widgets
		grid = Gtk.Grid()
		grid.attach(view, 0, 0, 1, 1)
		# grid.attach(self.label, 0, 1, 1, 1)
		# attach the grid to the window
		hbox.add(grid)

		scrollwindow.add(bigboxfieldatt)

		return scrollwindow

	def on_changed(self, selection):#NOT IN USE YET
		# get the model and the iterator that points at the data in the model
		(model, iter) = selection.get_selected()
		# set the label to a new value depending on the selection
		self.label.set_text("\n %s %s %s" %
			(model[iter][0],  model[iter][1], model[iter][2]))
		return True

	def fieldareainstructions(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)

		label1 = Gtk.Label()
		label1.set_markup("[ ] Select all fields      Field Name, ShowName, Value, and Length, are editable fields.")
		hbox.pack_start(label1, False, True, 0)


		return row







	def stagesrow(self): #OKAY
		box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		stage1 = Gtk.Button(label="Stage 1: Configuration and Setup")
		stage2 = Gtk.Button(label="Stage 2: Message Analysis")
		stage3 = Gtk.Button(label="Stage 3: Sequencing")
		stage4 = Gtk.Button(label="Stage 4: Code Generation")

		box.pack_start(stage1, True, True, 0)
		box.pack_start(stage2, True, True, 0)
		box.pack_start(stage3, True, True, 0)
		box.pack_start(stage4, True, True, 0)
		return box

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





win = mainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
