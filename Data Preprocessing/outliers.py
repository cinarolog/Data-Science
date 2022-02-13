# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:01:16 2022

@author: cinar
"""



#%% Libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#%% Aykırı Gözlem  Outliers

import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64']) 
df.isnull().sum()
df = df.dropna()
df.head()

table=df["table"]
table.head()

sns.boxplot(table)

Q1=table.quantile(0.25)
Q3=table.quantile(0.75)
IQR=Q3-Q1
IQR

alt_sinir=Q1 - 1.5 * IQR
ust_sinir=Q3 + 1.5 * IQR

(table < alt_sinir) | (table > ust_sinir)

aykiri_tf=(table < alt_sinir)

aykiri_tf.head()

table[aykiri_tf]
"""
1515     51.0
3238     50.1
3979     51.0
4150     51.0
5979     49.0
7418     50.0
8853     51.0
11368    43.0
22701    49.0
25179    50.0
26387    51.0
33586    51.0
35633    44.0
45798    51.0
46040    51.0
47630    51.0
"""
table[aykiri_tf].index
"""
Int64Index([ 1515,  3238,  3979,  4150,  5979,  7418,  8853, 11368, 22701,
            25179, 26387, 33586, 35633, 45798, 46040, 47630],
           dtype='int64')
"""


#%% Aykırı değer problemini çözmek

# Silmek

type(table)
table=pd.DataFrame(table)
type(table)

table.shape

t_df =table[~((table < (alt_sinir)) | (table > (ust_sinir))).any(axis = 1)]
t_df

t_df.shape



#%% ortalama ile doldurmak

#  

import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64']) 
df = df.dropna()
df.head()

table=df["table"]

aykiri_tf=(table < alt_sinir)

df["table"].mean() #  57.457184

table[aykiri_tf]=df["table"].mean()
table[aykiri_tf]
"""
1515     57.457184
3238     57.457184
3979     57.457184
4150     57.457184
5979     57.457184
7418     57.457184
8853     57.457184
11368    57.457184
22701    57.457184
25179    57.457184
26387    57.457184
33586    57.457184
35633    57.457184
45798    57.457184
46040    57.457184
47630    57.457184
"""


#%% Baskılama yöntemi


import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64']) 
df = df.dropna()
df.head()

table=df["table"]


Q1=table.quantile(0.25)
Q3=table.quantile(0.75)
IQR=Q3-Q1
IQR

alt_sinir=Q1 - 1.5 * IQR
ust_sinir=Q3 + 1.5 * IQR

aykiri_tf=(table < alt_sinir)

alt_sinir # 51.5

table[aykiri_tf]=alt_sinir
table[aykiri_tf]

"""
1515     51.5
3238     51.5
3979     51.5
4150     51.5
5979     51.5
7418     51.5
8853     51.5
11368    51.5
22701    51.5
25179    51.5
26387    51.5
33586    51.5
35633    51.5
45798    51.5
46040    51.5
47630    51.5
"""



#%% Çok Değişkenli Atkırı Gözlem Local Outlier Factor

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64']) 
df = df.dropna()
df.head()

from sklearn.neighbors import LocalOutlierFactor

clf = LocalOutlierFactor(n_neighbors = 20, contamination = 0.1)

clf.fit_predict(df)
df_scores = clf.negative_outlier_factor_
df_scores[0:10]
np.sort(df_scores)[0:20]

esik_deger = np.sort(df_scores)[13]

aykiri_tf = df_scores > esik_deger
aykiri_tf
"""
Out[11]: array([ True,  True,  True, ...,  True,  True,  True])
"""

yeni_df=df[df_scores > esik_deger]

df[df_scores < esik_deger]

df[df_scores == esik_deger]


#%% Baskılama

baski_deger = df[df_scores == esik_deger]

aykirilar = df[~aykiri_tf]


aykirilar

aykirilar.to_records(index = False)

res = aykirilar.to_records(index = False)

res[:] = baski_deger.to_records(index = False)

res
df[~aykiri_tf]
import pandas as pd
df[~aykiri_tf] = pd.DataFrame(res, index = df[~aykiri_tf].index)
df[~aykiri_tf]

"""
6341    0.45   68.6   57.0    756  4.73  4.5  3.19
10377   0.45   68.6   57.0    756  4.73  4.5  3.19
24067   0.45   68.6   57.0    756  4.73  4.5  3.19
31230   0.45   68.6   57.0    756  4.73  4.5  3.19
35633   0.45   68.6   57.0    756  4.73  4.5  3.19
36503   0.45   68.6   57.0    756  4.73  4.5  3.19
38840   0.45   68.6   57.0    756  4.73  4.5  3.19
41918   0.45   68.6   57.0    756  4.73  4.5  3.19
45688   0.45   68.6   57.0    756  4.73  4.5  3.19
48410   0.45   68.6   57.0    756  4.73  4.5  3.19
49189   0.45   68.6   57.0    756  4.73  4.5  3.19
50773   0.45   68.6   57.0    756  4.73  4.5  3.19
52860   0.45   68.6   57.0    756  4.73  4.5  3.19
52861   0.45   68.6   57.0    756  4.73  4.5  3.19

"""





