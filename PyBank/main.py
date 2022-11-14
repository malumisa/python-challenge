# import os and csv

import os
import csv

# path to collect data from the Resources folder
budget_csv=os.path.join( "Resources", "budget_data.csv")

# Results to Financial Analysis output
total_months = []
month_of_change = []
net_change_list = []
Total_ProfitLoss = 0
Average_Change = []
counter = 0
Previous_ProfitLoss = 1088983
sum_of_changes = 0
biggest_change =0
smallest_change =0
profit= []
change_profit = []

# With open  (udemy_csv, encoding ='utf-8') as csv file
with open (budget_csv, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#Reading the header row
    header = next(csvreader)

#Print the contents of each row
    for line in csvreader:
        Date = line [0]
        ProfitLoss = int(line[1])
        counter = counter + 1
        Total_ProfitLoss += int(line[1])
        changes =  (ProfitLoss - Previous_ProfitLoss)
        Previous_ProfitLoss = ProfitLoss
        sum_of_changes += changes
        if changes > biggest_change:
            biggest_change = changes
        if  changes < smallest_change:
            smallest_change = changes
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])



 # Track the total number of months
    print(f"Total months {counter}")

# The net total amount of "profit/Losses" over the entire period
    print(f"Sum ProfitLoss {Total_ProfitLoss}") 
        
 # The changes in "Profit/Losses" over the entire period, and then the average changes       
    print(f"Sum of changes in Profit/Losses  {sum_of_changes}")     
    print(f"Average changes $ {sum_of_changes/85}")


# The greatest increase in profits (date and amount) over the entire period
    print(f"Biggest Increase $ {biggest_change}")

#  # The greatest decrease in profits (date and amount) over the entire period
    print(f"Biggest Decrease $ {smallest_change}")
# 
#evaluate the max and min from list

#using the index, 
    # month_increase = change_profit.index(max(change_profit))+1
    # month_decrease = change_profit.index(min(change_profit))+1

# save the output file path
financial_analysis = os.path.join("Financial Analysis")
# # Calculate the Average Net Change

#  Export the results to text file
with open(financial_analysis, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Months: {counter}\n")
    txt_file.write(f"Total: ${Total_ProfitLoss}\n")
    txt_file.write(f"Average  Change: ${round(sum_of_changes/85, 2)}\n")
    # txt_file.write(f"Greatest Increase in Profits: {counter[month_increase]} (${(str(biggest_change))}\n")
    # txt_file.write(f"Greatest Decrease in Profits: {counter[month_increase]}  (${(str(smallest_change))}\n")
    txt_file.write(f"Greatest Increase in Profits: {counter} (${(str(biggest_change))})\n")
    txt_file.write(f"Greatest Decrease in Profits: {counter}  (${(str(smallest_change))})\n")

