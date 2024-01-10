import csv

#election_data = '/Users/alphamalenailcareservices/Desktop/Data Bootcamp/Python/Starter_Code_3/PyPoll/Resources/election_data.csv'
election_data = 'Resources/election_data.csv'
analysis_poll_path = 'analysis/pypoll.txt'

total_votes = 0
candidates = set()
candidate_votes = {}

with open (election_data, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    csv_header =  next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        candidates.add(candidate)
        candidate_votes[candidate] = candidate_votes.get( candidate,0)+ 1

candidate_percentages = {c: (votes/total_votes) * 100 for c,votes in candidate_votes.items()}
# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open (analysis_poll_path,"w") as pypoll_txt:
    pypoll_txt.write("Election Results\n")
    pypoll_txt.write("-------------------------\n")
    pypoll_txt.write(f"Total Votes: {total_votes}\n")
    pypoll_txt.write("-------------------------\n")
    for candidate in candidates:
        pypoll_txt.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    pypoll_txt.write("-------------------------\n")
    pypoll_txt.write(f"Winner: {winner}\n")
    pypoll_txt.write("-------------------------\n")
