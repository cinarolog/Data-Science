# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:08:06 2022

@author: cinar
"""

"""

Her bölümü ve değişkenleri bulunduğu bölüme göre değerlendiriniz.

"""

#%% libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%

pd.Series([23,45,2,3,5])
seri=pd.Series([23,45,2,3,5])
seri

type(seri)

seri.axes
seri.ndim
seri.dtype
seri.shape
seri.size

seri.values

seri.head(3)
seri.tail(3)


#%% index isimlendirmesi

a=pd.Series([33,4,5,3,334],index=[1,3,5,7,9])
a

b=pd.Series([33,4,5,3,334],index=["a","b","c","d","e"])
b

b["a"]

b["a":"d"]




#%% dictionary to pandas

sozluk={"reg":12,"log":45,"knn":78}

seri2=pd.Series(sozluk)
seri2


#%% 2 seriyi birleştirmek

pd.concat([seri,seri2])

#%% Eleman işlemleri

a=np.array([11,2,62,3,4,])
seri=pd.Series(a)
seri

seri[2]

seri[0:4]


b=pd.Series([33,4,5,3,334],index=["a","b","c","d","e"])


b.index

b.keys

list(b.items())
b.values


#%% Eleman sorgulama


seri=pd.Series([33,4,5,3,334],index=["asd","gf","jh","d","e"])

"asd" in seri




#%% fancy eleman


seri=pd.Series([33,4,5,3,334],index=["asd","gf","jh","d","e"])

seri[["gf","e"]]

seri["gf"]=6

seri["gf"]
seri


#%% Pandas dataFrame olusturma

l=[7,6,4,3,6,87]

seri=pd.DataFrame(l,columns=["degisken_ismi"])
seri

m=np.arange(1,10).reshape((3,3))
m

pd.DataFrame(m,columns=["var1","var2","var3"])





#%% df isimlendirme


df=pd.DataFrame(m,columns=["var1","var2","var3"])

df.columns=["deg1","deg2","deg3"]
df

type(df)
df.axes

df.shape
df.ndim

df.size

df.values
type(df.values)

df.tail()

#%% df eleman işlemleri
import pandas as pd
import numpy as np

s1=np.random.randint(10,size=5)
s2=np.random.randint(10,size=5)
s3=np.random.randint(10,size=5)

sozluk={"var1": s1,"var2": s2,"var3": s3}
sozluk
type(sozluk)


df=pd.DataFrame(sozluk)
df

df[0:2]

df.index

df.index=["a","b","c","d","e"]
df

df["b":"d"]

#silme

df.drop("a",axis=0)

df

df.drop("a",axis=0,inplace=True)
df

#fancy

l=["c","d"]

df.drop(l,axis=0)

df

df.drop(l,axis=0)

df

"var1" in df

df["var4"]=df["var1"] / df["var2"]

df

df.drop("var4",axis=1,inplace=True)
df


#%% # gözlem ve değişken seçimi loc ve iloc

import numpy as np 
import pandas as pd


a=np.random.randint(1,30,size=(10,3))
columns=["var1","var2","var3"]
df=pd.DataFrame(a,columns=columns)
df





df.iloc[0,0]

df.loc[0:3,"var3"]

#ya da

df.iloc[0:3]["var3"]

"""

loc tanımlandıgı gibi işlem yapar [0:3]   0 1 2 3
iloc ise klasik tarzda işlem yapar [0:3]  0 1 2    (3 dahil değil)

df.loc[0:3,"var3"]
Out[41]: 
0     5
1    22
2    26
3    10


df.iloc[0:3]["var3"]
Out[43]: 
0     5
1    22
2    26


"""


#%% kosullu eleman işlemleri

a=np.random.randint(1,30,size=(5,3))
columns=["var1","var2","var3"]
df=pd.DataFrame(a,columns=columns)
df


df[df.var1 > 15]

"""
Out[47]: 
   var1  var2  var3
0    22    11    28
1    23     5    28
2    22    22    25
3    10    18     6
4    27    12    26

df[df.var1 > 15]
Out[48]: 
   var1  var2  var3
0    22    11    28
1    23     5    28
2    22    22    25
4    27    12    26

