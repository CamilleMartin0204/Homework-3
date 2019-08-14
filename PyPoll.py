import os
import csv

poll_data = os.path.join('election_data.csv')
pypolldata = os.path.join('outputpypolldata.txt')

voterid = str(poll_data[0])
county = str(poll_data[1])
candidate = str(poll_data[2])

total_votes = 0
candidate_data = []
candidate_votes = {}
winner = "" 
winner_vote = 0

with open (poll_data, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1
        candidate = row[2]
    if candidate not in candidate_data 
        candidate_data.append(candidate)
        candidate_votes[candidate] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


with open(pypolldata, "w") as txt_file:
            election_results = (
                f"\n\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes}\n"
                f"-------------------------\n")
            print(election_results, end="")
            txt_file.write(election_results)

