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
BCal = Button(GUI,text='Plus(+)')
BCal.pack()

#Text box for value entry
Box1 = StringVar()
Input1 = ttk.Entry(GUI,textvariable = Box1, font=('Arial',20))
Input1.pack()


#Text box for value entry
Box2 = StringVar()
Input2 = ttk.Entry(GUI,textvariable = Box2, font=('Arial',20))
Input2.pack()

#Button2
BCal2 = ttk.Button(GUI,text='New Calculate',command=result)
BCal2.pack(ipadx = 20, ipady = 10)


GUI.mainloop()