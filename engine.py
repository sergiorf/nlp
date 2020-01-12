import nltk
from nltk import load_parser
from nltk.stem import WordNetLemmatizer 

#preprocessing:
#create a unittest framework to do testing 
class EngineHAL:

    def get_tree(self, query):

        original_tokens = query.split()
        pos_tags = nltk.pos_tag(original_tokens)

        # lemmatize verbs and replace some words by placeholders
        lemmatizer = WordNetLemmatizer()
        simplified_tokens = []
        for i in range(len(original_tokens)):
            t = original_tokens[i]
            pos = pos_tags[i][1]
            if pos in ('VBD', 'VBP'):
                simplified_tokens.append(lemmatizer.lemmatize(t, 'v'))
            elif t.isdigit():
                simplified_tokens.append('#NUM#')
            elif pos in ('NN', 'NNS'):
                simplified_tokens.append('#NN#')
            else:
                simplified_tokens.append('#'+pos+'#')

        print (pos_tags)
        print (simplified_tokens)

        # The grammar uses those '#*#' placeholders 
        cp = load_parser('hal.fcfg')
        trees = cp.parse(simplified_tokens)
        for tree in trees:
            # Put back the (lemmatized) names and numbers in the tree leaves 
            i = 0
            for leafPos in tree.treepositions('leaves'):
                if simplified_tokens[i] == '#NN#':
                    tree[leafPos] = lemmatizer.lemmatize(original_tokens[i])
                elif simplified_tokens[i] == '#NUM#':
                    tree[leafPos] = original_tokens[i]
                i = i + 1
            return tree

        return None        

if __name__ == "__main__":
    #queries:
    #what are the 10 shareholders of sony
    #what are the 10 largest shareholders of sony
    #what companies whent public in belgium from 2017 to 2019
    #give me 20 shipping companies worldwide ordered by sales 
    #give me all foreign companies that have operations in poland
    engine = EngineHAL()
    tree = engine.get_tree('what are the 10 shareholders of sony')
    print (tree)
    tree.pretty_print()