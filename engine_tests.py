import unittest
from nltk import Tree
from engine import EngineHAL

class EngineHALTest(unittest.TestCase):

    def setUp(self):
        self.engine = EngineHAL()

    def test_get_tree_1(self):
        t_a = '(S[]\n(WH[] (Ask[] #WDT#) (Be[] be))\n (NP[] (Det[] #DT#) (Num[] 10) (N[] shareholder))\n(PP[] (P[] #IN#) (N[] sony)))'
        t_b = self.engine.get_tree('what are the 10 shareholders of sony')
        print (t_a)
        print (t_b)
        self.compare_trees(t_a, str(t_b))

    def compare_trees(self, tree_a, tree_b):
        self.assertEqual(tree_a, tree_b, "Invalid tree")

if __name__ == '__main__':
    unittest.main()

