import sys


def max_value(state, t_table):
    max = -100000000000

    if state == 1:
        return -1

    for move in range(1, 4):
        if state-move > 0:
            if t_table[state][0] == -1:
                m = -1
            elif t_table[state][0] == 1:
                m = 1
            elif t_table[state][0] == None:
                m = min_value(state-move, t_table)
                t_table[state][1] = m
            max = m if m > max else max

    return max


def min_value(state, t_table):
    min = 10000000000000
    
    if state == 1:
        return 1

    for move in range(1, 4):
        if state-move > 0:
            if t_table[state][1] == -1:
                m = -1
            elif t_table[state][1] == 1:
                m = 1
            elif t_table[state][1] == None:
                m = max_value(state-move, t_table)
                t_table[state][0] = m
            min = m if m < min else min

    return min



def minimax_decision(state, turn):
    best_move = None

    if turn == 0:  # MAX' turn
        max = -100000000000

        for move in range(1, 4):
            if state - move > 0:
                m = min_value(state - move)
                if m > max:
                    max = m
                    best_move = move

    else:
        min = 10000000000000

        for move in range(1, 4):
            if state - move > 0:
                m = max_value(state-move)
                if m < min:
                    min = m
                    best_move = move

    return best_move

def negamax_decision(state, turn, t_table):
    best_move = None

    if turn == 0:  # MAX' turn
        max = -100000000000

        for move in range(1, 4):
            if state - move > 0:
                m = min_value(state - move, t_table)
                if m > max:
                    max = m
                    best_move = move

    else:
        min = 10000000000000

        for move in range(1, 4):
            if state - move > 0:
                m = max_value(state-move, t_table)
                if m < min:
                    min = m
                    best_move = move

    return best_move, m

def play_nim(state):
    t_table = [[None for x in range(2)] for y in range(state)]
    turn = 0
    wadeva = state
    while state != 1:
        move, valuation = negamax_decision(state, turn, t_table)

        print(str(state) + ": " + ("MAX" if not turn else "MIN") + " takes " + str(move) + " valuation " + str(valuation))

        state -= move
        turn = 1 - turn

    print("1: " + ("MAX" if not turn else "MIN") + " looses")
    for i in range(1, wadeva):
        print(str(i) + " matches, Max turn: " + str(t_table[i][0]))
        print(str(i) + " matches, Min Turn: " + str(t_table[i][1]))


def main():
    """
    Main function that will parse input and call the appropriate algorithm. You do not need to understand everything
    here!
    """

    try:
        if len(sys.argv) != 2:
            raise ValueError

        state = int(sys.argv[1])
        if state < 1 or state > 100:
            raise ValueError

        play_nim(state)

    except ValueError:
        print('Usage: python nim.py NUMBER')
        return False


if __name__ == '__main__':
    main()
