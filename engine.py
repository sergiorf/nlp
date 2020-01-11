import nltk
from nltk import load_parser
#queries:
#what are the 10 largest shareholders of sony
#what companies whent public in belgium from 2017 to 2019
#give me 20 shipping companies worldwide ordered by sales 
#give me all foreign companies that have operations in poland

#preprocessing:
#replace all verb tenses by root 
#replace names by placeholder 

sent = 'what are the 10 shareholders'
original_sent = sent.split()

# CFGs doens't handle multidigit numbers so we compress it before
tokens = ['#NUM#' if i.isdigit() else i for i in original_sent]

cp = load_parser('hal.fcfg')
trees = cp.parse(tokens)
for tree in trees:
    print (tree)
    tree.draw()

