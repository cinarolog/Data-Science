# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 22:19:33 2022

@author: cinar
"""


#%%  Eksik gözlem analizi Missing Values

import numpy as np
import pandas as pd

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}        
)

df

df.isnull()
"""
      V1     V2     V3
0  False  False   True
1  False   True  False
2  False  False  False
3   True  False  False
4  False  False  False
5  False   True  False
6   True   True   True
7  False  False  False
8  False  False  False
"""

df.isnull().sum()
"""
V1    2
V2    3
V3    2
"""

df.notnull().sum()
"""
V1    7
V2    6
V3    7

"""

df.isnull().sum().sum()# 7

df[df.isnull().any(axis=1)]
"""
    V1   V2    V3
0  1.0  7.0   NaN
1  3.0  NaN  12.0
3  NaN  8.0   6.0
5  1.0  NaN   7.0
6  NaN  NaN   NaN
"""

df[df.notnull().all(axis=1)]
"""
     V1    V2    V3
2   6.0   5.0   5.0
4   7.0  12.0  14.0
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

df[df["V1"].notnull() & df["V2"].notnull() & df["V3"].notnull()]
"""
     V1    V2    V3
2   6.0   5.0   5.0
4   7.0  12.0  14.0
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

#%% Eksik değerlerin direk silinmesi


df.dropna()
"""
     V1    V2    V3
2   6.0   5.0   5.0
4   7.0  12.0  14.0
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

df
"""
     V1    V2    V3
0   1.0   7.0   NaN
1   3.0   NaN  12.0
2   6.0   5.0   5.0
3   NaN   8.0   6.0
4   7.0  12.0  14.0
5   1.0   NaN   7.0
6   NaN   NaN   NaN
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

df.dropna(inplace=True)
df
"""
     V1    V2    V3
2   6.0   5.0   5.0
4   7.0  12.0  14.0
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""


#%% Basit değer Atama mean()

import numpy as np
import pandas as pd

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}        
)

df

#mean()

df["V1"]
"""
0     1.0
1     3.0
2     6.0
3     NaN***
4     7.0
5     1.0
6     NaN***
7     9.0
8    15.0
"""
df["V1"].mean() #6.0

df["V1"].fillna(df["V1"].mean(),inplace=True)

df["V1"]
"""
0     1.0
1     3.0
2     6.0***
3     6.0
4     7.0
5     1.0
6     6.0***
7     9.0
8    15.0
"""

#%% Basit değer Atama median()


import numpy as np
import pandas as pd

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}        
)

df

#median()

df["V3"]
"""
0     NaN***
1    12.0
2     5.0
3     6.0
4    14.0
5     7.0
6     NaN***
7     2.0
8    31.0
"""
df["V3"].median() #7.0

df["V3"].fillna(df["V3"].median(),inplace=True)

df["V3"]
"""
0     7.0***
1    12.0
2     5.0
3     6.0
4    14.0
5     7.0
6     7.0***
7     2.0
8    31.0
"""


#%% Basit değer Atama 0


import numpy as np
import pandas as pd

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}        
)

df

#median()

df["V2"]
"""
0     7.0
1     NaN***
2     5.0
3     8.0
4    12.0
5     NaN***
6     NaN***
7     2.0
8     3.0
"""

df["V2"].fillna(0,inplace=True)

df["V2"]
"""
0     7.0
1     0.0***
2     5.0
3     8.0
4    12.0
5     0.0***
6     0.0***
7     2.0
8     3.0
"""


#%% apply()

#apply() fonksıyonu sutun bazında işlem yapar

import numpy as np
import pandas as pd

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}        
)

df
"""
     V1    V2    V3
0   1.0   7.0   NaN
1   3.0   NaN  12.0
2   6.0   5.0   5.0
3   NaN   8.0   6.0
4   7.0  12.0  14.0
5   1.0   NaN   7.0
6   NaN   NaN   NaN
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

df.apply(lambda x: x.fillna(x.mean()),axis=0 )
"""
tüm gözlemleri tek seferde doldurduk

0   1.0   7.000000  11.0
1   3.0   6.166667  12.0
2   6.0   5.000000   5.0
3   6.0   8.000000   6.0
4   7.0  12.000000  14.0
5   1.0   6.166667   7.0
6   6.0   6.166667  11.0
7   9.0   2.000000   2.0
8  15.0   3.000000  31.0
"""

#%% Eksik veri yapsısın Görselleştirilmesi

import numpy as np
import pandas as pd
import missingno as msno

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}        
)

df

msno.bar(df)

msno.matrix(df)

import seaborn as sns

df=sns.load_dataset("planets")
df.head()

df.isnull().sum()
"""
method              0
number              0
orbital_period     43
mass              522
distance          227
year                0
"""

msno.matrix(df)

msno.heatmap(df)





#%% Silme Yöntemleri

import numpy as np
import pandas as pd
import missingno as msno

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
V4= np.array([4,12,5,6,14,7,8,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3,
         "V4" : V4}        
)

df
"""
     V1    V2    V3  V4
