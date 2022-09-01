from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
import pandas as pd


dataset = pd.read_csv(r"problem\cps_festival\resources.csv",sep=', ',engine='python')
# resources.csv
# date, temp, sales
# 2022-07-01, 18, 100
# 2022-07-02, 25, 187
# 2022-07-03, 22, 136
# 2022-07-04, 31, 259
# 2022-07-05, 33, 264
# 2022-07-06, 29, 210
# 2022-07-07, 35, 288
# 2022-07-08, 30, 234
# 2022-07-09, 38, 297
# 2022-07-10, 33, 271

pred = pd.read_csv(r"problem\cps_festival\resources2.csv",sep=', ',engine='python')
# resources2.csv
# date, temp
# 2022-07-11, 26
# 2022-07-12, 24
# 2022-07-13, 39



data = dataset['temp']
target = dataset['sales']

line_fitter = LinearRegression()
line_fitter.fit(data.values.reshape(-1,1), target)

clf = MLPClassifier(hidden_layer_sizes = (100,50,20), activation="relu",solver = "adam",alpha=0.0001,max_iter=1000)
clf.fit(data.values.reshape(-1,1), target)

print("-LinearRegression-")
predict = line_fitter.predict(pred['temp'].values.reshape(-1,1))
for i in predict:
    print(round(i))

print()

print("-NeuralNetwork-")
predict = clf.predict(pred['temp'].values.reshape(-1,1))
for i in predict:
    print(i)