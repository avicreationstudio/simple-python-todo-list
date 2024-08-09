from tkinter import *

HEADING_FONT = ( "Consolas", 13, "underline" )
NORMAL_FONT = ( "Consolas", 10 )

main_widget = Tk()
main_widget.geometry("500x500")

# your code
# 4 things
#    1. Label
#    2. Entry   : input
#    3. Button
#    4. Listbox : table
label_input_section = Label(main_widget, text="input section")
label_input_section.grid(column=1, row=1)
label_input_section.configure(font=HEADING_FONT)

label_name = Label(main_widget, text="name :")
label_name.grid(column=1, row=2)
label_name.configure(font=NORMAL_FONT)

label_age = Label(main_widget, text="age :")
label_age.grid(column=1, row=3)
label_age.configure(font=NORMAL_FONT)

label_dept = Label(main_widget, text="dept :")
label_dept.grid(column=1, row=4)
label_dept.configure(font=NORMAL_FONT)

input_name = Entry(main_widget,)
input_name.grid(column=2,row=2)

input_age = Entry(main_widget,)
input_age.grid(column=2,row=3)

input_dept = Entry(main_widget,)
input_dept.grid(column=2,row=4)

btn_add = Button(main_widget, text="add detail")
btn_add.grid(column=2,row=5)

label_table = Label(main_widget, text="table")
label_table.grid(column=2, row=6)
label_table.configure(font=HEADING_FONT)

listbox_table = Listbox(main_widget)
listbox_table.grid(column=2, row=7)
listbox_table.configure(width=50,height=10)

btn_del = Button(main_widget, text="remove item")
btn_del.grid(column=2,row=10)

main_widget.mainloop()