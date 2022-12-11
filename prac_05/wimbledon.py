import csv
import pandas as pd

def main():
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader_obj = csv.reader(in_file)
        for name in reader_obj:
            win_rate = 1
            if name[2] in reader_obj:
                win_rate += 1
            else:
                win_rate = 1