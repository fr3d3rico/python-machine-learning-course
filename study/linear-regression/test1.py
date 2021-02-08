import numpy as np
import matplotlib.pyplot as plt 

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 100)) * 3

print(pageSpeeds)
print(purchaseAmount)

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)

print(f'r_value ** 2 = {r_value ** 2}') #quality 0 ~ bad and 1 ~ good
print(f'slope = {slope}')
print(f'intercept = {intercept}')
print(f'r_value = {r_value}')
print(f'p_value = {p_value}')
print(f'std_err = {std_err}')

#def function bellow wat take on udemy course. But, why did he write slope * x + intercept is the question. 
#after internet search, i found out this article:
# https://www.dummies.com/education/math/statistics/using-linear-regression-to-predict-an-outcome/

# http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm
# A linear regression line has an equation of the form Y = a + bX, 
# where X is the explanatory variable and Y is the dependent variable.
#The slope of the line is b, and a is the intercept (the value of y when x = 0).
def predict (x) :
    return slope * x + intercept

fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()







# https://www.w3schools.com/python/python_ml_linear_regression.asp
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfuncPrediction(x):
  return slope * x + intercept

mymodel = list(map(myfuncPrediction, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()




# Predict

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

result = myfuncPrediction(10)

print(result)





# Bad Fit?
#Let us create an example where linear regression would not be the best method to predict future values.
import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

mymodel = list(map(myfuncPrediction, x))

plt.scatter(x, y)
plt.plot(x, mymodel)

print('')
print(f'slope = {slope}')
print(f'intercept = {intercept}')
print(f'r = {r}')

plt.show()
