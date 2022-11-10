# import os and csv
import os
import csv

# path to collect data from the Resources folder
budget_csv=os.path.join( "Resources", "budget_data.csv")

# Results to output
total_months = 0
month_of_change = []
net_change_list = []
ProfitLosses = 0
Greatest_Increase_in_Profits = []
Greatest_Decrease_in_Profits =  []
Average_Change = []


# With open  (udemy_csv, encoding ='utf-8') as csv file
with open (budget_csv, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#Reading the header row
    header = next(csvreader)

    for row in csvreader:
        #Add Date
        if row[0] == Date:
            print(len(row[0]))

  # Track the total number of months
    length = len(Date)
    print(length)

# The net total amount of "profit/Losses" over hte entire period

    ProfitLosses(row[1])
ProfitLosses += int(row[1])
        #print(int(row([1])))
    #print(ProfitLosses)
         
 # The changes in "Profit/Losses" over the entire period, and then the average changes       
changes = ProfitLosses (i+1) - ProfitLosses(i)

def average (changes)
    length = len(changes)
    total = 0.0
    for number in changes:
        total += number
    return total / length

# The greatest increase in profits (date and amount) over the entire period
ProfitLosses = int(row[1])
print(max(ProfitLosses))
       
    
 # The greatest decrease in profits (date and amount) over the entire period
ProfitLosses = int(row[1])
print(max(ProfitLosses))
    
        # Calculate the greatest decrease

# Calculate the Average Net Change

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average  Change: ${net_monthly_avg}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


    Date = str(budget_data[0])
    ProfitLosses = int(budget_data[1])




