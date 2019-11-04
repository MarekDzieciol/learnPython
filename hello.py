# lets create some gui app

import tkinter as tk
 
HEIGHT = 700
WIDTH = 800

#root contains everything
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#end of frame
root.mainloop()
