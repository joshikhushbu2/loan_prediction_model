import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = pd.read_csv('loan_data.csv')
X = data.drop(columns=['Loan_Status'])
y = data['Loan_Status']

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state = 42)

classifier=RandomForestClassifier()
classifier.fit(x_train,y_train)

with open ('loan_prediction_model.pkl','wb') as f:
    pickle.dump(classifier,f)