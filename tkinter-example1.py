from tkinter import *
from tkinter import messagebox
import sevaSQL


def button_click():
    sevaSQL.insert_into_sql((name, date, weight, dimensions_x, dimensions_y, dimensions_z, composition, qual_control))
    # messagebox.showinfo("GUI Python", name.get() + " " + date.get())


root = Tk()
root.title("GUI на Python")

name = StringVar()
date = StringVar()
weight = StringVar()
dimensions_x = StringVar()
dimensions_y = StringVar()
dimensions_z = StringVar()
composition = StringVar()
qual_control = StringVar()

name_label = Label(text="Название заготовки:")
name_label.grid(row=0, column=0, sticky="w")
date_label = Label(text="Дата изготовления:")
date_label.grid(row=1, column=0, sticky="w")
weight_label = Label(text="Вес заготовки:")
weight_label.grid(row=2, column=0, sticky="w")
dimensions_x = Label(text="Геометрические параметры заготовки (X):")
dimensions_x.grid(row=3, column=0, sticky="w")
dimensions_y = Label(text="Геометрические параметры заготовки (Y):")
dimensions_y.grid(row=4, column=0, sticky="w")
dimensions_z = Label(text="Геометрические параметры заготовки (Z):")
dimensions_z.grid(row=5, column=0, sticky="w")
composition = Label(text="Состав:")
composition.grid(row=6, column=0, sticky="w")
qual_control = Label(text="Отметка о прохождении контроля качества:")
qual_control.grid(row=7, column=0, sticky="w")
qual_control = Label(text="Отправить:")
qual_control.grid(row=8, column=0, sticky="w")

name_entry = Entry(textvariable=name)
name_entry.grid(row=0, column=1, padx=3, pady=3)
date_entry = Entry(textvariable=date)
date_entry.grid(row=1, column=1, padx=3, pady=3)
weight_entry = Entry(textvariable=weight)
weight_entry.grid(row=2, column=1, padx=3, pady=3)
dimensions_x_entry = Entry(textvariable=dimensions_x)
dimensions_x_entry.grid(row=3, column=1, padx=3, pady=3)
dimensions_y_entry = Entry(textvariable=dimensions_y)
dimensions_y_entry.grid(row=4, column=1, padx=3, pady=3)
dimensions_z_entry = Entry(textvariable=dimensions_z)
dimensions_z_entry.grid(row=5, column=1, padx=3, pady=3)
composition_entry = Entry(textvariable=composition)
composition_entry.grid(row=6, column=1, padx=3, pady=3)
qual_control_entry = Entry(textvariable=qual_control)
qual_control_entry.grid(row=7, column=1, padx=3, pady=3)

message_button = Button(text="Send to DataBase", command=button_click)
message_button.grid(row=8, column=1, padx=3, pady=3, sticky="e")


print(sevaSQL.select_sql())

root.mainloop()

# select_sql()
# name, date, weight, dimensions_x, dimensions_y, dimensions_z, composition, qual_control
