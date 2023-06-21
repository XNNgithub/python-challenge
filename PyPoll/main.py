# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

#import modules
import os
import csv

# path to collect data from resources folder
election_data_csv=os.path.join('/Users/hchen/Desktop/python-challenge/PyPoll/','Resource','election_data.csv')

# Lists to store data
candidates=[]
total_votes=0
candidate_votes={}
winner_count = 0
winner = str()
vote_percentage = []
vote_list = []

# open and read csv
with open(election_data_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

# read/skip the header row first
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")

# read through each row
    for row in csvreader:
        candidate=row[2]

#find out the unique candidates
        if candidate not in candidates:
            candidates.append((row[2]))
            candidate_votes[candidate]=0
        candidate_votes[candidate]=candidate_votes[candidate]+1

# The total number of votes cast
        total_votes=total_votes+1

# find out the winning candidate
for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage.append((candidate_votes[candidate])/(total_votes)*100)
        vote_list.append(votes)
        if votes > winner_count:
            winner_count = votes
            winner = candidate
vote_percentage = [ round(i, 3) for i in vote_percentage ]
print(vote_list)

# print the final results
print("Election results")
print("----------------------------------")
print("Total votes: " + str(total_votes))
print("----------------------------------")
for p1,p2,p3 in zip(candidate_votes, vote_percentage, vote_list):
     print(f"{p1} {p2}% ({p3})")
print("-----------------------------------")  
print("winner: " + winner)

#Export a text file with the results
with open('PyPoll.txt', 'w') as file:
        file.write('Election results\n')
        file.write('--------------------\n')
        file.write("Total votes: " + str(total_votes)+"\n")
        file.write("---------------------\n")
        #file.write(f"{candidate_votes}: {vote_percentage}%"+"\n")
        for p1,p2,p3 in zip(candidate_votes, vote_percentage, vote_list):
            file.write(f"{p1} {p2}% ({p3})" "\n")
        file.write("---------------------\n")
        file.write("winner: " + winner)
        