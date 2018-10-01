# LCA_test.py

import pytest
import LCA

# check printTree works
def test_print_tree(capsys):
    LCA.testTree.print_tree()
    captured = capsys.readouterr()
    assert captured.out == "8\n2\n9\n7\n10\n1\n4\n3\n5\n6\n"

def test_node_exists():
    assert LCA.node_exists(LCA.testTree, 22) == False
    assert LCA.node_exists(LCA.testTree, None) == False
    assert LCA.node_exists(LCA.testTree, 1) == True
    assert LCA.node_exists(LCA.testTree, 6) == True
    assert LCA.node_exists(LCA.testTree, 8) == True
    assert LCA.node_exists(LCA.testTree, 10) == True
    assert LCA.node_exists(LCA.testTree, 4) == True

# test lowest common ancestor with valid values
def test_LCA():
    assert LCA.LCA(LCA.testTree, 8, 9).value == 2
    assert LCA.LCA(LCA.testTree, 10, 3).value == 1
    assert LCA.LCA(LCA.testTree, 5, 6).value == 5
    assert LCA.LCA(LCA.testTree, 1, 6).value == 1
    assert LCA.LCA(LCA.testTree, 9, 6).value == 1
    assert LCA.LCA(LCA.testTree, 4, 6).value == 3

# test lowest common ancestor with non-present values
def test_LCA():
    assert LCA.LCA(LCA.testTree, 10, 16) == -1
    assert LCA.LCA(LCA.testTree, 22, 0) == -1
    assert LCA.LCA(LCA.testTree, 22, 2) == -1

# test various cases with None values
def test_none_LCA():
    assert LCA.LCA(LCA.testTree, None, 1) == -1
    assert LCA.LCA(LCA.testTree, 1, None) == -1
    assert LCA.LCA(LCA.testTree, None, None) == -1

# test various cases with None Node and None values
def test_none_node_LCA():
    test = LCA.Node(None)
    assert LCA.LCA(test, None, None).value == None
    assert LCA.LCA(test, None, 1) == -1
    assert LCA.LCA(test, 1, None) == -1
    assert LCA.LCA(test, 1, 1) == -1
