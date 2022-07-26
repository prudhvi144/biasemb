import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def read():
    with open("./char.csv", encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            print (row)
def read_pandas():
    df1 = pd.read_excel('./Embryoscope Image List 1-27-22.csv')
    df2 = pd.read_csv('./Bias EmbryoScope Data 4-29-22.csv')
    # print(df.head())
    i =0
    length = len(df2["EmbryoScope Image ID"])
    for y in df2["EmbryoScope Image ID"]:
        # print (y)
        for x in df1.Name:
            if (y==x):
               i+=1
    print(length)
    print(f"{i}")





if __name__ == '__main__':
    read_pandas()




