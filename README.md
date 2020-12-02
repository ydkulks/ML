## Machine Learning 
*work-in-progress-!*


### Linear Regression output:
Plots the *existing data* from the dataset and asks for the *test data* for testing from the user.
The user must provide the *X* value and it predicts the *Y* value as a prediction and plots it 
into the graph with the existing data.<br>
*Formula*: y=mx+b where *m* is the slope and *b* is the intercept.<br>
![Output of LR](https://github.com/ydkulks/ML/blob/master/outputs/LR-output.png?raq=true)


<br>Here, it is plotting the *line of best fit* for the data from the existing data from the 
data set.This is done to find the pattern in the data.<br>
![Output of LR](https://github.com/ydkulks/ML/blob/master/outputs/LR-Graph.png?raq=true)


After introducing the test data, it has updated the graph to the test data accordingly.
What it is doing here is that it takes in the known *X* value and tries to predict where 
the *Y* value might be for that data according to the pattern found in the data.<br>
![Output of LR](https://github.com/ydkulks/ML/blob/master/outputs/LR-TestGraph.png?raq=true)


### Polynomial Linear Regression output:
Similarly, in polynomial regression, it takes in the data from the provided data set and 
plots a graph to identify the pattern in the data.<br>
*Formula*: y = m2x2^2 + m1x1 +b , linear regression formula with 2nd order co-efficient.<br>
![Output of LR](https://github.com/ydkulks/ML/blob/master/outputs/PLR-output.png?raq=true)


But, unlike linear regression, it can plot the *line of best fit* for the scatter plot that 
has a curvature as it's pattern and fit a curve to it instead of a straight line. A straight line
for this kind of data might be an inaccurate representation. Because of this drawback, this 
    algorithm might be you're best bet for this kind of data.<br>
![Output of LR](https://github.com/ydkulks/ML/blob/master/outputs/PLR-Graph.png?raq=true)


As you can observe, the test data will fit the curve accordingly.<br>
![Output of LR](https://github.com/ydkulks/ML/blob/master/outputs/PLR-TestGraph.png?raq=true)
