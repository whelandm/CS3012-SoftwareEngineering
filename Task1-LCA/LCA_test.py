# LCA_test.py

import pytest
import LCA

# check printTree works
def test_print_tree(capsys):
    LCA.testTree.print_tree()
    captured = capsys.readouterr()
    assert captured.out == "8\n2\n9\n7\n10\n1\n4\n3\n5\n6\n"

# test lowest common ancestor
def test_LCA():
    assert LCA.LCA(LCA.testTree, 8, 9).value == 2
    assert LCA.LCA(LCA.testTree, 10, 3).value == 1
    assert LCA.LCA(LCA.testTree, 5, 6).value == 5
    assert LCA.LCA(LCA.testTree, 1, 6).value == 1
    assert LCA.LCA(LCA.testTree, 9, 6).value == 1
    assert LCA.LCA(LCA.testTree, 4, 6).value == 3

# test various cases with None Values
def test_none_LCA():
    assert LCA.LCA(LCA.testTree, None, 1).value == 1
    assert LCA.LCA(LCA.testTree, 1, None).value == 1
    assert LCA.LCA(LCA.testTree, None, None) == None

# test various cases with None Node
def test_none_node_LCA():
    test = LCA.Node(None)
    assert LCA.LCA(test, None, None).value == None
    assert LCA.LCA(test, None, 1).value == None
    assert LCA.LCA(test, 1, None).value == None
    assert LCA.LCA(test, 1, 1) == None
