import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg

mobile_list = []
def save_click():
    mobile = (brand.get(), model.get(), color.get())
    print(mobile)
    mobile_list.append(mobile)
    msg.showinfo("mobile Save", "mobile " + str(mobile) + " Saved")
    refresh_table()
    brand.set("")
    model.set("")
    color.set("")
def refresh_table():
    for item in table.get_children():
        table.delete(item)
    for mobile in mobile_list:
        table.insert("end", values= mobile, tags= mobile[3])

win = tkinter.Tk()

win.title("mobile Info")
win.geometry("600x300")

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

table = ttk.Treeview(win, columns=(1, 2, 3), height=12, show="headings")
table.heading(1, text="brand")
table.heading(2, text="mobile")
table.heading(3, text="color")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)

table.tag_configure("save", background="lightgreen")
table.tag_configure("does_not_save", background="red")

table.place(x=230, y=20)

refresh_table()

tkinter.Button(win, text="Save", width=10, command=save_click).place(x=80,y=240)

win.mainloop()


