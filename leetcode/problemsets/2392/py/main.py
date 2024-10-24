import collections
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set

@dataclass
class GraphNode:
    id: int
    child_idxs: Set[int] = field(default_factory=set)
    parent_idxs: Set[int] = field(default_factory=set)

@dataclass
class Graph:
    k: int
    idx_to_node: Dict[int, GraphNode]
    # Maintain a collection of nodes with no parents – for topological sort.
    idx_no_parent: Set[int]

DEBUG = False
def dbprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def build_graph(k: int, edges: List[List[int]]) -> Graph:
    idx_to_node = {}
    for i in range(1,k+1):
        idx_to_node[i] = GraphNode(i)
    for [before_idx, after_idx] in edges:
        # after node is a child of before node
        idx_to_node[before_idx].child_idxs.add(after_idx)
        # before node is a parent of after node
        idx_to_node[after_idx].parent_idxs.add(before_idx)
    idx_no_parent = set([n.id for n in idx_to_node.values() if not n.parent_idxs])
    return Graph(k, idx_to_node, idx_no_parent)
    
def remove_node(node_idx: int, graph: Graph) -> Optional[GraphNode]:
    if node_idx not in graph.idx_to_node:
        return None
    n = graph.idx_to_node.pop(node_idx)
    # All this node's parents need to remove a child.
    for p_idx in n.parent_idxs:
        p = graph.idx_to_node[p_idx]
        p.child_idxs.remove(node_idx)
    # All this node's children need to remove a parent.
    # This may orphan some children.
    for c_idx in n.child_idxs:
        c = graph.idx_to_node[c_idx]
        c.parent_idxs.remove(node_idx)
        if not c.parent_idxs:
            graph.idx_no_parent.add(c_idx)
    # If this node was in the no-parent set, remove it.
    graph.idx_no_parent.discard(node_idx)
    return n


def valid_order(graph: Graph) -> Optional[List[int]]:
    # Collect the set of nodes that have no parents.
    # Remove these from the graph, in any order.
    # If we end up with a cycle, return None.
    #
    # Destroys graph
    ordered_idxs = []
    while graph.idx_no_parent:
        # Necessary to prevent modifying the set while iterating.
        copy_idx_no_parent = list(graph.idx_no_parent)
        for idx in copy_idx_no_parent:
            dbprint(f"Removing node {idx}")
            n = remove_node(idx, graph)
            ordered_idxs.append(n.id)
    # If there are still elements in the graph, then there is a cycle.
    if graph.idx_to_node:
        return None
    return ordered_idxs

def build_matrix(row_order: List[int], col_order: List[int]) -> List[List[int]]:
    k = len(row_order)
    val_to_row = {v: i for (i, v) in enumerate(row_order)}
    val_to_col = {v: i for (i, v) in enumerate(col_order)}
    matrix = [[0 for _ in range(k)] for _ in range(k)]
    dbprint(matrix)
    for i in range(1, k+1):
        matrix[val_to_row[i]][val_to_col[i]] = i
    return matrix


class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        row_graph = build_graph(k, rowConditions)
        row_order = valid_order(row_graph)
        if row_order is None:
            return []
        col_graph = build_graph(k, colConditions)
        col_order = valid_order(col_graph)
        if col_order is None:
            return []
        matrix = build_matrix(row_order, col_order)
        return matrix



"""
Each pair (i, j) is a directed edge in a graph.
Organize the pairs, and then follow the graph.
If you reach a node with no outgoing edges, then you have a loop.  

Is it possible to have an invalid condition even if it is not invalid by looking
at just one of the constraints?  I don't think so.  I think you can do these
independently.



"""
