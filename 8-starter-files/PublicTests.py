import unittest
from solution import is_tree

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass


    def test1(self):
        """
        This is a linked-list-esque structure, which is a tree
        """
        assert is_tree(5, (e for e in [(0,1), (1,2), (2,3), (3, 4)])) == True
        n = int(1e4)
        assert is_tree(n, ((i, i + 1) for i in range(n-1))) == True

    def test2(self):
        """
        This is C_5 -- the cycle graph with 5 vertices.
        Trees do not have cycles; this is not a tree.
        """
        assert is_tree(5, (e for e in [(0,1), (1,2), (2,3), (3, 4), (0,4)])) == False
        assert is_tree(2, (e for e in [(0,1), (1,0)])) == False
        assert is_tree(3, (e for e in [(0,0), (1,2), (2, 1)])) == False
        assert is_tree(1, (e for e in [(0,0)])) == True
        assert is_tree(4, (e for e in [(0,0), (1,1), (2,2), (3,3)])) == False
        assert is_tree(6, (e for e in [(3,3), (2,2), (1,0), (1,2), (2,3), (2,4), (2,5),(3,5)])) == False
        assert is_tree(4, (e for e in [(0,0), (0,1), (1,2), (2,3)])) == True
        assert is_tree(4, (e for e in [(0,1), (2,3), (0,2)])) == True




    def test3(self):
        """
        The empty graph is a tree.
        Proof: Let G(V,E) denote the empty graph.
        For all u, v in V, u is reachable from v.
        Thus G is connected.
        Note that E is the null set; G is clearly acyclic.
        G is connected and acyclic, so G is a tree. QED
        """
        def empty_gen():
            yield from ()
        assert is_tree(0, empty_gen()) == True

    def test4(self):
        """
        Simple tree with five vertices
        """
        assert is_tree(5, (e for e in [(0, 1), (1, 2), (0, 3), (1, 4)])) == True



if __name__ == "__main__":
    unittest.main()
