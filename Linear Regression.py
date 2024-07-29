# Import necessary modules 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# read data
dataset = pd.read_csv("dataset/Student_Performance.csv")
X = dataset.drop(dataset.columns[-1], axis=1)
y = dataset[dataset.columns[-1]]

# Split into training and test set 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42) 

# model training
lr = LinearRegression()
lr.fit(X_train, y_train)

# testing
pred = lr.predict(X_test)
print(lr.score(X_test, y_test))