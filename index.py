import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400)
canvas1.pack()


def takeScreenshot():
    takeShot = pyautogui.screenshot()
    fileLocation = filedialog.asksaveasfilename(defaultextension='.png')
    takeShot.save(fileLocation)


myButton = tk.Button(text='Click Me For Screen-Shot', command=takeScreenshot, bg='green', fg='white', font=10)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()
