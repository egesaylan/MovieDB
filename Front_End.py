from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox





class Filmlik:
    def __init__(self,root):
        self.root = root
        self.root.title("Film Yönetim Sistemi")
        self.root.geometry("1350x750+0+0")

        title=Label(self.root,text="Film Yönetim Sistemi",bd=10,relief=GROOVE,font=("Arial Black",40,"bold"),bg="gray16",fg="red3")
        title.pack(side=TOP,fill=X)

    #==================All Variables=================
        self.Film_Ismi_var=StringVar()
        self.Yılı_var=StringVar()
        self.Puanı_var = StringVar()
        self.Yonetmeni_var = StringVar()
        self.Oyuncular_var = StringVar()
        self.Türü_var = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


    #==================Manage Frame==================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="gray16")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        self.m_title=Label(Manage_Frame,text="Filmleri Yönet",bg="gray16",fg="red3",font=("times new roman",30,"bold"))
        self.m_title.grid(row=0,columnspan=2,pady=20)

        self.lbl_Isim=Label(Manage_Frame,text="Film Adı:",bg="gray16",fg="red3",font=("times new roman",20,"bold"))
        self.lbl_Isim.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        self.txt_Isim=Entry(Manage_Frame,textvariable=self.Film_Ismi_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Isim.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        self.lbl_Yıl = Label(Manage_Frame, text="Yılı:", bg="gray16", fg="red3", font=("times new roman", 20, "bold"))
        self.lbl_Yıl.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_Yıl = Entry(Manage_Frame,textvariable=self.Yılı_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_Yıl.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        self.lbl_Puan = Label(Manage_Frame, text="Puanı:", bg="gray16", fg="red3", font=("times new roman", 20, "bold"))
        self.lbl_Puan.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_Puan = Entry(Manage_Frame,textvariable=self.Puanı_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_Puan.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        self.lbl_Yonetmen = Label(Manage_Frame, text="Yönetmeni:", bg="gray16", fg="red3", font=("times new roman", 20, "bold"))
        self.lbl_Yonetmen.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.txt_Yonetmen = Entry(Manage_Frame,textvariable=self.Yonetmeni_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_Yonetmen.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        self.lbl_Oyuncular = Label(Manage_Frame, text="Oyuncuları:", bg="gray16", fg="red3", font=("times new roman", 20, "bold"))
        self.lbl_Oyuncular.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.txt_Oyuncular = Entry(Manage_Frame,textvariable=self.Oyuncular_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_Oyuncular.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        self.lbl_Tur = Label(Manage_Frame, text="Türü:", bg="gray16", fg="red3",font=("times new roman", 20, "bold"))
        self.lbl_Tur.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.combo_tur=ttk.Combobox(Manage_Frame,textvariable=self.Türü_var,font=("times new roman", 13, "bold"))
        self.combo_tur['values']=("Aksiyon","Aile","Animasyon","Aşk","Bilim Kurgu","Dram","Doğa Üstü","Epik","Fantazi","Gerilim","Korku","Komedi","Macera","Mind Fuck","Mistik","Müzikal","Romantik","Suç","Spor","Western")
        self.combo_tur.grid(row=6,column=1,padx=20,pady=10)

    #==================Button Frame=================

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="gray16")
        btn_Frame.place(x=15,y=500,width=420)

        Addbtn = Button(btn_Frame,text="Ekle",width=10,command=self.add_film).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame, text="Güncelle", width=10,command=self.update).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="Sil", width=10,command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Temizle", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)







    #===================Detail Frame=================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray16")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_Arama = Label(Detail_Frame, text="Arama:", bg="gray16", fg="red3",font=("times new roman", 20, "bold"))
        lbl_Arama.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Arama = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width =10, font=("times new roman", 13, "bold"), state="readonly")
        combo_Arama['values'] = ("film","yıl","puan","oyuncu","yönetmen","tür")
        combo_Arama.grid(row=0, column=1, padx=20, pady=10)

        txt_Arama = Entry(Detail_Frame,textvariable=self.search_txt,width=15, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Arama.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Ara", width=10,pady=5,command=self.search).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Hepsini Göster", width=12,pady=5,command=self.fetch_all).grid(row=0, column=4, padx=10, pady=10)

    #===================Table Frame=================

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="gray16")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Film_Table = ttk.Treeview(Table_Frame, columns=("Film İsmi", "Yılı", "Puanı", "Yönetmeni", "Oyuncular", "Türü"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.Film_Table.xview)
        scroll_y.config(command=self.Film_Table.yview)
        self.Film_Table.heading("Film İsmi", text="Film İsmi")
        self.Film_Table.heading("Yılı", text="Yılı")
        self.Film_Table.heading("Puanı", text="Puanı")
        self.Film_Table.heading("Yönetmeni", text="Yönetmeni")
        self.Film_Table.heading("Oyuncular", text="Oyuncular")
        self.Film_Table.heading("Türü", text="Türü")
        self.Film_Table['show'] = 'headings'
        self.Film_Table.column("Film İsmi", width=100)
        self.Film_Table.column("Yılı", width=100)
        self.Film_Table.column("Puanı", width=100)
        self.Film_Table.column("Yönetmeni", width=100)
        self.Film_Table.column("Oyuncular", width=100)
        self.Film_Table.column("Türü", width=100)
        self.Film_Table.pack(fill=BOTH, expand=1)
        self.Film_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_all()

    def add_film(self):
            if self.Film_Ismi_var.get()=="" or self.Yılı_var.get()=="":
                messagebox.showerror("Error","Bütün bilgilerin doldurulması gerekmektedir")

            else:
                con = pymysql.connect(host="localhost", user="root", password="221122112211", database="FYS")
                cur=con.cursor()
                cur.execute("INSERT INTO filmler values(%s,%s,%s,%s,%s,%s)",(self.Film_Ismi_var.get(),
                                                                   self.Yılı_var.get(),
                                                                   self.Puanı_var.get(),
                                                                   self.Yonetmeni_var.get(),
                                                                   self.Oyuncular_var.get(),
                                                                   self.Türü_var.get()
                                                                   ))

                con.commit()
                self.fetch_all()
                self.clear()
                con.close()


    def fetch_all(self):
        con = pymysql.connect(host="localhost", user="root", password="221122112211", database="FYS")
        cur = con.cursor()
        cur.execute("SELECT * FROM filmler")
        rows=cur.fetchall()
        if len(rows) !=0:
                self.Film_Table.delete(*self.Film_Table.get_children())
                for row in rows:
                    self.Film_Table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.Film_Ismi_var.set("")
        self.Yılı_var.set("")
        self.Puanı_var.set("")
        self.Yonetmeni_var.set("")
        self.Oyuncular_var.set("")
        self.Türü_var.set("")

    def get_cursor(self,ev):
        cursor_row = self.Film_Table.focus()
        contents=self.Film_Table.item(cursor_row)
        row=contents['values']
        self.Film_Ismi_var.set(row[0])
        self.Yılı_var.set(row[1])
        self.Puanı_var.set(row[2])
        self.Yonetmeni_var.set(row[3])
        self.Oyuncular_var.set(row[4])
        self.Türü_var.set(row[5])

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="221122112211", database="FYS")
        cur = con.cursor()
        cur.execute("update filmler SET yıl=%s,puan=%s,yönetmen=%s,oyuncu=%s,tür=%s where film=%s", (

                                                                      self.Yılı_var.get(),
                                                                      self.Puanı_var.get(),
                                                                      self.Yonetmeni_var.get(),
                                                                      self.Oyuncular_var.get(),
                                                                      self.Türü_var.get(),
                                                                      self.Film_Ismi_var.get()
                                                                      ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="221122112211", database="FYS")
        cur = con.cursor()
        cur.execute("delete from filmler where film=%s",self.Film_Ismi_var.get())
        con.commit()
        con.close()
        self.fetch_all()
        self.clear()

    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="221122112211", database="FYS")
        cur = con.cursor()
        cur.execute("SELECT * FROM filmler where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) !=0:
                self.Film_Table.delete(*self.Film_Table.get_children())
                for row in rows:
                    self.Film_Table.insert('',END,values=row)
                con.commit()
        con.close()





root = Tk()
app = Filmlik(root)
root.mainloop()

