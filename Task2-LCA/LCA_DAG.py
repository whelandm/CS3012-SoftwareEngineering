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

#Lowest Common Ancestor - find lowest common ancester of x and y in graph g
def LCA(g, root, x, y):
    x_ancestors = BFS(g, r, x)
    y_ancestors = BFS(g, r, y)
    queue = []
    for x in x_ancestors:
        for next in y_ancestors:
            if next == x:
                    queue.append(x)
    lca = greatest_depth()
    return lca
