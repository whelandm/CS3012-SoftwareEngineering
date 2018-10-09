# LCA_DAG.py

from collections import defaultdict #unordered lists

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
def LCA_DAG:


#Create DAG for testing
dag = DAG()
