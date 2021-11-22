import pickle
import os
import pathlib


class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccount(self):
        self.accNo = int(input("Enter The Account Number: "))
        self.name = input("Enter The Account Holder Name: ")
        self.type = input("Enter The Type Of Account [C/S]: ")
        self.deposit = int(input("Enter The Initial Amount(>=500 For Savings And >=1000 For Current): "))
        print("\nAccount Created")

    def showAccount(self):
        print("Account Number: ", self.accNo)
        print("Account Holder Name: ", self.name)
        print("Type Of Account: ", self.type)
        print("Balance: ", self.deposit)

    def modifyAccount(self):
        print("Account Number: ", self.accNo)
        self.name = input("Modify Account Holder Name: ")
        self.type = input("Modify Type Of Account: ")
        self.deposit = int(input("Modify Balance: "))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


def intro():
    print("\t\t\t\t\t******************************************")
    print("\t\t\t\t\t**********BANK MANAGEMENT SYSTEM**********")
    print("\t\t\t\t\t******************************************")
    input()


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit)
        infile.close()
    else:
        print("No Records To Display")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print("Your Account Balance Is: ", item.deposit)
                found = True
    else:
        print("No Records To Search")
    if not found:
        print("No Existing Record With This Number")


def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input("Enter The Amount To Deposit: "))
                    item.deposit += amount
                    print("Your Account Is Updated")
                elif num2 == 2:
                    amount = int(input("Enter The Amount To Withdraw: "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        print("You Cannot Withdraw Larger Amount")

    else:
        print("No Records To Search")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == num:
                item.name = input("Enter The Account Holder Name: ")
                item.type = input("Enter The Account Type: ")
                item.deposit = int(input("Enter The Amount: "))

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


ch = ''
num = 0
intro()

while ch != 8:
    print("\nMain Menu")
    print("1. New Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Balance Enquiry")
    print("5. All Account Holders List")
    print("6. Close An Account")
    print("7. Modify An Account")
    print("8. Exit")
    print("Select Your Option (1-8): ")
    ch = input("Enter Your Choice: ")

    if ch == '1':
        writeAccount()
    elif ch == '2':
        num = int(input("Enter The Account Number: "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("Enter The Account Number: "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("Enter The Account Number: "))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num = int(input("Enter The Account Number: "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("Enter The Account Number: "))
        modifyAccount(num)
    elif ch == '8':
        print("Thanks For Using Bank Management System")
        break
    else:
        print("Invalid Choice")
