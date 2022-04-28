import sys

from data.data_resource import *
from data.text_process import clean
from ml.feature_construction import *

def main():
    df = read()
    data = get_column(df, 5)
    string = clean(data[0])
    string2 = clean(data[1])
    string3 = clean(data[2])
    string4 = clean(data[3])
    string5 = clean(data[4])

    aList_of_strings = []
    aList_of_strings.append(string)
    aList_of_strings.append(string2)
    aList_of_strings.append(string3)
    aList_of_strings.append(string4)
    aList_of_strings.append(string5)
    tf = computeTF(aList_of_strings, 2)
    print(tf)

if __name__ == "__main__":
    main()
