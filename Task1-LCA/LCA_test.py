# LCA_test.py

import pytest
import LCA

# check printTree works
def test_print_tree(capsys):
    LCA.testTree.print_tree()
    captured = capsys.readouterr()
    assert captured.out == "8\n2\n9\n7\n10\n1\n4\n3\n5\n6\n"
