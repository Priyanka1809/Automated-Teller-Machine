from tkinter import ttk
from tkinter import *
root=Tk()#window
content=ttk.Frame(root,padding=(20,20,30,30))


label0=ttk.Label(content,text="Welcome to ATM")
label1=ttk.Label(content,text="Select any one service:")

def balance():
    balance=1000
    print("Balance  $ ",balance)
def withdraw():
    balance=1000
    print("Balance  $  ",balance)
    Withdraw=float(input("Enter Withdraw amount $ "))
    if Withdraw>0:
        forewardbalance=(balance-Withdraw)
        print("Foreward Balance  $ ",forewardbalance)
    elif Withdraw>balance:
        print("No funds in account")
    else:
        print("None withdraw made")
def deposit():
    balance=1000
    print("Balance  $ ",balance)
    Deposit=float(input("Enter deposit amount $ "))
    if Deposit>0:
        forewardbalance=(balance+Deposit)
        print("Forewardbalance  $ ",forewardbalance)
    else:
        print("None deposit made")
def quit():
    exit()
    
button1=Button(content,text="Balance",command=balance)
button2=Button(content,text="Withdraw",command=withdraw)
button3=Button(content,text="Deposit",command=deposit)
button4=Button(content,text="Quit",command=quit)


content.grid(row=0,column=0)
label0.grid(row=0,column=0,columnspan=2)
label1.grid(row=1,column=0)
button1.grid(row=2,column=0)
button2.grid(row=3,column=0)
button3.grid(row=4,column=0)
button4.grid(row=5,column=0)

root.mainloop()


