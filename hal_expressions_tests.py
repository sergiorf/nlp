import unittest
from nltk import Tree
from hal_treeparser import HalTreeParser
from hal_expression import HalExpression

class HalExpressionsTests(unittest.TestCase):

    def test_expressions_1(self):
        query = "what are the 10 shareholders of sony"
        expected_sql = "SELECT top(10) * from shareholder_company as n1 " \
                "inner join shareholder_company as n2 on n2.id = n1.shareholder_id " \
                "inner join company as n3 on n3.id = n3.company_id " \
                "where n3.name = \"sony\""
        self.validate_sql(query, expected_sql)

    def test_expressions_2(self):
        query = "what are the 10 largest shareholders of sony"
        expected_sql = "SELECT top(10) * from shareholder_company as n1 " \
                "inner join shareholder_company as n2 on n2.id = n1.shareholder_id " \
                "inner join company as n3 on n3.id = n3.company_id " \
                "where n3.name = \"sony\" order by n2.participation desc"
        self.validate_sql(query, expected_sql)

    def validate_sql(self, query, expected_sql):
        parser = HalTreeParser()
        tree = parser.get_tree(query)
        expr = HalExpression(tree)
        gen_sql = expr.gen_sql()
        print ('query:        \"' + query + "\"")
        print ('expected sql: \"' + expected_sql + "\"")
        print ('gen sql:      \"' + gen_sql + "\"")
        self.assertEqual(expected_sql, gen_sql, "Invalid sql")

if __name__ == '__main__':
    unittest.main()
    #t = HalExpressionsTests()
    #t.setUp()
    #t.test_expressions_1()
