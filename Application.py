from tkinter import *
from tkinter import ttk

class Application(Frame):

	dataHeaders = [
		"name",
		"hard",
		"clean",
		"cond",
		"bubble",
		"cream",
		"sap"
	]

	#---------handle selection--------
	def __TableSelect(self, event):
		self.ID = int(self.table.focus())
		self.descText.delete(1.0, "end")
		self.descText.insert(1.0, self.Oils[self.ID].desc)

	def __GridBox(self, input, row, column):
		input["borderwidth"] = 1
		input["relief"] = "solid"

		input.grid(row=row, column=column, ipadx=5, ipady=5, sticky="nesw")

	#----------------init---------------
	def __init__(self, master=None, Oils=None):
		super().__init__(master)
		self.master = master
		self.Oils = Oils


		#---------------------table full of soaps---------------------------
		#make container and table
		tableFrame = Frame(self, bg="green")
		table = ttk.Treeview(tableFrame)
		self.table = table

		#make scrollbar
		scroll = Scrollbar(tableFrame, orient=VERTICAL, command=table.yview)
		table.configure(yscrollcommand=scroll.set)

		#bind function to handle selections
		table.bind("<ButtonRelease-1>", self.__TableSelect)

		#set table columns
		table["columns"] = Application.dataHeaders

		#define the columns
		table.column("#0", width=0, stretch=NO)
		table.column("name", width=150, minwidth=50, anchor=W)
		table.column("hard", width=75, minwidth=5, anchor=E)
		table.column("clean", width=75, minwidth=5, anchor=E)
		table.column("cond", width=75, minwidth=5, anchor=E)
		table.column("bubble", width=75, minwidth=5, anchor=E)
		table.column("cream", width=75, minwidth=5, anchor=E)
		table.column("sap", width=100, minwidth=5, anchor=E)
		#name the columns
		table.heading("#0", text="")
		table.heading("name", text="Name")
		table.heading("hard", text="Hardness")
		table.heading("clean", text="Cleaning")
		table.heading("cond", text="Conditioning")
		table.heading("bubble", text="Bubbly")
		table.heading("cream", text="Creamy")
		table.heading("sap", text="Sap Value")

		#populate the table with data from Oils
		for n, Oil in enumerate(Oils):
			table.insert('', 'end', iid=n, text='', values=[
				Oil.name,
				Oil.hard,
				Oil.clean,
				Oil.cond,
				Oil.bubble,
				Oil.cream,
				Oil.sapK,
			])

		#set locations in container
		table.grid(row=0, column=0, sticky="nesw")
		scroll.grid(row=0, column=1, sticky="ns")
		tableFrame.rowconfigure(0, weight=1)
		tableFrame.columnconfigure(0, weight=1)


		#------------------------------description and percents------------------
		#set up the description
		descFrame = LabelFrame(self, text="More Info")
		descText = Text(descFrame, width=40, padx=10, pady=10)
		self.descText = descText

		#percent input
		percentFrame = LabelFrame(self, text="Percent Oil")
		percentInput = Entry(percentFrame, justify=RIGHT)
		percentTag = Label(percentFrame, text="%")

		#set location
		descText.pack(padx=20, pady=20, fill=BOTH, expand=True, anchor=N)
		percentInput.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=10)
		percentTag.grid(row=0, column=1, padx=(0, 10), pady=10)
		percentFrame.columnconfigure(0, weight=1)

		#------------------------------------product information-----------------------------
		#setup frame and labels
		productFrame = LabelFrame(self, text="Product Info")

		levelFrame = Frame(productFrame, borderwidth=1, relief="solid")

		suggestedVals = [
			"29-54",
			"12-22",
			"44-69",
			"14-46",
			"16-48"
		]
		currentVals = [
			StringVar(),
			StringVar(),
			StringVar(),
			StringVar(),
			StringVar(),
		]
		for i in range(5):
			self.__GridBox(Label(levelFrame, text=Application.dataHeaders[i+1]), 0, i+1)
			self.__GridBox(Label(levelFrame, text=suggestedVals[i]), 1, i+1)
			self.__GridBox(Label(levelFrame, textvariable=currentVals[i]), 2, i+1)
			currentVals[i].set("0")

		self.__GridBox(Frame(levelFrame), 0, 0)
		self.__GridBox(Label(levelFrame, text="suggested"), 1, 0)
		self.__GridBox(Label(levelFrame, text="current"), 2, 0)




		#set location
		levelFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nesw")

		#--------------------------------set possitions in master------------------------
		productFrame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nesw")
		percentFrame.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="ew")
		tableFrame.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nesw")
		descFrame.grid(row=0, column=1, sticky="nesw", padx=10, pady=(10, 0))
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)


'''
suggested and current levels
input for amount and concentration
KOH or NaOH
liquid or solid
ingredient display
'''
