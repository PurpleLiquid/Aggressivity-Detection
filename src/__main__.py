import sys

from data.data_resource import *
from data.text_process import clean
from ml.feature_construction import *

def main():
    df = read()
    data = get_column(df, 5)
    string = clean(data[0])
    print("\n" + string + "\n")

    list = make_list(string)
    ngram = make_ngram(list, 2)

    for item in ngram:
        print(item)


if __name__ == "__main__":
    main()
