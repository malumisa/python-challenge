import os
import csv
budget_csv = os.path.join('Resources', 'budget_data.csv')
with open (budget_csv, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    header = next(csvreader)

    #list used to store budget data variables
    counter_month = []
    profit = []
    current_profit = []
    previous_profit = []
    delta_profit = []
                   
    #looping through budget values and adding to empty lists
    for line in csvreader:
        counter_month.append(line[0])
        profit.append(int(line[1]))
    for i in range(len(profit)-1):
        current_profit = profit[i+1]
        previous_profit = profit[i]
        delta_profit.append(current_profit - previous_profit)

    #looping through to find the greatest increase and greatest decrease from delta profit list
    for x in range(len(delta_profit)-1):
            greatest_increase = max(delta_profit)
            greatest_decrease = min(delta_profit)              

# getting the greatest increase month and greatest decrease month using the index and max and min functions
greatest_increase_month = delta_profit.index(max(delta_profit))+1
greatest_decrease_month= delta_profit.index(min(delta_profit))+1

print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(counter_month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(delta_profit)/len(delta_profit),2)}")
print(f"Greatest Increase in Profits: {counter_month[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {counter_month[greatest_decrease_month]} (${(str(greatest_decrease))})")      

output = os.path.join(".", 'Financial Analysis.txt')
#  Export the results to text file
with open(output, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Months: {len(counter_month)}\n")
    txt_file.write(f"Total: ${sum(profit)}\n")
    txt_file.write(f"Average  Change: ${round(sum(delta_profit)/len(delta_profit),2)}\n")
    txt_file.write(f"Greatest Increase in Profits: {counter_month[greatest_increase_month]} (${(str(greatest_increase))})\n")
    txt_file.write(f"Greatest Decrease in Profits: {counter_month[greatest_decrease_month]} (${(str(greatest_decrease))})\n")

   