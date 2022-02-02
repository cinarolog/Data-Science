# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:21:01 2022

@author: cinar
"""


#%% import libraries

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import missingno as msno

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, RepeatedStratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , precision_score ,confusion_matrix
from sklearn import tree



#%% Import Data and Analysis


data=pd.read_csv("water_potability.csv")
df=data.copy()
df.shape#(3276, 10)
df.head()
df.info()
"""
---  ------           --------------  -----  
 0   ph               2785 non-null   float64
 1   Hardness         3276 non-null   float64
 2   Solids           3276 non-null   float64
 3   Chloramines      3276 non-null   float64
 4   Sulfate          2495 non-null   float64
 5   Conductivity     3276 non-null   float64
 6   Organic_carbon   3276 non-null   float64
 7   Trihalomethanes  3114 non-null   float64
 8   Turbidity        3276 non-null   float64
 9   Potability       3276 non-null   int64  
dtypes: float64(9), int64(1)
memory usage: 256.1 KB

"""

df.describe().T

"""

                  count          mean  ...           75%           max
ph               2785.0      7.080795  ...      8.062066     14.000000
Hardness         3276.0    196.369496  ...    216.667456    323.124000
Solids           3276.0  22014.092526  ...  27332.762127  61227.196008
Chloramines      3276.0      7.122277  ...      8.114887     13.127000
Sulfate          2495.0    333.775777  ...    359.950170    481.030642
Conductivity     3276.0    426.205111  ...    481.792304    753.342620
Organic_carbon   3276.0     14.284970  ...     16.557652     28.300000
Trihalomethanes  3114.0     66.396293  ...     77.337473    124.000000
Turbidity        3276.0      3.966786  ...      4.500320      6.739000
Potability       3276.0      0.390110  ...      1.000000      1.000000

[10 rows x 8 columns]
"""
bool(df.isnull) #True

df.isnull().sum()

"""
ph                 491
Hardness             0
Solids               0
Chloramines          0
Sulfate            781
Conductivity         0
Organic_carbon       0
Trihalomethanes    162
Turbidity            0
Potability           0
dtype: int64
"""

df.columns

"""
Index(['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
       'Organic_carbon', 'Trihalomethanes', 'Turbidity', 'Potability'],
      dtype='object')
"""




#%% Analysis dependent Variable

y=df["Potability"]
y.value_counts()
# 0    1998 bad
# 1    1278 good

d = pd.DataFrame(df["Potability"].value_counts())

fig = px.pie(d, values = "Potability", names = ["Not Potable", "Potable"],
             hole = 0.35, opacity = 0.8,
            labels = {"label" :"Potability","Potability":"Number of Samples"})

fig.update_layout(title = dict(text = "Pie Chart of Potability Feature"))
fig.update_traces(textposition = "outside", textinfo = "percent+label")
fig.show()


#%% Correlation

df.corr()

sns.clustermap(df.corr(), cmap="vlag", dendrogram_ratio = (0.1, 0.2),
               annot = True, linewidths =1.0, figsize = (12,10))
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True,linewidths =1.0)
plt.show()




#%% Distribution of Features

non_pot=df[df.Potability==0]
pot=df[df.Potability==1]


plt.figure(figsize = (10,6))
for ax, col in enumerate(df.columns[:9]):
    plt.subplot(3,3, ax + 1)
    plt.title(col)
    sns.kdeplot(x = non_pot[col], label = "Non Potable")
    sns.kdeplot(x = pot[col], label = "Potable")
    plt.legend()
plt.tight_layout()




#%% Missing Values


msno.matrix(df)
plt.show()
bool(df.isnull) #True
df.isnull().sum()

"""
ph                 491
Hardness             0
Solids               0
Chloramines          0
Sulfate            781
Conductivity         0
Organic_carbon       0
Trihalomethanes    162
Turbidity            0
Potability           0
dtype: int64
"""

# handle missing value with average of features
df["ph"].fillna(value = df["ph"].mean(), inplace = True)
df["Sulfate"].fillna(value = df["Sulfate"].mean(), inplace = True)
df["Trihalomethanes"].fillna(value = df["Trihalomethanes"].mean(), inplace = True)


df.isnull().sum()
msno.matrix(df)
plt.show()

"""
ph                 0
Hardness           0
Solids             0
Chloramines        0
Sulfate            0
Conductivity       0
Organic_carbon     0
Trihalomethanes    0
Turbidity          0
Potability         0
dtype: int64

