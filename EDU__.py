from tkinter import *
import pyfiglet
import mysql.connector
#mydb
con=mysql.connector.connect(host='localhost',password='BRAIN',user='root')
#mycur
cur=con.cursor()

#==============================CREATING DB=====================================
cur.execute('create database if not exists landBnb ')
con.commit() 
cur.execute('use landBnb')
con.commit() 

cur.execute('create table if not exists prop(prop_id varchar(20) PRIMARY KEY, prop_name char(20) NOT NULL, prop_type char(12) NOT NULL, bhk int(2) NOT NULL, prop_add varchar(50) NOT NULL, prop_rent int(6) NOT NULL, status boolean NOT NULL)')
con.commit()

cur.execute('create table if not exists customer(customer_id varchar(10) PRIMARY KEY, name char(20) NOT NULL, phone_num int(10) NOT NULL, email varchar(50) NOT NULL, address varchar(100) NOT NULL, idProof_num int(12) NOT NULL)')
con.commit()

cur.execute('create table if not exists booking(book_date date NOT NULL, book_id varchar(20) PRIMARY KEY, customer_id varchar(10) NOT NULL, prop_id varchar(20) NOT NULL, FOREIGN KEY (customer_id) REFERENCES customer(customer_id) on delete cascade on update cascade, FOREIGN KEY (prop_id) REFERENCES prop(prop_id) on delete cascade on update cascade, invoice_date date NOT NULL, amount int(6) NOT NULL )')
con.commit()
count=0
#==============================CREATING DB=====================================

