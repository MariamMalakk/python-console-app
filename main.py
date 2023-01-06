
# ----------name validation-----------------

def menu():

    print(">>>>Welcome to your console<<<<")
    choice = input("""
    1: Register
    2: Login
    please choose an option:
     """)

    if choice == "1":
        reg()
    elif choice == "2":
        login()
    else:
        print("You must only select either 1 or 2")
        menu()
def uid():
    with open("userinfo.txt", 'r') as uid :
        y = len(uid.readlines())
        global userid
        userid = y+1
        return userid

def reg():
    while True:

            fname=input("enter your first name: ")
            lname = input("enter your last name: ")
            if not (fname.isalpha() and lname.isalpha()):
                print("not valid name")
            elif len(fname) < 3 and len(lname):
                print("not valid name")
                continue
            else:
               break
    # ---------------mail validation-----------------
    while True:
        mail = input("enter your email: ")
        if not (mail.__contains__('@') and mail.__contains__('.com')):
            print('mail not valid')
            continue
        else:
            break

    # --------------------password confirmation-------------
    while True:
        passw = input("enter your password :")
        if len(passw) < 5:
            print('Password too short')
            continue

        confpass = input("confirm your password: ")
        if confpass == passw:

            break
        else:
            print("password is not match")



    while True:
         mphone = input("enter your phone number: ")
         if not mphone.isdigit():
            print("not valid number")
            continue
         else:
            break

    userinfo = f"{uid()}:{fname}:{lname}:{mail}:{passw}:{mphone}\n"
    try:
        fileobj=open("userinfo.txt",'a')

    except Exception as e:
        print(e)
    else:
        fileobj.write(userinfo)
        fileobj.close()
        menu()

def login():
    print(">>>>Login to your profile<<<<")
    user_name = input("enter your name:")
    password = input("enter your password:")
    fileobj = open("userinfo.txt", "r")
    # users = fileobj.readlines()
    for i in fileobj:
         userinfo = i.strip("\n")
         userinfo = i.split(":")
         if (userinfo[1]==user_name and userinfo[4]==password):
             print ("logged in ")
             break
    else:
        print ("wrong user try again")
        login()


menu()























