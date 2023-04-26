#!/usr/bin/env python3
from fringe import Fringe
from state import State

def recursive_dls(state, maze, limit):
    lxl


def depth_limited_search(state, maze, depth):
    return recursive_dls(state, maze, depth)

def iterative_deepening_search(fr, state, maze):
    
    for d in range(1, 10000):
        result = depth_limited_search(state, maze, d)
        if result is not -1:
            return result
    
def solve_maze_general(maze, algorithm):
    """
    Finds a path in a given maze with the given algorithm
    :param maze: The maze to solve
    :param algorithm: The desired algorithm to use
    :return: True if solution is found, False otherwise
    """
    # select the right fringe for each algorithm
    if algorithm == "BFS":
        fr = Fringe("FIFO")
    elif algorithm == "DFS" or algorithm == "IDS":
        fr = Fringe("STACK")
    elif algorithm == "UCS" or algorithm == "GREEDY" or algorithm == "ASTAR":
        fr = Fringe("PRIORITY")
    else:
        print("Algorithm not found/implemented, exit")
        return

    # get the start room, create state with start room and None as parent and put it in fringe
    room = maze.get_room(*maze.get_start())
    state = State(room, None)
    fr.push(state)
    visited = [room]

    if algorithm == "IDS":
        room = iterative_deepening_search(fr, state, maze)
        
        if room.is_goal():
            # if room is the goal, print that with the statistics and the path and return
            print("solved")
            fr.print_stats()
            state.print_path()
            state.print_actions()
            print()  # print newline
            maze.print_maze_with_path(state)
            return True
        
            
    while not fr.is_empty():

        # get item from fringe and get the room from that state
        state = fr.pop()
        room = state.get_room()

        
        if room.is_goal():
            # if room is the goal, print that with the statistics and the path and return
            print("solved")
            fr.print_stats()
            state.print_path()
            state.print_actions()
            print()  # print newline
            maze.print_maze_with_path(state)
            return True
        
        visited.append(room)  
        for d in room.get_connections():
            new_room, cost = room.make_move(d, state.get_cost())    # Get new room after move and cost to get there
            
            # loop through every possible move
            if algorithm == "GREEDY":
                new_state = State(new_room, state, cost, priority = new_room.get_heuristic_value())               # Create new state with new room and old room
            elif algorithm == "ASTAR":
                new_state = State(new_room, state, cost, priority = cost + new_room.get_heuristic_value())               # Create new state with new room and old room
            else:
                new_state = State(new_room, state, cost, priority = cost)               # Create new state with new room and old room
            
            if new_room not in visited: #and new_state not in fr:
                fr.push(new_state)
                                                      # push the new state
                                             # add new state to visited

    print("not solved")     # fringe is empty and goal is not found, so maze is not solved
    fr.print_stats()        # print the statistics of the fringe
    return False


# all_visited_rooms = [], visited = False, number = 1
    
    