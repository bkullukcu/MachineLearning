# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:22:59 2020

@author: Ege
"""
# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling:
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""


#Simple Linear Regression:
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
 
#Predicting the Test set results:
y_pred = regressor.predict(X_test) #Bu y_pred regressor'ı eğittikten sonra y_testle karşılaştırmak için yaptığımız predictionlar

#Visulizing the Training set results
plt.scatter(X_train, y_train,color ='red')
plt.plot(X_train, regressor.predict(X_train), color= 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Visulizing the Test set results
plt.scatter(X_test, y_test,color ='red')
plt.plot(X_train, regressor.predict(X_train), color= 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()