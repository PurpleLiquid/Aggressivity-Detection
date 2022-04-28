import nltk

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer

from nltk.util import ngrams
from nltk.util import pad_sequence
from nltk.lm.preprocessing import pad_both_ends

from sklearn.feature_extraction.text import TfidfVectorizer

# Helper functions
def make_list(string):
    alist = list(string.split(" "))
    return alist

def list_to_string(list):
    aString = " "
    return (aString.join(list))

# Stemming and lemmatizing
def stem(list_of_words):
    ps = PorterStemmer()
    stemmed_words = []

    for word in list_of_words:
        stemmed_words.append(ps.stem(word))

    return stemmed_words

# def lemmatize(list_of_words):
#     lemmatizer = WordNetLemmatizer()
#     lemmatized_words = []
#
#     for word in list_of_words:
#         lemmatized_words.append(lemmatizer.lemmatize(word))
#
#     return lemmatized_words

# TF-IDF
def computeTF(list_of_sentences, n):
    vectorizer = TfidfVectorizer()
    response = vectorizer.fit_transform(list_of_sentences)
    return response

# N-gram model
def make_ngram(list_of_words, n):
    processed = list(pad_both_ends(list_of_words, n))
    ngram = ngrams(processed, n)
    return ngram
