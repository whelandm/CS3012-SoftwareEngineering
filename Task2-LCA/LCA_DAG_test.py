# LCA_DAG_test.py

import pytest
import LCA_DAG

## coverage py.test --cov lca_dag.py test

# check BFS works
def test_BFS():
    result = LCA_DAG.BFS(LCA_DAG.testDAG, 1, 9)
    assert list(result) == [[1, 3, 9]]
    result = LCA_DAG.BFS(LCA_DAG.testDAG, 1, 8)
    assert list(result) == [[1, 2, 8]]
    result = LCA_DAG.BFS(LCA_DAG.testDAG, 4, 8)
    assert list(result) == [[4, 8],[4,5,6,8]]

# check shortest path works
def test_shortest_path():
    result = LCA_DAG.shortest_path(LCA_DAG.testDAG, 1, 9)
    assert list(result) == [1, 3, 9]
    result = LCA_DAG.shortest_path(LCA_DAG.testDAG, 1, 20)
    assert result == None
    result = LCA_DAG.shortest_path(LCA_DAG.testDAG, 4, 8)
    assert list(result) == [4, 8]

def test_greatest_depth():
    result = LCA_DAG.greatest_depth(LCA_DAG.testDAG, 1, 9)
    assert result == 3
    result = LCA_DAG.greatest_depth(LCA_DAG.testDAG, 4, 8)
    assert result == 4

# check common ancestors works
def test_common_ancestors():
    result = LCA_DAG.find_common_ancestors([[1, 2, 3]], [[0, 3, 6]])
    assert result == [3]
    result = LCA_DAG.find_common_ancestors([[1, 2, 3, 6]], [[0, 3, 6]])
    assert result == [3, 6]
    result = LCA_DAG.find_common_ancestors([[1, 2, 4]], [[0, 3, 6]])
    assert result == []

def test_lca():
    result = LCA_DAG.LCA(LCA_DAG.testDAG, 4, 6, 9)
    assert result == 5
