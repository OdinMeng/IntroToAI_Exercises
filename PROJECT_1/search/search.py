# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from typing import List
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state) -> List:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    stack = util.Stack()
    visited = set()

    s0 = problem.getStartState()
   
    stack.push((s0, [])) # each item in the stack is a pair state-actions where actions is a list of necessary actions to reach said state

    while not stack.isEmpty():
        node, actions = stack.pop()

        if node in visited:
            continue 

        visited.add(node)

        if problem.isGoalState(node):
            return actions # OK
        
        else:
            for child, action, cost in problem.getSuccessors(node):
                if child not in visited:
                    stack.push((child, actions + [action]))

    print("WARNING: SOLUTION NOT FOUND.")
    return [None]

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    visited = set()

    s0 = problem.getStartState()
   
    queue.push((s0, [])) # each item in the stack is a pair state-actions where actions is a list of necessary actions to reach said state

    while not queue.isEmpty():
        node, actions = queue.pop()

        if node in visited:
            continue 

        visited.add(node)

        if problem.isGoalState(node):
            return actions # OK
        
        else:
            for child, action, cost in problem.getSuccessors(node):
                if child not in visited:
                    queue.push((child, actions + [action]))

    print("WARNING: SOLUTION NOT FOUND.")
    return [None]

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    heap = util.PriorityQueue()
    best_cost = dict()

    s0 = problem.getStartState()
    best_cost[s0] = 0
   
    heap.push((s0, [], 0), 0) # each item in the stack is a triple state-actions-cost where actions is a list of necessary actions to reach said state

    while not heap.isEmpty():
        node, actions, cost = heap.pop()
        if problem.isGoalState(node):
            return actions # OK
        
        else:
            for child, action, c_cost in problem.getSuccessors(node):
                new_cost = c_cost + cost 

                if new_cost < best_cost.get(child, float('inf')):
                    heap.update((child, actions + [action], new_cost), new_cost)
                    best_cost[child] = new_cost

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    heap = util.PriorityQueue()
    best_cost = dict()

    s0 = problem.getStartState()
    best_cost[s0] = heuristic(s0, problem)

    heap.update((s0, [], heuristic(s0, problem)), heuristic(s0, problem)) # each item in the stack is a triple state-actions-cost where actions is a list of necessary actions to reach said state

    while not heap.isEmpty():
        node, actions, f_cost = heap.pop()

        if problem.isGoalState(node):
            return actions # OK
        
        else:
            for child, action, c_cost in problem.getSuccessors(node):
                forward = heuristic(child, problem)
                backward = c_cost + best_cost[node]

                # if the backward cost is better then re-evaluate the node, otherwise ignore it (already visited)
                if backward < best_cost.get(child, float('inf')):
                    heap.update((child, actions + [action], forward+backward), forward+backward)
                    best_cost[child] = backward

                else:
                    continue


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
