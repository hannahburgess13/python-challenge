import os
import csv

# create path for election data
election_csv = os.path.join('PyPoll','Resources', 'election_data.csv')


# Read csv file
with open( election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    data = list(csvreader)

    # total votes
    total_votes = len(data)

    # total votes for each candidate
    candidates_votes = {}
    for row in data:
        candidate = row[2]
        if candidate in candidates_votes:
            candidates_votes[candidate]["votes"] += 1
        else:
            candidates_votes[candidate] = {"votes": 1}

# percentage of total votes
for candidate in candidates_votes:
    votes = candidates_votes[candidate]["votes"]
    percentage = (votes/total_votes) * 100
    candidates_votes[candidate]["percentage"] = round(percentage, 3)

# winner
new_votes_dict = candidates_votes
max_candidate = []
max_vote = 0
for candidate, new_votes_dict in new_votes_dict.items():
    for votes in new_votes_dict.items():
        if votes[1] > max_vote:
            max_vote = votes[1]
            max_candidate = [candidate, votes[1]]

# analysis text
outcome = f"""
Election Results\n
-------------------------\n
Total Votes: {total_votes}\n
-------------------------\n
"""

for candidate in candidates_votes:
        votes = candidates_votes[candidate]["votes"]
        percentage = candidates_votes[candidate]["percentage"]
        outcome += f'{candidate}: {percentage}%  ({votes})\n \n'

outcome += f"""
-------------------------\n
Winner: {max_candidate[0]}\n
-------------------------\n
"""
print(outcome)

# output analysis
output_path = os.path.join('PyPoll',"analysis", "analysis.txt")

# export analysis
with open(output_path, 'w') as txtfile:
    txtfile.write(outcome)

print("Analysis results have been saved to analysis.txt.")