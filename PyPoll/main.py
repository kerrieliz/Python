#PyPoll

import os
import csv

electiondata_csv = os.path.join("/Users/kerriegill/Documents/GitHub/Python/PyPoll/Python_PyPoll_election_data.csv")

with open(electiondata_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csv_reader, None)


#Find the total number of votes cast  
total_votes = 0 

#Find complete list of candidates who received votes
candidates = set()

for row in (csv_reader):
    candidate = row[2]
    candidates.add(candidate)

#Find percentage of votes each candidate won


#Find total number of votes each candidate won
total_candidates = {} 

    if candidate in total_candidates:
        total_candidates[candidate] += 1
    else:
        total_candidates[candidate] = 1

#Find winner of the election based on popular vote.


#Final script should both print the analysis to the terminal and export a text file with the results.
print(winner)

outputtxt = os.path.join('filename.txt')
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(Winner)
