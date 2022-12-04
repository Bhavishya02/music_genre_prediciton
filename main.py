import pandas as pd
df = pd.read_csv('music.csv')
df.describe()
inputs = df.drop('genre',axis = 'columns')

targets = df['genre']
from sklearn import LabelEncoder
le_age = LabelEncoder()
le_gender = LabelEncoder()
le_genre = LabelEncoder()

from sklearn import tree
inputs['age_n'] = le_age.fit_transform(inputs['age'])
inputs['gender'] = le_gender.fit_transform(inputs[gender])
inputs_n = inputs.drop('age', 'gender')
inputs.head()
model = tree.DecisionTreeClassifier()
model.fit(inputs, targets)
