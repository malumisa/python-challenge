import os
import csv

# path to collect data from the Resources folder
election_csv =os.path.join("Resources", 'election_data.csv')

# with open (csv, encoding = 'utf -8')  as csv file
with open (election_csv, encoding = 'utf') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
# Reading the header row
    header = next(csv_reader)

#Calculating the Total number of votes cast
    election_data = list(csv_reader)
    total_vote = len(election_data)

print("Election Results")
print("--------------------------------------")

print(f"The total number of votes cast is {total_vote}")
print("--------------------------------------")

# Calculating the total number of votes won per candidate. 
candidates = []
for row in election_data:
        if row[2] not in candidates:
            candidates.append(row[2])

votes = {}
for name in candidates:
        votes[name]=0
    
for name in candidates:
        for row in election_data:
            if row[2]==name:
                votes[name]=votes[name]+1

percentage_votes={}
for name in votes:
        percentage_votes[name]= votes[name]/total_vote*100


for x in votes:
        print(x + ":   " +str(round(percentage_votes[x],2)) + "%  "+ "("+str(votes[x])+")")

# Getting the winning candidate   
winner = ""
max_vote=0
for name in votes:
        if votes[name]>max_vote:
            winner=name
            max_vote=votes[name]
    
print("--------------------------------------")
print("Winner: " +winner)
print("--------------------------------------")

 # Exporting data to a text file
electionfile = open("Election Results.txt","w")
electionfile.write("Elections Results\n")
electionfile.writelines("--------------------------------------\n")
electionfile.writelines("The total number of votes is "+ str(total_vote))
electionfile.write(" \n")
electionfile.writelines("--------------------------------------")
electionfile.write(" \n")

for x in votes:
        electionfile.writelines([x + ":   " +str(round(percentage_votes[x],2)) + "%  "+ "("+str(votes[x])+")\n"])     

electionfile.writelines("--------------------------------------\n")
electionfile.writelines("Winner:  " + (winner))    
electionfile.write(" \n")
electionfile.writelines("--------------------------------------\n")
electionfile.close() 



