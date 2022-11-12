import os
import csv

# path to collect data from the Resources folder
election_csv =os.path.join("Resources", 'election_data.csv')

# Results to output
total_votes_cast = 0
list_candidates_with_votes = []
percentage_votes_per_candidate = []
total_votes_per_candidate = []
winner_based_on_vote = []
counter = 0
candidateList = []
votes = 0


# with open (csv, encoding = 'utf -8')  as csv file
with open (election_csv, encoding = 'utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Reading the header row
    header = next(csvreader)

#print the contents of each row
    
    for line in csvreader:
        counter = counter + 1
        candidate = str(line[2])
        votes = str(line[1])
        # Total_ProfitLoss += int(Line[1])
        # changes =  (ProfitLoss - Previous_ProfitLoss)
        # Previous_ProfitLoss = ProfitLoss
        # sum_of_changes += changes
        # if changes > biggest_change:
        #     biggest_change = changes
        # if  changes < smallest_change:
        #     smallest_change = changes

 # Total number of votes cast
    print(f"Total Votes {counter}")

# Candidate List
    print("f{candidate}") 
        
 # Number of votes eacg candidate won       
    print(f"{candidate}, {votes}")

# # The greatest increase in profits (date and amount) over the entire period
#     print(f"Biggest Increase {biggest_change}")

# # The total number of votes cast
# total_votes_cast = len(int(BallotID))
# print(total_votes_cast)


# # Complete list of candidates who received votes
# #Candidate_list = list(Candidate)

# Percentage of votes each candidate won to 3 decimal places
#percent= round(int([2] /int([1]) * 100,3)
#percentage_votes.append(str(percent) + "%"))

#Total number of votes each candodate won


#Winner of the election based on popular votes


# save results to output file
election_results = os.path.join("Election Results")
# Export the electoion results to text file
with open(election_results, "w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Votes : {total_votes_cast}\n")
    txt_file.write(f"TList of candidates who received votes: ${total_votes_per_candidate}\n")
    txt_file.write(f"Percentage of votes per candidate: ${total_votes_per_candidate[0]}) (${candidate_list[1]} \n")
    txt_file.write(f"Total number of votes per candidate: {total_votes_per_candidate[0]}) (${candidate_list[1]}\n")
    txt_file.write(f"Winner: {popular_vote})\n")
