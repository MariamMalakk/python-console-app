import main
from datetime import datetime
def projmenu():

    print(">>>>Welcome to your profile<<<<")
    choice = input("""
    1: Create a project
    2: View all projects
    3: Edit your projects
    4: Delete your projects
    please choose an option:
     """)

    if choice == "1":
        create()
    elif choice == "2":
        view()
    elif choice == "3":
        edit()
    elif choice == "4":
        delete()
    else:
        print("You must only select an option")
    projmenu()
def pid():
    with open("userproj.txt", 'r') as pid :
        x = len(pid.readlines())
        global projid
        projid = x+1
        return projid


def create():
    while True:
        us = input("enter your id: ")
        usid = open("userinfo.txt", 'r')
        for i in usid:
            userinfo = i.strip("\n")
            userinfo = i.split(":")
            if not userinfo[0] == us:
                continue
        else:
            break

    while True :
        title = input("type your project title:")
        if not title.isalpha():
            print("it should be string only")
            continue
        else:
            break

    while True :
        details = input("Write your project details:")
        if len(details) == 0 :
            print("it shouldn't be null")
            continue
        else:
            break

    while True :
        totaltarget = input("Enter your total target in EGP:")
        if not totaltarget.isdigit():
            print("it should be only numbers")
            continue
        else:
            break


    while True:
        startdate = input("Enter your start date YYY-MM-DD:")
        enddate = input("Enter your end date YYY-MM-DD:")
        date_format = '%Y-%m-%d'

        try:

            dateObject = datetime.strptime(startdate, date_format)
            dateObject = datetime.strptime(enddate, date_format)

            break


        except ValueError:

            print("Incorrect data format, should be YYYY-MM-DD")
            continue



    projdata = f"{us}:{pid()}:{title}:{details}:{totaltarget}:{startdate}:{enddate}\n"
    try:
        fileobjc = open("userproj.txt", 'a')
    except Exception as e:
        print(e)
    else:
        fileobjc.write(projdata)
        fileobjc.close()
        projmenu()


def view():
    try:
        pfile=open("userproj.txt","r")
    except Exception as e:
        print(e)
    else:
        file=pfile.read()
        print(file)
        projmenu()


def edit():

    inputFile = "userproj.txt"
    with open("userproj.txt", 'r') as filedata:
        inputFilelines = filedata.readlines()
        lineindex = 1
        editLine = int(input("Enter the line number to be updated = "))
        with open(inputFile, 'r') as filedata:
            for textline in inputFilelines:
                if lineindex == editLine:
                    create()
                    filedata.write(textline)
                    lineindex += 1
    print("Line", editLine, 'is updated successfully\n')
    filedata.close()

def delete():

    inputFile = "userproj.txt"
    with open("userproj.txt", 'r') as filedata:
        inputFilelines = filedata.readlines()
        lineindex = 1
        deleteLine = int(input("Enter the line number to be deleted = "))
        with open(inputFile, 'w') as filedata:
            for textline in inputFilelines:
                if lineindex != deleteLine:
                    filedata.write(textline)
                    lineindex += 1
    print("Line", deleteLine, 'is deleted successfully\n')
    filedata.close()
projmenu()