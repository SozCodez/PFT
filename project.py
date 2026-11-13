import time
from functions import *
from clearTerm import *

#Phase 1
#Building main command-line menu
menuOptions = {
    "1.": "Add a transaction",
    "2.": "View all transactions",
    "3.": "View total income",
    "4.": "View total expenses",
    "5.": "View account balance",
    "6.": "Convert currencies",
    "7.": "Exit program"
}
menuHead = """
========================
PERSONAL FINANCE TRACKER
========================
"""

def main():
    while True:
        print(menuHead)
        for option in menuOptions:
            print(option, menuOptions[option])
        print()
        selectedOpt = input("Select an option: ") + "."
        if selectedOpt == "1.":
            clearTerminal()
            addTransaction()
            time.sleep(1)
            clearTerminal()
        elif selectedOpt == "2.":
            clearTerminal()
            viewTransactions()
            time.sleep(1)
            clearTerminal()
        elif selectedOpt == "3.":
            clearTerminal()
            viewIncome()
            time.sleep(1)
            clearTerminal()
        elif selectedOpt == "4.":
            clearTerminal()
            viewExpenses()
            time.sleep(1)
            clearTerminal()
        elif selectedOpt == "5.":
            clearTerminal()
            viewBalance()
            time.sleep(1)
            clearTerminal()
        elif selectedOpt == "6.":
            clearTerminal()
            convertCurr()
            time.sleep(1)
            clearTerminal()
        elif selectedOpt == "7.":
            exitProgram()
            break
        else:
            print("Not a valid option.")
            time.sleep(1)
            clearTerminal()

main()