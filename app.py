import Tkinter as tk
from PIL import Image, ImageTk

class app(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.file_path_label = tk.Label(parent, text = "Image File Path")
		self.file_path_label.pack()

		self.file_path = tk.Entry(parent, justify = tk.LEFT)
		self.file_path.pack()
		self.file_path.insert(0, "")

		self.image = tk.Label(parent, text = "Image")
		self.image.pack()

		self.get_image = tk.Button(parent, text = "Input Image", command = open_image)
		self.get_image.pack()

def open_image(self):
	filename = tk.askopenfilename(filetypes = [("jpgs", "*.jpg"), ("pngs","*.png"), ("gifs", "*.gifs"), ("allfiles", "*")] )
	print filename
	self.file_path.delete(1.0, END)
	self.file_path.insert(0, filename)

	img = tk.PhotoImage(Image.open(filename))
	self.image.delete(1.0, END)
	self.image.insert(0, img)

if __name__ == "__main__":
	root = tk.Tk()
	app(root).pack(side = "top", fill = "both", expand = True)
	root.title("Imagine Engine")
	root.mainloop()
