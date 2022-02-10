# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 00:26:03 2022

@author: cinar
"""


"""
           EXPLORATORY DATA ANALYSIS
"""
#%% import libraries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly 

#%% import data / Veri Setinin hikayesi nedir?

planets=sns.load_dataset("planets")
df=planets.copy()

df.head()
df.tail()

df.groupby("method").count()
df.groupby("method").mean()
df.groupby("method")["number"].count()
df.groupby("method")["mass"].mean()


df.info()
"""
---  ------          --------------  -----  
 0   method          1035 non-null   object  *********
 1   number          1035 non-null   int64  
 2   orbital_period  992 non-null    float64
 3   mass            513 non-null    float64
 4   distance        808 non-null    float64
 5   year            1035 non-null   int64  
"""
df.dtypes

df.describe().T
"""
                 count         mean  ...       75%       max
number          1035.0     1.785507  ...     2.000       7.0
orbital_period   992.0  2002.917596  ...   526.005  730000.0
mass             513.0     2.638161  ...     3.040      25.0
distance         808.0   264.069282  ...   178.500    8500.0
year            1035.0  2009.070531  ...  2012.000    2014.0
"""




#%% object to categorical

df.dtypes

df.method=pd.Categorical(df.method)
df.dtypes
"""
method            category *******  değişti
number               int64
orbital_period     float64
mass               float64
distance           float64
year                 int64
dtype: object
"""

#%% Veri setinin Betimlenmesi

df.shape

df.columns
"""
Out[34]: Index(['method', 'number', 'orbital_period',
                'mass', 'distance', 'year'], dtype='object')
"""

df.describe().T

"""
eksik gözlemleri ve categorik değişkenleri dahil etmez***********

Out[35]: 
                 count         mean  ...       75%       max
number          1035.0     1.785507  ...     2.000       7.0
orbital_period   992.0  2002.917596  ...   526.005  730000.0
mass             513.0     2.638161  ...     3.040      25.0
distance         808.0   264.069282  ...   178.500    8500.0
year            1035.0  2009.070531  ...  2012.000    2014.0
"""

#%% Eksik Değerler/ Missing values

# eksik değer varmı?
df.isnull().values.any() #Out[3]: True

df.isnull()

df.isnull().sum()
"""
method              0
number              0
orbital_period     43
mass              522
distance          227
year                0
dtype: int64

"""

# eksik verileri doldurma
"""
df["değişkenismi"].fillna(0,inplace=True)

****inplace true olunca df yapısı değişiir****

# df["orbital_period"].fillna(0,inplace=True)
# df["değişkenismi"].fillna(df.değişkenismi.mean(),inplace=True)
# df["değişkenismi"].fillna(df.değişkenismi.median(),inplace=True)

# df["mass"].fillna(df.mass.mean(),inplace=True)
# df["mass"].fillna(df.mass.median(),inplace=True)

*tum değikenlere ortalama ve mediyanı ile doldur
# df.fillna(df.mean(),inplace=True)
# df.fillna(df.median(),inplace=True)


"""
df.isnull().sum()

df


#%% Kategorik Değişken Özetleri

"""sadece kategorik değişkenler ve  ve özetleri"""

#kat_df=df.select_dtypes(include=["object"])
kat_df=df.select_dtypes(include=["category"])
kat_df.head()

""" kategorik değişkenler sınıflarına ve sınıf sayısına erişmek"""

kat_df.method.unique()
# Out[13]: 
# ['Radial Velocity', 'Imaging', 'Eclipse Timing Variations', 'Transit', 'Astrometry', 'Transit Timing Variations', 'Orbital Brightness Modulation', 'Microlensing', 'Pulsar Timing', 'Pulsation Timing Variations']
# Categories (10, object): ['Astrometry', 'Eclipse Timing Variations', 'Imaging', 'Microlensing', ...,
#                           'Pulsation Timing Variations', 'Radial Velocity', 'Transit',
#                           'Transit Timing Variations']

kat_df.method.value_counts().count() #Out[21]: 10
kat_df["method"].value_counts().count()

""" kategorik değişkenler sınıflarına ve frekanslarına erişmek"""

kat_df.method.value_counts()
kat_df["method"].value_counts()
# Radial Velocity                  553
# Transit                          397
# Imaging                           38
# Microlensing                      23
# Eclipse Timing Variations          9
# Pulsar Timing                      5
# Transit Timing Variations          4
# Orbital Brightness Modulation      3
# Astrometry                         2
# Pulsation Timing Variations        1

df.method.value_counts().plot.barh()


#%% Sürekli değişken özetleri

df_num=df.select_dtypes(include=["float64","int64"])

df_num.value_counts()
df_num.value_counts().count()#Out[31]: 498

df_num.head()

"""
   number  orbital_period   mass  distance  year
0       1         269.300   7.10     77.40  2006
1       1         874.774   2.21     56.95  2008
2       1         763.000   2.60     19.84  2011
3       1         326.030  19.40    110.62  2007
4       1         516.220  10.50    119.47  2009

"""

df_num.describe().T

"""
                 count         mean  ...       75%       max
number          1035.0     1.785507  ...     2.000       7.0
orbital_period   992.0  2002.917596  ...   526.005  730000.0
mass             513.0     2.638161  ...     3.040      25.0
distance         808.0   264.069282  ...   178.500    8500.0
year            1035.0  2009.070531  ...  2012.000    2014.0

[5 rows x 8 columns]
"""

df_num.distance.head()
df_num.year.tail()
df_num.mass.describe().T

df_num[["mass","year"]].head()

print("Ortalama: " + str(df_num["distance"].mean()))
print("Dolu Gözlem Sayısı: " + str(df_num["distance"].count())) 
print("Maksimum Değer: " + str(df_num["distance"].max()))
print("Minimum Değer: " + str(df_num["distance"].min()))
print("Medyan: " + str(df_num["distance"].median()))
print("Standart Sapma: " + str(df_num["distance"].std()))
"""
Ortalama: 264.06928217821786
Dolu Gözlem Sayısı: 808
Maksimum Değer: 8500.0
Minimum Değer: 1.35
Medyan: 55.25
Standart Sapma: 733.1164929404422

"""

#%%

""" DAğılım Grafikleri """

#%% Barplot

""" kategorik değişkenleri goselleştşrmek için kullanılır"""

import seaborn as sns
diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()
df.head()

df.info()

df.describe().T

df.cut.value_counts().count() 
df["cut"].value_counts().count()

df["cut"].value_counts()

df["color"].value_counts().count()
df["color"].value_counts()


#%% ordinal tanımlama

from pandas.api.types import CategoricalDtype

df.cut.head()
df.cut=df.cut.astype(CategoricalDtype(ordered=True))
df.cut
#Categories (5, object): ['Ideal' < 'Premium' < 'Very Good' < 'Good' < 'Fair']

cut_category=["Fair","Good","Very Good","Premium","Ideal"]
df.cut=df.cut.astype(CategoricalDtype(categories=cut_category,ordered=True))
df.cut
#Categories (5, object): ['Fair' < 'Good' < 'Very Good' < 'Premium' < 'Ideal']





