import csv
import os
import glob
import pandas as pd

def read():
    path = os.getcwd()
    print(path)
    csv_file = glob.glob(os.path.join(path, "Data/Raw/training.csv"))

    # Only has 1 file
    for f in csv_file:
        # read the csv file
        df = pd.read_csv(f, encoding='latin-1')

        print('Content:')
        print(df)
