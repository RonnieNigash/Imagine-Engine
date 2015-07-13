#!/usr/bin/python
from Tkinter import *
from tkFileDialog import *
class App:
	def __init__(self, parent = Tk()):
		self.mainWindow = parent
		self.mainWindow.title("Image Engine")
		self.makemenu()
		self.makelabel()
		self.makeimage()

	def makemenu(self):
		self.menubar = Menu(self.mainWindow)
		self.filemenu = Menu(self.menubar, tearoff = 0)
		self.filemenu.add_command(label = "Open", command = self.openfile)
		self.filemenu.add_separator()
		self.filemenu.add_command(label = "Exit", command = self.mainWindow.destroy)
		self.menubar.add_cascade(label = "File", menu = self.filemenu)
		self.mainWindow.config(menu = self.menubar)

	def openfile(self):
		filename = askopenfilename(filetypes = [("jpgs", "*.jpg"), ("pngs","*.png"), ("gifs", "*.gifs"), ("allfiles", "*")] )
		print filename
		self.text.delete(1.0, END)
		self.text.insert(1.0, filename)

	def makeimage(self):
		pass
		#filename = Entry(self.text)
		#Image = PhotoImage(file = filename)

	def makelabel(self):
		self.text = Text(self.mainWindow, width = 60, height = 1, background = 'white')
		self.text.pack(expand = TRUE, fill = BOTH)

	def find(self):
		# @TODO
		pass

	def close(self):
		# @TODO
		pass

app = App()
app.mainWindow.mainloop()
