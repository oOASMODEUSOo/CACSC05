
def add_listing():
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
    prop_list=('Appartment','Villa','Penthouse','Farmhouse')
    prop_type=StringVar()
    prop_type_entry=OptionMenu(root,prop_type,*prop_list).place(x=400,y=315)      
    # Entry(root,textvariable=prop_type,width=25,bg='white').place(x=400,y=161)
    

    #==========================BHK====================================
    Label(root,text='No. of Bedrooms ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=390)
    bhk_list=('1','2','3','4','5','6','7','8','9','10')
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

        cur.execute("insert into prop values('{}','{}','{}','{}','{}','{}','{}','{}')".format(prop_id,em,nm,pt,bh,add,rt,st))
        con.commit()
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
