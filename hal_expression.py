from nltk.grammar import FeatStructNonterminal
from hal_treeparser import HalTreeParser

class HalExpression:

    def __init__(self, tree): 
        self.tree = tree
        self.table_metadata = {
            "shareholder": ["id", "name", "company_id"],
            "company": ["id", "name"]
        }

    def gen_sql(self):

        if (len(self.tree) != 2 and
            all(isinstance(x, FeatStructNonterminal) for x in tree)):
            raise ValueError('Invalid sentence: a sentence is composed of VP and NP')

        sent_struct = [repr(tree[i].label()) for i in range(2)]
        sql_tokens = []
        if (['NP[]', 'VP[]'] == sent_struct):
            self.gen_npfirst_sent(tree[0], tree[1], sql_tokens)
        elif (['VP[]', 'NP[]'] == sent_struct):
            self.gen_vpfirst_sent(tree[0], tree[1], sql_tokens)
        else:
            raise ValueError('Invalid sentence structure: a sentence is a NP followed by VP or viceversa')
        
        return ' '.join(sql_tokens)


    def gen_npfirst_sent(self, np, vp, sql_tokens):
        pass
    
    def gen_vpfirst_sent(self, vp, np, sql_tokens):
        leaves = vp.leaves()
        if (['#WDT#', 'be'] == leaves):
            sql_tokens.append('SELECT')
            self.gen_vpfirst_np(np, sql_tokens)
        else: 
            raise ValueError('Invalid sentence structure') 

    def gen_vpfirst_np(self, np, sql_tokens):
        num_rows = None
        table_1 = None
        table_2 = None
        # number just replace by top 
        # take two names in order, see if first name has an attribute of second name -> gen sql inner join
        leaves = self.get_annotated_leaves(np)
        print (leaves)

    def get_annotated_leaves(self, tree):
        leaves = []
        for idx, leave in enumerate(tree.leaves()):
            tree_location = tree.leaf_treeposition(idx)
            non_terminal = tree[tree_location[:-1]]
            leaves.append((repr(non_terminal.label()), leave))
        return leaves
    
if __name__ == '__main__':
    tree = HalTreeParser().get_tree(query = "what are the 10 shareholders of sony")
    print (HalTreeParser().get_pprint(tree))
    expr = HalExpression(tree)
    print (expr.gen_sql())


#"select top(10) * from shareholder as sh " \
#                  "join company as co on co.id = sh.company_id "  \
#                  "where co.name = \"sony\"" \
#                   )
