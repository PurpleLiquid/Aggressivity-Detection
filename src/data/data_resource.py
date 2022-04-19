import csv
import os
import glob
import pandas as pd
import string

def read():
    path = os.getcwd()
    print(path)
    csv_file = glob.glob(os.path.join(path, "Data/Raw/training.csv"))

    # Only has 1 file
    for f in csv_file:
        # read the csv file
        df = pd.read_csv(f, encoding='latin-1')

        return df

def get_column(df, index):
    i = 0;
    for col in df.columns:
        if i == index:
            data = list(df[col])
            data.insert(0, col)
            return data

        i = i + 1

# def clean(data):
#     table = str.maketrans('', '', string.punctuation)
#     stripped = [sentences.translate(table) for sentences in data]
#     print(stripped[0])
