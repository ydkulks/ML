#Simple Linear Regression
#m = n (Σxy) - (Σx)(Σy) /n(Σx2) - (Σx)2
#b = (Σy)(Σx2) - (Σx)(Σxy)/ n(Σx2) - (Σx)2
#y = mx + b
import matplotlib as mp
mp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

def main():
    dataset = pd.read_csv('../data/Real-estate-valuation-data-set.csv')#Loading dataset
    x = np.array(dataset['X2 house age'])#Ages
    y = np.array(dataset['Y house price of unit area'])#Price
    X = []#Empty for random data
    Y = []#Empty for random data
    choice = input("\nDo you want:-\n=>'Sample' data\n=>'Randomized' data?[s/r]:")
    if choice == 's':#Sample data route
        print("About dataset:\nHistorical data set of real estate valuation are collected from Sindian Dist., New Taipei City, Taiwan.")
        ys = linearRegression(x,y)
        plot(x,y,ys)
    elif choice == 'r':#Random data route
        X,Y = rand_data(X,Y)
        print("\nRandomly generated x,y values:\n",X,Y)
        ys = linearRegression(X,Y)
        plot(X,Y,ys)

def rand_data(X,Y):
    len = int(input("\nWhat should be the length of the dataset?:"))
    for i in range(0,len+1):
        n = random.uniform(1,20)#Generates random int
        X.append(n)#Adds that number at the end of X
        m = random.uniform(1,20)#Generates random int
        Y.append(m)#Adds that number at the end of Y
    X = np.array(X)
    Y = np.array(Y)
    return(X,Y)

def linearRegression(x,y):
    b = ((sum(y)*sum(x*x))-(sum(x)*sum(x*y)))/(len(x)*sum(x*x)-sum(x)**2)
    m = ((len(x)*sum(x*y))-(sum(x)*sum(y)))/(len(x)*sum(x*x)-sum(x)**2)
    #ys = (m *x )+b
    return(m *x )+b

def plot(x,y,ys):
    mp.rc('lines',linewidth=4)
    with plt.style.context('dark_background'):#Dark theme
        plt.scatter(x,y,label="Houses",c='lightgrey',alpha=0.5)#Plots x,y data into graph
        plt.plot(x,ys,label="Line of best fit",c='red')#Plots the line of best fit
        plt.legend(loc='upper right')#legend location
    plt.xlabel("Age of the house")#x axis labeling
    plt.ylabel("House pricing")#y axis labeling
    plt.title("Linear Regression")#Graph labeling
    plt.show()#Displaying the graph

if __name__=="__main__":
    main()
