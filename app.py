import Tkinter
import sys

class App(Tkinter.Tk):
	


	def __init__(self):
		Tkinter.Tk.__init__(self)
		toolbar = Tkinter.Frame(self)
		toolbar.pack(side="top", fill="x")

		button1 = Tkinter.Button(self, text = "Find matches", command = self.find)
		button2 = Tkinter.Button(self, text = "Close", command = self.close)
		
		button1.pack(in_=toolbar, side = "left")
		button2.pack(in_=toolbar, side = "right")

		self.text = Tkinter.Text(self, wrap = "word")
		self.text.pack(side = "top", fill = "x", expand = True)
	

	def find(self):
		# @TODO
		pass
	
	def close(self):
		# @TODO
		pass

app = App()
app.mainloop()
