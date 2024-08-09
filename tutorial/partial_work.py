from tkinter import *
from tkinter import messagebox

MY_TABLE = []

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

# INPUT 🥺 Below code are input. 
# Please use it with variables

# NEW CODE 🚀🤪
# ----------------------------------------------
tk_name = StringVar(main_widget)
tk_age = StringVar(main_widget)
tk_dept = StringVar(main_widget)
# ----------------------------------------------

input_name = Entry(main_widget,textvariable=tk_name)
input_name.grid(column=2,row=2)

input_age = Entry(main_widget,textvariable=tk_age)
input_age.grid(column=2,row=3)

input_dept = Entry(main_widget,textvariable=tk_dept)
input_dept.grid(column=2,row=4)

# ----------------------------------------------------


label_table = Label(main_widget, text="table")
label_table.grid(column=2, row=6)
label_table.configure(font=HEADING_FONT)

listbox_table = Listbox(main_widget)
listbox_table.grid(column=2, row=7)
listbox_table.configure(width=50,height=10)

# --------------------------------------------------
#  WHAT TO HAPPEN AFTER BTN is clicked.
# --------------------------------------------------

def handle_add_btn():
    name = tk_name.get()
    dept = tk_dept.get()
    age = tk_age.get()

    if "" in [ name.strip(), age.strip(), dept.strip() ]:
        messagebox.showwarning("invalid","input box should not be empty")
    else:
        print("executed query")
        # add in table
        row = (name, age, dept)
        MY_TABLE.append(row)
        # make input box empty after query is executed.
        input_name.delete(0,END);
        input_age.delete(0,END);
        input_dept.delete(0,END);
        # update the list in list_box_table
        update_list()

def handle_remove_btn():
    select_id = listbox_table.get(listbox_table.curselection())[0]

def update_list():
    for row in MY_TABLE:
        listbox_table.insert(END,row)

# --------------------------------------------------

btn_add = Button(main_widget, text="add detail", command=handle_add_btn)
btn_add.grid(column=2,row=5)

btn_del = Button(main_widget, text="remove item",command=handle_remove_btn)
btn_del.grid(column=2,row=10)

main_widget.mainloop()