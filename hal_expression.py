from nltk.grammar import FeatStructNonterminal
from hal_treeparser import HalTreeParser

class HalExpression:

    def __init__(self, tree): 
        self.tree = tree

    def gen_sql(self):
        if (len(self.tree) != 2 and
            all(isinstance(x, FeatStructNonterminal) for x in tree)):
            raise ValueError('Invalid sentence: a sentence is composed of VP and NP')

        sent_struct = [repr(tree[i].label()) for i in range(2)]
        if (['NP[]', 'VP[]'] == sent_struct):
            return self.gen_npfirst_sent(tree[0], tree[1])
        elif (['VP[]', 'NP[]'] == sent_struct):
            return self.gen_vpfirst_sent(tree[0], tree[1])
        
        raise ValueError('Invalid sentence structure: a sentence is a NP followed by VP or viceversa')
    
    def gen_npfirst_sent(self, np, vp):
        pass
    
    def gen_vpfirst_sent(self, vp, np):
        pass
    
if __name__ == '__main__':
    tree = HalTreeParser().get_tree(query = "what are the 10 shareholders of sony")
    expr = HalExpression(tree)
    print (expr.gen_sql())
