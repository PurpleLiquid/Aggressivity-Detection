import sys

from data.data_resource import *
from data.text_process import clean

def main():
    df = read()
    data = get_column(df, 5)
    string = clean(data[0])
    print(string)


if __name__ == "__main__":
    main()
