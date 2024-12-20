# structure
# structure data

# create table <newTableName> like <existingTableName>
# create table <newTableName> AS (select * from <existingTableName>)

# DDL, DML, DCL, TCL

# MYSQL  PYTHON

# DRiver : mysql-connector
# pip install mysql-connector



import mysql.connector as my
con = my.connect(host = "127.0.0.1",user = "root",password ="",database = "batch_9")
#print(con)
cur = con.cursor() # Request Response
#cur.execute("create database batch_9")

#sql = "create table student (id int primary key auto_increment, name varchar(200), college varchar(200), branch varchar(200))"
#cur.execute(sql)

def registration():
    name = input("NAME: ")
    college = input("Collge: ")
    branch = input("Branch: ")

    insert_sql = "insert into student (college, name, branch) values(%s,%s,%s)"
    val = (college, name, branch)
    cur.execute(insert_sql,val)

    '''
    login_sql = "insert into login (user, pwd) values(%s,%s)"
    val1 = (name,branch)
    cur.execute(login_sql, val1)
    '''
    con.commit()


fetch_sql = "select * from student where name = 'Lilesh'"
cur.execute(fetch_sql)
data = cur.fetchall() # fetchall()
print(data)

#registration()


'''
Project:
    BANKING SYSTEM
        1. ADD USER
                a. name b. account number(radom unique 10 digit)
                c. dob d. city e.password (validate) f. initial balance(minimum)
                g. contact number h. Email ID i. Address
        2. SHOW USER
        3. LOGIN
            a. acc nu b. password
                i) show balance
                ii) show transaction
                iii) credit amount
                iv) Debit amount
                v) Transfer amount
                vi) Active/Deactive account
                vii) change password
                viii) update profile
                ix) Logout
        4. EXIT


        DB:
            DB NAME : banking_system
            Tables:
                    1) users
                    2) login
                    3) transaction

'''



