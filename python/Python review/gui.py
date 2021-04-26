import tkinter as tk
from tkinter.messagebox import *

root = tk.Tk()
lb = tk.Listbox(root)
sl = tk.Scrollbar(root)
sl.pack(side = 'right', expand = 'yes', fill = 'y')
lb['yscrollcommand'] = sl.set
for i in range(100):
    lb.insert('end', str(i))
lb.pack(side = 'left', expand = 'yes')
sl['command'] = lb.yview
root.mainloop()