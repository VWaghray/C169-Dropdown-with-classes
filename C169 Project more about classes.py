from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()

root.geometry("700x800")
root.title("More about Classes")
root.configure(bg = "#02343F")

cb1_get=StringVar()
cb1 = ttk.Combobox(root, textvariable=cb1_get, state="readonly", values=["Label", "Button", "Dropdown"], font = ("Cooper Black", 13, "bold"))
cb1.pack(pady=10)
class CreateElements:
    def __init__(self):
        print("This is CreateElements CLass")
        
    def createNewElement(self):
        cbb1 = cb1.get()
        if (cbb1 == "Label"):
            label=Label(root,text="A new label has been created using class", fg = "#F0EDCC", bg = "#02343F", font = ("Cooper Black", 13, "bold"))
            label.pack(pady = 10)
        elif(cbb1=="Button"):
            btn = Button(root,text="Button",command = self.message, font = ("Cooper Black", 13, "bold"), bg = "Salmon")
            btn.pack(pady = 10)
        elif(cbb1=="Dropdown"):
            cb_get=StringVar()
            cb = ttk.Combobox(root,textvariable= cb_get, state="readonly",values=[1,2,3,4], font = ("Cooper Black", 13, "bold"))
            cb.pack(pady=10)
    def message(self):
         messagebox.showinfo("showinfo","You clicked a button created using class 😀")
    
    
                    

obj = CreateElements()
btn = Button(root, text= "Create Element", command = obj.createNewElement, font = ("Cooper Black", 13, "bold"), bg = "Salmon")
btn.pack(pady=10)


root.mainloop() 