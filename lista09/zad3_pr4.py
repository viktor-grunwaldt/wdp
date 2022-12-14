from itertools import combinations, permutations
import random as r


arabia = ("Arabia_Saudyjska", 2, 3, 0.3, 0.3)
argentyna = ("Argentyna", 4, 6, 0.5, 0.8)
meksyk = ("Meksyk", 3, 4, 0.6, 0.5)
polska = ("Polska", 2, 3, 0.9, 0.8)
# (name, def, atk, block, acc)
grupa = [arabia, argentyna, meksyk, polska]


def mecz(team_a, team_b) -> tuple[int, int]:
    rolls_a = (team_a[1] + r.randint(1, 6), team_a[2] + r.randint(1, 6))
    rolls_b = (team_b[1] + r.randint(1, 6), team_b[2] + r.randint(1, 6))

    shot_opportunities_a = max(0, rolls_a[0] - rolls_b[1])
    shot_opportunities_b = max(0, rolls_b[0] - rolls_a[1])
    score_a = sum(1 for _ in range(shot_opportunities_a) if r.uniform(0.0, team_a[4]) > r.uniform(0.0, team_b[3]))
    score_b = sum(1 for _ in range(shot_opportunities_b) if r.uniform(0.0, team_b[4]) > r.uniform(0.0, team_a[3]))

    return (score_a, score_b)


def chance_to_win(team_a, team_b, rolls):
    team_a_wins = lambda x: x[0] > x[1]
    wins = sum(1 for _ in range(rolls) if team_a_wins(mecz(team_a, team_b)))

    return (wins / rolls) * 100


ch = chance_to_win(polska, argentyna, 1000)
print(f"polska ma {ch}% szansy na wygranie meczu")


def rozgrywki_grupowe(teams, write_scores=False):
    n = len(teams)
    scores = [0] * n
    goals_balance = [[0, 0] for _ in range(n)]

    for a, b in combinations(range(n), 2):
        result = mecz(teams[a], teams[b])
        if write_scores:
            print(f"mecz {teams[a][0]} - {teams[b][0]} zakończył się wynikiem {result}")
        goals_balance[a][0] += result[0]
        goals_balance[a][1] += result[1]

        goals_balance[b][0] += result[1]
        goals_balance[b][1] += result[0]

        scores[a] += 1 if result[0] == result[1] else 0 + 2 if result[0] > result[1] else 0
        scores[b] += 1 if result[0] == result[1] else 0 + 2 if result[0] < result[1] else 0

    print(*teams, sep="\n")
    print(scores)


rozgrywki_grupowe(grupa, True)
