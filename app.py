import Tkinter as tk
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk


class app(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.file_path_label = tk.Label(parent, text = "Image File Path")
		self.file_path_label.pack()

		self.file_path = tk.Entry(parent, justify = tk.LEFT)
		self.file_path.pack()
		self.file_path.insert(0, "")

		self.image = tk.Label(parent, width = 60, height = 40)
		self.image.pack()

		self.get_image = tk.Button(parent, text = "Input Image", command = self.open_image)
		self.get_image.pack()

	def open_image(self):
		filename = askopenfilename(filetypes = [("pngs","*.png")])
		print filename
		self.file_path.delete(0, tk.END)
		self.file_path.insert(0, filename)
		
		if filename:
			img = ImageTk.PhotoImage(file = filename)
			self.image.configure(image = img)

if __name__ == "__main__":
	root = tk.Tk()
	app(root).pack(side = "top", fill = "both", expand = True)
	root.title("Imagine Engine")
	root.mainloop()
