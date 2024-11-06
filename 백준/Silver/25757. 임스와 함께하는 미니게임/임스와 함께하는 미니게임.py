import sys
input = sys.stdin.readline

N, game = input().split()
games = {'Y': 1, 'F': 2, 'O': 3}
players = set()


for _ in range(int(N)):
    players.add(input().strip())

print(len(players) // games[game])
