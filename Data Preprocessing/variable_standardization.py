# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:35:01 2022

@author: cinar
"""


#%% DEğişken Standardizasyon

import numpy as np
import pandas as pd
V1 = np.array([1,3,6,5,7])
V2 = np.array([7,7,5,8,12])
V3 = np.array([6,12,5,6,14])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3})

df = df.astype(float)
df

"""
    V1    V2    V3
0  1.0   7.0   6.0
1  3.0   7.0  12.0
2  6.0   5.0   5.0
3  5.0   8.0   6.0
4  7.0  12.0  14.0
"""

#%% Standardizasyon -3,+3 aralığı

from sklearn import preprocessing

preprocessing.scale(df)
"""
Out[22]: 
array([[-1.57841037, -0.34554737, -0.70920814],
       [-0.64993368, -0.34554737,  0.92742603],
       [ 0.74278135, -1.2094158 , -0.98198051],
       [ 0.27854301,  0.08638684, -0.70920814],
       [ 1.2070197 ,  1.81412369,  1.47297076]])
"""



#%% Normalizasyon -1,+1 aralığı

from sklearn import preprocessing

preprocessing.normalize(df)

"""
Out[23]: 
array([[0.10783277, 0.75482941, 0.64699664],
       [0.21107926, 0.49251828, 0.84431705],
       [0.64699664, 0.53916387, 0.53916387],
       [0.4472136 , 0.71554175, 0.53665631],
       [0.35491409, 0.60842415, 0.70982818]])
"""


#%% Min-Max Dönüşümü

from sklearn import preprocessing

scaler=preprocessing.MinMaxScaler(feature_range=(10,20))
scaler.fit_transform(df)

"""

array([[10.        , 12.85714286, 11.11111111],
       [13.33333333, 12.85714286, 17.77777778],
       [18.33333333, 10.        , 10.        ],
       [16.66666667, 14.28571429, 11.11111111],
       [20.        , 20.        , 20.        ]])

"""




