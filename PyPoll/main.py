import os
import csv

election_csv = os.path.join("..", "PyPoll", "election_data.csv")

with open(election_csv, newline="",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    