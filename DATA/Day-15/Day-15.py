# GUI -Graphical User Interface

#  Libraries
#1. Tkinter
#2. PyOT
#3. Turtle

import tkinter as ttk
app=ttk.Tk()
app.title('My App')
app.geometry('600x400')

ttk.Label(app, text = 'A simple Text Label').place(x=50,y=50)
ttk.Label(app, text = 'Ashish Lekhyani').place(x=285,y=200)

app.mainloop()