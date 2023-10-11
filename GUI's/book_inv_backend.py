import sqlite3

def create_table():
    conect=sqlite3.connect("Books.db")
    cur=conect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conect.commit()
    conect.close()


def insert(title,author,year,isbn):
    conect=sqlite3.connect("Books.db")
    cur=conect.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conect.commit()
    conect.close()

def view():
    conect=sqlite3.connect("Books.db")
    cur=conect.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conect.close()
    return rows

def search(title='',author='',year='',isbn=''):
    conect=sqlite3.connect("Books.db")
    cur=conect.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conect.close()
    return rows

def delete(id):
    conect=sqlite3.connect("Books.db")
    cur=conect.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conect.commit()
    conect.close()

def update(id,title,author,year,isbn):
    conect=sqlite3.connect("Books.db")
    cur=conect.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conect.commit()
    conect.close()

create_table()
#insert ("The Qaami Wahdat",'afzal khan',2010,1245)
#insert ("man of Honor",'Kareem Gabralay',2013,1236)
#insert ("Majlise Aaam",'sir syed ',1991,5689)
#print(view())


