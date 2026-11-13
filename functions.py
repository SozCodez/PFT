import datetime
import json
import time
import requests
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
        while True:
            typeTransaction = input("Enter 'Expense' or 'Income': ")
            if "Income" != typeTransaction != "Expense":
                print("Enter 'Income' or 'Expense' please")
            else:
                break
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
    
    while True:
        print("""
        ===================
        TRANSACTION HISTORY
        ===================
        """)
        with open("tran.json", "r") as f:
            jsonData = json.load(f)
        for item in jsonData["Transactions"]:
            print(
                f"{item["Desc"]}\n",
                f"${item["Amount"]:.2f}\n"
                f" {item["Type"]}\n",
                f"{item["Category"]}\n",
                f"{item["Date"]}\n"
            )
        

        input0 = input("Enter 'q' to go back, or e/i for\nexpense or income only: ")
        if input0 == "q":
            break
        elif input0 == "e":
            clearTerminal()
            while True:
                print("""
                ========
                EXPENSES
                ========
                """)
                for item in jsonData["Transactions"]:
                    if item["Type"] == "Expense":
                        print(
                            f"{item["Desc"]}\n",
                            f"-${item["Amount"]:.2f}\n",
                            f"{item["Category"]}\n",
                            f"{item["Date"]}\n"
                        )
                input1 = input("Enter 'q' to go back: ")
                if input1 == "q":
                    clearTerminal()
                    break
                else:
                    clearTerminal()
        elif input0 == "i":
            clearTerminal()
            while True:
                print("""
                ======
                INCOME
                ======
                """)
                for item in jsonData["Transactions"]:
                    if item["Type"] == "Income":
                        print(
                            f"{item["Desc"]}\n",
                            f"${item["Amount"]:.2f}\n",
                            f"{item["Category"]}\n",
                            f"{item["Date"]}\n"
                        )
                input2 = input("Enter 'q' to go back: ")
                if input2 == "q":
                    clearTerminal()
                    break
                else:
                    clearTerminal()
        else:
            print("Please enter 'q', 'e', or 'i'..")
            time.sleep(1)
            clearTerminal()


def viewExpenses():
    while True:
        print("""
        ==============
        TOTAL EXPENSES
        ==============
        """)
        with open("tran.json", "r") as f:
            jsonData = json.load(f)
        menuTE = []
        expenseDict = {}
        expensesT = 0
        largest = ["", 0]
        for item in jsonData["Transactions"]:
            if item["Type"] == "Expense":
                if item["Desc"] not in expenseDict:
                    expenseDict[item["Desc"]] = item["Amount"]
                else:
                    expenseDict[item["Desc"]] += item["Amount"]
                menuTE.append(item["Desc"])
                expensesT += float(item["Amount"])
        setMenuTE = set(menuTE)
        listSetMenuTE = list(setMenuTE)
        menuTEcnt = 0
        menuTEidx = {}
        for desc in setMenuTE:
            menuTEcnt += 1
            menuTEidx[menuTEcnt] = desc
            print(f"{str(menuTEcnt)}. {desc} - ${expenseDict[desc]}")
        print(f"Total: ${expensesT}")
        for desc, expense in expenseDict.items():
            if expense > largest[1]:
                largest[1] = expense
                largest[0] = desc
        if largest != ["", 0]:
            print(f"Highest expense: {largest[0]} is ${largest[1]:.2f} of your expenses")
            input0 = input("Enter expense # or 'q' to go back: ")
        else:
            input0 = input("Enter 'q' to go back: ")

        category = ""
        while True:
            try:
                intInput0 = int(input0)
                break
            except ValueError:
                if input0 != "q":
                    input0 = input("Invalid option: ")
                else:
                    break
                    
        if input0 != "q":
            for index in listSetMenuTE:
                if (intInput0-1) == listSetMenuTE.index(index):
                    category = listSetMenuTE[intInput0 - 1]
            
        if category == "":

            if input0 == "q":
                break
            else:
                clearTerminal()
        else:
            while True:
                clearTerminal()
                print(f"""
                ============
                 {category}
                ============
                """)
                for item in jsonData["Transactions"]:
                    if item["Desc"] == category and item["Type"] == "Expense":
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
                else:
                    clearTerminal()
        
            
def viewIncome():
    while True:
        print("""
    ============
    TOTAL INCOME
    ============
    """)
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
        print(f"Total: ${incomeT}")
        if menuTI == []:
            input0 = input("Enter 'q' to go back: ")
        else:
            input0 = input("Enter expense # or 'q' to go back: ")
        
        if input0 == "q":
            break
        else:
            clearTerminal()

def viewBalance():
    while True:
        print("""
        ==============
        WALLET BALANCE
        ==============
        """)
        with open("tran.json", "r") as f:
            jsonData = json.load(f)
        menuWB = []
        incomeT = 0
        expenseT = 0
        highestE = 0
        for item in jsonData["Transactions"]:
            if item["Type"] == "Income":
                incomeT += float(item["Amount"])
            elif item["Type"] == "Expense":
                expenseT += float(item["Amount"])
        balance = incomeT - expenseT
        print()
        print(f"Balance: ${balance}")
        input0 = input("Enter 'q' to go back: ")
        if input0 == "q":
            break
        else:
            clearTerminal()

def convertCurr():
    while True:
        print("""
        ==================
        CURRENCY CONVERTER
        ==================
        """)
        print("caution: follow instructions")
        print()
        baseCode = input("Enter ISO 4217 of currency to convert: ").upper()
        baseAmount = input(f"Enter amount in {baseCode}: ")
        targetCode = input("Enter ISO 4217 of currency converting to: ").upper()
        conversion = requests.get(f"https://v6.exchangerate-api.com/v6/abacf29534c61155763f60ab/pair/{baseCode}/{targetCode}")
        conversion = conversion.json()
        #print(conversion)
        targetAmount = float(baseAmount) * conversion["conversion_rate"]
        print()
        print(f"{baseAmount} in {baseCode} is {targetAmount:,.2f} in {targetCode}")
        input0 = input("Enter 'q' to go back: ")
        if input0 == "q":
            clearTerminal()
            break
        else:
            clearTerminal()

def exitProgram():
    print()
    print("Make sure to check in everytime your wallet changes!")
    print("Until next time..:)")
    time.sleep(1)
    clearTerminal()