import datetime
import json
import time
from clearTerm import *

#PHASE 2
#building transaction/json functions
def addTransaction():
    print("""
    =================
    ADD A TRANSACTION
    =================
    """)
    while True:
        description = input("Enter desc. of item or 'q' to go back: ")
        if description == "q":
            break
        amount = float(input("Enter amount spent: "))
        typeTransaction = input("Enter 'Expense' or 'Income': ")
        category = input("Enter best fitting category: ")
        writeJson = {
            "Desc": description,
            "Amount": amount,
            "Type": typeTransaction,
            "Category": category,
            "Date": datetime.datetime.now().strftime("%Y-%m-%d")
            }
        #read json file first
        with open("tran.json", "r") as f:
            jsonData = json.load(f)
        #insert file to dict. we pulled from json
        jsonData["Transactions"].append(writeJson)
        #write updated data back to json
        with open("tran.json", "w") as f:
            json.dump(jsonData, f, indent=4)
        break
    

def viewTransactions():
    print("""
    ===================
    TRANSACTION HISTORY
    ===================
    """)
    while True:
        with open("tran.json", "r") as f:
            jsonData = json.load(f)
        for item in jsonData["Transactions"]:
            print(
                f"{item["Desc"]}\n",
                f"{item["Amount"]}\n",
                f"{item["Type"]}\n",
                f"{item["Category"]}\n",
                f"{item["Date"]}\n"
            )
        input0 = input("Enter 'q' to go back, or e/i for\nexpense or income only: ")
        if input0 == "q":
            clearTerminal()
            break
        elif input0 == "e":
            clearTerminal()
            print("""
            ========
            EXPENSES
            ========
            """)
            while True:
                for item in jsonData["Transactions"]:
                    if item["Type"] == "Expense":
                        print(
                            f"{item["Desc"]}\n",
                            f"-${item["Amount"]}\n",
                            f"{item["Category"]}\n",
                            f"{item["Date"]}\n"
                        )
                input1 = input("Enter 'q' to go back: ")
                if input1 == "q":
                    clearTerminal()
                    break
        elif input0 == "i":
            clearTerminal()
            print("""
            ======
            INCOME
            ======
            """)
            while True:
                for item in jsonData["Transactions"]:
                    if item["Type"] == "Income":
                        print(
                            f"{item["Desc"]}\n",
                            f"${item["Amount"]}\n",
                            f"{item["Category"]}\n",
                            f"{item["Date"]}\n"
                        )
                input2 = input("Enter 'q' to go back: ")
                if input2 == "q":
                    clearTerminal()
                    break

def viewExpenses():
    print("""
    ==============
    TOTAL EXPENSES
    ==============
    """)
    while True:
        with open("tran.json", "r") as f:
            jsonData = json.load(f)
        menuTE = []
        expensesT = 0
        for item in jsonData["Transactions"]:
            if item["Type"] == "Expense":
                menuTE.append(item["Desc"])
                expensesT += float(item["Amount"])
        setMenuTE = set(menuTE)
        menuTEcnt = 0
        menuTEidx = {}
        for desc in setMenuTE:
            menuTEcnt += 1
            menuTEidx[menuTEcnt] = desc
            print(str(menuTEcnt) + ". " + desc)
        print("Total:", expensesT)
        input0 = input("Enter expense # or 'q' to go back: ")
        if input0 == "q":
            break
            
def viewIncome():
    print("""
    ============
    TOTAL INCOME
    ============
    """)
    while True:
        with open("tran.json", "r") as f:
            jsonData = json.load(f)
        menuTI = []
        incomeT = 0
        for item in jsonData["Transactions"]:
            if item["Type"] == "Income":
                menuTI.append(item["Desc"])
                incomeT += float(item["Amount"])
        setMenuTI = set(menuTI)
        menuTIcnt = 0
        menuTIidx = {}
        for desc in setMenuTI:
            menuTIcnt += 1
            menuTIidx[menuTIcnt] = desc
            print(str(menuTIcnt) + ". " + desc)
        print("Total:", incomeT)
        if menuTI == []:
            input0 = input("Enter 'q' to go back: ")
        else:
            input0 = input("Enter expense # or 'q' to go back: ")
        
        if input0 == "q":
            break

#def viewBalance():


def exitProgram():
    print()
    print("Make sure to check in everytime your wallet changes!")
    print("Until next time..:)")
    time.sleep(1)
    clearTerminal()