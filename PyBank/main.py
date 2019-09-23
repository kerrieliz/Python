#PyBank

import os
import csv

budgetdata_csv = os.path.join("/Users/kerriegill/Documents/GitHub/Python/PyBank/Python_PyBan_budget_data.csv")

with open(budgetdata_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csv_reader, None)

total_months = 0
total_revenue = 0
prev_revenue = 0
greatest_rev_increase = 0
greatest_rev_decrease = 0 

#list 
Rev_Change = []

for row in budgetdata_csv

#Calculate the total number of months included in the dataset
total_months = len(column)

#Calculate the net total amount of "Profit/Losses" over the entire period
total_revenue = total_revenue(int(row[1]))

#Calculate the average of the changes in "Profit/Losses" over the entire period
monthly_change = int(row[1]) - prev_revenue
prev_revenue = int(row[1])
Rev_Change.append(monthly_change)

avg_rev_change = round(sum(Rev_Change)/total_months)

#Calculate the greatest increase in profits (date and amount) over the entire period
if (monthlyRevChange > greatest_rev_increase):
    greatest_month_increase = row[0]
    greatest_rev_increase = monthlyRevChange 

#Calculate the greatest decrease in losses (date and amount) over the entire period
if (monthlyRevChange < greatest_rev_decrease):
    greatest_month_decrease = row[0]
    greatest_rev_decrease = monthlyRevChange

#final script should both print the analysis to the terminal and export a text file with the results.
print(avg_rev_change)

outputtxt = os.path.join('filename.txt')
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(Results)
