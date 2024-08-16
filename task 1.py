import tkinter
import tkinter.ttk as ttk
def test():
    print(brand.get())
    print(Model.get())

def reset_form():
    brand.set("")
    Model.set("")
    color.set("")
    glass.set(False)
    Memory.set(False)

win = tkinter.Tk()
win.title("Mobile info")
win.geometry("600x300")

tkinter.Label(win, text="brand").place(x=20, y=40)
brand = tkinter.StringVar()
ttk.Combobox(win,
textvariable=brand,
values=["Apple", "Samsung", "Sony", "Nokia"],
state="readonly"
).place(x=20, y=60)

tkinter.Label(win, text="Model").place(x=20, y=60)
Model = tkinter.StringVar()
tkinter.Entry(win, textvariable=Model,width=23).place(x=40, y=60)