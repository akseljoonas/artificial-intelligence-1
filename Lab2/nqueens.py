import sys
import random
import math

MAXQ = 100


def in_conflict(column, row, other_column, other_row):
    """
    Checks if two locations are in conflict with each other.
    :param column: Column of queen 1.
    :param row: Row of queen 1.
    :param other_column: Column of queen 2.
    :param other_row: Row of queen 2.
    :return: True if the queens are in conflict, else False.
    """
    if column == other_column:
        return True  # Same column
    if row == other_row:
        return True  # Same row
    if abs(column - other_column) == abs(row - other_row):
        return True  # Diagonal

    return False


def in_conflict_with_another_queen(row, column, board):
    """
    Checks if the given row and column correspond to a queen that is in conflict with another queen.
    :param row: Row of the queen to be checked.
    :param column: Column of the queen to be checked.
    :param board: Board with all the queens.
    :return: True if the queen is in conflict, else False.
    """
    for other_column, other_row in enumerate(board):
        if in_conflict(column, row, other_column, other_row):
            if row != other_row or column != other_column:
                return True
    return False


def count_conflicts(board):
    """
    Counts the number of queens in conflict with each other.
    :param board: The board with all the queens on it.
    :return: The number of conflicts.
    """
    cnt = 0

    for queen in range(0, len(board)):
        for other_queen in range(queen+1, len(board)):
            if in_conflict(queen, board[queen], other_queen, board[other_queen]):
                cnt += 1

    return cnt


def evaluate_state(board):
    """
    Evaluation function. The maximal number of queens in conflict can be 1 + 2 + 3 + 4 + .. +
    (nquees-1) = (nqueens-1)*nqueens/2. Since we want to do ascending local searches, the evaluation function returns
    (nqueens-1)*nqueens/2 - countConflicts().

    :param board: list/array representation of columns and the row of the queen on that column
    :return: evaluation score
    """
    return (len(board)-1)*len(board)/2 - count_conflicts(board)


def print_board(board):
    """
    Prints the board in a human readable format in the terminal.
    :param board: The board with all the queens.
    """
    print("\n")

    for row in range(len(board)):
        line = ''
        for column in range(len(board)):
            if board[column] == row:
                line += 'Q' if in_conflict_with_another_queen(row, column, board) else 'q'
            else:
                line += '-'
        print(line)


def init_board(nqueens):
    """
    :param nqueens integer for the number of queens on the board
    :returns list/array representation of columns and the row of the queen on that column
    """

    board = []

    for column in range(nqueens):
        board.append(random.randint(0, nqueens-1))

    return board


"""
------------------ Do not change the code above! ------------------
"""


def random_search(board):
    """
    This function is an example and not an efficient solution to the nqueens problem. What it essentially does is flip
    over the board and put all the queens on a random position.
    :param board: list/array representation of columns and the row of the queen on that column
    """

    i = 0
    optimum = (len(board) - 1) * len(board) / 2

    while evaluate_state(board) != optimum:
        i += 1
        print('iteration ' + str(i) + ': evaluation = ' + str(evaluate_state(board)))
        if i == 1000:  # Give up after 1000 tries.
            break

        for column, row in enumerate(board):  # For each column, place the queen in a random row
            board[column] = random.randint(0, len(board)-1)

    if evaluate_state(board) == optimum:
        print('Solved puzzle!')

    print('Final state is:')
    print_board(board)

"""
def find_best_neighbor(board):
 best_board = board.copy()
    new_board = board.copy()
    for i in range(200):
        new_board[random.randint(0, len(board)-1)] = random.randint(0, len(board)-1)
        if evaluate_state(new_board) > evaluate_state(best_board):
                best_board = new_board.copy()
        elif evaluate_state(new_board) == evaluate_state(best_board):
                if random.randint(0, 1) == 1:
                    best_board = new_board.copy()
    return best_board

best_board = board.copy()
    for i in range(200):
        row = random.randint(0, len(board)-1)
        col = random.randint(0, len(board)-1)
        while board[row] == col:
            col = random.randint(0, len(board)-1)
        new_board = board.copy()
        new_board[row] = col
        if evaluate_state(new_board) > evaluate_state(best_board):
            best_board = new_board.copy()
        elif evaluate_state(new_board) == evaluate_state(best_board):
            if random.randint(0, 1) == 1:
                best_board = new_board.copy()
    return best_board

"""
def find_best_neighbor(board):
    best_board = board.copy()
    for i in range(200):
        row = random.randint(0, len(board)-1)
        column = random.randint(0, len(board)-1)
        while board[column] == row:
            row = random.randint(0, len(board)-1)
        new_board = board.copy()
        new_board[column] = row
        if evaluate_state(new_board) > evaluate_state(best_board):
            best_board = new_board.copy()
        elif evaluate_state(new_board) == evaluate_state(best_board):
            if random.randint(0, 1) == 1:
                best_board = new_board.copy()
    return best_board

