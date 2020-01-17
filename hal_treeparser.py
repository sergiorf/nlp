import nltk
import io
from nltk import load_parser
from nltk import Tree
from nltk.stem import WordNetLemmatizer, PorterStemmer

class HalTreeParser:

    def get_tree(self, query):

        original_tokens = query.split()
        pos_tags = nltk.pos_tag(original_tokens)

        # lemmatize verbs and replace some words by placeholders
        lemmatizer = WordNetLemmatizer()
        simplified_tokens = []
        for i in range(len(original_tokens)):
            t = original_tokens[i]
            pos = pos_tags[i][1]
            if pos.startswith('VB'):
                simplified_tokens.append('#V#')
            elif t.isdigit():
                simplified_tokens.append('#NUM#')
            elif pos in ('NN', 'NNS'):
                simplified_tokens.append('#NN#')
            elif pos in ('JJS', 'JJ'):
                simplified_tokens.append('#JJ#')
            else:
                simplified_tokens.append('#'+pos+'#')

        print (pos_tags)
        print (simplified_tokens)

        # The grammar uses those '#*#' placeholders 
        cp = load_parser('hal.fcfg')
        trees = cp.parse(simplified_tokens)
        for tree in trees:
            # Put back the lemmas and numbers in the tree leaves 
            i = 0
            for leafPos in tree.treepositions('leaves'):
                if simplified_tokens[i] in ('#V#'):
                    #verbs -> base form
                    tree[leafPos] = lemmatizer.lemmatize(original_tokens[i], 'v')
                elif simplified_tokens[i] in ('#NN#'):
                    tree[leafPos] = lemmatizer.lemmatize(original_tokens[i])
                elif simplified_tokens[i] == '#JJ#':
                    tree[leafPos] = lemmatizer.lemmatize(original_tokens[i], 'a')
                elif simplified_tokens[i] in ('#NUM#', '#PDT#', '#JJR#', '#CC#'):
                    tree[leafPos] = original_tokens[i]
                i = i + 1
            return tree

        return None   

    def get_pprint(self, tree):
        content = ""
        stream = io.StringIO(content)
        # Some issue with the tree structure causes a problem with pprint
        # That's why we have to convert to string and then parse 
        Tree.fromstring(str(tree)).pretty_print(stream = stream)
        return stream.getvalue()


if __name__ == "__main__":
    treeparser = HalTreeParser()
    #tree = treeparser.get_tree('What are the sales of airbus in 2018')
    #tree = treeparser.get_tree('what is the average stock of airbus in 2018')
    tree = treeparser.get_tree('what is the average stock of airbus between 2015 and 2018')
    print (treeparser.get_pprint(tree))