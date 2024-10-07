import collections


class Graph(object):
    def __init__(self, k, edges):
        self.k = k
        self.edges = edges
        self.source_nodes = set(i for [i, _] in edges)

    def has_loops(self):
        self.grey_nodes = set(self.source_nodes)
        for n in self.grey_nodes:
            if self.has_loop_from(n):
                return True
            
    def has_loop_from(self, node):
        self.visited = [False] * self.k
        self.stack = []
        self.visited[node] = True

        for [i, j] in self.edges:
            if self.visited

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        if (not self.validConditions(rowConditions, k) or 
            not self.validConditions(colConditions, k)):
            return []

    def validConditions(self, conditions, k):
        # Condtions are invalid if it contains any value greater than k
        # Condtions are invalid if it contains any value less than 1
        for [i, j] in conditions:
            if i == j:
                return False
            if i > k or j > k:
                return False
            if i < 1 or j < 1:
                return False
        # Conditions are invalid if they form a loop.
        # Treat conditions as a directed graph.  Check the DAG for loops.
        # Fail if loop.
        graph = Graph(k, conditions)
        if graph.has_loops():
            return False
        return True


"""
Each pair (i, j) is a directed edge in a graph.
Organize the pairs, and then follow the graph.
If you reach a node with no outgoing edges, then you have a loop.  

Is it possible to have an invalid condition even if it is not invalid by looking
at just one of the constraints?  I don't think so.  I think you can do these
independently.



"""
