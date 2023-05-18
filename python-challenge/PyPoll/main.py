import os
import csv

csvpath = os.path.join('/Users/jackielarios/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

with open(csvpath, 'r') as electionfile:
    csvreader = csv.reader(electionfile)
    # Read & skip header
    header = next(csvreader)
    # Read remaining data
    data = list(csvreader)

    # Calculate total number of votes cast
    total_votescast = len(data)

def get_voted_candidates(data):
    candidates = set()

    for line in data:
        _, _, candidate = line
        candidates.add(candidate)
#sort in alphabetical order
    return sorted(list(candidates))  

# get voted candidates
voted_candidates = get_voted_candidates(data)

# count votes for candidates
vote_counts = {}

for candidate in voted_candidates:
    vote_counts[candidate] = 0

for line in data:
    _, _, candidate = line
    vote_counts[candidate] += 1

# define output file
output_folder = '/Users/jackielarios/Desktop/python-challenge/PyPoll/Analysis'  
output_file = os.path.join(output_folder, 'election_results.txt')

# open the output file in write mode
with open(output_file, 'w') as outfile:
    # write results to file
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votescast}\n")
    outfile.write("-------------------------\n")
    outfile.write("Candidates who received votes:\n")
    for candidate, votes in vote_counts.items():
        percentage = (votes / total_votescast) * 100
        outfile.write(f"{candidate}: {votes} ({percentage:.3f}%)\n")
    outfile.write("-------------------------\n")
    winner = max(vote_counts, key=vote_counts.get)
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")

# print
with open(output_file, 'r') as outfile:
    for line in outfile:
        print(line.strip())

print("Results written in Analysis folder:", output_file)
