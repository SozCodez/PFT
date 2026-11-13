import json
from datetime import *
import time
#functions of monthly reports
def averageMonthly():
    while True:
        monthlyExpenses = {"Expenses": 
        [

        ]
        }
        monthlyIncomes = {"Incomes":
        [

        ]       
        }
        monthExpense = 0

        with open("tran.json", "r") as f:
            jsonData = json.load(f)
        for item in jsonData["Transactions"]:
            if item["Type"] == "Expense":
                dateString = item["Date"]
                #numbered
                dateObj = datetime.strptime(dateString, "%Y-%m-%d")
                #word
                dateMonth = dateObj.strftime("%B")
                dateYear = dateObj.year
                #monthExpense += item["Amount"]
                if dateMonth not in monthlyExpenses["Expenses"]:
                    monthlyExpenses["Expenses"].append({"Month": dateMonth, "Month#": dateObj.month, "Amount": item["Amount"]})
                else:
                    dateMonth["Amount"] += item["Amount"]
            if item["Type"] == "Income":
                dateString = item["Date"]
                #numbered
                dateObj = datetime.strptime(dateString, "%Y-%m-%d")
                #word
                dateMonth = dateObj.strftime("%B")
                dateYear = dateObj.year
                #monthExpense += item["Amount"]
                if dateMonth not in monthlyIncomes["Incomes"]:
                    monthlyIncomes["Incomes"].append({"Month": dateMonth, "Month#": dateObj.month, "Amount": item["Amount"]})
                else:
                    dateMonth["Amount"] += item["Amount"]
        #print(monthlyExpenses)
        #print(monthlyIncomes)
        #time.sleep(4)