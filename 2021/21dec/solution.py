import sys

from functools import cache

player1_pos = int(sys.stdin.readline().split("position: ")[1]) - 1
player2_pos = int(sys.stdin.readline().split("position: ")[1]) - 1

die100 = (x % 100 + 1 for x in range(999999))

def play_part1(player_state, opp_state, num_rolls):
    (player_pos, player_score) = player_state

    # move and score
    new_pos = (player_pos + next(die100) + next(die100) + next(die100)) % 10 
    new_score = player_score + new_pos + 1
    num_rolls += 3

    # check if winner
    if new_score >= 1000:
        return ((new_pos, new_score), opp_state, num_rolls)
    else:
        return play_part1(opp_state, (new_pos, new_score), num_rolls)

(_, (_, loser_score), num_rolls) = play_part1((player1_pos, 0), (player2_pos, 0), 0)
print("part1", num_rolls * loser_score)

@cache
def play_part2(player_state, opp_state):
    (player_pos, player_score) = player_state

    player_wins = 0
    opp_wins = 0
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                # move and score
                new_pos = (player_pos + d1 + d2 + d3) % 10
                new_score = player_score + new_pos + 1

                # check if winner
                if new_score >= 21:
                    player_wins += 1
                else:
                    (d_owins, d_pwins) = play_part2(opp_state, (new_pos, new_score))
                    opp_wins += d_owins
                    player_wins += d_pwins
    
    return (player_wins, opp_wins)

print("part2", max(play_part2((player1_pos, 0), (player2_pos, 0))))