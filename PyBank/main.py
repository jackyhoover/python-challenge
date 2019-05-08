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
    print(total_months)

    total_profit = []
    profit_change = []

    total = 0
    for row in csvreader:
        total_profit.append(int(row[1]))

    for x in range(len(total_profit)-1):
        profit_change.append(total_profit[x+1]-total_profit[x])

    
    print(sum(total_profit))
    print(sum(profit_change)/len(profit_change))

    

    
        
        
    


    #The net amount of "Profit/Losses" over the entrie period


    #Average of the changes in "Profit/Losses" over the entire period


    #greatest increase in profits (date and amount) over the entire period


    #greatest decrease in losses (date and amount) over the entire period



