from tkinter import *
import tkinter as tk 

root =tk.Tk()
root.title("Calculator")
root.geometry("435x600+10+5")
root.resizable(False,False)
root.configure(bg='skyblue')

expression=" "
#calculation

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def calculate():

    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=" "
    except:
            equation.set(' Error!')
            expression=" "
def clear():
    expression=" "
    equation.set(" ")
def clickcut():
    global expression
    expression=expression[:-1]
    equation.set(expression)
    
l1=Label(root,text="Calculator",font=("arial black",15,"bold"),background="black", foreground="white",padx=160,pady=15)
l1.place(x=0,y=0)
#textbox=Label(root,text="100",font='Arial 20',padx=160,pady=15)
equation=StringVar()
textbox=Entry(root,font='Arial 25',width=20,borderwidth=5 ,textvariable=equation)
textbox.place(x=30,y=90)

b1=Button(root,text="C",font='Arial 20', padx=23,pady=5,command=clear)
b2=Button(root,text="%",font='Arial 20', padx=21,pady=5,command=lambda:press('%'))
b3=Button(root,text="X",font='Arial 20', padx=24,pady=5,command=clickcut)
b4=Button(root,text="/",font='Arial 20', padx=30,pady=5,command=lambda:press('/'))

b5=Button(root,text="7",font='Arial 20', padx=25,pady=5,command=lambda:press(7))
b6=Button(root,text="8",font='Arial 20', padx=25,pady=5,command=lambda:press(6))
b7=Button(root,text="9",font='Arial 20', padx=25,pady=5,command=lambda:press(5))
b8=Button(root,text="*",font='Arial 20', padx=28,pady=5,command=lambda:press('*'))

b9=Button(root,text="4",font='Arial 20', padx=25,pady=5,command=lambda:press(4))
b10=Button(root,text="5",font='Arial 20', padx=25,pady=5,command=lambda:press(5))
b11=Button(root,text="6",font='Arial 20', padx=25,pady=5,command=lambda:press(6))
b12=Button(root,text="-",font='Arial 20', padx=29,pady=5,command=lambda:press('-'))

b13=Button(root,text="1",font='Arial 20', padx=25,pady=5,command=lambda:press(1))
b14=Button(root,text="2",font='Arial 20', padx=25,pady=5,command=lambda:press(2))
b15=Button(root,text="3",font='Arial 20', padx=25,pady=5,command=lambda:press(3))
b16=Button(root,text="+",font='Arial 20', padx=25,pady=5,command=lambda:press('+'))

b17=Button(root,text="0",font='Arial 20', padx=25,pady=5,command=lambda:press(0))
b18=Button(root,text=".",font='Arial 20', padx=28,pady=5,command=lambda:press('.'))
b19=Button(root,text="=",font='Arial 20', padx=72,pady=5 ,command=calculate)

b1.place(x=30,y=240)
b2.place(x=125,y=240)
b3.place(x=220,y=240)
b4.place(x=315,y=240)

b5.place(x=30,y=310)
b6.place(x=125,y=310)
b7.place(x=220,y=310)
b8.place(x=315,y=310)

b9.place(x=30,y=380)
b10.place(x=125,y=380)
b11.place(x=220,y=380)
b12.place(x=315,y=380)

b13.place(x=30,y=450)
b14.place(x=125,y=450)
b15.place(x=220,y=450)
b16.place(x=315,y=450)

b17.place(x=30,y=520)
b18.place(x=125,y=520)
b19.place(x=220,y=520)

root.mainloop()
