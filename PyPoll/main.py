import os
import csv

election_csv = os.path.join("..", "PyPoll", "election_data.csv")

with open(election_csv, newline="",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otool_votes = 0

    next(csvreader)

    for row in csvreader:

        total_votes +=1

        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row [2] == "O'Tooley":
            otool_votes +=1

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otool_votes]

candidates_with_votes = dict(zip(candidates,votes))
winner = max(candidates_with_votes, key=candidates_with_votes.get)

khan_percent = (khan_votes/total_votes)*100
correy_percent = (correy_votes/total_votes)*100
li_percent = (li_votes/total_votes)*100
otool_percent = (otool_votes/total_votes)* 100

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Khan: {round(khan_percent, 3)}% ({khan_votes})")
print(f"Correy: {round(correy_percent, 3)}% ({correy_votes}) ")
print(f"Li: {round(li_percent, 3)}% ({li_votes})")
print(f"O'Tooley: {round(otool_percent, 3)}% ({otool_votes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

f = open("output.txt", "w")
print(f"Election Results", file=f)
print(f"-------------------------", file=f)
print(f"Total Votes: {total_votes}", file=f)
print(f"-------------------------", file=f)
print(f"Khan: {round(khan_percent, 1)}% ({khan_votes})", file=f)
print(f"Correy: {round(correy_percent, 1)}% ({correy_votes})", file=f)
print(f"Li: {round(li_percent, 1)}% ({li_votes})", file=f)
print(f"O'Tooley: {round(otool_percent, 1)}% ({otool_votes})", file=f)
print(f"-------------------------", file=f)
print(f"Winner: {winner}", file=f)
print(f"-------------------------", file=f)
f.close()





    