#Polynomial Linear Regression
import matplotlib as mp
mp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

def main():
    dataset = pd.read_csv('../data/Real-estate-valuation-data-set.csv')#Loading dataset
    x = np.array(dataset['X3 distance to the nearest MRT station'])#MRT station distance
    y = np.array(dataset['Y house price of unit area'])#Price
    X = []#Empty for random data
    Y = []#Empty for random data
    choice = input("\nDo you want:-\n=>'Sample' data\n=>'Randomized' data?[s/r]:")
    if choice == 's':#Sample data route
        print("About dataset:\nHistorical data set of real estate valuation are collected from Sindian Dist., New Taipei City, Taiwan.")
        ys = model(x,y)
        plot(x,y,ys)
    elif choice == 'r':#Random data route
        X,Y = rand_data(X,Y)
        print("\nRandomly generated x,y values:\n",X,Y)
        ys = model(X,Y)
        plot(X,Y,ys)

def rand_data(X,Y):
    len = int(input("\nWhat should be the length of the dataset?:"))
    for i in range(0,len):
        n = random.uniform(1,20)#Generates random int
        X.append(n)#Adds that number at the end of X
        m = random.uniform(1,20)#Generates random int
        Y.append(m)#Adds that number at the end of Y
    X = np.array(X)
    Y = np.array(Y)
    return(X,Y)

def model(x,y):
    b = ((sum(y)*sum(x*x))-(sum(x)*sum(x*y)))/(len(x)*sum(x*x)-sum(x)**2)
    m = ((len(x)*sum(x*y))-(sum(x)*sum(y)))/(len(x)*sum(x*x)-sum(x)**2)
    ys = ((m *x )**2)+(m*x)+b
    #print("\nRegression value:",ys)
    return(ys)

def plot(x,y,ys):
    xN=int(np.max(x))
    yN=int(np.max(y))
    mp.rc('lines',linewidth=3)
    with plt.style.context('dark_background'):#Dark theme
        plt.scatter(x,y,label="Houses",c='lightgrey',alpha=0.5)#Plots x,y data into graph
        plt.plot(np.linspace(1,xN,yN),np.poly1d(np.polyfit(x,y,2))(np.linspace(1,xN,yN))
                ,label="Line of best fit",c='red')#Plots the line of best fit
        plt.legend(loc='upper right')
    plt.xlabel("MRT station distance")#x axis labeling
    plt.ylabel("House pricing")#y axis labeling
    plt.title("Polynomial Linear Regression")#Graph labeling
    plt.show()#Displaying the graph

if __name__=="__main__":
    main()
