from tkinter import *
import random
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Billing Software")
        title=Label(self.root,text="Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)

        # Variables
        self.nutella=IntVar()
        self.noodles=IntVar()
        self.lays=IntVar()
        self.oreo=IntVar()
        self.muffin=IntVar()
        self.silk=IntVar()
        self.namkeen=IntVar()
        self.atta=IntVar()
        self.pasta=IntVar()
        self.rice=IntVar()
        self.oil=IntVar()
        self.sugar=IntVar()
        self.dal=IntVar()
        self.tea=IntVar()
        self.soap=IntVar()
        self.shampoo=IntVar()
        self.lotion=IntVar()
        self.cream=IntVar()
        self.foam=IntVar()
        self.mask=IntVar()
        self.sanitizer=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()

        # Customer Details Label Frame
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)

        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)
        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)
        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)
        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)

        # Snacks Label Frame
        snacks=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Nutella Choco Spread",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.nutella).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Noodles(1 Pack)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.noodles).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Lays(10Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.lays).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Oreo(20Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.oreo).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Chocolate Muffin",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.muffin).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Dairy Milk Silk(60Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.silk).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Namkeen(15Rs)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.namkeen).grid(row=6,column=1,padx=10)

        # Grocery Label Frame
        grocery=LabelFrame(self.root,text="Grocery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        grocery.place(x=340,y=180,height=380,width=325)

        item8=Label(grocery,text="Aashirvaad Atta(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.atta).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="Pasta(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Basmathi Rice(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.rice).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Sunflower Oil(1ltr)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.oil).grid(row=3,column=1,padx=10)

        item12=Label(grocery,text="Refined Sugar(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.sugar).grid(row=4,column=1,padx=10)

        item13=Label(grocery,text="Daal(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.dal).grid(row=5,column=1,padx=10)

        item14=Label(grocery,text="Tea Powder(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.tea).grid(row=6,column=1,padx=10)

        # Beauty and Hygiene Label Frame
        hygine=LabelFrame(self.root,text="Beauty & Hygiene",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        hygine.place(x=670,y=180,height=380,width=325)

        item15=Label(hygine,text="Bathing Soap(1 Unit)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.soap).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Shampoo(1 Unit)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.shampoo).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Body Lotion(1 Unit)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.lotion).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Face Cream(1 Unit)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.cream).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Face Wash Foam(1 Unit)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.foam).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Face Mask(1 Unit)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.mask).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Hand Sanitizer(1 Unit)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.sanitizer).grid(row=6,column=1,padx=10)
       
       # Overall background color
        self.root.configure(bg="#FADBD8")

        # Bill Area
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#00FFFF")
        billarea.place(x=1000,y=180,width=350,height=380)
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",15),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set,bg="#f2f2f2")
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # Button Frame
        btn_frame=Frame(self.root,bd=7,relief=GROOVE,bg="#FADBD8")
        btn_frame.place(x=0,y=560,relwidth=1,height=140)
        total_btn=Button(btn_frame,command=self.total,text="Total",bg="#A569BD",fg="white",pady=15,width=10,font="arial 12 bold").grid(row=0,column=0,padx=15,pady=20)
        genbill_btn=Button(btn_frame,command=self.bill_area,text="Generate Bill",bg="#A569BD",fg="white",pady=15,width=10,font="arial 12 bold").grid(row=0,column=1,padx=15,pady=20)
        clr_btn=Button(btn_frame,command=self.clear,text="Clear",bg="#A569BD",fg="white",pady=15,width=10,font="arial 12 bold").grid(row=0,column=2,padx=15,pady=20)
        exit_btn=Button(btn_frame,command=self.exit,text="Exit",bg="#A569BD",fg="white",pady=15,width=10,font="arial 12 bold").grid(row=0,column=3,padx=15,pady=20)

    def total(self):
        self.sna_price=self.nutella.get()*100 + self.noodles.get()*50 + self.lays.get()*10 + self.oreo.get()*30 + self.muffin.get()*35 + self.silk.get()*60 + self.namkeen.get()*20
        self.total_sna.set("Rs. "+str(self.sna_price))

        self.gro_price=self.atta.get()*200 + self.pasta.get()*150 + self.rice.get()*180 + self.oil.get()*120 + self.sugar.get()*45 + self.dal.get()*80 + self.tea.get()*70
        self.total_gro.set("Rs. "+str(self.gro_price))

        self.hyg_price=self.soap.get()*30 + self.shampoo.get()*180 + self.lotion.get()*150 + self.cream.get()*120 + self.foam.get()*60 + self.mask.get()*50 + self.sanitizer.get()*45
        self.total_hyg.set("Rs. "+str(self.hyg_price))

        self.a.set("Rs. "+str(self.sna_price))
        self.b.set("Rs. "+str(self.gro_price))
        self.c.set("Rs. "+str(self.hyg_price))
        self.Total_bill=float(self.sna_price+self.gro_price+self.hyg_price)

    def welcome_soft(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to Retail Billing Software\n")
        self.txtarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.phone.get()}")
        self.txtarea.insert(END,f"\n===================================")
        self.txtarea.insert(END,f"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n===================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.phone.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        else:
            self.welcome_soft()
            # ========Snacks
            if self.nutella.get()!=0:
                self.txtarea.insert(END,f"\nNutella Choco Spread\t\t{self.nutella.get()}\t\t{self.nutella.get()*100}")
            if self.noodles.get()!=0:
                self.txtarea.insert(END,f"\nNoodles\t\t{self.noodles.get()}\t\t{self.noodles.get()*50}")
            if self.lays.get()!=0:
                self.txtarea.insert(END,f"\nLays\t\t{self.lays.get()}\t\t{self.lays.get()*10}")
            if self.oreo.get()!=0:
                self.txtarea.insert(END,f"\nOreo\t\t{self.oreo.get()}\t\t{self.oreo.get()*30}")
            if self.muffin.get()!=0:
                self.txtarea.insert(END,f"\nChocolate Muffin\t\t{self.muffin.get()}\t\t{self.muffin.get()*35}")
            if self.silk.get()!=0:
                self.txtarea.insert(END,f"\nDairy Milk Silk\t\t{self.silk.get()}\t\t{self.silk.get()*60}")
            if self.namkeen.get()!=0:
                self.txtarea.insert(END,f"\nNamkeen\t\t{self.namkeen.get()}\t\t{self.namkeen.get()*20}")

            # ========Grocery
            if self.atta.get()!=0:
                self.txtarea.insert(END,f"\nAashirvaad Atta\t\t{self.atta.get()}\t\t{self.atta.get()*200}")
            if self.pasta.get()!=0:
                self.txtarea.insert(END,f"\nPasta\t\t{self.pasta.get()}\t\t{self.pasta.get()*150}")
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\nBasmathi Rice\t\t{self.rice.get()}\t\t{self.rice.get()*180}")
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\nSunflower Oil\t\t{self.oil.get()}\t\t{self.oil.get()*120}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nRefined Sugar\t\t{self.sugar.get()}\t\t{self.sugar.get()*45}")
            if self.dal.get()!=0:
                self.txtarea.insert(END,f"\nDaal\t\t{self.dal.get()}\t\t{self.dal.get()*80}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\nTata Tea\t\t{self.tea.get()}\t\t{self.tea.get()*70}")

            # ========Hygiene
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\nBathing Soap\t\t{self.soap.get()}\t\t{self.soap.get()*30}")
            if self.shampoo.get()!=0:
                self.txtarea.insert(END,f"\nShampoo\t\t{self.shampoo.get()}\t\t{self.shampoo.get()*180}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\nBody Lotion\t\t{self.lotion.get()}\t\t{self.lotion.get()*150}")
            if self.cream.get()!=0:
                self.txtarea.insert(END,f"\nFace Cream\t\t{self.cream.get()}\t\t{self.cream.get()*120}")
            if self.foam.get()!=0:
                self.txtarea.insert(END,f"\nFace Wash Foam\t\t{self.foam.get()}\t\t{self.foam.get()*60}")
            if self.mask.get()!=0:
                self.txtarea.insert(END,f"\nFace Mask\t\t{self.mask.get()}\t\t{self.mask.get()*50}")
            if self.sanitizer.get()!=0:
                self.txtarea.insert(END,f"\nHand Sanitizer\t\t{self.sanitizer.get()}\t\t{self.sanitizer.get()*45}")

            self.txtarea.insert(END,f"\n-----------------------------------")
            if self.a.get()!="Rs. 0":
                self.txtarea.insert(END,f"\nTotal Snacks Price :\t\t{self.a.get()}")
            if self.b.get()!="Rs. 0":
                self.txtarea.insert(END,f"\nTotal Grocery Price :\t\t{self.b.get()}")
            if self.c.get()!="Rs. 0":
                self.txtarea.insert(END,f"\nTotal Hygiene Price :\t\t{self.c.get()}")

            self.txtarea.insert(END,f"\nTotal Bill :\t\t{self.Total_bill}")
            self.txtarea.insert(END,f"\n-----------------------------------")
            self.txtarea.insert(END,f"\n\n\n")

    def clear(self):
        self.txtarea.delete(1.0,END)
        self.c_name.set("")
        self.phone.set("")
        self.bill_no.set("")
        self.bill_no.set(str(random.randint(1000,9999)))

        self.nutella.set(0)
        self.noodles.set(0)
        self.lays.set(0)
        self.oreo.set(0)
        self.muffin.set(0)
        self.silk.set(0)
        self.namkeen.set(0)

        self.atta.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.dal.set(0)
        self.tea.set(0)

        self.soap.set(0)
        self.shampoo.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.foam.set(0)
        self.mask.set(0)
        self.sanitizer.set(0)

        self.total_sna.set("")
        self.total_gro.set("")
        self.total_hyg.set("")

        self.a.set("")
        self.b.set("")
        self.c.set("")
        self.Total_bill=0

    def exit(self):
        self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()