"""

#%% birleştirme joınişlemleri 

import numpy as np
import pandas as pd

a=np.random.randint(1,30,size=(5,3))
columns=["var1","var2","var3"]
df1=pd.DataFrame(a,columns=columns)
df1


df2=df1+99
df2

satır=pd.concat([df1,df2],axis=0)
satır

sutun=pd.concat([df1,df2],axis=1)
sutun

satır

# ?pd.concat

satır=pd.concat([df1,df2],ignore_index=True)
satır

df.columns
sutun=pd.concat([df1,df2],axis=1,ignore_index=True)
sutun

#%%


import pandas as pd
#birebir birlestirme
df1 = pd.DataFrame({'calisanlar': ['Ali', 'Veli', 'Ayse', 'Fatma'],
                    'grup': ['Muhasebe', 'Muhendislik', 'Muhendislik', 'İK']})

df1

df2 = pd.DataFrame({'calisanlar': ['Ayse', 'Ali', 'Veli', 'Fatma'],
                    'ilk_giris': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)

pd.merge(df1, df2, on = "calisanlar")

#coktan teke 
df3 = pd.merge(df1, df2)
df3

df4 = pd.DataFrame({'grup': ['Muhasebe', 'Muhendislik', 'İK'],
                    'mudur': ['Caner', 'Mustafa', 'Berkcan']})

df4

pd.merge(df3,df4)

# çoktan çoka
df5 = pd.DataFrame({'grup': ['Muhasebe', 'Muhasebe',
                              'Muhendislik', 'Muhendislik', 'İK', 'İK'],
                    'yetenekler': ['matematik', 'excel', 'kodlama', 'linux',
                               'excel', 'yonetim']})

df5

df1

pd.merge(df1, df5)


#%% toplulastırma 

import pandas as pd
import numpy as np
import seaborn as sns

df=sns.load_dataset("planets")

df.head()
df.shape

df.mean()

df["mass"].mean()

df.describe().T


#%%gruplastırma


df.groupby("method").count()

df.groupby("method").mean()


df.groupby("method")["orbital_period"].mean()
df.groupby("method")["mass"].mean()



#%% groupby

df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])
df


df.groupby("gruplar").mean()

df.groupby("gruplar").sum()

df=sns.load_dataset("planets")

df.head()
df.shape

df.groupby("method").count()
df.groupby("method").mean()
df.groupby("method").sum()


df.groupby("method")["orbital_period"].mean()

df.groupby("method")["orbital_period"].describe()



#%% Aggregate


import pandas as pd
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])
df


df.groupby("gruplar").mean()

#Aggregate
df.groupby("gruplar").aggregate([min, np.median, max])

df.groupby("gruplar").aggregate({"degisken1": "min", "degisken2": "max"})


#%% filter

import pandas as pd
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])
df

def filter_func(x):
    return x["degisken1"].std() > 9

df.groupby("gruplar").std()

df.groupby("gruplar").filter(filter_func)


#%%transform

#
import pandas as pd
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])
df

df["degisken1"]*9
df

df_a = df.iloc[:,1:3]
df_a
df_a.transform(lambda x: (x-x.mean()) / x.std())





#%% apply


import pandas as pd
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])
df

df.apply(np.sum)

df.groupby("gruplar").apply(np.mean)


#%% Pivot tablollar

import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()

titanic.groupby("sex")[["survived"]].mean()

titanic.groupby(["sex","class"])[["survived"]].aggregate("mean").unstack()

#%% pivot ile table
titanic.pivot_table("survived", index = "sex", columns = "class")

titanic.age.head()


age = pd.cut(titanic["age"], [0, 18, 90])
age.head(10)

titanic.pivot_table("survived", ["sex", age], "class")

#%% Dış Kaynaklı Veri Okumak

import pandas as pd

"""

Signature:
pd.read_csv(
    filepath_or_buffer,
    sep=',',
    delimiter=None,
    header='infer',
    names=None,
    index_col=None,
    usecols=None,
    squeeze=False,
    prefix=None,
    mangle_dupe_cols=True,
    dtype=None,
    engine=None,
    converters=None,
    true_values=None,
    false_values=None,
    skipinitialspace=False,
    skiprows=None,
    skipfooter=0,
    nrows=None,
    na_values=None,
    keep_default_na=True,
    na_filter=True,
    verbose=False,
    skip_blank_lines=True,
    parse_dates=False,
    infer_datetime_format=False,
    keep_date_col=False,
    date_parser=None,
    dayfirst=False,
    iterator=False,
    chunksize=None,
    compression='infer',
    thousands=None,
    decimal=b'.',
    lineterminator=None,
    quotechar='"',
    quoting=0,
    doublequote=True,
    escapechar=None,
    comment=None,
    encoding=None,
    dialect=None,
    tupleize_cols=None,
    error_bad_lines=True,
    warn_bad_lines=True,
    delim_whitespace=False,
    low_memory=True,
    memory_map=False,
    float_precision=None,
)



"""











