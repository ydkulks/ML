#Simple Linear Regression
import matplotlib as mp
mp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = [1.4, 3.3, 5.7, 8.7, 11.4]
    y = [2.5, 4.3, 7.3, 10.9, 14.6]
    print("\nPlotting given data (close graph to continue)")
    plot(x,y)
    choice=input("\nWant to predict the data?[y/n]:")
    while choice=='y':
        xtest = float(input("\nEnter the test data b/w 0 & 20:\n"))
        if xtest < 20 and xtest > 0:
            pred(x,y,xtest)
            plot(x,y)
            print("=====END=====")
            choice=input("\nWant to predict the data?[y/n]:")
        else:
            print("=====END=====")
            break

def plot(x,y):
    plt.plot(np.unique(x),np.poly1d(np.polyfit(x,y,1))(np.unique(x)))
    plt.plot(x, y, 'o')
    plt.axis([0,20,0,20])
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Linear Regression")
    plt.show()

def pred(x,y,xtest):
    prediction = np.poly1d(np.polyfit(x,y,1))(xtest)
    print("\nPrediction:\n",prediction)
    x.append(xtest)
    y.append(prediction)

if __name__=="__main__":
    main()
