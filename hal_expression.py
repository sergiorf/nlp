from nltk.grammar import FeatStructNonterminal
from hal_treeparser import HalTreeParser

class HalExpression:

    def __init__(self, tree): 

        self.tree = tree
        self.table_metadata = {
            "shareholder_company": { 
                "id":"id", 
                "shareholder_id":"shareholder_id",
                "company_id":"company_id",
                "large": "participation" 
            },
            "shareholder": { "id":"id", "name":"name" },
            "company": { "id":"id", "name":"name" }
        }

    def gen_sql(self):

        if (len(self.tree) != 2 and
            all(isinstance(x, FeatStructNonterminal) for x in tree)):
            raise ValueError('Invalid sentence: a sentence is composed of VP and NP')

        sent_struct = [repr(self.tree[i].label()) for i in range(2)]
        sql_tokens = []
        if (['NP[]', 'VP[]'] == sent_struct):
            self.gen_npfirst_sent(self.tree[0], self.tree[1], sql_tokens)
        elif (['VP[]', 'NP[]'] == sent_struct):
            self.gen_vpfirst_sent(self.tree[0], self.tree[1], sql_tokens)
        else:
            raise ValueError('Invalid sentence structure: a sentence is a NP followed by VP or viceversa')
        
        return ' '.join(sql_tokens)


    def gen_npfirst_sent(self, np, vp, sql_tokens):
        pass
    
    def gen_vpfirst_sent(self, vp, np, sql_tokens):

        leaves = vp.leaves()
        if (['#WDT#', 'be'] == leaves):
            sql_tokens.append('SELECT')
            leaves = self.get_annotated_leaves(np)
            if self.get_form1(leaves, sql_tokens):
                return sql_tokens
            
        else: 
            raise ValueError('Invalid sentence structure') 

    def get_form1(self, leaves, sql_tokens):

        num, adj, name1, _, name2 = self.grep_leaves(leaves, 'NUM[]*Adj[]*N[]*P[]*N[]')
        if not name1 or not name2:
            num, name1, _, name2 = self.grep_leaves(leaves, 'NUM[]*N[]*P[]*N[]')
        if num and name1 and name2:
            sql_tokens.append('top(' + num + ')')
            sql_tokens.append('*')
            sql_tokens.append('from shareholder_company as n1')
            sql_tokens.append('inner join shareholder_company as n2 on n2.id = n1.shareholder_id')
            sql_tokens.append('inner join company as n3 on n3.id = n3.company_id')                
            sql_tokens.append("where n3.name = \"" + name2 + "\"")                
            if adj:
                sql_tokens.append("order by n2.participation desc")
            return True
        return False

    def grep_leaves(self, leaves, regex):
        i = 0
        r = regex.split('*')
        c = 0
        result = [None for i in range(len(r))]
        for i in range(len(leaves)):
            if c == len(r):
                break
            leave = leaves[i]
            if leave[0] == r[c]:
                result[c] = leave[1]
                c += 1
            i += 1
        return result            

    def get_annotated_leaves(self, tree):
        leaves = []
        for idx, leave in enumerate(tree.leaves()):
            tree_location = tree.leaf_treeposition(idx)
            non_terminal = tree[tree_location[:-1]]
            leaves.append((repr(non_terminal.label()), leave))
        return leaves
    
if __name__ == '__main__':
    tree = HalTreeParser().get_tree(query = "what are the 10 largest shareholders of sony")
    print (HalTreeParser().get_pprint(tree))
    expr = HalExpression(tree)
    print (expr.gen_sql())
