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

#Directed Acyclic Graph
class DAG:
    #Init
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    #Add edge to graph
    def add_Edge(self,edge,vertices,weight):
        self.graph[edge].append((vertices,weight))

#Lowest Common Ancestor - find lowest common ancester of x and y
