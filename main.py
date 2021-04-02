import tkinter as tki
from tkinter import messagebox

root = tki.Tk()
root.title('TicTacTie')

clicked=True
count=0
#disable all the buttons
def disable_all_buttons():
    b1.config(state=tki.DISABLED)
    b2.config(state=tki.DISABLED)
    b3.config(state=tki.DISABLED)
    b4.config(state=tki.DISABLED)
    b5.config(state=tki.DISABLED)
    b6.config(state=tki.DISABLED)
    b7.config(state=tki.DISABLED)
    b8.config(state=tki.DISABLED)
    b9.config(state=tki.DISABLED)
#cheking wining situations
def checkWon():
    global winner
    winner=False

    #win for "X"
    if b1["text"]=="X" and  b2["text"]=="X" and  b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X wins")
        disable_all_buttons()
    elif b4["text"]=="X" and  b5["text"]=="X" and  b6["text"]=="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X wins")
        disable_all_buttons()
    elif b7["text"]=="X" and  b8["text"]=="X" and  b9["text"]=="X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X wins")
        disable_all_buttons()
    elif b1["text"]=="X" and  b5["text"]=="X" and  b9["text"]=="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X wins")
        disable_all_buttons()
    elif b3["text"]=="X" and  b5["text"]=="X" and  b7["text"]=="X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X wins")
        disable_all_buttons()
    elif b1["text"]=="X" and  b4["text"]=="X" and  b7["text"]=="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X wins")
        disable_all_buttons()
    elif b2["text"]=="X" and  b5["text"]=="X" and  b8["text"]=="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X wins")
        disable_all_buttons()
    elif b3["text"]=="X" and  b6["text"]=="X" and  b9["text"]=="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X wins")
        disable_all_buttons()
    
    #win for "O"

    elif b1["text"]=="O" and  b2["text"]=="O" and  b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O wins")
        disable_all_buttons()
    elif b4["text"]=="O" and  b5["text"]=="O" and  b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O wins")
        disable_all_buttons()
    elif b7["text"]=="O" and  b8["text"]=="O" and  b9["text"]=="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O wins")
        disable_all_buttons()
    elif b1["text"]=="O" and  b5["text"]=="O" and  b9["text"]=="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O wins")
        disable_all_buttons()
    elif b3["text"]=="O" and  b5["text"]=="O" and  b7["text"]=="O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O wins")
        disable_all_buttons()
    elif b1["text"]=="O" and  b4["text"]=="O" and  b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O wins")
        disable_all_buttons()
    elif b2["text"]=="O" and  b5["text"]=="O" and  b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O wins")
        disable_all_buttons()
    elif b3["text"]=="O" and  b6["text"]=="O" and  b9["text"]=="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O wins")
        disable_all_buttons()
    else:
        pass


#when button clicked, function run.
def b_click(b):
    global clicked,count

    if b["text"]==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        checkWon()
    elif b["text"]==" " and clicked==False:
        b["text"]="O"
        clicked=True
        count+=1
        checkWon()
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