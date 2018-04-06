import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
print("===")



play_tennis = pd.read_csv('dataset.csv')

features = ["height", "weight", "error", "age"]
target = "class"

print(play_tennis.head())
print ("Dataset Lenght:: ", len(play_tennis))
print ("Dataset Shape:: ", play_tennis.shape)


number = LabelEncoder()

play_tennis['height'] = number.fit_transform(play_tennis['height'])

play_tennis['weight'] = number.fit_transform(play_tennis['weight'])

play_tennis['error'] = number.fit_transform(play_tennis['error'])

play_tennis['age'] = number.fit_transform(play_tennis['age'])

play_tennis['class'] = number.fit_transform(play_tennis['class'])




# play_tennis['Outlook'] = number.fit_transform(play_tennis['Outlook'])
#
# play_tennis['Temperature'] = number.fit_transform(play_tennis['Temperature'])
#
# play_tennis['Humidity'] = number.fit_transform(play_tennis['Humidity'])
#
# play_tennis['Wind'] = number.fit_transform(play_tennis['Wind'])
#
# play_tennis['Play Tennis'] = number.fit_transform(play_tennis['Play Tennis'])
#
#
# features = ["Outlook", "Temperature", "Humidity", "Wind"]
#
# target = "Play Tennis"

features_train, features_test, target_train, target_test = train_test_split(play_tennis[features],play_tennis[target],test_size = 0.33,random_state = 54)

model = GaussianNB()

model.fit(features_train, target_train)

pred = model.predict(features_test)

accuracy = accuracy_score(target_test, pred)
print(accuracy)

print (model.predict([[2,1,0,1]]))



