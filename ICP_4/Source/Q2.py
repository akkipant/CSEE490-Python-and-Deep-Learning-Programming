import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import classification_report

# Importing the dataset
dataset = pd.read_csv('Python_Lesson4/glass.csv')
X = dataset.drop('Type', axis=1)
X = dataset.drop('Ca', axis=1)
y = dataset['Type'].values

# Splitting the dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.35, random_state = 0)

cor = dataset.corr()
cor_target = abs(cor["Type"])

print()
print()
print(cor_target)


# Fitting Naive Bayes to the Training set
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#Calculating Accuracy
print("Naive Bayes accuracy is: ",metrics.accuracy_score(y_test,y_pred)*100)

print(classification_report(y_test,y_pred))
