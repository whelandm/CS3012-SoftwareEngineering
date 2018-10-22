# LCA_DAG.py

from collections import defaultdict #unordered lists

# Graph for Testing
testDAG = {     1 : set([2, 3]),
                2 : set([8]),
                3 : set([9]),
                4 : set([5, 8, 9]),
                5 : set([6, 7]),
                6 : set([8]),
                7 : set([9]),
                8 : set([]),
                9 : set([])        }

#Breath-First Search - return all ancestors of x from graph g
def BFS(g, root, x):
    queue = [(root, [root])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in g[vertex] - set(path):
            if next == x:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

#Shortest Path - find shortest path using BFS, else if no path return None
def shortest_path(g, root, x):
    try:
        return next(BFS(g, root, x))
    except StopIteration:
        return None

#Find Depth
def greatest_depth(g, root, x):
    paths = BFS(g, root, x)
    depth = -1
    for next in paths:
        if len(next) > depth:
            depth = len(next)
    return depth

#find the common ancestors of two lists
def find_common_ancestors(x, y):
    ca = []
    for i in x:
        for j in y:
            if j == i:
                    ca.append(j)
    if ca == []:
        return None
    return ca

#Lowest Common Ancestor - find lowest common ancester of x and y in graph g
def LCA(g, root, x, y):
    x_ancestors = BFS(g, root, x)
    y_ancestors = BFS(g, root, y)
    common_ancestors = find_common_ancestors(x_ancestors, y_ancestors)
    return lca
