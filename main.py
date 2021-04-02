import tkinter as tki
from tkinter import messagebox

root = tki.Tk()
root.title('TicTacTie')

clicked=True
count=0

#when button clicked, function will run.
def b_click(b):
    global clicked,count

    if b["text"]==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
    elif b["text"]==" " and clicked==False:
        b["text"]="O"
        clicked=True
        count+=1
    else:
        messagebox.showerror("Tic Tac Toe","Hey! That box has already been selected\nPick another box...")


#Build out buttons
b1=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b1))
b2=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b2))
b3=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b3))

b4=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b4))
b5=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b5))
b6=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b6))

b7=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b7))
b8=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b8))
b9=tki.Button(root, text=" ", font=("Helvetica",20),height=3, width=6,bg="SystemButtonFace",command=lambda:b_click(b9))

#grid our button on UI
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

root.mainloop()