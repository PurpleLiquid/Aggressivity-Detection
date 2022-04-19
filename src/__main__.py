import sys

from data.data_resource import read, get_column

def main():
    df = read()
    data = get_column(df, 5)

if __name__ == "__main__":
    main()
