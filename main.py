import mysql.connector

con = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "",
    database = "python new"
)
 
# if con:
#    print("connection successful") 
# else:
#     print("connection failed")


def insert ():
    name = input("Enter your name:")
    email = input("Enter your Email")
    city = input("Enter your city")

    res = con.cursor()
    sql = "insert into user (name,email,city) values (%s,%s,%s)"
    res.execute(sql,(name,email,city))
    con.commit()
    print("data insert successfully")

insert() 

def read():
    res =con.cursor()
    sql = "select * from user"
    res.execute(sql)
    result = res.fetchall
    print(result)

read()




