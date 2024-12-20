#file handling

'''
open(filename,access_mode)
Access_mode:
    r = read the content of the file, if file not available then return
        file not found error
        read() -> read all data return string
        readline() -> read first line return string
        readllines() -> read all lines retrun list with each line as element
    w = write the content in the file, if file not available then create
        new file
    a = append
    r+ = read and write
    rb = read binary files
'''
'''
file = open('example.txt','a')
file.write("['BYE HELLO','HI']")

file.close()
print(file)
'''
'''
with open('example.txt','a') as file:
    for i in range(1,10):
        file.write(f"Line number {i}\n")
print("HELLO")
'''
with open('example.txt','r') as fi:
    da = fi.readlines()
    print(da)

logged = False
log_user = ''

def register():
    na = input("Enter your name: ")
    en = input("Enter your enrollment: ")
    clg = input("Enter your college: ")
    pwd = input("Enter your password: ")

    with open('userDetails.txt','a') as user:
        user.write(f"{na},{en},{clg},{pwd}\n")

    with open('loginDetails.txt','a') as login:
        login.write(f"{en},{pwd}\n")


def login():
    en = input("Enter your Enrollment: ")
    pw = input("Enter your password: ")

    with open('loginDetails.txt','r') as login:
        us = login.readlines()
        for i in us:
            i = i.replace('\n','')
            li = i.split(',')
            if li[0] == en and li[1] == pw:
                print("login successful")
                
                logged = True
                log_user = en
                break
        else:
            print("Wrong Credentials")
                
#login()


def changePassword():
    global logged
    global log_user

    if logged:
        with open('loginDetails.txt','r') as file:
            file.readlines()


def main():
    op = input("""Choose an option 
                1. Register
                2. Login
                3. Attempt quiz a. DSA b. DBMS c. Python
                4. Show result
                5. Exit
                Enter your choice : """)
    if op == '1':
        register()
    elif op == '2':
        login()
    elif op == '3':
        attemptQuiz()
    elif op == '4':
        showResult()
    elif op == '5':
        exit()
    else:
        print("Wrong choice")
        main()
        


