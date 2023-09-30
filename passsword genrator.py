from tkinter import*
import random
import string


root =Tk()
root.geometry("750x430")
root.title("Password Generator")
root.resizable(False,False)
root.config(bg="white")


passstr = StringVar()
pwd_len = IntVar()

img=PhotoImage(file="bg.png")
Label(root,image=img,bg='white').place(x=2,y=1)

def get_pass():
    pass1 = string.ascii_letters + string.digits +string.punctuation
    password =""

    for x in range (pwd_len.get()):
        password = password + random.choice(pass1)
        passstr.set(password)

Label(root,text="Password Generator",font="calibiri 18 bold",bg="white").pack()
Label(root,text="Length of Password",fg="light sea green",bg="white",font=("Helvetica",16)).place(x=495,y=60)
Entry(root,textvariable=pwd_len,width=15,font=("Helvetica",18)).place(x=500,y=100)
Button(root,text="Generate Password",command=get_pass,bg="light sea green",fg="white",font=("Helvetica",14)).place(x=505,y=160)
Entry(root,textvariable=passstr,width=15,font=("Helvetica",18)).place(x=500,y=240)
Button(root,text="Re-Generate Password",command=get_pass,bg="light sea green",fg="white",font=("Helvetica",14)).place(x=490,y=300)

root.mainloop()