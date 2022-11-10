import os
import csv

# path to collect data from the Resources folder
election_csv =os.path.join('..', 'Resources', 'election_data.csv')

# Results to output
total_votes_cast = 0
list_candidates_with_votes = []
percentage_votes_per_candidate = []
total_votes_per_candidate = []
winner_based_on_vote = []


# with open (csv, encoding = 'utf -8')  as csv file
with open (election_csv, encoding = 'utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Reading the header row
header = next(csvreader)

for row in csvreader:
    if row[0] == BallotID:

def print_election(election_data):
    BallotID = int(election_data [0])
    County = str(election_data [1])
    Candidate = str(election_data [2])

# The total number of votes cast
Total_votes_cast = len(BallotID)

# Complete list of candidates who received votes
Candidate_list = list(Candidate)

# Percentage of votes each candidate won to 3 decimal places
percent= round(int([2] /int([1]) * 100,3)
percentage_votes.append(str(percent) + "%"))

#Total number of votes each candodate won


#Winner of the election based on popular votes


# Export the electoion results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total number of votes cast : {}\n")
    txt_file.write(f"TList of candidates hwo received votes: ${}\n")
    txt_file.write(f"Percentage of votes per candidate: ${total_votes_per_candidate[0]}) (${candidate_list[1]} \n")
    txt_file.write(f"Total number of votes per candidate: {total_votes_per_candidate[0]}) (${candidate_list[1]}\n")
    txt_file.write(f"Winner: {popular_vote})\n")
