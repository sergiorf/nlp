from nltk import load_parser

sent = 'who do you like'
tokens = sent.split()
cp = load_parser('feat1.fcfg')
trees = cp.parse(tokens)
for tree in trees:
    tree.draw()

