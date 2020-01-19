import unittest
from nltk import Tree
from hal_treeparser import HalTreeParser

class HalExpressionsTests(unittest.TestCase):

    def setUp(self):
        self.treeparser = HalTreeParser()

    def test_expressions_1(self):
        self.validate_sql(query = "what are the 10 shareholders of sony",
            sql = "select top(10) * from shareholder as sh " \
                  "join company as co on co.id = sh.company_id "  \
                  "where co.name = \"sony\"" \
                   )

    def validate_sql(self, query, sql):
        tree = self.treeparser.get_tree(query)
        expression = self.treeparser.get_expression(tree)
        print ('1: ' + query)
        print ('2: ' + expression.gen_sql())
        self.assertEqual(sql, expression.gen_sql(), "Invalid sql")

if __name__ == '__main__':
    unittest.main()
    #t = HalExpressionsTests()
    #t.setUp()
    #t.test_expressions_1()
