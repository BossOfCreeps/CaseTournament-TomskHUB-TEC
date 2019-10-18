from tkinter import *
from tkinter import messagebox
from sevaSQL import *
from sevaQR import *
import os

#def button_click():

    
    #sevaSQL.insert_into_sql
    # print(insert_into_sql(name.get() + date.get() + float(weight.get()) + float(dimensions_x.get()) + float(dimensions_y.get()) + float(dimensions_z.get()) + composition.get() + int(qual_control.get())))
    # messagebox.showinfo("GUI Python", name.get() + " " + date.get())

def generate_QR_code():
    global name, date, weight, dimensions_x, dimensions_y, dimensions_z, composition, qual_control
    generate_QR(name.get(), "'"+name.get() + "', '" + date.get() + "', " + weight.get() + ", " + dimensions_x.get() + ", " + dimensions_y.get() + ", " + dimensions_z.get()  + ", '" + composition.get() +"', '"+ qual_control.get()+"'")

def print_QR_code():
    global name
    os.startfile(name.get()+".png", "print")

def load_from_db():
    global name_for_load, name, date, weight, dimensions_x, dimensions_y, dimensions_z, composition, qual_control
    col = find_sql(name_for_load.get())
    print(col[0][1])

    name.set(col[0][1])
    date.set(col[0][2])
    weight.set(col[0][3])
    dimensions_x.set(col[0][4])
    dimensions_y.set(col[0][5])
    dimensions_z.set(col[0][6])
    composition.set(col[0][7])
    qual_control.set(col[0][8])

def load_to_db():
    update_sql(name.get(), date.get(), weight.get(), dimensions_x.get(), dimensions_y.get(), dimensions_z.get(), composition.get(), qual_control.get())

root = Tk()
root.title("App")

name_for_load = StringVar()
name = StringVar()
date = StringVar()
weight = StringVar()
dimensions_x = StringVar()
dimensions_y = StringVar()
dimensions_z = StringVar()
composition = StringVar()
qual_control = StringVar()

name_for_load_label = Label(text="Название для внесения изменений:")
name_for_load_label.grid(row=0, column=0, sticky="w")
empty_label = Label(text=" ")
empty_label.grid(row=1, column=0, sticky="w")
name_label = Label(text="Название заготовки:")
name_label.grid(row=2, column=0, sticky="w")
date_label = Label(text="Дата изготовления:")
date_label.grid(row=3, column=0, sticky="w")
weight_label = Label(text="Вес заготовки:")
weight_label.grid(row=2+2, column=0, sticky="w")
dimensions_x_label = Label(text="Геометрические параметры заготовки (X):")
dimensions_x_label.grid(row=3+2, column=0, sticky="w")
dimensions_y_label = Label(text="Геометрические параметры заготовки (Y):")
dimensions_y_label.grid(row=4+2, column=0, sticky="w")
dimensions_z_label = Label(text="Геометрические параметры заготовки (Z):")
dimensions_z_label.grid(row=5+2, column=0, sticky="w")
composition_label = Label(text="Состав:")
composition_label.grid(row=6+2, column=0, sticky="w")
qual_control_label = Label(text="Отметка о прохождении контроля качества:")
qual_control_label.grid(row=7+2, column=0, sticky="w")
gen_qr_label = Label(text="Сгенерировать QR:")
gen_qr_label.grid(row=8+2, column=0, sticky="w")
print_qr_label = Label(text="Напечатать QR:")
print_qr_label.grid(row=9+2, column=0, sticky="w")

name_for_load = Entry(textvariable=name_for_load)
name_for_load.grid(row=0, column=1, padx=3, pady=3)
name_entry = Entry(textvariable=name)
name_entry.grid(row=0+2, column=1, padx=3, pady=3)
date_entry = Entry(textvariable=date)
date_entry.grid(row=1+2, column=1, padx=3, pady=3)
weight_entry = Entry(textvariable=weight)
weight_entry.grid(row=2+2, column=1, padx=3, pady=3)
dimensions_x_entry = Entry(textvariable=dimensions_x)
dimensions_x_entry.grid(row=3+2, column=1, padx=3, pady=3)
dimensions_y_entry = Entry(textvariable=dimensions_y)
dimensions_y_entry.grid(row=4+2, column=1, padx=3, pady=3)
dimensions_z_entry = Entry(textvariable=dimensions_z)
dimensions_z_entry.grid(row=5+2, column=1, padx=3, pady=3)
composition_entry = Entry(textvariable=composition)
composition_entry.grid(row=6+2, column=1, padx=3, pady=3)
qual_control_entry = Entry(textvariable=qual_control)
qual_control_entry.grid(row=7+2, column=1, padx=3, pady=3)


gen_qr_button = Button(text="Загрузить из БД: ", command=load_from_db)
gen_qr_button.grid(row=0, column=2, padx=3, pady=3, sticky="e")
gen_qr_button = Button(text="Загрузить в БД: ", command=load_to_db)
gen_qr_button.grid(row=0, column=3, padx=3, pady=3, sticky="e")
gen_qr_button = Button(text="Сгенерировать QR code", command=generate_QR_code)
gen_qr_button.grid(row=8+2, column=1, padx=3, pady=3, sticky="e")
print_qr_button = Button(text="Напечатать QR code", command=print_QR_code)
print_qr_button.grid(row=9+2, column=1, padx=3, pady=3, sticky="e")


#print(sevaSQL.select_sql())

root.mainloop()

# select_sql()
# name, date, weight, dimensions_x, dimensions_y, dimensions_z, composition, qual_control
