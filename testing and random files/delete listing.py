
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
        cur.execute("delete from prop where prop_id=('{}') ".format(pid))
        con.commit()
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
        cur.execute("delete from booking where book_id=('{}') ".format(bid))
        con.commit()
        # print(' '*242+'Deletion Successful...')           
    
    Button(delete_booking_window,text='DELETE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    delete_booking_window.mainloop()
