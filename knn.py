# Import necessary modules 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

# read data
dataset = pd.read_csv("dataset/KNNAlgorithmDataset.csv")
x = dataset.drop("diagnosis", axis=1)
y = dataset["diagnosis"]

# remove outliers
def outlier(df):
    for col in df.columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        IQR = q3 - q1
        min_range = q1 - 1.5 * IQR
        max_range = q3 + 1.5 * IQR

        # Create a boolean mask for outliers
        outliers_mask = (df[col] < min_range) | (df[col] > max_range)

        # Replace outliers with the median
        df.loc[outliers_mask, col] = np.median(df[col])

    return df
outlier(x)

# scale the data
ss=StandardScaler()
X=ss.fit_transform(x)
X=pd.DataFrame(X,columns=x.columns)

# Split into training and test set 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42) 

# model training
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)

# testing
pred = knn.predict(X_test)
print(accuracy_score(y_test, pred))