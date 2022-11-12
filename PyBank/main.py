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
Greatest_Increase_in_Profits = []
Greatest_Decrease_in_Profits =  []
Average_Change = []
counter = 0
Previous_ProfitLoss = 1088983
sum_of_changes = 0
biggest_change =0
smallest_change =0

# With open  (udemy_csv, encoding ='utf-8') as csv file
with open (budget_csv, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#Reading the header row
    header = next(csvreader)

#Print the contents of each row
    for Line in csvreader:
        Date = Line [0]
        ProfitLoss = int(Line[1])
        counter = counter + 1
        Total_ProfitLoss += int(Line[1])
        changes =  (ProfitLoss - Previous_ProfitLoss)
        Previous_ProfitLoss = ProfitLoss
        sum_of_changes += changes
        if changes > biggest_change:
            biggest_change = changes
        if  changes < smallest_change:
            smallest_change = changes




 # Track the total number of months
    print(f"Total months {counter}")

# The net total amount of "profit/Losses" over the entire period
    print(f"Sum ProfitLoss {Total_ProfitLoss}") 
        
 # The changes in "Profit/Losses" over the entire period, and then the average changes       
    print(f"Sum of changes in Profit/Losses  {sum_of_changes}")     
    print(f"Average changes {sum_of_changes/85}")


# The greatest increase in profits (date and amount) over the entire period
    print(f"Biggest Increase {biggest_change}")

#  # The greatest decrease in profits (date and amount) over the entire period
    print(f"Biggest Decrease {smallest_change}")
# 
# 
# ProfitLosses = int(row[1])
# print(f'[{int(max(ProfitLosses))}] {Date}')
    
#         # Calculate the greatest decrease


# # save the output file path
# financial_analysis = os.path.join("Financial Analysis")
# # Calculate the Average Net Change

# # Export the results to text file
# with open(financial_analysis, "w") as txt_file:
#     txt_file.write(f"Financial Analysis\n")
#     txt_file.write(f"----------------------------\n")
#     txt_file.write(f"Total Months: {total_months}\n")
#     txt_file.write(f"Total: ${total_net}\n")
#     txt_file.write(f"Average  Change: ${net_monthly_avg}\n")
#     txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
#     txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


#     Date = str(budget_data[0])
#     ProfitLosses = int(budget_data[1])




