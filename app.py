import Tkinter as tk

class app(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		

if __name__ == "__main__":
	root = tk.Tk()
	app(root).pack(side = "top", fill = "both", expand = True)
	root.title("Imagine Engine")
	root.mainloop()
