import psycopg2


def create_table():
    conect=psycopg2.connect("dbname='database 1' user='postgres' password='postgres3059' host='localhost' port='5432'")
    cur=conect.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store(item  TEXT,quantity INTEGER,price REAL)')
    conect.commit()
    conect.close()

def insert(item,quantity,price):
     conect=psycopg2.connect("dbname='database 1' user='postgres' password='postgres3059' host='localhost' port='5432'")
     cur=conect.cursor()
     cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
     conect.commit()
     conect.close()


def view():
    conect=psycopg2.connect("dbname='database 1' user='postgres' password='postgres3059' host='localhost' port='5432'")
    cur=conect.cursor()
    cur.execute('SELECT * FROM store')
    rows=cur.fetchall()
    conect.close()
    return rows

def update(quantity,price,item):
    conect=psycopg2.connect("dbname='database 1' user='postgres' password='postgres3059' host='localhost' port='5432'")
    cur=conect.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    rows=cur.fetchall()
    conect.commit()
    conect.close()
    return rows

def delete(item):
    conect=psycopg2.connect("dbname='database 1' user='postgres' password='postgres3059' host='localhost' port='5432'")
    cur=conect.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conect.commit()
    conect.close()



create_table()

#delete('coffe')
#insert('choclate',1,20)
#insert('water Bottle',1,30)
#insert('coffe',1,60)
#delete('water Bottle')
print(view())