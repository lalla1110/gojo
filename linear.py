# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ggCK7cbBvkffKQ5AA_B5xFh1HGQnxUkU
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/content/placement(1).csv")
df.head()

x=df.iloc[:,0:1]

y=df.iloc[:,-1]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

x_train

from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(x_train,y_train)

lr.predict(x_test.iloc[0].values.reshape(1,1))
plt.scatter(df["cgpa"],df["package"])
plt.plot(x_train,lr.predict(x_train),color="red")

