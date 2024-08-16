import tkinter
import tkinter.ttk as ttk

def test():
    print(model.get())

win = tkinter.Tk()

win.title("mobile Info")
win.geometry("300x300")

tkinter.Label(win, text="brand").place(x=20, y=20)
brand = tkinter.StringVar()
ttk.Combobox(win,
             textvariable=brand,
             values=["apple", "samsung", "sony", "nokia"],
             state="readonly"
             ).place(x=80, y=20)

tkinter.Label(win, text="model").place(x=20, y=60)
model = tkinter.StringVar()
tkinter.Entry(win, textvariable=model).place(x=80, y=60)

tkinter.Label(win, text="color").place(x=20, y=100)
color = tkinter.StringVar()
ttk.Combobox(win,
             textvariable=color,
             values=["rose_gold", "white", "silver", "black , others"],
             state="readonly"
             ).place(x=80, y=100)


tkinter.Label(win, text="glass").place(x=20, y=140)
glass = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="glass", variable=glass).place(x=80, y=140)

tkinter.Label(win, text="memory").place(x=20, y=180)
memory = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="memory", variable=memory).place(x=80, y=180)

tkinter.Button(win, text="Sell", width=10, command=test).place(x=80,y=240)

win.mainloop()

