# შესავალი მასივებში/სიებში
team_members = ["John Doe", "Jane Smith", "Michael Johnson", "Sarah Williams", "David Brown",
                "Emily Davis", "Michael Wilson", "Sarah Thompson", "Daniel Lee", "David Johnson"]

team_odds = []
team_evens = []

for i in range(1, len(team_members)):
    if i % 2 == 0:
        team_evens.append(team_members[i-1])
    else:
        team_odds.append(team_members[i-1])

print("Even-length names:", team_evens)

print("Odd-length names:", team_odds)
