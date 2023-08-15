import mysql.connector
import random

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='kingdom12!',
    
)
# toss="""select * from toss;"""
# user_accountnumber=input("Please type your accountnumber:")
# user_password = input("Please type your password:")
# user_address = input("please type your address:")
# user_gender = input("Please type your gender:")
# user_age = input("please type your age:")
# # print(user_accountnumber,user_password, user_address, user_gender,user_age)
# Insert= f"""INSERT INTO toss (accountnumber, pw, address, gender, age) values({user_accountnumber}, {user_password}, {user_address}, {user_gender}, {user_age});"""


cursorObject=dataBase.cursor()
cursorObject.execute("use Bank")
# Here is the Python version of your Java code.


class Bank:
    def __init__(self):
        self.owner = None
        self.account = None
        self.activation = False
        self.balance = 0
        self.amount =0 
        self.password = None

def create_bank(KB):
    bank = Bank()
    bank.owner = input("성함을 입력해주세요: ")
    bank.account = generate_bank_account()
    bank.activation = True
    password = input("설정할 비밀번호 4자리를 입력해주세요: ")
    password_check = input("비밀번호 4자리를 다시 입력해주세요: ")
    if password == password_check:
        bank.password = password
    else:
        print("입력하신 비밀번호가 올바르지 않습니다.")
        return
    bank.balance = 0
    str(bank.owner).replace("'", '"')
    print("계좌번호: ", bank.account)
    sql = f"""Insert into toss(accountnumber, pw, ownername, balance) values({bank.account}, {bank.password}, '{bank.owner}', {bank.balance})"""
    cursorObject.execute(sql)
    dataBase.commit()

def check_balance(KB):
    bank = Bank()
    index = validate(KB)
    if index != -1:
        print("고객님의 잔액은 :", int(KB[index].balance),"원 입니다.\n")
    bank.balance=0
    sql = f"""select ID from toss where balance={bank.balance};"""
    cursorObject.execute(sql)
    dataBase.commit()

def add_balance(KB):
    bank = Bank()
    index = validate(KB)
    if index != -1:
        add = int(input("충전하실 액수를 입력해주세요: "))
        KB[index].balance += add
        print("충전후 잔액은 ", KB[index].balance, "원 입니다")
    else:
        print("비밀번호가 틀렸습니다.")
    bank.amount=0
    sql = f"""select ID from toss where amount={bank.amount};"""
    cursorObject.execute(sql)
    dataBase.commit()

def validate(KB):
    account = input("계좌번호를 입력해주세요: ")
    password = input("비밀번호를 입력해주세요: ")
    sql = f"""select ID from toss where accountnumber={account} and pw={password};"""
    cursorObject.execute(sql)
    result=cursorObject.fetchall()
    if result != None:
        return result
    else:
        create_bank()
        
        
    
    # for i in range(len(KB)):
    #     if KB[i].account == account:
    #         password = input("비밀번호를 입력해주세요: ")
            
    #     if KB[i].password == password:
    #             return i
    # return -1

def generate_bank_account():
    first_part = str(random.randint(1000000, 1999999))
    second_part = str(random.randint(10, 99))
    last_part = str(random.randint(1000000, 1999999))
    return first_part + "-" + second_part + "-" + last_part

def transfer(KB):
    index = validate(KB)
    if index != -1:
        receiver = input("받으실 분의 계좌번호를 작성해주세요: ")
        for j in range(len(KB)):
            if KB[j].account == receiver:
                amount = int(input("송금하실 금액을 입력해주세요: "))
                if amount > KB[index].balance:
                    print("잔액이 부족합니다")
                else:
                    KB[index].balance -= amount
                    KB[j].balance += amount
                    print("송금 후 잔액은 ", KB[index].balance, "원 입니다.")

def main():
    KB = []
    while True:
        print("원하시는 서비스를 선택해주세요")
        print("1.계좌생성 2.잔액 조회 3. 잔액 충전 4. 송금 5. 종료")
        user_input = input()
        if user_input == "1":
            create_bank(KB)
        elif user_input == "2":
            check_balance(KB)
        elif user_input == "3":
            add_balance(KB)
        elif user_input == "4":
            transfer(KB)
        elif user_input == "5":
            print("시스템을 종료합니다")
            break
        else:
            print("존재하지 않는 숫자입니다 다시 입력해주세요.")

main()
# cursorObject.execute(Insert)
# dateBase.commit()
# cursorObject.execute("INSERT INTO toss (id, accountnumber, pw, address, gender, age) values(11, '05123', 'asdf' 'Jeju', 'female', '45');")
# result=cursorObject.fetchall()
# print(result)