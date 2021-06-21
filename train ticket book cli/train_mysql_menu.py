import mysql.connector as db

try:
    conn=db.connect(host="localhost",user="root",passwd="",database="train")
except:
    print("You did not enter either correct host name or database name")
    
cur=conn.cursor()

print("Enter 1 for ticket generation")
print("Enter 2 for getting details of particular ticket number")
print("Enter 3 for getting complete information of tickets")
m=int(input("Enter your choice"))

if(m==1):
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
    conn.close()

elif(m==2):
    n=int(input("Enter that ticket number whose information you want"))
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
    conn.close()

elif(m==3):
    q="select * from bookticket"
    try:
        cur.execute(q)
    except:
        print("You did not enter either correct sql or error in query")
    a=cur.fetchall()
    print("ticket_no","name".center(16),"age".center(49),"source".center(27),"destination".center(23))
    print("\n")
    for i in a:
        print(i[0],i[1].center(32),str(i[2]).center(35),i[3].center(37),i[4].center(23))
        #age is integer so typecasting

else:
    print("You did not enter correct choice.Please enter correct choice.")

    
