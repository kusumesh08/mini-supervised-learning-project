# Task 1: Perform EDA and Preprocessing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# #Load data set
# data = fetch_california_housing(as_frame=True)
# df = data.frame

# #Inspect data
# print(df.info())
# print(df.describe())

# #visualize relationships 
# sns.pairplot(df, vars=['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal'])
# plt.show()

# #checking for missing values
# print(df.isnull().sum())

#Load telco customer churn dataset
df_telco= pd.read_csv('Telco-Customer-Churn.csv.')

#Inspect data
print(df_telco.info())
print(df_telco.describe())

#Visualize churn distribution
sns.countplot(x='churn', data=df_telco)
plt.title('Churn Distribution')
plt.show()

#Hande the missing values
df_telco.fillna(df_telco.mean(), inplace=True)
