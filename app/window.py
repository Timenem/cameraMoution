import tkinter as tk 
from tkinter import * 
from tkinter.ttk import Combobox
from cam import startCamera

window = tk.Tk()


def timerValues()->int:
    timerText = Label(window,text="установите задержку").grid(column=0,row=0)
    combo =  Combobox(window,values=(5,10,30))  
    combo['values'] = (5, 10, 30)  
    combo.current(1) 
    combo.grid(column=0,row=1)
    return int(combo.get())


def mainWindow():
    window.title("moution cam")
    window.geometry('400x200')
    t = timerValues()
    startRecordBtn = Button(window,text='start record',command=lambda:startCamera(t)).grid(column=2, row=1)
    stopRecordBtn = Button(window,text='stop record',command=lambda:window.bind("<Escape>")).grid(column=3, row=1)
    window.mainloop()   

if __name__ == '__main__':
    mainWindow()