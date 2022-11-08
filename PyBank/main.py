# import os and csv
import os
import csv

# path to collect data from the Resources folder
budgdet_csv=os.path.join("..", "Resources", "budget_data.csv")

#List to store data
Date = []
ProfitLosses =[]


# With open  (udemy_csv, encoding ='utf-8') as csv file
with open (budgdet_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print(row) 


        #Add Date
        Date.append(row[0])

        # Add profit/Losses
        ProfitLosses.append(row[1])




#Calculating the net total amount of "Profit/Losses" over the entire period
Total = sum(int(ProfitLoss))

#Determining the changes in "Profit/Losses" over th entire period
#x = [1, 3, 5, 8]
#for i in range(1, len(x)):
    #print(x[i] - x[i-1])


# The greatest increase in profits (date and amount) over the entire period



# The greatest decrease in profits (date and amount) over the entire period