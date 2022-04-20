import csv
import os
import glob
import pandas as pd
import string

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

# Processes a dataframe to get a specific coulmn in .csv
def get_column(df, index):
    i = 0;
    for col in df.columns:
        if i == index:
            data = list(df[col])
            data.insert(0, col)
            return data

        i = i + 1
