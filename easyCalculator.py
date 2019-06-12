from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def result():
    Value1 = int(Box1.get())
    #print(Value1)
    Value2 = int(Box2.get())
    text1 = '{:,d}'.format(Value1)
    text2 = ' + {:,d}\n'.format(Value2)
    textshow = 'Result: {:,d}'.format(Value1 + Value2)
    messagebox.showinfo('Result', text1+text2+textshow)


GUI = Tk()
GUI.geometry('500x300+100+100')
GUI.title('Calculator')

#Button1
#BCal = Button(GUI,text='Plus(+)')
#BCal.pack(pady=20)

#Text
Note1 = ttk.Label(GUI, text = 'Input Number 1 :')
Note1.pack(pady=10)
#Text box for value entry
Box1 = StringVar()
Input1 = ttk.Entry(GUI,textvariable = Box1, font=('Arial',20))
Input1.pack(pady=20)

#Text
Note2 = ttk.Label(GUI, text = 'Input Number 2 :')
Note2.pack(pady=10)
#Text box for value entry
Box2 = StringVar()
Input2 = ttk.Entry(GUI,textvariable = Box2, font=('Arial',20))
Input2.pack(pady=20)

#Button2
BCal2 = ttk.Button(GUI,text='Plus Result',command=result)
BCal2.pack(ipadx = 20, ipady = 10)


GUI.mainloop()