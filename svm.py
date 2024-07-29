# Import necessary modules 
from sklearn.svm import SVC 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

dataset = pd.read_csv("dataset/Cellphone.csv")
X = dataset.drop(dataset.columns[-1], axis=1)
y = dataset[dataset.columns[-1]]

# Split into training and test set 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42) 

# model training 
svm = SVC(kernel='linear')
svm.fit(X_train, y_train) 

# model testing
pred = svm.predict(X_test)
print(accuracy_score(y_test, pred))