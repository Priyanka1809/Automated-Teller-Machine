from tkinter import ttk
from tkinter import *
root=Tk()#window
content=ttk.Frame(root,padding=(7,7,12,12))

label0=ttk.Label(content,text="Student Information")

label1=ttk.Label(content,text="ID:")
a=IntVar()
entry1=ttk.Entry(content,text=a)

label2=ttk.Label(content,text="Name:")
b=StringVar()
entry2=ttk.Entry(content,text=b)

label3=ttk.Label(content,text="Surname:")
c=StringVar()
entry3=ttk.Entry(content,text=c)

label4=ttk.Label(content,text="City:")
d=StringVar()
entry4=ttk.Entry(content,text=d)

label5=ttk.Label(content,text="Branch:")
e=StringVar()
entry5=ttk.Entry(content,text=e)

label6=ttk.Label(content,text="Gender:")
label7=ttk.Label(content,text="Country:")
label8=ttk.Label(content,text="State:")


CheckVar1=BooleanVar()
CheckVar2=BooleanVar()
check1=ttk.Checkbutton(content,text="Male",onvalue=True,offvalue=False,variable=CheckVar1)
check2=ttk.Checkbutton(content,text="Female",onvalue=True,offvalue=False,variable=CheckVar2)

v=StringVar()
radio1=ttk.Radiobutton(content,text="India",variable=v,value="India")
radio2=ttk.Radiobutton(content,text="Others",variable=v,value="Others")

name=["Maharashtra","Goa","Chennai","Gujrat"]
k=StringVar()
combo1=ttk.Combobox(content,values=name,width=10,text=k)

def submit():
    print("ID:",a.get())
    print("Name:",b.get())
    print("Surname:",c.get())
    print("City:",d.get())
    print("Branch:",e.get())
    if (CheckVar1.get()==True):
        print("Gender:Male")
    else:
        print("Gender:Female")
    print("Country:",v.get())
    print("State:",k.get())
    
def exit():
    root.destroy()

button1=ttk.Button(content,text="Submit",command=submit)
button2=ttk.Button(content,text="Exit",command=exit)

content.grid(row=0,column=0)
label0.grid(row=0,column=0,columnspan=2)
label1.grid(row=1,column=0)
entry1.grid(row=1,column=1)
label2.grid(row=2,column=0)
entry2.grid(row=2,column=1)
label3.grid(row=3,column=0)
entry3.grid(row=3,column=1)
label4.grid(row=4,column=0)
entry4.grid(row=4,column=1)
label5.grid(row=5,column=0)
entry5.grid(row=5,column=1)
label6.grid(row=6,column=0,rowspan=2)


check1.grid(row=6,column=1)
check2.grid(row=7,column=1)

label7.grid(row=8,column=0)
radio1.grid(row=8,column=1)
radio2.grid(row=9,column=1)

label8.grid(row=10,column=0)
combo1.grid(row=10,column=1)

button1.grid(row=11,column=0)
button2.grid(row=11,column=1)

root.mainloop()
