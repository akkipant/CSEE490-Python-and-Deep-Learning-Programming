import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('winequality-red.csv')

# Working with Numeric Features
numeric_features = train.select_dtypes(include=[np.number])
corr = numeric_features.corr()
plt.figure(figsize=(20, 20));
sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.show();

# print (corr['quality'].sort_values(ascending=False)[:-1], '\n')
print(corr['quality'].sort_values(ascending=False)[1:4], '\n')

##Null values
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

##handling the missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))

# Transforming and engineering non-numeric features
train = data.apply(LabelEncoder().fit_transform)

##Build a multiple model
y = data['quality']
X = data[['quality','alcohol', 'sulphates', 'citric acid']]
plt.hist(y)
plt.show()

y = np.log(y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.20)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

##Evaluate the performance and visualize results
print("R^2 is: ", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print('RMSE is: ', mean_squared_error(y_test, predictions))


plt.hist(y)
plt.show()


