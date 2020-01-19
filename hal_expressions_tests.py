import unittest
from nltk import Tree
from hal_treeparser import HalTreeParser
from hal_expression import HalExpression

class HalExpressionsTests(unittest.TestCase):

    def test_expressions_1(self):
        self.validate_sql(query = "what are the 10 shareholders of sony",
            expected_sql = "select top(10) * from shareholder as sh " \
                  "join company as co on co.id = sh.company_id "  \
                  "where co.name = \"sony\"" \
                   )

    def validate_sql(self, query, expected_sql):
        tree = HalTreeParser().get_tree(query)
        gen_sql = HalExpression(tree).gen_sql()
        print ('query: ' + query)
        print ('expected sql: ' + expected_sql)
        print ('gen sql: ' + gen_sql)
        self.assertEqual(expected_sql, gen_sql, "Invalid sql")

if __name__ == '__main__':
    unittest.main()
    #t = HalExpressionsTests()
    #t.setUp()
    #t.test_expressions_1()
