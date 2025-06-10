# Read the number of candidates
N = int(input())
# Read the votes for each candidate in order
votes = [int(input()) for _ in range(N)]
# Find the maximum votes received
max_votes = max(votes)
# Check how many candidates have the max votes
max_count = votes.count(max_votes)
# If Carlos (first candidate) has the most votes and no tie, he is elected
if votes[0] == max_votes:
    print('S')
# Otherwise, he is not elected
else:
    print('N')