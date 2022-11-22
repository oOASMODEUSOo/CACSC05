from tkinter import *
from tkinter import ttk

def property_list():
    pl = Tk()
    pl.geometry("720x720")
    pl.title("Property Listing")
    tree_frame = Frame(pl)
    tree_frame.pack(pady=10)
    tree_scrollbar=Scrollbar(tree_frame, )
    tree_scrollbar.pack(side="right", fill=Y)
    my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scrollbar.set)  #, selectmode="none"
    my_tree.pack()

    #config of scrolbar
    tree_scrollbar.config(command=my_tree.yview)

    my_tree['columns'] = ("Pid", "Property name", "BHK", "Address", "Rent")

    my_tree.column("#0", width=0,stretch=NO)
    my_tree.column("Pid", anchor="w", width=60)
    my_tree.column("Property name", anchor="center", width=100)
    my_tree.column("BHK", anchor="w",width=60)
    my_tree.column("Address", anchor="w",width=150)
    my_tree.column("Rent", anchor="w",width=100)

    my_tree.heading("#0", text="", anchor="w")
    my_tree.heading("Pid", text="Pid", anchor="w")
    my_tree.heading("Property name",text="Name", anchor="center")
    my_tree.heading("BHK", text="BHK", anchor="w")
    my_tree.heading("Address", text="Address", anchor="w")
    my_tree.heading("Rent", text="Rent", anchor="w")

    fetchdata = f"select pid, prop_name, BHK, prop_add, prop_rent from prop"
    # mycur.execute(fetchdata)
    # result_table_data = mycur.fetchall()

    count = 0
    for rec in result_table_data:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(rec[0], rec[1], rec[2], rec[3], rec[4]))
        count += 1

    pl.mainloop()

property_list()