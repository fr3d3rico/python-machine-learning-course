# https://www.w3schools.com/python/python_ml_multiple_regression.asp
import pandas
df = pandas.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']

from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)