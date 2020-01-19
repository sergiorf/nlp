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

    def test_get_test_7(self):
        t_a = self.treeparser.get_tree('give me all foreign companies that have operations in poland')
        t_b = "(S[]\n" \
        "  (VP[] (V[] give) (PR[] #PRP#))\n" \
        "  (NP[]\n" \
        "    (NP[]\n" \
        "      (Det[] #DT#)\n" \
        "      (Adj[] foreign)\n" \
        "      (NP[]\n" \
        "        (NP[] (N[] company))\n" \
        "        (PP[] (Ask[] #WDT#) (V[] have) (NP[] (N[] operation)))))\n" \
        "    (PP[] (P[] #IN#) (N[] poland))))"
        self.compare_trees(t_a, t_b)

    def test_get_test_8(self):
        t_a = self.treeparser.get_tree('select the top 10 companies that produce chocolate in belgium')
        t_b = "(S[]\n" \
        "  (VP[] (V[] select))\n" \
        "  (NP[]\n" \
        "    (NP[]\n" \
        "      (Det[] #DT#)\n" \
        "      (Adj[] top)\n" \
        "      (NUM[] 10)\n" \
        "      (NP[]\n" \
        "        (NP[] (N[] company))\n" \
        "        (PP[] (Ask[] #WDT#) (V[] produce) (NP[] (N[] chocolate)))))\n" \
        "    (PP[] (P[] #IN#) (N[] belgium))))"
        self.compare_trees(t_a, t_b)

    def test_get_test_9(self):
        t_a = self.treeparser.get_tree('select all the companies that have more employees than amazon')
        t_b = "(S[]\n" \
        "  (VP[] (V[] select))\n" \
        "  (NP[]\n" \
        "    (NP[] (Pdt[] all) (Det[] #DT#) (N[] company))\n" \
        "    (PP[]\n" \
        "      (Ask[] #WDT#)\n" \
        "      (V[] have)\n" \
        "      (NP[] (Comp[] more) (N[] employee) (P[] #IN#) (N[] amazon)))))"
        self.compare_trees(t_a, t_b)

    def test_get_test_10(self):
        t_a = self.treeparser.get_tree('select all new and modified companies between 2015 and 2018')
        t_b = "(S[]\n" \
        "  (VP[] (V[] select))\n" \
        "  (NP[]\n" \
        "    (NP[]\n" \
        "      (Det[] #DT#)\n" \
        "      (Adj[] new)\n" \
        "      (Conj[] and)\n" \
        "      (Adj[] modified)\n" \
        "      (N[] company))\n" \
        "    (PP[] (P[] #IN#) (NUM[] 2015) (Conj[] and) (NUM[] 2018))))"
        self.compare_trees(t_a, t_b)

    def test_get_test_11(self):
        t_a = self.treeparser.get_tree('what is the average stock of airbus between 2015 and 2018')
        t_b = "(S[]\n" \
        "  (WH[] (Ask[] #WP#) (V[] be))\n" \
        "  (NP[]\n" \
        "    (NP[]\n" \
        "      (Det[] #DT#)\n" \
        "      (Adj[] average)\n" \
        "      (NP[] (NP[] (N[] stock)) (PP[] (P[] #IN#) (N[] airbus))))\n" \
        "    (PP[] (P[] #IN#) (NUM[] 2015) (Conj[] and) (NUM[] 2018))))"
        self.compare_trees(t_a, t_b)

    def test_get_test_12(self):
        t_a = self.treeparser.get_tree('What are the sales of airbus in 2018')
        t_b = "(S[]\n" \
        "  (WH[] (Ask[] #WP#) (V[] be))\n" \
        "  (NP[]\n" \
        "    (NP[]\n" \
        "      (NP[] (Det[] #DT#) (N[] sale))\n" \
        "      (PP[] (P[] #IN#) (N[] airbus)))\n" \
        "    (PP[] (P[] #IN#) (NUM[] 2018))))"
        self.compare_trees(t_a, t_b)

    def test_get_test_13(self):
        t_a = self.treeparser.get_tree('what is the average stock of airbus in 2018')
        t_b = "(S[]\n" \
        "  (WH[] (Ask[] #WP#) (V[] be))\n" \
        "  (NP[]\n" \
        "    (NP[]\n" \
        "      (Det[] #DT#)\n" \
        "      (Adj[] average)\n" \
        "      (NP[] (NP[] (N[] stock)) (PP[] (P[] #IN#) (N[] airbus))))\n" \
        "    (PP[] (P[] #IN#) (NUM[] 2018))))"
        self.compare_trees(t_a, t_b)

    def compare_trees(self, tree_a, tree_b):
        print ('1: ' + str(str.splitlines(str(tree_a))))
        print ('2: ' + str(str.splitlines(str(tree_b))))
        self.assertEqual(str.splitlines(str(tree_a)), str.splitlines(tree_b), "Invalid tree")

if __name__ == '__main__':
    unittest.main()
    #t = HalTreeParserTests()
    #t.setUp()
    #t.test_get_test_13()
