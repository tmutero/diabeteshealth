import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

# Importing dataset
data = pd.read_csv("uploads/dataset2.csv")

# Convert categorical variable to numeric



# Cleaning dataset of NaN
data=data[[
    "height",
    "weight",
    "age",
    "error",
    "class"


]].dropna(axis=0, how='any')

# Split dataset in training and test datasets
X_train, X_test = train_test_split(data, test_size=0.5, random_state=int(time.time()))
gnb = GaussianNB()
used_features =[
    "height",
    "weight",
    "age",
    "error"

]
gnb.fit(
    X_train[used_features].values,
    X_train["class"]
)
y_pred = gnb.predict(X_test[used_features])
print(data.head())
print ("Dataset Lenght:: ", len(data))
print ("Dataset Shape:: ", data.shape)

print (gnb.predict([[9,19.6,0.810,22]]))
