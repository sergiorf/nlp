from nltk.grammar import FeatStructNonterminal
from hal_treeparser import HalTreeParser

class HalExpression:

    def __init__(self, tree): 

        self.tree = tree
        self.table_metadata = {
            "shareholder": ["id", "name", { "of": ["company", "company_id"] }]
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
            leaves = self.get_annotated_leaves(np)
            if self.get_form1(leaves, sql_tokens):
                return sql_tokens
            
        else: 
            raise ValueError('Invalid sentence structure') 

    def get_form1(self, leaves, sql_tokens):

        num, name1, _, name2 = self.grep_leaves(leaves, 'NUM[]*N[]*P[]*N[]')
        if num and name1 and name2:
            if name1 in self.table_metadata:

                sql_tokens.append'top(' + num + ')')
                sql_tokens.append('*')
                sql_tokens.append('from')
                sql_tokens.append(name1 + ' as n1')
                sql_tokens.append('inner join')
                sql_tokens.append(self.table_metadata["of"][0])
                sql_tokens.append("as n2")
                sql_tokens.append("on n2.id = n1." + self.table_metadata["of"[1]])
                sql_tokens.append("where n2.name = " + name2)                
                return True

        return False

#"select top(10) * from shareholder as sh " \
#                  "join company as co on co.id = sh.company_id "  \
#                  "where co.name = \"sony\"" \
#                   )
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
    tree = HalTreeParser().get_tree(query = "what are the 10 shareholders of sony")
    print (HalTreeParser().get_pprint(tree))
    expr = HalExpression(tree)
    print (expr.gen_sql())
