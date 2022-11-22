from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("500x550")
root.title("TreeView Testing")

tree_frame = Frame(root)
tree_frame.pack(pady=20)

#tree view scrollbar
tree_scrollbar=Scrollbar(tree_frame, )
tree_scrollbar.pack(side="right", fill=Y)

my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scrollbar.set)  #, selectmode="none"
my_tree.pack()

#config of scrolbar
tree_scrollbar.config(command=my_tree.yview)

#defining our columns
my_tree['columns'] = ("Name", "Id", "Pizza")

#formatting our columns
my_tree.column("#0", width=0,stretch=NO)
my_tree.column("Name", anchor="w", width=120)
my_tree.column("Id", anchor="center", width=80)
my_tree.column("Pizza", anchor="w",width=120)

#creating headings
my_tree.heading("#0", text="", anchor="w")
my_tree.heading("Name", text="DName", anchor="w")
my_tree.heading("Id",text="ID", anchor="center")
my_tree.heading("Pizza", text="Pizza", anchor="w")

#--------------------------------------------------------------------------

#add data
data=[["John", 1 ,"Pepperoni"],
      ["Mary", 2 ,"Cheese"],
      ["Tim", 3 ,"Mushroom"],
      ["Bob", 4 ,"Onion"],
      ["John", 5 ,"Pepperoni"],
      ["Mary", 6 ,"Cheese"],
      ["Tim", 7 ,"Mushroom"],
      ["Bob", 8 ,"Onion"],
      ["John", 9 ,"Pepperoni"],
      ["Mary", 10 ,"Cheese"],
      ["Tim", 11 ,"Mushroom"],
      ["Bob", 12 ,"Onion"],
      ["John", 13 ,"Pepperoni"],
      ["Mary", 14 ,"Cheese"],
      ["Tim", 15 ,"Mushroom"],
      ["Bob", 16 ,"Onion"],
      ["John", 17 ,"Pepperoni"],
      ["Mary", 18 ,"Cheese"],
      ["Tim", 19 ,"Mushroom"],
      ["Bob", 20 ,"Onion"]

      ]

global count

count=0
for rec in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(rec[0], rec[1], rec[2]))
    count+=1

'''
my_tree.insert(parent='', index='end', iid=0, text="", values=("Ojas", 1, "Barbeque chicken"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Tanishka", 2, "Peppy Paneer"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Lakshay", 3, "IDK"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Jaskirat", 4, "FarmHouse"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Shivam", 5, "Anything"))
'''


add_frame=Frame(root)
add_frame.pack(pady=20)
n1=Label(add_frame, text="Name")
n1.grid(row=0, column=0)
il=Label(add_frame, text="ID")
il.grid(row=0,column=1)
tl=Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

name_box=Entry(add_frame)
name_box.grid(row=1, column=0)
id_box=Entry(add_frame)
id_box.grid(row=1, column=1)
topping_box=Entry(add_frame)
topping_box.grid(row=1, column=2)

def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()))
    count+=1
    name_box.delete(0,'end')
    id_box.delete(0, 'end')
    topping_box.delete(0, 'end')

def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

def remove_one():
    x = my_tree.selection()[0]
    print(my_tree.selection())
    print(x)
    my_tree.delete(x)

add_record=Button(root, text="Add Record", command=add_record)
add_record.pack(pady=20)

#remove all button
remove_all=Button(root, text="Remove All Entries", command=remove_all)
remove_all.pack(pady=10)

#remove selected records
remove_one=Button(root, text="Remove One Selected", command=remove_one)
remove_one.pack(pady=20)

root.mainloop()