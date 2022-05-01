import sys

from data.data_resource import *
from data.text_process import clean
from ml.feature_construction import *
from ml.classifier import *

def clean_tweets(tweets):
    clean_tweets = []
    for tweet in tweets:
        clean_tweets.append(clean(tweet))

    return clean_tweets

def feature_modelling(train_tweets, test_tweets):
    stemmed_tweets_train = []
    stemmed_tweets_test = []
    # stem each tweet
    for tweet in train_tweets:
        list_of_words = make_list(tweet)
        stemmed_words = stem(list_of_words)
        stemmed_tweets_train.append(list_to_string(stemmed_words))

    for tweet in test_tweets:
        list_of_words = make_list(tweet)
        stemmed_words = stem(list_of_words)
        stemmed_tweets_test.append(list_to_string(stemmed_words))

    # TFidf in ngrams
    features_train, features_test = computeTFidf(stemmed_tweets_train, stemmed_tweets_test)

    return features_train, features_test

def main():
    df = read()
    train_tweets_raw, test_tweets_raw, train_dependents_s, test_dependents_s = get_data(df)

    # clean data
    train_tweets = clean_tweets(train_tweets_raw)
    test_tweets = clean_tweets(test_tweets_raw)

    train_dependents = [int(i) for i in train_dependents_s]
    test_dependents = [int(i) for i in test_dependents_s]

    # Feature construction
    train_tfidf, test_tfidf = feature_modelling(train_tweets, test_tweets)

    svm_classifier(train_tfidf, test_tfidf, train_dependents, test_dependents)
    sgd_classifier(train_tfidf, test_tfidf, train_dependents, test_dependents)

if __name__ == "__main__":
    main()
