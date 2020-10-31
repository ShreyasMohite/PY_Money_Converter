from tkinter import *
from tkinter.ttk import Notebook,Progressbar,Combobox
import tkinter.messagebox
from currency_converter import CurrencyConverter




class Money:
    def __init__(self,root):
        self.root=root
        self.root.title("Money Converter")
        self.root.geometry("500x300")
        self.root.iconbitmap("logo281.ico")
        self.root.resizable(0,0)

        value=StringVar()
        frm=StringVar()
        to=StringVar()


        def on_enter1(e):
            but_convert['background']="black"
            but_convert['foreground']="cyan"  
        def on_leave1(e):
            but_convert['background']="SystemButtonFace"
            but_convert['foreground']="SystemButtonText"
                           

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        def convert():
            try:

                if frm.get()!="select Currency From":
                    if to.get()!="select Currency To":
                        if value.get()!="":
                            c = CurrencyConverter()
                            x=c.convert(value.get(),frm.get() ,to.get())
                            ans="{:.2f}".format(x)
                            answer="{0} {1} = {2} {3}".format(value.get(),frm.get(),ans,to.get())
                            lab_ans.config(text=answer)

                        else:
                            tkinter.messagebox.showerror("Error","Please Enter value")
                    else:
                        tkinter.messagebox.showerror("Error","Please Select Currency To")
                else:
                    tkinter.messagebox.showerror("Error","PLease Select Currency From")
            except:
                pass
           

        def clear():
            frm.set("select Currency From")
            value.set("")
            to.set("select Currency To")
            lab_ans.config(text="")

#======================frame===================================#
        mainframe=Frame(self.root,width=500,height=300,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=240,relief="ridge",bd=3,bg="#6fb0ad")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=54,relief="ridge",bd=3,bg="#72edab")
        secondframe.place(x=0,y=240)


#======================firstframe==============================================#
        
        lab_from=Label(firstframe,text="From",font=('times new roman',12),bg="#6fb0ad",fg="white")
        lab_from.place(x=90,y=10)


        list_currency_from=['TRY', 'USD', 'MYR', 'NZD', 'SIT', 'ISK', 'HRK', 'RUB', 'LVL', 'TRL', 'NOK',\
                            'GBP', 'PHP', 'ROL', 'BRL', 'KRW', 'IDR', 'ILS', 'JPY', 'HKD', 'MXN', 'EEK', 'SGD', 'CZK', 'SKK',\
                            'LTL', 'CYP', 'AUD', 'ZAR', 'RON', 'CAD', 'SEK', 'EUR', 'HUF', 'CHF', 'CNY', 'DKK', 'BGN', 'INR', 'PLN',\
                            'MTL', 'THB']
        list_currency_from_combo=Combobox(firstframe,values=list_currency_from,font=('arial',12),width=17,state="readonly",textvariable=frm)
        list_currency_from_combo.set("select Currency From")
        list_currency_from_combo.place(x=35,y=60)


        lab_to=Label(firstframe,text="To",font=('times new roman',12),bg="#6fb0ad",fg="white")
        lab_to.place(x=350,y=10)



        list_currency_to=['TRY', 'USD', 'MYR', 'NZD', 'SIT', 'ISK', 'HRK', 'RUB', 'LVL', 'TRL', 'NOK',\
                            'GBP', 'PHP', 'ROL', 'BRL', 'KRW', 'IDR', 'ILS', 'JPY', 'HKD', 'MXN', 'EEK', 'SGD', 'CZK', 'SKK',\
                            'LTL', 'CYP', 'AUD', 'ZAR', 'RON', 'CAD', 'SEK', 'EUR', 'HUF', 'CHF', 'CNY', 'DKK', 'BGN', 'INR', 'PLN',\
                            'MTL', 'THB']
        list_currency_to_combo=Combobox(firstframe,values=list_currency_to,font=('arial',12),width=17,state="readonly",textvariable=to)
        list_currency_to_combo.set("select Currency To")
        list_currency_to_combo.place(x=275,y=60)


        lab_value=Label(firstframe,text="Value",font=('times new roman',12),bg="#6fb0ad",fg="white")
        lab_value.place(x=220,y=120)

        ent_value=Entry(firstframe,width=24,font=('times new roman',12),relief="ridge",bd=3,textvariable=value)
        ent_value.place(x=140,y=150)

        lab_ans=Label(firstframe,text="",font=('times new roman',12),bg="#6fb0ad",fg="white")
        lab_ans.place(x=150,y=200)
        

#=======================secondframe============================================#

        but_convert=Button(secondframe,width=13,text="Convert",font=('times new roman',12,'bold'),cursor="hand2",command=convert)
        but_convert.place(x=80,y=7)
        but_convert.bind("<Enter>",on_enter1)
        but_convert.bind("<Leave>",on_leave1)

        but_clear=Button(secondframe,width=13,text="Clear",font=('times new roman',12,'bold'),cursor="hand2",command=clear)
        but_clear.place(x=280,y=7)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#====================================================================#
        





if __name__ == "__main__":
    root=Tk()
    app=Money(root)
    root.mainloop()