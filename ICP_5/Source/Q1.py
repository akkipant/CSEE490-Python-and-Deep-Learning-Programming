import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import seaborn as sns

#Set up the output screen
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = [10, 6]

#Read data
train1 = pd.read_csv('./train.csv')

#Display the scatter plot of GarageArea and SalePrice
plt.scatter(train1.GarageArea, train1.SalePrice, color='black')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()

#Delete the outlier value of GarageArea
outlier_drop = train1[(train1.GarageArea < 1000) & (train1.GarageArea > 180) & (train1.SalePrice < 600000)]

##Display the scatter plot of GarageArea and SalePrice after deleting
plt.scatter(outlier_drop.GarageArea, outlier_drop.SalePrice, color='gray')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()