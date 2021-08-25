import sqlite3


def FilmData():
    con = sqlite3.connect("Filmlerimiz.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS filmlerim(isim TEXT,yılı TEXT,puan TEXT,yönetmen TEXT,oyuncular TEXT,tür TEXT)")
    con.commit()
    con.close()

def filmekle(Filmİsmi,Yılı,Puanı,Yonetmeni,Oyuncuları,Türü):
    con = sqlite3.connect("Filmlerimiz.db")
    cur = con.cursor()
    cur.execute("INSERT INTO filmlerim VALUES(?,?,?,?,?,?)",Filmİsmi,Yılı,Puanı,Yonetmeni,Oyuncuları,Türü)
    con.commit()
    data_to_list()
    con.close()

def data_to_list():
    con = sqlite3.connect("Filmlerimiz.db")
    cur = con.cursor()
    cur.execute("select * from filmlerim")
    rows = cur.fetchall()
    con.close()
    return rows

def sil(isim):
    con = sqlite3.connect("Filmlerimiz.db")
    cur = con.cursor()
    cur.execute("delete from filmlerim where isim=?",(isim,))
    con.commit()
    con.close()

def data_ara(isim="",yılı="",puan="",yönetmen="",oyuncular="",tür=""):
    con = sqlite3.connect("Filmlerimiz.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM filmlerim WHERE isim =? or yılı=? or puan=? or yönetmen=? or oyuncular=? or tür=?",(isim,yılı,puan,yönetmen,oyuncular,tür))
    rows=cur.fetchall()
    con.close()
    return rows

def data_güncelle(isim="",yılı="",puan="",yönetmen="",oyuncular="",tür=""):
    con = sqlite3.connect("Filmlerimiz.db")
    cur = con.cursor()
    cur.execute("UPDATE filmlerim SET isim =?  yılı=?  puan=?  yönetmen=?  oyuncular=?  tür=?",(isim,yılı,puan,yönetmen,oyuncular,tür))
    con.commit()
    con.close()