def add_record():
    root=Tk()
    root.title('ADD LISTING')
    root.geometry('720x720+0+0')
    Frame(root,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=720 )
    Label(root,text='ADD NEW LISTING',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #==========================NAME====================================
    Label(root,text='Property Name ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    prop_name=StringVar()
    prop_name_entry=Entry(root,textvariable=prop_name,width=25,bg='white').place(x=400,y=160)
   
    #===========================Prop type.================================
    Label(root,text='Type',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=250)
    prop_list=('Appartment','Villa','Penthouse','Farmhouse')
    prop_type=StringVar()
    prop_type_entry=OptionMenu(root,prop_type,*prop_list).place(x=400,y=251)      
    # Entry(root,textvariable=prop_type,width=25,bg='white').place(x=400,y=161)
    

    #==========================BHK====================================
    Label(root,text='No. of Bedrooms ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=350)
    bhk_list=('1','2','3','4','5','6','7','8','9','10')
    bhk=IntVar()
    bhk_entry=OptionMenu(root,bhk,*bhk_list).place(x=400,y=355)

    #==========================ADDRESS====================================
    Label(root,text='Address ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=450)
    prop_address=StringVar()
    prop_address_entry=Entry(root,textvariable=prop_address,width=25,bg='white').place(x=400,y=460)

    #==========================RENT====================================
    Label(root,text='Rent ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=550)
    prop_rent=IntVar()
    prop_rent_entry=Entry(root,textvariable=prop_rent,width=25,bg='white').place(x=400,y=560)

   
    
    def do_it():
        nm=str(prop_name.get()).upper()
        pt=str(prop_type.get()).upper()
        bh=int(bhk.get())
        add=str(prop_address.get()).upper()
        rt=int(prop_rent.get())
        st=1
        pid=nm+str(bh)
        cur.execute("insert into prop values('{}','{}','{}','{}','{}','{}','{}')".format(pid,nm,pt,bh,add,rt,st))
        con.commit()
        # prop_name_entry.delete(0, 'end')
        # prop_type_entry.delete(0, 'end')
        # bhk_entry.delete(0, 'end')
        # prop_address_entry.delete(0, 'end')
        # prop_rent_entry.delete(0, 'end')
        # print(' '*242+'Record Added Successfully...')
          
   
    Button(root,text='ADD',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    root.mainloop()

def show_data():
    cur.execute('select * from prop')
    data=cur.fetchall()
    for i in data:
        print(i)

def update_data():
    
    root=Tk()
    root.title('UPDATE LISTING')
    root.geometry('720x720+0+0')
    Frame(root,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=720)
    Label(root,text='UPDATE LISTING ',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #==========================PID====================================
    Label(root,text='Property ID ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    prop_ID=StringVar()
    prop_ID_entry=Entry(root,textvariable=prop_ID,width=25,bg='white').place(x=400,y=160)

    #==========================NAME====================================
    Label(root,text='Property Name ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=230)
    prop_name=StringVar()
    prop_name_entry=Entry(root,textvariable=prop_name,width=25,bg='white').place(x=400,y=240)
   
    #===========================Prop type.================================
    Label(root,text='Type',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=310)
    prop_list=('NO CHANGE','Appartment','Villa','Penthouse','Farmhouse')
    prop_type=StringVar()
    prop_type_entry=OptionMenu(root,prop_type,*prop_list).place(x=400,y=315)      
    # Entry(root,textvariable=prop_type,width=25,bg='white').place(x=400,y=161)
    

    #==========================BHK====================================
    Label(root,text='No. of Bedrooms ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=390)
    bhk_list=('0','1','2','3','4','5','6','7','8','9','10')
    bhk=IntVar()
    bhk_entry=OptionMenu(root,bhk,*bhk_list).place(x=400,y=395)

    #==========================ADDRESS====================================
    Label(root,text='Address ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=470)
    prop_address=StringVar()
    prop_address_entry=Entry(root,textvariable=prop_address,width=25,bg='white').place(x=400,y=480)

    #==========================RENT====================================
    Label(root,text='Rent ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=550)
    prop_rent=IntVar()
    prop_rent_entry=Entry(root,textvariable=prop_rent,width=25,bg='white').place(x=400,y=560)
    
    def do_it():                #WORK HERE
        id=str(prop_ID.get()).upper()
        nm=str(prop_name.get()).upper()
        pt=str(prop_type.get()).upper()
        bh=int(bhk.get())
        add=str(prop_address.get()).upper()
        rt=int(prop_rent.get())
        if nm != '0':
            cur.execute("update prop set prop_name=('{}') where prop_id=('{}') ".format(nm,id))
            con.commit()
        if pt != 'NO CHANGE':
            cur.execute("update prop set prop_type=('{}') where prop_id=('{}') ".format(pt,id))
            con.commit()
        if bh != '0':
            cur.execute("update prop set bhk=('{}') where prop_id=('{}') ".format(bh,id))
            con.commit()
        if add != '0':
            cur.execute("update prop set prop_add=('{}') where prop_id=('{}') ".format(add,id))
            con.commit()
        if rt != 0:
            cur.execute("update prop set prop_rent=('{}') where prop_id=('{}') ".format(rt,id))
            con.commit()
        
        print(' '*242+'Updation Successful...')           
    
    Button(root,text='UPDATE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    root.mainloop()

def delete_data():
    root=Tk()
    root.title('DELETE DATA')
    root.geometry('500x500+0+0')
    Frame(root,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=600)
    Label(root,text='DELETE RECORD',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #===========================ADM NO.================================
    Label(root,text='ADMISSION NUMBER ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    adm_no=StringVar()
    Entry(root,textvariable=adm_no,width=25,bg='white').place(x=325,y=161)

    def do_it():
        an=str(adm_no.get()).upper()
        cur.execute("delete from pystudent where ADMISSION_NUMBER=('{}') ".format(an))
        con.commit()
        print(' '*242+'Deletion Successful...')           
    
    Button(root,text='DELETE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    root.mainloop()


while True:
    print(pyfiglet.figlet_format('WELCOME TO EDUSERV',font='speed'))
    print('*'*501)
    print('MAIN MENU'.center(501))
    print('1. Enter New Data'.center(501))
    print('2. Display Existing Data'.center(501))
    print('3. Update Existing Record'.center(501))
    print('4. Delete Existing Record'.center(501))
    print('5. EXIT'.center(501))
    
    print('*'*501)
    ch=int(input(' '*242+'Enter your Choice: '))
    if ch==1:
        add_record()
    if ch==2:
        show_data()
    if ch==3:
        update_data()
    if ch==4:
        delete_data()
    if ch==5:
        break