0   1.0   7.0   NaN   4
1   3.0   NaN  12.0  12
2   6.0   5.0   5.0   5
3   NaN   8.0   6.0   6
4   7.0  12.0  14.0  14
5   1.0   NaN   7.0   7
6   NaN   NaN   NaN   8
7   9.0   2.0   2.0   2
8  15.0   3.0  31.0  31
"""

"""  tüm gözlemleri tek seferde silmek """

df.dropna(how="all")
"""
     V1    V2    V3
0   1.0   7.0   NaN
1   3.0   NaN  12.0
2   6.0   5.0   5.0
3   NaN   8.0   6.0
4   7.0  12.0  14.0
5   1.0   NaN   7.0
*********************** 6.gozlem uctu
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

df.dropna(axis=1)
"""
   V4
0   4
1  12
2   5
3   6
4  14
5   7
6   8
7   2
8  31
"""

#%% Basit değer atama /Sayısal Değişkenlerde atama 2.yol


import numpy as np
import pandas as pd
import missingno as msno

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}        
)

df


"""
     V1    V2    V3
0   1.0   7.0   NaN
1   3.0   NaN  12.0
2   6.0   5.0   5.0
3   NaN   8.0   6.0
4   7.0  12.0  14.0
5   1.0   NaN   7.0
6   NaN   NaN   NaN
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

#mean
df.fillna(df.mean()[:])
"""
     V1         V2    V3
0   1.0   7.000000  11.0
1   3.0   6.166667  12.0
2   6.0   5.000000   5.0
3   6.0   8.000000   6.0
4   7.0  12.000000  14.0
5   1.0   6.166667   7.0
6   6.0   6.166667  11.0
7   9.0   2.000000   2.0
8  15.0   3.000000  31.0
"""

#median
df.fillna(df.median())
"""
     V1    V2    V3
0   1.0   7.0   7.0
1   3.0   6.0  12.0
2   6.0   5.0   5.0
3   6.0   8.0   6.0
4   7.0  12.0  14.0
5   1.0   6.0   7.0
6   6.0   6.0   7.0
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

#herhangi bir sayıyla doldurmak  mesela 0
df.fillna(0)
"""
     V1    V2    V3
0   1.0   7.0   0.0
1   3.0   0.0  12.0
2   6.0   5.0   5.0
3   0.0   8.0   6.0
4   7.0  12.0  14.0
5   1.0   0.0   7.0
6   0.0   0.0   0.0
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""


df.fillna(df.mean()["V1":"V2"])
"""
     V1         V2    V3
0   1.0   7.000000   NaN
1   3.0   6.166667  12.0
2   6.0   5.000000   5.0
3   6.0   8.000000   6.0
4   7.0  12.000000  14.0
5   1.0   6.166667   7.0
6   6.0   6.166667   NaN
7   9.0   2.000000   2.0
8  15.0   3.000000  31.0
"""


#%%Basit değer atama /Sayısal Değişkenlerde atama 3.yol

df

"""
     V1    V2    V3
0   1.0   7.0   NaN
1   3.0   NaN  12.0
2   6.0   5.0   5.0
3   NaN   8.0   6.0
4   7.0  12.0  14.0
5   1.0   NaN   7.0
6   NaN   NaN   NaN
7   9.0   2.0   2.0
8  15.0   3.0  31.0
"""

df.where(pd.notna(df),df.mean(),axis="columns")
"""
     V1         V2    V3
0   1.0   7.000000  11.0
1   3.0   6.166667  12.0
2   6.0   5.000000   5.0
3   6.0   8.000000   6.0
4   7.0  12.000000  14.0
5   1.0   6.166667   7.0
6   6.0   6.166667  11.0
7   9.0   2.000000   2.0
8  15.0   3.000000  31.0
"""

#%% Basit değer atama /Kategorik Değişkenlerde atama

import numpy as np
import pandas as pd
 
V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
V4 = np.array(["IT","IT","IK","IK","IK","IK","IK","IT","IT"])

df = pd.DataFrame(
        {"maas" : V1,
         "V2" : V2,
         "V3" : V3,
        "departman" : V4}        
)

df

"""
   maas    V2    V3 departman
0   1.0   7.0   NaN        IT
1   3.0   NaN  12.0        IT
2   6.0   5.0   5.0        IK
3   NaN   8.0   6.0        IK
4   7.0  12.0  14.0        IK
5   1.0   NaN   7.0        IK
6   NaN   NaN   NaN        IK
7   9.0   2.0   2.0        IT
8  15.0   3.0  31.0        IT

"""

df.groupby("departman")["maas"].value_counts()
"""
departman  maas
IK         1.0     1
           6.0     1
           7.0     1
IT         1.0     1
           3.0     1
           9.0     1
           15.0    1
