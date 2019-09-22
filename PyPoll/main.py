#PyPoll

import os
import csv

electiondata_csv = os.path.join("/Users/kerriegill/Documents/GitHub/Python/PyPoll/Python_PyPoll_election_data.csv")

with open(electiondata_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csv_reader, None)

 #Three columns in the Dataset: Voter ID, County, and Candidate
 Voter_ID = 0
 County = 0
 Candidate = 0

#Find the total number of votes cast


#Find complete list of candidates who received votes


#Find percentage of votes each candidate won


#Find total number of votes each candidate won


#Find winner of the election based on popular vote.


#Final script should both print the analysis to the terminal and export a text file with the results.
