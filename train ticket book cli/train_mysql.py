import mysql.connector as db

try:
    conn=db.connect(host="localhost",user="root",passwd="",database="train")
except:
    print("You did not enter either correct host name or database name")
    
cur=conn.cursor()

q="insert into bookticket(name,age,source,destination) values(%s,%s,%s,%s)"
p=input("Enter name")
t=int(input("Enter age"))
r=input("Enter source")
s=input("Enter destination")
val=(p,t,r,s)
try:
    cur.execute(q,val)
except:
    print("You did not enter either correct sql or error in query")
conn.commit()
print("\n\n\nYour ticket is generated!!")
n=cur.lastrowid
print("\n\nYour ticket number is:",n)

q="select * from bookticket where ticket_no='"+str(n)+"'"
try:
    cur.execute(q)
except:
    print("You did not enter either correct sql or error in query")
a=cur.fetchone()
print("Name=",a[1])
print("age=",a[2])
print("source=",a[3])
print("destination=",a[4])
print("\n\n\n")
q="select * from bookticket"
try:
    cur.execute(q)
except:
    print("You did not enter either correct sql or error in query")
a=cur.fetchall()
for i in a:
    print(i)

conn.close()
