# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 23:09:54 2022

@author: cinar
"""


#%% Sürekli Değişkeni kategorik değişkene çevirme


import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('tips')
df.head()


dff=df.select_dtypes(include=["float64","int64"])

from sklearn import preprocessing
est=preprocessing.KBinsDiscretizer(n_bins=[3,2,2],
                               encode="ordinal",
                               strategy="quantile").fit(dff)

est.transform(dff)[0:10]
"""
array([[1., 0., 1.],
       [0., 0., 1.],
       [2., 1., 1.],
       [2., 1., 1.],
       [2., 1., 1.],
       [2., 1., 1.],
       [0., 0., 1.],
       [2., 1., 1.],
       [1., 0., 1.],
       [0., 1., 1.]])
"""


#%% Değişkeni indexe, indexi değişkene çevirmek

df.head()
"""
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
"""

df["new_var"]=df.index

df.head()

"""
   total_bill   tip     sex smoker  day    time  size  new_var
0       16.99  1.01  Female     No  Sun  Dinner     2        0
1       10.34  1.66    Male     No  Sun  Dinner     3        1
2       21.01  3.50    Male     No  Sun  Dinner     3        2
3       23.68  3.31    Male     No  Sun  Dinner     2        3
4       24.59  3.61  Female     No  Sun  Dinner     4        4
"""

df["new_var2"]=df["new_var"] + 10

df.head()

"""
   total_bill   tip     sex smoker  day    time  size  new_var  new_var2
0       16.99  1.01  Female     No  Sun  Dinner     2        0        10
1       10.34  1.66    Male     No  Sun  Dinner     3        1        11
2       21.01  3.50    Male     No  Sun  Dinner     3        2        12
3       23.68  3.31    Male     No  Sun  Dinner     2        3        13
4       24.59  3.61  Female     No  Sun  Dinner     4        4        14
"""


