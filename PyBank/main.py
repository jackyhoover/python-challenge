#Import modules
import os
import csv

#Set path for the file
budget_csv = os.path.join("..", "PyBank", "budget_data.csv")

#Lists to store data

month = []
profit_loss = []


#Open and Read the csv in block
with open(budget_csv, newline="",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    row_count = sum(1 for line in open(budget_csv))-1

    print(row_count)

    #for row in csvreader:
        #profit_loss.append(row[1])
        
        
    


    #The net amount of "Profit/Losses" over the entrie period


    #Average of the changes in "Profit/Losses" over the entire period


    #greatest increase in profits (date and amount) over the entire period


    #greatest decrease in losses (date and amount) over the entire period



