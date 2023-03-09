import tkinter as tk
from tkinter import ttk
from PIL import _imaging, _imagingtk
from Start.cla_start import Vistas

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root = tk.Tk()
root.title('Vista')
root.geometry('600x400')
user_name = tk.StringVar()

frame1 = ttk.Frame(root)
frame1.pack(side='left', fill='both', expand=True)


label_1 = tk.Label(frame1, text='Label 1', bg='green', fg='white')
label_1.pack(ipadx=10, ipady=10, expand=True, fill='both', side='top')

label_2 = tk.Label(frame1, text='Label 2', bg='green', fg='white')
label_2.pack(ipadx=10, ipady=10, expand=True, fill='both', side='top')

label_3 = tk.Label(root, text='Label 3', bg='red', fg='white')
label_3.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')

Entry1 = ttk.Entry(root, width=20, textvariable=user_name)
Entry1.pack(side='left')
Entry1.focus()

button1 = ttk.Button(root, text='Avanzar', command=Vistas.menu)
button1.pack(side='left', fill='x', expand=True)

root.mainloop()




