def main():
    with open('./input.txt', 'r') as f:
        ll = f.read().split('\n')
    # print(ll)
    total_score = 0
    for l in ll:
        op, my = l.split(' ')
        # print(op, my)
        score = decide_score(op, my)
        # print(score)
        hand_score = decide_hand_score(my)
        # print(hand_score)
        round_score = score + hand_score
        # print(round_score)
        total_score += round_score
    print(total_score)

    part_two_result = decide_adjusted_points(ll)
    print(part_two_result)
    return 0

def decide_adjusted_points(rounds):
    adjusted_points = {
        "A X": 0 + 3,
        "A Y": 3 + 1,
        "A Z": 6 + 2,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 0 + 2,
        "C Y": 3 + 3,
        "C Z": 6 + 1,
    }

    scores = [adjusted_points[round] for round in rounds]
    return sum(scores)

def decide_hand_score(my):
    if my == 'X': # rock
            return 1
    elif my == 'Y': # paper
        return 2
    else: # scissors
        return 3

def decide_score(op, my):
    if op == 'A': # rock
        if my == 'X': # draw
            return 3
        elif my == 'Y': # won
            return 6
        else: # lost
            return 0
    elif op == 'B': # paper
        if my == 'X': # lost
            return 0
        elif my == 'Y': # draw
            return 3
        else: # won
            return 6
    elif op == 'C': # scissors
        if my == 'X': # won
            return 6
        elif my == 'Y': # lost
            return 0
        else: # draw
            return 3
    else:
        raise Exception('unknown symbol')

if __name__ == "__main__":
    main()