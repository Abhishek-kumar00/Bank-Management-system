import mysql.connector
import pickle
mydb=mysql.connector.connect(user='root',passwd='abhishek1',host='localhost',database='BankDB',charset='utf8')
mycursor=mydb.cursor(buffered=True)
def Menu():
    print("*"*140)
    print("MAIN MENU".center(140))
    print("1.Insert Record/Records".center(140))
    print("2.Display Records as per account number".center(140))
    print("    a.sorted as per account number".center(140))
    print("    b.sorted as per customer name".center(140))
    print("    c.shorted as per customer balance".center(140))
    print("3.Search Record details as per the account number".center(140))
    print("4.Delete record".center(140))
    print("5.Exit".center(140))
    print("*"*140)

def MenuSort():
    print("    a.Sorted as per Account Number".center(140))
    print("    b.sorted as per customer name".center(140))
    print("    c.sorted as per customer balance".center(140))
    print("    d.Back".center(140))


def create():
    try:
        mycursor.execute('create table bank(ACCNo varchar(10),NAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),CITY varchar(50),COUNTRY varchar(50),BALANCE varchar(50))')
        print("table created")
        insert()
    except:
        print("Table exist")
        insert()

def insert():
    while True:
        Acc=input("Enter account no")
        Name=input("Enter name")
        Mob=input("Enter mobile")
        email=input("Enter Email")
        Add=input("Enter Address")
        city=input("Enter City")
        country=input("Enter country")
        Bal=float(input("Enter Balance"))
        Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),city.upper(),country.upper(),Bal]
        cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(cmd,Rec)
        mydb.commit()
        ch=input("Do you want to enter more records")
        if ch=='N' or ch=='n':
            break
def DispSortAcc():
    try:
        cmd="select* from BANK order by ACCNo"
        mycursor.execute(cmd)
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F%("ACCNo","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("table doesn't exist")
def DispSortName():
    try:
        cmd="select* from BANK order by NAME"
        mycursor.execute(cmd)
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F%("ACCNo","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s"%j, end=' ')
            print()
        print("="*125)
    except:
        print("table doesn't exist")

def DispSortBal():
    try:
        cmd="select* from BANK order by BALANCE"
        mycursor.execute(cmd)
        f="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(f%("ACCNo","NAME","MOBILE","EMAIL", "ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s"%j, end=' ')
            print()
        print("="*125)
    except:
        print("table doesn't exist")
def DispsearchAcc():
    try:
        cmd="select* from BANK"
        mycursor.execute(cmd)
        ch=input("Enter the accountno to be searched")
        for i in mycursor:
            
            if i[0]==ch:
                print("="*125)
                f="%15s %15s %15s %15s %15s %15s %15s %15s"
                print(f%("ACCNo","NAME","MOBILE","EMAIL", "ADDRESS","CITY","COUNTRY","BALANCE"))
                print("="*125)
                for j in i:
                    print("%14s"%j, end=' ')
                print()
                break
            else:
                print("record Not found")
    except:
        print("Table doesn't exist")


def delete():
    try:
        cmd="select* from BANK"
        mycursor.execute(cmd)
        A=input("Enter the account no whose details to be changed")
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                cmd="delete from BANK where accno=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("account deleted")
                break
        else:
            print("record not found")
    except:
        print("No such table")


                 


while True:
    Menu()
    ch=input("Enter your choice")
    if ch=="1":
        create()
    elif ch=="2":
        while True:
            MenuSort()
            ch1=input("Enter choice a/b/c/d")
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print("Back to main menu")
                break
            else:
                print("Invalid choice")
    elif ch=="3":
        DispsearchAcc()
    elif ch=="4":
        delete()
    elif ch=="5":
        print("Exiting...")
        break
    else:
        print("wrong choice Entered")

    
            
        
    
        
        
                
                

