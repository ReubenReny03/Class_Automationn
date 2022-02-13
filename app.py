import tkinter as tk
from frontpage import mainfile
from test import work
from tkinter import filedialog, Text
root = tk.Tk()      #to make GUI
openFile = tk.Button(root, text="START AUTOMATION",padx=50,pady=50,fg="white",bg="#263D42",command=mainfile)
openFile2 = tk.Button(root, text="TEST",padx=20,pady=20,fg="white",bg="#263D42",command=work)
openFile.pack()
openFile2.pack()
root.mainloop()