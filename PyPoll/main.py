import os
import csv

file_num = 1
# path to collect data from the Resources folder
election_csv =os.path.join("Resources", 'election_data.csv')

# Lists to store data
poll = {}
total_votes = 0
total_votes_cast = 0
percent_count = []
#candidates = list(df_ed["candidate"]. unique())
elections = []
percentage_votes_per_candidate = []
total_votes_per_candidate = []
winner_based_on_vote = []
counter = 0


# with open (csv, encoding = 'utf -8')  as csv file
with open (election_csv, encoding = 'utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    

# Reading the header row
    header = next(csvreader)

#print the contents of each row
   
    for line in csvreader:
        counter = counter + 1
        total_votes += 1
        if line[2] in poll.keys():
            poll[line[2]] = poll[line[2]]+1
        else:
            poll[line[2]] = 1

candidates = []
num_votes = []

for key, value in poll.items():
        candidates.append(key)
        num_votes.append(value)

vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 3)) 

clean_data = list(zip(candidates, vote_percent, num_votes))
for i in range(0, len(clean_data)): 
     print(*clean_data[i])

winner_list = []


for name in clean_data:
    if max(vote_percent) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]
   

 # Total number of votes cast
    #print(f"Total Votes {counter}")




# Percentage of votes each candidate won to 3 decimal places
#percent= round(int([2] /int([1]) * 100,3)
#percentage_votes.append(str(percent) + "%"))

#Total number of votes each candodate won


#Winner of the election based on popular votes


#  save results to output file
election_results = os.path.join("Election Results")
#  Export the electoion results to text file
with open(election_results, "w") as txt_file:
     txt_file.write(f"Election Results\n")
     txt_file.write(f"----------------------------\n")
     txt_file.write(f"Total Votes : {counter}\n")
     txt_file.write(f"{(clean_data[0])}\n")
     txt_file.write(f"{clean_data[1]} + \n")
     txt_file.write(f"{clean_data[2]}\n")
     txt_file.write(f"----------------------------\n")
     txt_file.write(f"Winner: {winner})\n")
     txt_file.write(f"----------------------------\n")