def hill_climbing(board):
    solved = 0
    for iterations in range(10):
        board = init_board(len(board))
        i = 0
        optimum = (len(board) - 1) * len(board) / 2

        while evaluate_state(board) != optimum:
            i += 1
            #print('iteration ' + str(i) + ': evaluation = ' + str(evaluate_state(board)))
            #print_board(board)
            if i == 1000:  # Give up after 1000 tries.
                break

            best_neighbor = find_best_neighbor(board)
            if evaluate_state(best_neighbor) >= evaluate_state(board):
                board = best_neighbor.copy()

        if evaluate_state(board) == optimum:
            solved += 1
            #print('Solved puzzle!')

        #print('Final state is:')
        #print_board(board)

    print("the puzzle was solved " + str(solved) + " times.")

def time_to_temperature(time):
    return 1000 * pow(0.999, time)

def simulated_annealing(board):
    optimum = (len(board) - 1) * len(board) / 2
    current_board = board.copy()
    T = 1000
    time = 0
    while evaluate_state(board) != optimum:
        time += 1
        #print('iteration ' + str(i) + ': evaluation = ' + str(evaluate_state(board)))
        print('iteration ' + str(time) + ': evaluation = ' + str(evaluate_state(current_board)))
        T = time_to_temperature(time)

        new_board = current_board.copy()
        new_board[random.randint(0, len(board)-1)]= random.randint(0, len(board)-1)
        delta_e = count_conflicts(new_board) - count_conflicts(current_board)

        if T == 0 or time == 100000:
            break

        if delta_e <= 0:
            current_board = new_board.copy()
        else:
            random_chance = random.random()
            p = math.exp(-delta_e / T)
            if random_chance < p:
                current_board = new_board.copy()

        board = current_board.copy()


        if evaluate_state(board) == optimum:
            print('Solved puzzle!')
            break

    print('Final state is:')
    print_board(board)




def genetic_algortihm(board):
    iterations = 0
    optimum = (len(board) - 1) * len(board) / 2

    population  = []
    population_fitness = []
    POPULATION_SIZE = 100
    NEW_GEN_CUT = 0.4
    MUTATION_PROBABILITY = 0.1
    
    for i in range(POPULATION_SIZE):
        temp = init_board(len(board))
        population.append(temp)
        population_fitness.append(get_fitness(temp))


    while evaluate_state(board) != optimum:
        iterations += 1
        print('iteration ' + str(iterations) + ': evaluation = ' + str(evaluate_state(board)))
        if iterations == 1000:  # Give up after 1000 tries.
            break

        # START OF GENETIC
        new_population = []
        new_population_fitness = []
        
        for i in range(POPULATION_SIZE):
            mom = random.choice(population)
            dad = random.choice(population)
            child = reproduce(mom, dad)
            if (random.random() < MUTATION_PROBABILITY):
                child = mutate(child)
            
            new_population.append(child)
            new_population_fitness.append(get_fitness(child))
            
        #map fitness to state and sort it
        
        top10, top10_fitness = [list(a) for a in zip(*sorted(zip(new_population, new_population_fitness), key=lambda pair: pair[1], reverse=True))]

        
        #print(new_population, new_population_fitness)
        
        population = top10[:int(POPULATION_SIZE * NEW_GEN_CUT)]
        
        population_fitness = top10_fitness[:int(POPULATION_SIZE * NEW_GEN_CUT)]

        """for i in range(int(POPULATION_SIZE * NEW_GEN_CUT)):
        if population_fitness[i] == 1.0:
        print('Solved puzzle! BUT DIDNT ASSIGN')"""

        
        board = top10[0]


    if evaluate_state(board) == optimum:
        print('Solved puzzle!')

    print('Final state is:')
    print_board(board)

def get_fitness(board):
    return 1/(1+count_conflicts(board))

def reproduce(x,y): # finish this shit
    cut = random.randint(0, len(x)-1)
    return x[:cut] + y[cut:]


def mutate(child):
    child[random.randint(0, len(child)-1)] = random.randint(0, len(child)-1)
    return child


def main():
    """
    Main function that will parse input and call the appropriate algorithm. You do not need to understand everything
    here!
    """

    try:
        if len(sys.argv) != 2:
            raise ValueError

        n_queens = int(sys.argv[1])
        if n_queens < 1 or n_queens > MAXQ:
            raise ValueError

    except ValueError:
        print('Usage: python n_queens.py NUMBER')
        return False

    print('Which algorithm to use?')
    algorithm = input('1: random, 2: hill-climbing, 3: simulated annealing, 4: genetic algorithm \n')

    try:
        algorithm = int(algorithm)

        if algorithm not in range(1, 5):
            raise ValueError

    except ValueError:
        print('Please input a number in the given range!')
        return False

    board = init_board(n_queens)
    print('Initial board: \n')
    print_board(board)

    if algorithm == 1:
        random_search(board)
    if algorithm == 2:
        hill_climbing(board)
    if algorithm == 3:
        simulated_annealing(board)
    if algorithm == 4:
        genetic_algortihm(board)
        


# This line is the starting point of the program.
if __name__ == "__main__":
    main()
