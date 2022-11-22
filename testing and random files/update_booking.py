from tkinter import *
def update_Booking():
    
    booking_window=Tk()
    booking_window.title('UPDATE BOOKING')
    booking_window.geometry('720x600+0+0')
    Frame(booking_window,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=600)
    Label(booking_window,text='UPDATE BOOKING',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #===========================BOOKING ID================================
    Label(booking_window,text='Booking ID ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=170)
    book_id=StringVar()
    book_id_entry=Entry(booking_window,textvariable=book_id,width=25,bg='white').place(x=400,y=181)
    

    #========================DOB=======================================
    Label(booking_window,text='Date of Booking',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=330)
    date_list=(' ','NO CHANGE','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
    month_list=(' ','NO CHANGE','1','2','3','4','5','6','7','8','9','10','11','12')
    year_list=(' ','NO CHANGE','2022','2023')
    date=StringVar()
    month=StringVar()
    year=StringVar()
    OptionMenu(booking_window,date,*date_list).place(x=400,y=330)
    OptionMenu(booking_window,month,*month_list).place(x=480,y=330)
    OptionMenu(booking_window,year,*year_list).place(x=560,y=330)
    
    def do_it():
        an=str(book_id.get()).upper()
        db=str(date.get())+' '+str(month.get())+' '+str(year.get())

        if 'NO CHANGE' not in db :
            pass
            # cur.execute("update booking set invoice_date =('{}') where book_id=('{}') ".format(db,an))
            # con.commit()
        # print(' '*242+'Updation Successful...')           
    
    Button(booking_window,text='UPDATE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    booking_window.mainloop()
