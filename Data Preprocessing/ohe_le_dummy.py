# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 22:39:05 2022

@author: cinar
"""


#%%  Değişken dönüşümleri

import pandas as pd
import numpy as np
import seaborn as sns
df = sns.load_dataset('tips')
df.head()


"""
  total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
"""


#%% Label Encoder  0-1 Dönüşümü

from sklearn.preprocessing import LabelEncoder

df["sex"].head()
"""
0    Female
1      Male
2      Male
3      Male
4    Female
"""
lbe=LabelEncoder()
df["new_sex"]=lbe.fit_transform(df["sex"])
df["new_sex"].head(10)
"""
0    0
1    1
2    1
3    1
4    0
5    1
6    1
7    1
8    1
9    1
"""

df
"""
     total_bill   tip     sex smoker   day    time  size  new_sex
0         16.99  1.01  Female     No   Sun  Dinner     2        0
1         10.34  1.66    Male     No   Sun  Dinner     3        1
2         21.01  3.50    Male     No   Sun  Dinner     3        1
3         23.68  3.31    Male     No   Sun  Dinner     2        1
4         24.59  3.61  Female     No   Sun  Dinner     4        0
..          ...   ...     ...    ...   ...     ...   ...      ...
239       29.03  5.92    Male     No   Sat  Dinner     3        1
240       27.18  2.00  Female    Yes   Sat  Dinner     2        0
241       22.67  2.00    Male    Yes   Sat  Dinner     2        1
242       17.82  1.75    Male     No   Sat  Dinner     2        1
243       18.78  3.00  Female     No  Thur  Dinner     2        0
"""


#%% ilgilendiğimiz 1 ,  diğerleri 0

df["day"]
"""
0       Sun
1       Sun
2       Sun
3       Sun
4       Sun

239     Sat
240     Sat
241     Sat
242     Sat
243    Thur
"""

# Sun==1   others==0
df["new_day"]=np.where(df["day"].str.contains("Sun"),1,0)

df["new_day"]
"""
0      1
1      1
2      1
3      1
4      1
      ..
239    0
240    0
241    0
242    0
243    0
"""


#%% Çok Sınıflı Dönüşümler

from sklearn.preprocessing import LabelEncoder

lbe=LabelEncoder()
lbe.fit_transform(df["day"])

"""
array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
       3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3,
       3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 3])
"""

#%% One Hot Encoding OHE ve Dummy Tuzağı

df.head()
"""
   total_bill   tip     sex smoker  day    time  size  new_sex  new_day
0       16.99  1.01  Female     No  Sun  Dinner     2        0        1
1       10.34  1.66    Male     No  Sun  Dinner     3        1        1
2       21.01  3.50    Male     No  Sun  Dinner     3        1        1
3       23.68  3.31    Male     No  Sun  Dinner     2        1        1
4       24.59  3.61  Female     No  Sun  Dinner     4        0        1
"""

df.sex
"""
0      Female
1        Male
2        Male
3        Male
4      Female
 
239      Male
240    Female
241      Male
242      Male
243    Female
"""

df_ohe=pd.get_dummies(df,columns=["sex"],prefix=["sex"])
df_ohe.head(10)
"""
   total_bill   tip smoker  day  ... new_sex  new_day  sex_Male  sex_Female
0       16.99  1.01     No  Sun  ...       0        1         0           1
1       10.34  1.66     No  Sun  ...       1        1         1           0
2       21.01  3.50     No  Sun  ...       1        1         1           0
3       23.68  3.31     No  Sun  ...       1        1         1           0
4       24.59  3.61     No  Sun  ...       0        1         0           1
5       25.29  4.71     No  Sun  ...       1        1         1           0
6        8.77  2.00     No  Sun  ...       1        1         1           0
7       26.88  3.12     No  Sun  ...       1        1         1           0
8       15.04  1.96     No  Sun  ...       1        1         1           0
9       14.78  3.23     No  Sun  ...       1        1         1           0
"""

df_ohe=pd.get_dummies(df,columns=["day"],prefix=["day"])
df_ohe.head(10)

"""
   total_bill   tip     sex smoker  ... day_Thur  day_Fri  day_Sat  day_Sun
0       16.99  1.01  Female     No  ...        0        0        0        1
1       10.34  1.66    Male     No  ...        0        0        0        1
2       21.01  3.50    Male     No  ...        0        0        0        1
3       23.68  3.31    Male     No  ...        0        0        0        1
4       24.59  3.61  Female     No  ...        0        0        0        1
5       25.29  4.71    Male     No  ...        0        0        0        1
6        8.77  2.00    Male     No  ...        0        0        0        1
7       26.88  3.12    Male     No  ...        0        0        0        1
8       15.04  1.96    Male     No  ...        0        0        0        1
9       14.78  3.23    Male     No  ...        0        0        0        1
"""





