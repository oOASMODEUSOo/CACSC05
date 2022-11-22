from tkinter import *
import mysql.connector as sqlc
from tkinter import ttk
from datetime import datetime
import tkinter.messagebox as tkmessage
import smtplib
import random
import PIL 
import qrcode

# mydb = sqlc.connect(
#     host="localhost",
#     user="root",
#     password="tiger",
#     database="dabbabnb"
# )

def list_New_Property():
    root=Tk()
    root.title('ADD LISTING')
    root.geometry('720x720+0+0')
    Frame(root,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=720 )
    Label(root,text='ADD NEW LISTING',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #==========================P_EMAIL====================================
    Label(root,text='Your E-Mail ID ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    prop_mail=StringVar()
    prop_mail_entry=Entry(root,textvariable=prop_mail,width=25,bg='white').place(x=400,y=160)

    #==========================NAME====================================
    Label(root,text='Property Name ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=230)
    prop_name=StringVar()
    prop_name_entry=Entry(root,textvariable=prop_name,width=25,bg='white').place(x=400,y=240)
   
    #===========================Prop type.================================
    Label(root,text='Type',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=310)
    prop_list=(' ','Appartment','Villa','Penthouse','Farmhouse')
    prop_type=StringVar()
    prop_type_entry=ttk.OptionMenu(root,prop_type,*prop_list).place(x=400,y=315)      
    # Entry(root,textvariable=prop_type,width=25,bg='white').place(x=400,y=161)
    
    #==========================BHK====================================
    Label(root,text='No. of Bedrooms ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=390)
    bhk_list=(' ','1','2','3','4','5','6','7','8','9','10')
    bhk=IntVar()
    bhk_entry=ttk.OptionMenu(root,bhk,*bhk_list).place(x=400,y=395)

    #==========================ADDRESS====================================
    Label(root,text='Address ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=470)
    prop_address=StringVar()
    prop_address_entry=Entry(root,textvariable=prop_address,width=25,bg='white').place(x=400,y=480)

    #==========================RENT====================================
    Label(root,text='Rent ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=550)
    prop_rent=IntVar()
    prop_rent_entry=Entry(root,textvariable=prop_rent,width=25,bg='white').place(x=400,y=560)
    
    def do_it():
        em=str(prop_mail.get()).upper()
        nm=str(prop_name.get()).upper()
        pt=str(prop_type.get()).upper()
        bh=int(bhk.get())
        add=str(prop_address.get()).upper()
        rt=int(prop_rent.get())
        st=1
        
        number=random.randint(100,999999)
        prop_id='P'+str(number)
        sender_email="landbnbn@outlook.com"
        password="landbnb@1234"
        TEXT='\n Please note your Property ID: '+prop_id
        SUBJECT='Property Listed Successfully.'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        # message=
        # print(message)

        server=smtplib.SMTP('smtp.office365.com',587)
        server.starttls()
        server.login(sender_email,password)
        # print('login success')
        server.sendmail(sender_email,em,message)
        # print('email sent')

        # cur.execute("insert into prop values('{}','{}','{}','{}','{}','{}','{}','{}')".format(prop_id,em,nm,pt,bh,add,rt,st))
        # con.commit()
        server=smtplib.SMTP('smtp.office365.com',587)
        server.starttls()
        server.login(sender_email,password)
        # print('login success')
        server.sendmail(sender_email,em,message)
        # print('email sent')

        tkmessage.showinfo("Success!","Property Listed Successfully!")
        # prop_name_entry.delete(0, 'end')
        # prop_type_entry.delete(0, 'end')
        # bhk_entry.delete(0, 'end')
        # prop_address_entry.delete(0, 'end')
        # prop_rent_entry.delete(0, 'end')
        # print(' '*242+'Record Added Successfully...')
          
   
    Button(root,text='ADD',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    root.mainloop()

def Booking():      #booking function list the property in the CLI and that opens a window for customer details

    book = Tk()
    book.title('ADD LISTING')
    book.geometry('720x720+0+0')
    book.iconbitmap('prop.ico')

    def customer_button():      #customer details:- name, phone num, email, address, Id proof
        customer_details = Tk()
        customer_details.title('Property Details')
        customer_details.geometry('720x720+0+0')
        customer_details.iconbitmap('prop.ico')

        frame_for_heading = Frame(customer_details, bg="yellow", borderwidth=3, relief="raised")
        frame_for_heading.pack(fill=BOTH, anchor="c")
        Label(frame_for_heading, text="Booking Details", fg="blue", relief="ridge", font="goldman 19 bold").pack()

        #for checkin date
        Label(customer_details,text='DATE OF BIRTH ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=50)
        date_list=(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
        month_list=(' ','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER')
        year_list=(' ','2022', '2023')
        date=StringVar()
        month=StringVar()
        year=StringVar()
        ttk.OptionMenu(customer_details, date, *date_list).place(x=400,y=50)
        ttk.OptionMenu(customer_details, month, *month_list).place(x=450,y=50)
        ttk.OptionMenu(customer_details, year, *year_list).place(x=540,y=50)

        #for cust name 
        Label(customer_details,text='Name ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=130)
        cust_name=StringVar()
        cust_name_entry=Entry(customer_details,textvariable=cust_name,width=25,bg='white').place(x=400,y=140)

        #for cust phone number
        Label(customer_details,text='Phone No. ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=230)
        cust_phone = IntVar()
        cust_phone_entry = Entry(customer_details, textvariable=cust_phone, width=25, bg = 'white').place(x=400, y= 240)

        #for email
        Label(customer_details,text='Email ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=330)
        cust_email = StringVar()
        cust_email_entry = Entry(customer_details, textvariable=cust_email, width=25, bg = 'white').place(x=400, y= 340)
        
        #for address
        Label(customer_details,text='Address ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=430)
        cust_Add = StringVar()
        cust_Add_Entry = Entry(customer_details, textvariable=cust_Add, width=25, bg = 'white').place(x=400, y= 440)

        #for idproof number
        Label(customer_details,text='ID proof number ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=530)
        cust_id = IntVar()
        cust_id_entry = Entry(customer_details, textvariable=cust_id, width=25, bg = 'white').place(x=400, y= 540)

        def do_it():
            dd = date.get()
            mm = month.get()
            yy = year.get()
            namecust = cust_name.get()
            phonenum = cust_phone.get()
            email = cust_email.get()
            address = cust_Add.get()
            idNumber = cust_id.get()

            #cur.execute("insert into customer value()")
            #con.commit()


        Button(customer_details,text='Confirm Book',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'), command=customer_details).pack(side=BOTTOM, fill=X)
        
        customer_details.mainloop()

    Button(book, text="List new property", command=customer_button).pack()
    book.mainloop()

def update_Listing():   
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
    prop_list=(' ', 'NO CHANGE','Appartment','Villa','Penthouse','Farmhouse')
    prop_type=StringVar()
    prop_type_entry=ttk.OptionMenu(root,prop_type,*prop_list).place(x=400,y=315)      
    # Entry(root,textvariable=prop_type,width=25,bg='white').place(x=400,y=161)

    #==========================BHK====================================
    Label(root,text='No. of Bedrooms ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=390)
    bhk_list=(' ','0','1','2','3','4','5','6','7','8','9','10')
    bhk=IntVar()
    bhk_entry=ttk.OptionMenu(root,bhk,*bhk_list).place(x=400,y=395)

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
            # cur.execute("update prop set prop_name=('{}') where prop_id=('{}') ".format(nm,id))
            # con.commit()
            pass
        if pt != 'NO CHANGE':
            # cur.execute("update prop set prop_type=('{}') where prop_id=('{}') ".format(pt,id))
            # con.commit()
            pass
        if bh != '0':
            # cur.execute("update prop set bhk=('{}') where prop_id=('{}') ".format(bh,id))
            # con.commit()
            pass
        if add != '0':
            # cur.execute("update prop set prop_add=('{}') where prop_id=('{}') ".format(add,id))
            # con.commit()
            pass
        if rt != 0:
            # cur.execute("update prop set prop_rent=('{}') where prop_id=('{}') ".format(rt,id))
            # con.commit()
            pass
        
        print(' '*242+'Updation Successful...')           
    
    Button(root,text='UPDATE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    root.mainloop()

def update_Booking():
    pass

def delete_listing():            
    delete_listing_window=Tk()
    delete_listing_window.title('DELETE LISTING')
    delete_listing_window.geometry('500x500+0+0')
    Frame(delete_listing_window,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=600)
    Label(delete_listing_window,text='DELETE LISTING',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #===========================PROP ID================================
    Label(delete_listing_window,text='Property ID ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    prop_id=StringVar()
    prop_id_entry=Entry(delete_listing_window,textvariable=prop_id,width=25,bg='white').place(x=325,y=161)

    def do_it():
        pid=str(prop_id.get()).upper()
        # cur.execute("delete from prop where prop_id=('{}') ".format(pid))
        # con.commit()
        # print(' '*242+'Deletion Successful...')           
    
    Button(delete_listing_window,text='DELETE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    delete_listing_window.mainloop()

def delete_booking():           
    delete_booking_window=Tk()
    delete_booking_window.title('DELETE BOOKING')
    delete_booking_window.geometry('500x500+0+0')
    Frame(delete_booking_window,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=600)
    Label(delete_booking_window,text='DELETE BOOKING',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #===========================BOOKING ID.================================
    Label(delete_booking_window,text='Booking ID ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    book_id=StringVar()
    book_id_entry=Entry(delete_booking_window,textvariable=book_id,width=25,bg='white').place(x=325,y=161)

    def do_it():
        bid=str(book_id.get()).upper()
        # cur.execute("delete from booking where book_id=('{}') ".format(bid))
        # con.commit()
        # print(' '*242+'Deletion Successful...')           
    
    Button(delete_booking_window,text='DELETE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    delete_booking_window.mainloop()

def aggregate():
    agg = Tk()
    agg.geometry("720x400+0+0")
    agg.title("Perform aggregate functions")
    agg.iconbitmap("prop.ico")

    def count_something_1():
        pass

    def count_something_2():
        pass

    def count_something_3():
        pass
    
    Label(agg, text="Perform aggregate function", bg='cyan',fg='black',font=('arial',20,'bold')).pack(side=TOP, fill=X)
    butt1 = Button(agg, text='Button 1', bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'), command=count_something_1)
    butt1.pack(side=TOP, fill=X)

    butt2 = Button(agg, text='Button 2', bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'), command=count_something_2)
    butt2.pack(side=TOP, fill=X)

    butt3 = Button(agg, text='Button 3', bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'), command=count_something_3)
    butt3.pack(side=TOP, fill=X)

    agg.mainloop()

def KILLSWITCH():
    master.destroy()

master = Tk()
master.iconbitmap("prop.ico")

master.geometry("500x500")
master.minsize(300, 300)
master.title("DabbaBnB")

frame = Frame(master, bg="yellow", borderwidth=3, relief="raised")
frame.pack(fill=BOTH, anchor="c")
Label(frame, text="Welcome to DabbaBnB", fg="blue", relief="ridge", font="goldman 19 bold").pack()

#button for listing a new property in the database
frame_for_list = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_list.pack(anchor="center", pady=10)
b1_list = Button(frame_for_list, text="List new property", command=list_New_Property)  
b1_list.pack(anchor="center")

#button for booking a new property
frame_for_book = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_book.pack(anchor="center", pady=10)
b2_book = Button(frame_for_book, text="Do a booking", command=Booking) #, command=remove
b2_book.pack(anchor="center")

#button for updating details about already listed property
frame_for_updateL = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_updateL.pack(anchor="center", pady=10)
b4_updateL = Button(frame_for_updateL, text="Update listing", command=update_Listing) #, command=show_bill
b4_updateL.pack()

#button for updating booking already booked
frame_for_updateR = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_updateR.pack(anchor="center", pady=10)
b3_updateR = Button(frame_for_updateR, text="Update Booking", command=update_Booking) #, command=LogOff
b3_updateR.pack()

#button for delete listing
frame_for_deleteListing = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_deleteListing.pack(anchor="center", pady=10)
b4_deleteListing = Button(frame_for_deleteListing, text="Delete Listing", command=delete_listing) #, command=LogOff
b4_deleteListing.pack()

#button for canceling a booking
frame_for_deleteBooking = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_deleteBooking.pack(anchor="center", pady=10)
b4_deleteBooking = Button(frame_for_deleteBooking, text="Cancel Booking", command=delete_booking) #, command=LogOff
b4_deleteBooking.pack()

frame_for_aggregate = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_aggregate.pack(anchor="center", pady=10)
b4_aggregate = Button(frame_for_aggregate, text="Aggregate", command=aggregate) #, command=LogOff
b4_aggregate.pack()

frame_for_quit = Frame(master, borderwidth="6", bg="grey", relief="raised")
frame_for_quit.pack(anchor="center", pady=10)
b4_quit = Button(frame_for_quit, text="KILLSWITCH", command=KILLSWITCH) #, command=LogOff
b4_quit.pack()

master.mainloop()