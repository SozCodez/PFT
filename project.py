import time
import datetime
import json
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
    "6.": "Exit"
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
        elif selectedOpt == "6.":
            exitProgram()
            break
        else:
            print("Not a valid option.")
            time.sleep(1)
            clearTerminal()

main()