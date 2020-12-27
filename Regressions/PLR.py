# Polynomial Linear Regression
import random
import matplotlib as mp
mp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    x=[1.41, 2.21, 3.06,  7.13,  11.25, 13.06, 14.31, 15.28]
    y=[2.39, 5.90, 10.29, 16.24, 14.29, 10.50, 6.23,  2.87]
    #x=[]
    #y=[]
    #x,y=data(x,y)  
    print("\nPlotting given data(close graph to continue)")
    plot(x,y)
    choice = input("\nWant to predict with new data?[y/n]:")
    while choice=='y':
        xtest=float(input("\nEnter test data b/w 0 & 20:\n"))
        if xtest < 20 and xtest > 0:
            ypred=pred(x,y,xtest)
            plot(x,y) 
            print("=====END=====")
            choice = input("\nWant to predict with new data?[y/n]:")
        else:
            print("=====END=====")
            break

#Generates random dataset
def data(x,y):
    for i in range(0,5):
        n=random.randint(1,20)
        y=random.randint(1,20)
        x.append(n)
        y.append(y)
    print("Data:",x,y)
    return x,y;

def plot(x,y):
    plt.plot(np.linspace(1,20,20),np.poly1d(np.polyfit(x,y,2))(np.linspace(1,20,20)))
    plt.plot(x,y,'o')
    plt.axis([0,20,0,20])
    plt.title("Polynomial Linear Regression")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

def pred(x,y,xtest):
    prediction = np.poly1d(np.polyfit(x,y,2))(xtest)
    print("\nPrediction:\n",prediction)
    x.append(xtest)
    y.append(prediction)

if __name__=="__main__":
    main()

