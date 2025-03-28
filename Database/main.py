import sqlite3

conn = sqlite3.connect("Bank.db")

cursor = conn.cursor()

print("connected db successfully")


# cursor.execute(''' create table Accounts( name varchar(32) not null  , account_num integer primary key  AUTOINCREMENT  ,balance number(7,2) default (500), phone number (10) not null  ,mail varchar(30)  ,pin number (4) not null default(0)); ''')

# print("table created successfully")

def acc_creation(name,phone,email):
    print(name,phone,email)
    cursor.execute(f''' insert into Accounts(name,phone,mail) values ('{name}',{phone},'{email}'); ''')
    account_num = cursor.lastrowid
    # print(account_num)
    conn.commit()
    print("account has been created")


def pin_gen(acc , pin1 , pin2):
    if pin1 == pin2 :
        # print("pin is matching")
        cursor.execute(f''' update Accounts set pin =  {pin1} where account_num = {acc} ;''')
        conn.commit()
        print("pin set successfully")


    else:
        print("enter the same pin as pin1")


def balance(acc,pin):
    cursor.execute(f''' select * from Accounts where account_num = {acc} ;''')    
    details = cursor.fetchone()
    # print(details)
    if details[-1] == pin:
        print(f'the available balance is {details[2]}')
    else :
        print("please enter the valid pin")


def deposit(acc,pin,amt):
    cursor.execute(f''' select * from Accounts where account_num = {acc} ;''')    
    details = cursor.fetchone()
    print(details)
    amount = details[2]
    if 0<=  amt <= 10000:
        if details[-1] == pin:
            cursor.execute(f'''update Accounts set balance = {amount+amt} where account_num = {acc};''')
            conn.commit()
        else:
            print("enter the valid pin")
    else:
        print("limit exceeded")


def withdrawl(acc,pin,amt):
    cursor.execute(f''' select * from Accounts where account_num = {acc} ;''')    
    details = cursor.fetchone()
    print(details)
    bal = details[2]
    if details[-1] == pin:
        if 100 <= amt < bal:
            cursor.execute(f''' update Accounts set balance = {bal-amt} where account_num = {acc}; ''')
            conn.commit()
        else:
            print("enter the valid amt")
    else:
        print("enter the vaild pin ")


        








while True:
    print('*'*32)
    print("#######",'welcome to FBI',"#########")

    print(''' 1) enter 1 to create an account \n 2)enter 2 to generate a pin \n 3) enter  3 for balance enquiry\n 4) enter 4 for Deposit \n 5) enter 5 for Withdrawl ''')

    option = int(input("enter the option  :  "))

    if option == 1:
        # cursor.execute(''' insert into Accounts(name,phone,mail,account_num) values ('vijay mallya',9848582826,'vijay420@gmail.com',123456789010); ''')
        # conn.commit()
        print('*'*32)
        print("thank you for choosing FBI(Fraud Bank of Italy) \n please enter your name : ")
        name = input(">>>")
        print("enter the phone number")
        phone = int(input(">>>"))
        print("enter your email ")
        email = input(">>>")
        acc_creation(name,phone,email)


    elif option == 2:
        print("generate pin")
        print("enter the account number")
        try:
            acc = int(input('>>>'))
        except Exception as e:
            print("please enter the proper acccount number",e)
        print("enter the pin")
        pin1 = int(input('>>>'))
        print("enter the confirm pin")
        pin2 = int(input('>>>'))

        pin_gen(acc , pin1,pin2)
    
    elif option == 3 :
        print("enter the account number")
        acc = int(input(">>>"))
        print("enter the pin")
        pin = int(input(">>>"))

        balance(acc,pin)

    elif option == 4:
        print("enter the account number")
        acc = int(input(">>>"))
        print("enter the pin")
        pin = int(input(">>>"))
        print("enter the amount to deposit ")
        amt  = int(input('>>>'))


        deposit(acc,pin,amt)
    elif option == 5 :
        print("enter the account number")
        acc = int(input(">>>"))
        print("enter the pin")
        pin = int(input(">>>"))
        print("enter the amount to withdraw ")
        amt  = int(input('>>>'))
        withdrawl(acc,pin,amt)





