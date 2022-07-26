# This is a sample Python script.
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
def reed_pand():
    # df = pd.read_csv('./Bias EmbryoScope Data 4-29-22.csv', encoding='utf-8')
    # print(df.head(0))
    df = pd.read_csv('./char.csv', encoding='utf-8')
    sns.set()
    ncols = len(df.columns)
    print(ncols)
    fig, axes = plt.subplots(2,3)

    for x,ax in (zip(df.head(0), axes.flatten())):
       print (x)
       # df[x].value_counts().plot(kind="hist")
       # sns.set(rc={"figure.figsize": (16, 10)})
       s=sns.countplot(x=df[x],orient='v',ax=ax)
       s.set_xticklabels(s.get_xticklabels(), rotation=45,ha="right",fontsize=15)
       fig=s.get_figure()

       # print(f",./{x}.png")
       # fig.savefig(f"./{x}.png")
       # plt.savefig(f"./{x}.png", bbox_inches='tight')
       # plt.show()
    # p = df["Sperm Source Race"].value_counts().plot(kind='bar')
    #plt.hist(p)
    plt.subplots_adjust(hspace=0.1)
    plt.tight_layout()
    plt.show()
def reed_hist():
    # df = pd.read_csv('./Bias EmbryoScope Data 4-29-22.csv', encoding='utf-8')
    # print(df.head(0))
    df = pd.read_csv('./hist.csv', encoding='utf-8')
    sns.set()
    ncols = len(df.columns)
    print(ncols)
    fig, axes = plt.subplots(3,3)

    for x,ax in (zip(df.head(0), axes.flatten())):
       print (x)
       # df[x].value_counts().plot(kind="hist")
       # sns.set(rc={"figure.figsize": (16, 10)})
       s=sns.histplot(x=df[x],ax=ax, bins=20)
       # s.set_xticklabels(s.get_xticklabels(), rotation=45,ha="right",fontsize=15)
       fig=s.get_figure()
       # print(f",./{x}.png")
       # fig.savefig(f"./{x}.png")
       # plt.savefig(f"./{x}.png", bbox_inches='tight')
       # plt.show()
    # p = df["Sperm Source Race"].value_counts().plot(kind='bar')
    #plt.hist(p)
    plt.subplots_adjust(hspace=0.1)
    plt.tight_layout()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reed_pand()
    reed_hist()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
