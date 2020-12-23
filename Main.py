import json
from tkinter import *
import os
import Application


#make Oil class ot unify
class Oil:
	def __init__(self, Dict):
		self.name = Dict["name"]
		self.hard = Dict["hard"]
		self.clean = Dict["clean"]
		self.cond = Dict["cond"]
		self.bubble = Dict["bubble"]
		self.cream = Dict["cream"]
		self.sapNa = Dict["sap Na"]
		self.sapK = Dict["sap K"]
		self.desc = Dict["desc"]
		self.dict = Dict


#get soap values
with open("Values.json") as JsonData:
	Values = json.load(JsonData)

#convert to object
Oils = []
for Val in Values:
	Oils.append( Oil(Val) )


#create window
window = Tk()
window.resizable(True, True)
window.title("Soap Calulator")
window.geometry("1000x600")

#load window content
app = Application.Application(window, Oils)
app.pack(fill=BOTH, expand=True)
window.mainloop()
