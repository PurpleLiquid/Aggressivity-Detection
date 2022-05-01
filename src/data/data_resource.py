import csv
import os
import glob
import pandas as pd
import string

TWEET_COLUMN_INDEX = 5
DEPENDENTS_COLUMN_INDEX = 0

# Function reads from a .csv file and returns a dataframe
def read():
    path = os.getcwd()
    print(path)
    csv_file = glob.glob(os.path.join(path, "Data/Raw/training.csv"))

    # Only has 1 file
    for f in csv_file:
        # read the csv file
        df = pd.read_csv(f, encoding='latin-1')

        return df

# Processes a dataframe to get a specific coulmn in .csv and put them into lists
def get_data(df):
    i = 0;
    dependents_column = None
    tweets_column = None
    for col in df.columns:
        if i == DEPENDENTS_COLUMN_INDEX:
            dependents_column = col

        if i == TWEET_COLUMN_INDEX:
            tweets_column = col

        i = i + 1

    df = df.sample(frac=1)
    tweets = df[tweets_column].tolist()
    dependents = df[dependents_column].tolist()

    train_tweets_data = tweets[:int(len(tweets) * 0.7)]
    test_tweets_data = tweets[-int(len(tweets) * 0.3):]

    train_dependents_data = dependents[:int(len(dependents) * 0.7)]
    test_dependents_data = dependents[-int(len(dependents) * 0.3):]

    return train_tweets_data, test_tweets_data, train_dependents_data, test_dependents_data
