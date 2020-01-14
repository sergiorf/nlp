import unittest
from nltk import Tree
from hal_treeparser import HalTreeParser

class HalTreeParserTests(unittest.TestCase):

    def setUp(self):
        self.treeparser = HalTreeParser()

    def test_get_tree_1(self):
        t_a = self.treeparser.get_tree('what are the 10 shareholders of sony')
        t_b = "(S[]\n" \
        "  (WH[] (Ask[] #WDT#) (V[] be))\n" \
        "  (NP[]\n" \
        "    (Det[] #DT#)\n" \
        "    (NUM[] 10)\n" \
        "    (NP[] (NP[] (N[] shareholder)) (PP[] (P[] #IN#) (N[] sony)))))"
        self.compare_trees(t_a, t_b)

    def test_get_tree_2(self):
        t_a = self.treeparser.get_tree('what are the 10 largest shareholders of sony')
        t_b = "(S[]\n" \
        "  (WH[] (Ask[] #WDT#) (V[] be))\n" \
        "  (NP[]\n" \
        "    (Det[] #DT#)\n" \
        "    (NUM[] 10)\n" \
        "    (Adj[] large)\n" \
        "    (NP[] (NP[] (N[] shareholder)) (PP[] (P[] #IN#) (N[] sony)))))"
        self.compare_trees(t_a, t_b)

    def test_get_tree_3(self):
        t_a = self.treeparser.get_tree('what companies went public in belgium in 2017')
        t_b = "(S[]\n" \
        "  (WH[] (Ask[] #WP#) (N[] company))\n" \
        "  (VP[]\n" \
        "    (VP[]\n" \
        "      (VP[] (V[] go) (Adj[] public))\n" \
        "      (PP[] (P[] #IN#) (N[] belgium)))\n" \
        "    (PP[] (P[] #IN#) (NUM[] 2017))))"
        self.compare_trees(t_a, t_b)

    def test_get_tree_4(self):
        t_a = self.treeparser.get_tree('what companies went public in belgium from 2017 to 2019')
        t_b = "(S[]\n" \
        "  (WH[] (Ask[] #WP#) (N[] company))\n" \
        "  (VP[]\n" \
        "    (VP[]\n" \
        "      (VP[] (V[] go) (Adj[] public))\n" \
        "      (PP[] (P[] #IN#) (N[] belgium)))\n" \
        "    (PP[] (P[] #IN#) (NUM[] 2017) (P[] #TO#) (NUM[] 2019))))"
        self.compare_trees(t_a, t_b)

    def test_get_test_5(self):
        t_a = self.treeparser.get_tree('give me the top 20 shipping companies in the world')
        t_b = "(S[]\n" \
        "  (VP[] (V[] give) (PR[] #PRP#))\n" \
        "  (NP[]\n" \
        "    (NP[]\n" \
        "      (Det[] #DT#)\n" \
        "      (Adj[] top)\n" \
        "      (NUM[] 20)\n" \
        "      (NP[] (N[] shipping) (N[] company)))\n" \
        "    (PP[] (P[] #IN#) (Det[] #DT#) (N[] world))))"
        self.compare_trees(t_a, t_b)

    def test_get_test_6(self):
        t_a = self.treeparser.get_tree('give me 20 shipping companies in the world ordered by sales')
        t_b = "(S[]\n" \
        "  (VP[] (V[] give) (PR[] #PRP#))\n" \
        "  (NP[]\n" \
        "    (NP[]\n" \
        "      (NUM[] 20)\n" \
        "      (V[] ship)\n" \
        "      (NP[]\n" \
        "        (NP[] (N[] company))\n" \
        "        (PP[] (P[] #IN#) (Det[] #DT#) (N[] world))))\n" \
        "    (PP[] (V[] order) (P[] #IN#) (N[] sale))))"
        self.compare_trees(t_a, t_b)


    def compare_trees(self, tree_a, tree_b):
        print ('1: ' + str(str.splitlines(str(tree_a))))
        print ('2: ' + str(str.splitlines(str(tree_b))))
        self.assertEqual(str.splitlines(str(tree_a)), str.splitlines(tree_b), "Invalid tree")

if __name__ == '__main__':
    unittest.main()
    #t = HalTreeParserTests()
    #t.setUp()
    #t.test_get_test_6()
