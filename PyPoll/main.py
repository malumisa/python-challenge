import os
import csv

election_csv =os.path.join("..", "Resources", "election_data.csv")

#Lists to store
BallotID = []
County = []
Candidate = []


# with open (udemy_scv, encoding= 'utf-8') as csvfile:
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add BallotID
        BallotID.append(row[0])

        #Add County
        County.append(row[1])

        #Add Candidate
        Candidate.append(row[2])

# The total number of votes cast


# Complete list of candidates who received votes


# Percentage of votes each candidate won to 3 decimal places
percent= round(int(row[2] /int(row[1]) * 100,3)
percentage_votes.append(str(percent) + "%"))



#Total number of votes each candodate won


#Winner of the election based on popular votes



