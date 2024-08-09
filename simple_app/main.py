from tkinter import *
from tkinter import messagebox
from db_query import DB_Query

# # ---------------------------------
# #      BASIC THINGS TO UPDATE
# # ---------------------------------

COLUMNS = ("PHONE_NO","FIRST_NAME","LAST_NAME","SURNAME","EMAIL","JOB","RELATIONSHIP","ADDRESS","BIRTHDAY","NICK_NAME")
DB_NAME = "todo_list.db"
TABLE_NAME = "task"

## INITIAL CODE to create table
DB_Query.createTable(DB_NAME, TABLE_NAME)


MY_TABLE = []

HEADING_FONT = ( "Consolas", 13, "underline" )
NORMAL_FONT = ( "Consolas", 10 )

main_widget = Tk()
main_widget.geometry("500x500")


# NEW CODE 🚀🤪
# ----------------------------------------------
tk_PHONE_NO = StringVar(main_widget)
tk_FIRST_NAME = StringVar(main_widget)
tk_LAST_NAME = StringVar(main_widget)
tk_SURNAME = StringVar(main_widget)
tk_EMAIL = StringVar(main_widget)
tk_JOB = StringVar(main_widget)
tk_RELATIONSHIP = StringVar(main_widget)
tk_ADDRESS = StringVar(main_widget)
tk_BIRTHDAY = StringVar(main_widget)
tk_NICK_NAME = StringVar(main_widget)
# ----------------------------------------------



# your code
# 4 things
#    1. Label
#    2. Entry   : input
#    3. Button
#    4. Listbox : table


label_PHONE_NO = Label(main_widget,text="PHONE_NO")
label_PHONE_NO.grid(column=1, row=1)
input_PHONE_NO = Entry(main_widget,textvariable=tk_PHONE_NO)
input_PHONE_NO.grid(column=2, row=1)

label_FIRST_NAME = Label(main_widget,text="FIRST_NAME")
label_FIRST_NAME.grid(column=1, row=2)
input_FIRST_NAME = Entry(main_widget,textvariable=tk_FIRST_NAME)
input_FIRST_NAME.grid(column=2, row=2)

label_LAST_NAME = Label(main_widget,text="LAST_NAME")
label_LAST_NAME.grid(column=1, row=3)
input_LAST_NAME = Entry(main_widget,textvariable=tk_LAST_NAME)
input_LAST_NAME.grid(column=2, row=3)

label_SURNAME = Label(main_widget,text="SURNAME")
label_SURNAME.grid(column=1, row=4)
input_SURNAME = Entry(main_widget,textvariable=tk_SURNAME)
input_SURNAME.grid(column=2, row=4)

label_EMAIL = Label(main_widget,text="EMAIL")
label_EMAIL.grid(column=1, row=5)
input_EMAIL = Entry(main_widget,textvariable=tk_EMAIL)
input_EMAIL.grid(column=2, row=5)

label_JOB = Label(main_widget,text="JOB")
label_JOB.grid(column=1, row=6)
input_JOB = Entry(main_widget,textvariable=tk_JOB)
input_JOB.grid(column=2, row=6)

label_RELATIONSHIP = Label(main_widget,text="RELATIONSHIP")
label_RELATIONSHIP.grid(column=1, row=7)
input_RELATIONSHIP = Entry(main_widget,textvariable=tk_RELATIONSHIP)
input_RELATIONSHIP.grid(column=2, row=7)

label_ADDRESS = Label(main_widget,text="ADDRESS")
label_ADDRESS.grid(column=1, row=8)
input_ADDRESS = Entry(main_widget,textvariable=tk_ADDRESS)
input_ADDRESS.grid(column=2, row=8)

label_BIRTHDAY = Label(main_widget,text="BIRTHDAY")
label_BIRTHDAY.grid(column=1, row=9)
input_BIRTHDAY = Entry(main_widget,textvariable=tk_BIRTHDAY)
input_BIRTHDAY.grid(column=2, row=9)

label_NICK_NAME = Label(main_widget,text="NICK_NAME")
label_NICK_NAME.grid(column=1, row=10)
input_NICK_NAME = Entry(main_widget,textvariable=tk_NICK_NAME)
input_NICK_NAME.grid(column=2, row=10)

# INPUT 🥺 Below code are input. 
# Please use it with variables

# ----------------------------------------------------

list_box = Listbox(main_widget,width=100)
list_box.grid(column=2,row=14)

# --------------------------------------------------
#  WHAT TO HAPPEN AFTER BTN is clicked.
# --------------------------------------------------

def handle_add_btn():
    PHONE_NO = tk_PHONE_NO.get()
    FIRST_NAME = tk_FIRST_NAME.get()
    LAST_NAME = tk_LAST_NAME.get()
    SURNAME = tk_SURNAME.get()
    EMAIL = tk_EMAIL.get()
    JOB = tk_JOB.get()
    RELATIONSHIP = tk_RELATIONSHIP.get()
    ADDRESS = tk_ADDRESS.get()
    BIRTHDAY = tk_BIRTHDAY.get()
    NICK_NAME = tk_NICK_NAME.get()
    row = (
        PHONE_NO.strip(),
        FIRST_NAME.strip(),
        LAST_NAME.strip(),
        SURNAME.strip(),
        EMAIL.strip(),
        JOB.strip(),
        RELATIONSHIP.strip(),
        ADDRESS.strip(),
        BIRTHDAY.strip(),
        NICK_NAME.strip()
    )
    if "" in row:
        messagebox.showwarning("invalid","input box should not be empty")
    else:
        DB_Query.insertTable(DB_NAME,TABLE_NAME,COLUMNS,row)
        # make input box empty after query is executed.
        input_PHONE_NO.delete(0,END)
        input_FIRST_NAME.delete(0,END)
        input_LAST_NAME.delete(0,END)
        input_SURNAME.delete(0,END)
        input_EMAIL.delete(0,END)
        input_JOB.delete(0,END)
        input_RELATIONSHIP.delete(0,END)   
        input_ADDRESS.delete(0,END)
        input_BIRTHDAY.delete(0,END)
        input_NICK_NAME.delete(0,END)
        # update the list in list_box_table
        update_list()

def handle_remove_btn():
    try:
        select_id = list_box.get(list_box.curselection())[0]
        DB_Query.deleteTable(DB_NAME,TABLE_NAME,select_id)
        update_list()
    except:
        messagebox.showwarning("warning","You must select a task to remove.")

def update_list():
    list_box.delete(0, END)
    table = DB_Query.selectTable(DB_NAME,TABLE_NAME)
    for row in table:
        list_box.insert(END, row)

# --------------------------------------------------


Btn_add = Button(main_widget, text="Add contact")
Btn_add.grid(column=2,row=12)
Btn_add.configure(bg="#16A0D5", command=handle_add_btn)


Btn_delete = Button(main_widget, text="Delete contact")
Btn_delete.grid(column=2,row=15)
Btn_delete.configure(bg="#16A0D5", command=handle_remove_btn)

update_list()


main_widget.mainloop()