"""

#%% Train test split and Normalization

from sklearn.model_selection import train_test_split

X = df.drop("Potability", axis = 1).values
y = df["Potability"].values

X.shape
y.shape

# train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 2)
print("X_train",X_train.shape)
print("X_test",X_test.shape)
print("y_train",y_train.shape)
print("y_test",y_test.shape)


# min-max normalization

x_train_max = np.max(X_train)
x_train_min = np.min(X_train)
X_train = (X_train - x_train_min)/(x_train_max-x_train_min)
X_test = (X_test - x_train_min)/(x_train_max-x_train_min)



#%%Create Model  Decision Tree and Random Forest

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score , precision_score ,confusion_matrix , roc_auc_score
"""
models=["DCT",DecisionTreeClassifier(max_depth=3),
        "RF",RandomForestClassifier()]

finalResults = []
cmList = []

for name, model in models:
    model.fit(X_train, y_train) # train
    model_result = model.predict(X_test) # prediction
    score = precision_score(y_test, model_result)
    cm = confusion_matrix(y_test, model_result)
    
    finalResults.append((name, score))
    cmList.append((name, cm))

"""


"""
DECISION TREE

"""

dec_tree=DecisionTreeClassifier(max_depth=3)
dec_tree.fit(X_train,y_train)
dt_pred=dec_tree.predict(X_test)

#accuracy
acc=accuracy_score(y_test, dt_pred)
print("Decision tree Accuracy Score :",acc*100) # Decision tree Accuracy Score : 64.32926829268293

#Precision Score
prec_score=precision_score(y_test,dt_pred)
print("Precision Score :",prec_score*100) # Precision Score : 58.18181818181818

#roc_auc
roc_auc=roc_auc_score(y_test, dt_pred)
print("RocAuc  Score :",roc_auc*100) # RocAuc  Score : 53.79985850795643

#confusion matrix
cm=confusion_matrix(y_test, dt_pred)
cm

plt.figure(figsize=(10,6))
sns.heatmap(cm,annot=True,linewidths=1,linecolor="green",fmt=".1f")
plt.title("Decision Tree Confusion matrix")
plt.show()



"""
Random Forest Classifier
"""

rf=RandomForestClassifier(max_depth=3,random_state=42)
rf.fit(X_train,y_train)
rf_pred=rf.predict(X_test)

#accuracy
acc2=accuracy_score(y_test, rf_pred)
print("Decision tree Accuracy Score :",acc2*100) #Decision tree Accuracy Score : 65.70121951219512

#Precision Score
prec_score2=precision_score(y_test, rf_pred)
print("Precision Score :",prec_score2*100) # Precision Score : 84.61538461538461

#roc_auc
roc_auc2=roc_auc_score(y_test, rf_pred)
print("RocAuc  Score :",roc_auc2*100) # RocAuc  Score : 54.04248746998277

#confusion matrix
cm2=confusion_matrix(y_test, rf_pred)
cm2

plt.figure(figsize=(10,6))
sns.heatmap(cm2,annot=True,linewidths=1,linecolor="blue",fmt=".1f")
plt.title("Random Forest Confusion matrix")
plt.show()




#%% Visualize Decision Tree

from sklearn import tree

names=df.columns.tolist()[:-1]

plt.figure()
tree.plot_tree(dec_tree,feature_names=names,class_names=["0","1"],filled=True,precision=5)
plt.title("Tree Visualization")
plt.show()


#%% Random Forest Hyperparameter Tuning

from sklearn.model_selection import RandomizedSearchCV, RepeatedStratifiedKFold

model_params = {
    "Random Forest":
    {
        "model":RandomForestClassifier(),
        "params":
        {
            "n_estimators":[10, 50, 100],
            "max_features":["auto","sqrt","log2"],
            "max_depth":list(range(1,21,3))
        }
    }
    
}
    
model_params

cv = RepeatedStratifiedKFold(n_splits = 5, n_repeats = 2)
scores = []

for model_name, params in model_params.items():
    rs = RandomizedSearchCV(params["model"], params["params"], cv = cv, n_iter = 10)
    rs.fit(X,y)
    scores.append([model_name, dict(rs.best_params_),rs.best_score_])
    
scores
"""
[['Random Forest',
  {'n_estimators': 100, 'max_features': 'log2', 'max_depth': 19},
  0.6715481288400671]]
"""









