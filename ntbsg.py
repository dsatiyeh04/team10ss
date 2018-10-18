import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf

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
		listbox_2.add(self.nametagarea())
		listbox_2.add(self.tagname())
		listbox_2.add(self.taggedfield())
		listbox_2.add(self.tagDescription())
		listbox_2.add(self.updatingtag())


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
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, False, True, 0)

		label2 =Gtk.Label()
		label2.set_markup("Saved Tag")
		vbox.pack_start(label2,False,True,0)


		currencies = ["Euro", "US Dollars", "British Pound", "Japanese Yen",
		"Russian Ruble", "Mexican peso", "Swiss franc"]
		currency_combo = Gtk.ComboBoxText()
		currency_combo.set_entry_text_column(0)
		currency_combo.connect("changed", self.on_currency_combo_changed)
		for currency in currencies:
			currency_combo.append_text(currency)

		hbox.pack_start(currency_combo, False, True, 0)

		return row

	def on_currency_combo_changed(self, combo):
		text = combo.get_active_text()
		if text is not None:
			print("Selected: currency=%s" % text)

	def tagname(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, False, True, 0)

		label2 =Gtk.Label()
		label2.set_markup("Tag \n Name")
		vbox.pack_start(label2,False,True,0)

		self.entry = Gtk.Entry()
		self.entry.set_text('Tag Name')

		hbox.pack_start(self.entry, False, True, 0)

		return row

	def taggedfield(self):
	 	row = Gtk.ListBoxRow()
	 	hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
	 	row.add(hbox)
	 	vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	 	hbox.pack_start(vbox, False, True, 0)

	 	label2 =Gtk.Label()
	 	label2.set_markup("Tagged \n Field")
	 	vbox.pack_start(label2,False,True,0)

	 	self.entry = Gtk.Entry()
	 	self.entry.set_text('Tagged Field')

	 	hbox.pack_start(self.entry, False, True, 0)

	 	return row

	def tagDescription(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		hbox.pack_start(vbox, False, True, 0)

		label2 =Gtk.Label()
		label2.set_markup("Tagged \n Description")
		vbox.pack_start(label2,False ,True,0)

		self.entry = Gtk.Entry()
		self.entry.set_text('Tagged Description')

		hbox.pack_start(self.entry, False, True, 0)
		return row

	def updatingtag(self):

		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		row.add(hbox)

		update = Gtk.Button(label = "Update")
		cancel = Gtk.Button(label = "Cancel")

		hbox.add(update)
		hbox.add(cancel)
		return row

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

		label2 =Gtk.Button(label = "Save as New \n PDML State")
		hbox.pack_start(label2,False,False,0)

		savecurrButton =Gtk.Button(label = "Save Current \n PDML State")
		hbox.pack_start(savecurrButton,False,False,0)

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


		self.entry = Gtk.Entry()
		self.entry.set_text('Filter Expression')
		hbox.pack_start(self.entry, False, False, 0)

		label2 =Gtk.Button(label = "Apply")
		hbox.pack_start(label2,False,False,0)

		savecurrButton =Gtk.Button(label = "Clear")
		hbox.pack_start(savecurrButton,False,False,0)

		closecurrButton =Gtk.Button(label = "Save")
		hbox.pack_start(closecurrButton,False,False,0)

		savefilterlabel = Gtk.Label()
		savefilterlabel.set_markup("<b>Saved Filter</b> ")
		hbox.pack_start(savefilterlabel, False, True, 0)

		currencies = ["Euro", "US Dollars", "British Pound", "Japanese Yen",
		"Russian Ruble", "Mexican peso", "Swiss franc"]
		currency_combo = Gtk.ComboBoxText()
		currency_combo.set_entry_text_column(0)
		currency_combo.connect("changed", self.on_savedfiltercombo)
		for currency in currencies:
			currency_combo.append_text(currency)

		hbox.pack_start(currency_combo, False, True, 0)

		applybutton =Gtk.Button(label = "Apply")
		hbox.pack_start(applybutton,False,False,0)


		return row

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

	def treeFrame(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)

		frame = [
		["Frame 718: frame, eth, ic, tcp",
		["Frame 718:74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface 0", True],
		["Ehernet II: Src: Elitegro_dd:12:cd(00:19:21:dd:12:cd), Dst:Broadcom_de:ad:05(00:10:18:de:ad:05)", False],
		["Internet Control Message Protocol",False],
		["Tramsimission Control Protocol, Src Port: (55394), Dst Port: 80 (80), Seq:0,Len:0",False]],
		["Frame 767: frame, eth, ip, tcp", ["frame", False]],
		["Frame 768: frame, eth, ip, tcp", ["frame", False]],
		["Frame 767: frame, eth, ip, tcp", ["frame", False]]
		]
		# the data are stored in the model
		# create a treestore with two columns
		hbox.store = Gtk.TreeStore(str, bool)
		# fill in the model
		for i in range(len(frame)):
			# the iter piter is returned when appending the author in the first column
			# and False in the second
			piter = hbox.store.append(None, [frame[i][0], False])
			# append the books and the associated boolean value as children of
			# the author
			j = 1
			while j < len(frame[i]):
				hbox.store.append(piter, frame[i][j])
				j += 1

		# the treeview shows the model
		# create a treeview on the model self.store
		view = Gtk.TreeView()
		view.set_model(hbox.store)
		# the cellrenderer for the first column - text
		renderer_in_framebutt = Gtk.CellRendererToggle()

		column_in_size = Gtk.TreeViewColumn("Frame Button", renderer_in_framebutt, active =1)


		view.append_column(column_in_size)

		renderer_frame = Gtk.CellRendererText()

		column_frame = Gtk.TreeViewColumn("Frame", renderer_frame, text=0)

		view.append_column(column_frame)

		renderer_in_size = Gtk.CellRendererToggle()

		column_in_size = Gtk.TreeViewColumn("Size", renderer_in_size, text=0)


		view.append_column(column_in_size)

		#renderer_in_out.connect("toggled", hbox.on_toggled())
		# add the treeview to the window
		hbox.add(view)
		hbox.add(self.removalclearbutt())

		return row

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
		hbox.pack_end(self.messagetypearea(),True,True,0)

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

		remove = Gtk.Button(label = "Remove") #the label
		clear = Gtk.Button(label = "Clear") # teh actual excel looking sheet

		hbox.add(remove)
		hbox.add(clear)

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







win = mainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
