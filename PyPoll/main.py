#PyPoll

import os
import csv

electiondata_csv = os.path.join("PyPoll_election_data.csv")

with open(electiondata_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csv_reader, None)

 #Three columns in the Dataset: Voter ID, County, and Candidate

total_votes = {}
candidates = set()
total_candidates = {} 
vote_percent = {}

#Find the total number of votes cast    

        if row[2] not in candidates:
            total_votes[row[2]] = 1
        elif row[2] in candidates:
            total_votes[row[2]] = total_votes[row[2]] + 1


#Find complete list of candidates who received votes

for row in (csv_reader):
    candidate = row[2]
    candidates.add(candidate)


#Find percentage of votes each candidate won
 
 for key, value in total_votes.items():
        vote_percent[key] = str(round(((value/total_votes)*100),3)) + "% ("+str(value) + ")"

#Find total number of votes each candidate won

    if candidate in total_candidates:
        total_candidates[candidate] += 1
    else:
        total_candidates[candidate] = 1

#Find winner of the election based on popular vote.

winner = max(vote_percent)


#Final script should both print the analysis to the terminal and export a text file with the results.
print(winner)

outputtxt = os.path.join('filename.txt')
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(winner)
