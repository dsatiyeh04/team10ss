import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio 
from gi.repository.GdkPixbuf import Pixbuf

class mainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title= "Filter")
		self.set_border_width(10) #border around window
		#self.set_default_size(300,200)

		hb = Gtk.HeaderBar(title= "Filter")
		#hb.set_show_close_button(False)

		# hb.props.title = "Filter"
		self.set_titlebar(hb)

		closebutton = Gtk.Button(label="X")
		closebutton.set_relief(Gtk.ReliefStyle.NONE)
		img = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.MENU)
		closebutton.set_image(img)
		closebutton.connect("clicked", Gtk.main_quit)
		hb.pack_end(closebutton)



		#stageboxes

		mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(mainbox)

		mainbox.add(self.stagesrow())

		mainListbox = Gtk.ListBox()
		mainListbox.set_selection_mode(Gtk.SelectionMode.NONE)
		mainbox.pack_start(mainListbox, False, False, 0) # box, cihld, expand ,fill, padding
		mainListbox.add(self.mainListBox())

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

		

		listbox_2 = Gtk.ListBox()
		listbox_2.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox_2,False, False, 0)

		return sessionbox


	def pdmlviewCol(self):
		sessionbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		
		listbox = Gtk.ListBox()
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox, False, False, 0)

		listbox_3 = Gtk.ListBox()
		listbox_3.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox_3,False,False,0)

		listbox_3.add(self.packetAreaName())
		listbox_3.add(self.treeFrame())
		listbox_2 = Gtk.ListBox()
		listbox_2.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox_2,False, False, 0)

		listbox_2.add(self.filterAreaName())
		listbox_2.add(self.filterAreaSaving())

		listbox_4 = Gtk.ListBox()
		listbox_4.set_selection_mode(Gtk.SelectionMode.NONE)
		sessionbox.pack_start(listbox_4,False,False,0)

		listbox_4.add(self.bottomarea())

		return sessionbox

		return row

	def filterAreaName(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)

		label1 = Gtk.Label()
		label1.set_markup("<u>Create/Update a Filter</u> ")
		hbox.pack_start(label1, False, True, 0)


		return row

	def filterAreaSaving(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		row.add(hbox)

		label1 = Gtk.Label()
		label1.set_markup("<b>Filter Name</b> ")
		hbox.pack_start(label1, False, True, 0)


		self.entry = Gtk.Entry()
		self.entry.set_text('Filter Name')
		hbox.pack_start(self.entry, False, False, 0)
		
		label1 = Gtk.Label()
		label1.set_markup("<b>Filter Expression</b> ")
		hbox.pack_start(label1, False, True, 0)
		
		self.entry = Gtk.Entry()
		self.entry.set_text('Filter Expression')
		hbox.pack_start(self.entry, False, False, 0)

		label2 =Gtk.Button(label = "Save")
		hbox.pack_start(label2,False,False,0)

		savecurrButton =Gtk.Button(label = "Cancel")
		hbox.pack_start(savecurrButton,False,False,0)


		return row

	def on_savedfiltercombo(self, combo):
		text = combo.get_active_text()
		if text is not None:
			print("Selected: currency=%s" % text)

	def packetAreaName(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)
		return row

	def treeFrame(self):
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		row.add(hbox)

		frame = [
		["ipx",
		["tcp", True], 
		["upd", False],
		["!{udp.port=53 || tcp.port==53}",False],
		["Eth.addr==ff;ff;ff;ff;ff;ff",False]],
		["tcp", ["frame", False]],
		["upd", ["frame", False]],
		["!{udp.port=53 || tcp.port==53}", ["frame", False]]
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

		column_in_size = Gtk.TreeViewColumn("Saved Filter", renderer_in_framebutt, active =1)


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
			copy = Gtk.Button(label = "Copy")
			update = Gtk.Button(label = "Update")
			delete = Gtk.Button(label = "Delete")
			vbox.add(copy)
			vbox.add(update)
			vbox.add(delete)
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

		return buttonbox

	def messagetypearea(self):
		bigboxmessagetypearea = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		bigboxmessagetypearea.add(hbox)

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
		
		return box







win = mainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
