from nltk.util import ngrams
from nltk.util import pad_sequence
from nltk.lm.preprocessing import pad_both_ends

def make_list(string):
    alist = list(string.split(" "))
    return alist

def make_ngram(alist, n):
    processed = list(pad_both_ends(alist, n))
    ngram = ngrams(processed, n)
    return ngram
