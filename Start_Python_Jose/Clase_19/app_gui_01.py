import tkinter as tk
from tkinter import ttk


def greet():
    print('Aloha mate!!')
    
   
root = tk.Tk()
root.title('Hello')

greet_button = ttk.Button(root, text='Greet', command=greet)
greet_button.pack(side='left', fill='x', expand=True)

exit_button = ttk.Button(root, text='Exit', command=root.destroy)
exit_button.pack(side='left', fill='x', expand=True)

root.mainloop()
