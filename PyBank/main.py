#Import modules
import os
import csv

#Set path for the file
budget_csv = os.path.join("..", "PyBank", "budget_data.csv")

#Open and Read the csv in block
with open(budget_csv, newline="",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Skip first row
    next(csvreader)

    total_months = sum(1 for line in open(budget_csv))-1

    total_profit = []
    profit_change = []
    months = []

    
    for row in csvreader:
        total_profit.append(int(row[1]))
        months.append(row[0])

    for x in range(len(total_profit)-1):
        profit_change.append(total_profit[x+1]-total_profit[x])

    avg_change = sum(profit_change)/len(profit_change)
    max_increase = max(profit_change)
    min_decrease = min(profit_change)

    max_month = profit_change.index(max(profit_change))+1
    min_month = profit_change.index(min(profit_change))+1


    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits:{months[max_month]} (${max_increase})")
    print(f"Greatest Increase in Profits:{months[min_month]} (${min_decrease})")




    

    
        
        
    


    #The net amount of "Profit/Losses" over the entrie period


    #Average of the changes in "Profit/Losses" over the entire period


    #greatest increase in profits (date and amount) over the entire period


    #greatest decrease in losses (date and amount) over the entire period



