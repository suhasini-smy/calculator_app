import tkinter as tk 

#main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")

entry = tk.Entry(root,width=16,font=('Arial',24),bd=10,relief='ridge',justify='right')
entry.grid(row=0,column=0,columnspan=4)


expression=""

def press(num):
    global expression
    expression+=str(num)
    entry.delete(0,tk.END)
    entry.insert(tk.END,expression)

#function to evaluate the expression 
def equal(): 
    global expression
    try:
        total = str(eval(expression))
        entry.delete(0,tk.END)
        entry.insert(tk.END,total)
        expression=total 
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")
        expression=""

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

buttons = [
                ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
                ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
                ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
                ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
           ]

for(text,row,column) in buttons:
    if text== '=':
        tk.Button(root,text=text,width=5,height=2,font=('Arial',18),
        command=equal).grid(row=row,column=column,padx=5,pady=5)
    else:
        tk.Button(root,text=text,width=5,height=2,font=('Arial,18'),
        command=lambda t=text:press(t)).grid(row=row,column=column,padx=5,pady=5)

#clear button 
tk.Button(root,text='C',width=22,height=2,font=('Arial',18),
          command=clear).grid(row=5,column=0,columnspan=4,padx=5,pady=5)

root.mainloop()