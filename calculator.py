from tkinter import *
root = Tk()
root.title("Calculator")

i = 0
def get_input(num):
    global i
    display.insert(i,num)
    i+=1

display = Entry(root)
display.grid(row=0,columnspan=3)
Button(root,text="1",command = lambda: get_input(1)).grid(row=1,column=0)
Button(root,text="2",command = lambda: get_input(2)).grid(row=1,column=1)
Button(root,text="3",command = lambda: get_input(3)).grid(row=1,column=2)

Button(root,text="4",command = lambda: get_input(4)).grid(row=2,column=0)
Button(root,text="5",command = lambda: get_input(5)).grid(row=2,column=1)
Button(root,text="6",command = lambda: get_input(6)).grid(row=2,column=2)

Button(root,text="7",command = lambda: get_input(7)).grid(row=3,column=0)
Button(root,text="8",command = lambda: get_input(8)).grid(row=3,column=1)
Button(root,text="9",command = lambda: get_input(9)).grid(row=3,column=2)
root.mainloop()