"""

df.groupby("departman")["maas"].mean()
"""
departman
IK    4.666667
IT    7.000000
"""

df.maas
"""
0     1.0
1     3.0
2     6.0
3     NaN
4     7.0
5     1.0
6     NaN
7     9.0
8    15.0
"""

df["maas"].fillna(df.groupby("departman")["maas"].transform("mean"))

"""
0     1.000000
1     3.000000
2     6.000000
3     4.666667
4     7.000000
5     1.000000
6     4.666667
7     9.000000
8    15.000000
"""



#%%

import numpy as np
import pandas as pd
V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V4 = np.array(["IT",np.nan,"IK","IK","IK","IK","IK","IT","IT"], dtype=object)

df = pd.DataFrame(
        {"maas" : V1,
        "departman" : V4}        
)

df

"""
   maas departman
0   1.0        IT
1   3.0       NaN
2   6.0        IK
3   NaN        IK
4   7.0        IK
5   1.0        IK
6   NaN        IK
7   9.0        IT
8  15.0        IT
"""
df.departman.mode()

df.fillna(df.departman.mode()[0])
"""
   maas departman
0   1.0        IT
1   3.0        IK
2   6.0        IK
3    IK        IK
4   7.0        IK
5   1.0        IK
6    IK        IK
7   9.0        IT
8  15.0        IT
"""

df.fillna(method="bfill")
"""
nan dan sonrasınnı doldurur  IK
   maas departman
0   1.0        IT
1   3.0        IK
2   6.0        IK
3   7.0        IK
4   7.0        IK
5   1.0        IK
6   9.0        IK
7   9.0        IT
8  15.0        IT
"""

df.fillna(method="ffill")
"""
nan dan öncesini doldurur  IT
   maas departman
0   1.0        IT
1   3.0        IT
2   6.0        IK
3   7.0        IK
4   7.0        IK
5   1.0        IK
6   9.0        IK
7   9.0        IT
8  15.0        IT
"""

#%% Tahmine dayalı değer atama yöntemleri

import pandas as pd
import numpy as np
import seaborn as sns
import missingno as msno
df = sns.load_dataset('titanic')
df = df.select_dtypes(include = ['float64', 'int64'])

df.isnull().sum()
"""
survived      0
pclass        0
age         177
sibsp         0
parch         0
fare          0
dtype: int64
"""

print(df.head())
"""
   survived  pclass   age  sibsp  parch     fare
0         0       3  22.0      1      0   7.2500
1         1       1  38.0      1      0  71.2833
2         1       3  26.0      0      0   7.9250
3         1       1  35.0      1      0  53.1000
4         0       3  35.0      0      0   8.0500

"""

#KNN
from ycimpute.imputer import knnimput

var_names = list(df)

n_df = np.array(df)
n_df[0:10]

n_df.shape
dff = knnimput.KNN(k = 4).complete(n_df)

type(dff)

dff=pd.DataFrame(dff,columns=var_names)
type(dff)


dff.isnull().sum()
"""
survived    0
pclass      0
age         0
sibsp       0
parch       0
fare        0
"""




#%%

import pandas as pd
import numpy as np
import seaborn as sns
import missingno as msno
df = sns.load_dataset('titanic')
df = df.select_dtypes(include = ['float64', 'int64'])

df.isnull().sum()
"""
survived      0
pclass        0
age         177
sibsp         0
parch         0
fare          0
dtype: int64
"""

print(df.head())
"""
   survived  pclass   age  sibsp  parch     fare
0         0       3  22.0      1      0   7.2500
1         1       1  38.0      1      0  71.2833
2         1       3  26.0      0      0   7.9250
3         1       1  35.0      1      0  53.1000
4         0       3  35.0      0      0   8.0500

"""

#Random Forest
from ycimpute.imputer import iterforest

var_names = list(df)

n_df = np.array(df)
n_df[0:10]

n_df.shape

dff = iterforest.IterImput().complete(n_df)

type(dff)

dff=pd.DataFrame(dff,columns=var_names)
type(dff)


dff.isnull().sum()
"""
survived    0
pclass      0
age         0
sibsp       0
parch       0
fare        0
"""


#%% Em


import pandas as pd
import numpy as np
import seaborn as sns
import missingno as msno
df = sns.load_dataset('titanic')
df = df.select_dtypes(include = ['float64', 'int64'])

df.isnull().sum()
"""
survived      0
pclass        0
age         177
sibsp         0
parch         0
fare          0
dtype: int64
"""

print(df.head())
"""
   survived  pclass   age  sibsp  parch     fare
0         0       3  22.0      1      0   7.2500
1         1       1  38.0      1      0  71.2833
2         1       3  26.0      0      0   7.9250
3         1       1  35.0      1      0  53.1000
4         0       3  35.0      0      0   8.0500

"""

#EM
from ycimpute.imputer import EM

var_names = list(df)

n_df = np.array(df)
n_df[0:10]

n_df.shape

dff = EM().complete(n_df)

type(dff)

dff=pd.DataFrame(dff,columns=var_names)
type(dff)


dff.isnull().sum()
"""
survived    0
pclass      0
age         0
sibsp       0
parch       0
fare        0
"""






