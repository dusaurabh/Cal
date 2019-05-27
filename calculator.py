from tkinter import *
import parser

root = Tk()
root.title("Calculator")

i = 0
def get_input(num):
    global i
    display.insert(i,num)
    i+=1
    
def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def calculate():
    entire_string = display.get()
    try:
        result =   parser.expr(entire_string).compile()
        new_result = eval(result)
        clear_all()
        display.insert(0,new_result)
    except:
        clear_all()
        display.insert(0,"Zero Divison Error")
      
    
def clear_all():
    display.delete(0,END)
    
    
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,'Error')
    
display = Entry(root)
display.grid(row=0,columnspan=3)
Button(root,text="1",command = lambda: get_input(1)).grid(row=1,column=0)
Button(root,text="2",command = lambda: get_input(2)).grid(row=1,column=1)
Button(root,text="3",command = lambda: get_input(3)).grid(row=1,column=2)
Button(root,text="+",command = lambda: get_operator("+")).grid(row=1,column=3)
Button(root,text="pie",command = lambda: get_operator("*3.14")).grid(row=1,column=4)
Button(root,text="Delete",command = lambda: undo()).grid(row=1,column=5)


Button(root,text="4",command = lambda: get_input(4)).grid(row=2,column=0)
Button(root,text="5",command = lambda: get_input(5)).grid(row=2,column=1)
Button(root,text="6",command = lambda: get_input(6)).grid(row=2,column=2)
Button(root,text="-",command = lambda: get_operator("-")).grid(row=2,column=3)
Button(root,text="%",command = lambda: get_operator("%")).grid(row=2,column=4)



Button(root,text="7",command = lambda: get_input(7)).grid(row=3,column=0)
Button(root,text="8",command = lambda: get_input(8)).grid(row=3,column=1)
Button(root,text="9",command = lambda: get_input(9)).grid(row=3,column=2)
Button(root,text="*",command = lambda: get_operator("*")).grid(row=3,column=3)
Button(root,text="(",command = lambda: get_operator("(")).grid(row=3,column=4)
Button(root,text=")",command = lambda: get_operator(")")).grid(row=3,column=5)

Button(root,text="AC",command = lambda: clear_all()).grid(row=4,column = 0)
Button(root,text="0",command = lambda: get_input(0)).grid(row=4,column=1)
Button(root,text="=",command = lambda: calculate()).grid(row=4,column=2)
Button(root,text="/",command = lambda: get_operator("/")).grid(row=4,column=3)
Button(root,text="exp",command = lambda: get_operator("**")).grid(row=4,column=4)
Button(root,text="^2",command = lambda: get_operator("**2")).grid(row=4,column=5)

root.mainloop()
