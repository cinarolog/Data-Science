# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:44:49 2022

@author: cinar
"""

"""
             DATA VISUALIZATION
"""
#%% import libraries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly 

#%% barplot

import seaborn as sns
diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()
df.head()

#kategorik değişkenlerin
df.cut.value_counts().plot.barh() ;
df.cut.value_counts().plot.barh().set_title("Cut değişkeninin frekansları")

# ya da şu sekilde  yapabiliriz
(df.cut
 .value_counts()
 .plot.barh()
 .set_title("Cut değişkeninin frekansları"))


#%% seaborn

import seaborn as sns

sns.barplot(x="cut",y=df.cut.index,data=df)

#%% Çaprazlamalar

import seaborn as sns
from pandas.api.types import CategoricalDtype
diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()
cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories = cut_kategoriler, ordered = True))
df.head()


sns.catplot(x="cut",y="price",data=df)

df.color.value_counts()
"""
G    11292
E     9797
F     9542
H     8304
D     6775
I     5422
J     2808
"""
sns.barplot(x="cut",y="price",hue="color",data=df)


df.groupby(["cut","color"])["price"].mean()
"""

   ****************  DOĞRULAMA İŞLEMİ  ***********
   
cut        color
Fair       D        4291.061350
           E        3682.312500
           F        3827.003205
           G        4239.254777
           H        5135.683168
           I        4685.445714
           J        4975.655462
        Good       D        3405.382175
                   E        3423.644159
                   F        3495.750275
                   G        4123.482204
                   H        4276.254986
                   I        5078.532567
                   J        4574.172638
                Very Good  D        3470.467284
                           E        3214.652083
                           F        3778.820240
                           G        3872.753806
                           H        4535.390351
                           I        5255.879568
                           J        5103.513274
                    Premium    D        3631.292576
                               E        3538.914420
                               F        4324.890176
                               G        4500.742134
                               H        5216.706780
                               I        5946.180672
                               J        6294.591584
                        Ideal      D        2629.094566
                                   E        2597.550090
                                   F        3374.939362
                                   G        3720.706388
                                   H        3889.334831
                                   I        4451.970377
                                   J        4918.186384

"""


#%% Histogram ve Yoğunluk Grafiğinin Oluşturulması

"""   sayısal değişkenler için    """

import seaborn as sns
from pandas.api.types import CategoricalDtype
diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()

sns.distplot(df.price,kde=False)

sns.distplot(df.price,kde=True)

?sns.distplot
"""
Signature:
sns.distplot(
    a=None,
    bins=None,
    hist=True,
    kde=True,
    rug=False,
    fit=None,
    hist_kws=None,
    kde_kws=None,
    rug_kws=None,
    fit_kws=None,
    color=None,
    vertical=False,
    norm_hist=False,
    axlabel=None,
    label=None,
    ax=None,
    x=None,
)
"""


sns.distplot(df.price,bins=1000,kde=False)
sns.distplot(df.price,bins=10,kde=False)

sns.distplot(df.price)
sns.distplot(df.price,hist=False)

?sns.kdeplot
"""
Signature:
sns.kdeplot(
    x=None,
    *,
    y=None,
    shade=None,
    vertical=False,
    kernel=None,
    bw=None,
    gridsize=200,
    cut=3,
    clip=None,
    legend=True,
    cumulative=False,
    shade_lowest=None,
    cbar=False,
    cbar_ax=None,
    cbar_kws=None,
    ax=None,
    weights=None,
    hue=None,
    palette=None,
    hue_order=None,
    hue_norm=None,
    multiple='layer',
    common_norm=True,
    common_grid=False,
    levels=10,
    thresh=0.05,
    bw_method='scott',
    bw_adjust=1,
    log_scale=None,
    color=None,
    fill=None,
    data=None,
    data2=None,
    warn_singular=True,
    **kwargs,
)
"""

sns.kdeplot(df.price,shade=True)



#%% Histogram ve Yoğunluk Çaprazlamalar

sns.kdeplot(df.price,shade=True)


(sns
 .FacetGrid(df,
              hue = "cut",
              height = 5,
              xlim = (0, 10000))
 .map(sns.kdeplot, "price", shade= True)
 .add_legend()
);




sns.catplot(x = "cut", y = "price", hue = "color", kind = "point", data = df);




#%% Boxplot

import seaborn as sns

tips = sns.load_dataset("tips")
df = tips.copy()
df.head()



df.describe().T

df["sex"].value_counts()
df["smoker"].value_counts()
df["day"].value_counts()
df["time"].value_counts()

"""

Male      157
Female     87
Name: sex, dtype: int64
 
No     151
Yes     93
Name: smoker, dtype: int64

Sat     87
Sun     76
Thur    62
Fri     19
Name: day, dtype: int64

Dinner    176
Lunch      68
Name: time, dtype: int64

"""


sns.boxplot(df["total_bill"])
# sns.boxplot(df.total_bill)
 
sns.boxplot(x=df["total_bill"] , orient="v");



#%% Çaprazlamalar

df.describe().T


#Hangi günler daha fazla kazanıyoruz


sns.boxplot(x="day",y="total_bill",data=df)

sns.boxplot(df.day,df.total_bill)
df["day"].value_counts()
df.groupby(["total_bill"])["day"].value_counts().count()


#  sabahh mı  yoksa akşammı daha fazla kaznıyoruz


df["time"].value_counts()
"""
Dinner    176
Lunch      68"

"""
df
sns.boxplot(df.time,df.total_bill)

df.groupby(["time"])["total_bill"].mean()
# Lunch     17.168676
# Dinner    20.797159

df.groupby(["time"])["total_bill"].median()
# Lunch     15.965
# Dinner    18.390


# kişi sayaısı kazanç

sns.boxplot(x="size",y="total_bill",data=df)

df.groupby(["size"])["total_bill"].mean()
# 1     7.242500
# 2    16.448013
# 3    23.277632
# 4    28.613514
# 5    30.068000
# 6    34.830000inner    20.797159

df.groupby(["size"])["total_bill"].median()
# 1     7.915
# 2    15.370
# 3    20.365
# 4    25.890
# 5    29.850
# 6    32.050


sns.boxplot(x=df["day"],y=df["total_bill"],hue=df["sex"],data=df)
sns.boxplot(x=df.day,y=df.total_bill,hue=df.sex)



#%% Violin Grafiği

df.head()
"""
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
"""
sns.catplot(y="total_bill",kind="violin", data=df)


sns.catplot(x="day",y="total_bill",kind="violin", data=df)


sns.catplot(x="day",y="total_bill",hue="sex",kind="violin", data=df)


#%% Korelasyon Grafiğinin oluşturulması Scatter plot

#scatterplot

sns.scatterplot(x=df.total_bill,y=df.tip)
# sns.scatterplot(x="total_bill",y="tip",data=df)

sns.scatterplot(x="total_bill",y="tip",hue="time",data=df)
df.groupby(["tip"])["time"].value_counts()

sns.scatterplot(x="total_bill",y="tip",hue="day",style="time",data=df)

sns.scatterplot(x="total_bill",y="tip",size="size",data=df)

sns.scatterplot(x="total_bill",y="tip",hue="day",size="size",style="time",data=df,)

sns.scatterplot(x="total_bill",y="tip",hue="size",size="size",style="time",data=df,)


#%% Doğrusal ilişkilerin gösterilmesi

import seaborn as sns 
import matplotlib.pyplot as plt

sns.lmplot(x="total_bill",y="tip",data=df)

sns.lmplot(x="total_bill",y="tip",hue="smoker",col="time",data=df)

sns.lmplot(x="total_bill",y="tip",hue="smoker",col="time",row="sex",data=df)


#%% scatterplot matrisi

import seaborn as sns

iris = sns.load_dataset("iris")
df = iris.copy()
df.head()
"""
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
"""


df.dtypes
"""
sepal_length    float64
sepal_width     float64
petal_length    float64
petal_width     float64
species          object
"""
df.shape

df.info


sns.pairplot(df,hue="species")

sns.pairplot(df,hue="species",markers=["o","s","D"])

sns.pairplot(df,hue="species",kind="reg",markers=["o","s","D"])



#%% Isı haritası heat map

import seaborn as sns

flights = sns.load_dataset("flights")
df = flights.copy()
df.head()

"""
   year month  passengers
0  1949   Jan         112
1  1949   Feb         118
2  1949   Mar         132
3  1949   Apr         129
4  1949   May         121
"""

df.shape

df.describe().T

df=df.pivot("month","year","passengers")
df

"""
year   1949  1950  1951  1952  1953  1954  1955  1956  1957  1958  1959  1960
month                                                                        
Jan     112   115   145   171   196   204   242   284   315   340   360   417
Feb     118   126   150   180   196   188   233   277   301   318   342   391
Mar     132   141   178   193   236   235   267   317   356   362   406   419
Apr     129   135   163   181   235   227   269   313   348   348   396   461
May     121   125   172   183   229   234   270   318   355   363   420   472
Jun     135   149   178   218   243   264   315   374   422   435   472   535
Jul     148   170   199   230   264   302   364   413   465   491   548   622
Aug     148   170   199   242   272   293   347   405   467   505   559   606
Sep     136   158   184   209   237   259   312   355   404   404   463   508
Oct     119   133   162   191   211   229   274   306   347   359   407   461
Nov     104   114   146   172   180   203   237   271   305   310   362   390
Dec     118   140   166   194   201   229   278   306   336   337   405   432
"""

sns.heatmap(df,annot=True,fmt="d")

sns.heatmap(df,annot=True,fmt="d",linewidths=.5)


#%% Çizgi grafik


import seaborn as sns

fmri = sns.load_dataset("fmri")
df = fmri.copy()
df.head()

"""
  subject  timepoint event    region    signal
0     s13         18  stim  parietal -0.017552
1      s5         14  stim  parietal -0.080883
2     s12         18  stim  parietal -0.081033
3     s11         18  stim  parietal -0.046134
4     s10         18  stim  parietal -0.037970

"""

df.shape

df.info()

"""
---  ------     --------------  -----  
 0   subject    1064 non-null   object 
 1   timepoint  1064 non-null   int64  
 2   event      1064 non-null   object 
 3   region     1064 non-null   object 
 4   signal     1064 non-null   float64
"""

df.groupby("timepoint")["signal"].count()


sns.lineplot(x = "timepoint", y = "signal", data = df);

sns.lineplot(x = "timepoint", y = "signal",hue="event",style="event", data = df);


sns.lineplot(x = "timepoint", 
             y = "signal", 
             hue = "event", 
             style = "event", 
             markers = True,  dashes = False, data = df);



sns.lineplot(x = "timepoint", 
             y = "signal", 
             hue = "region", 
             style = "event", 
             data = df);


#%% Basit Zaman serisi grafiği

import pandas_datareader as pr

df = pr.get_data_yahoo("AAPL", start = "2016-01-01", end = "2019-08-25")


df.head()
close=df["Close"]

close.head()
"""
2016-01-04    26.337500
2016-01-05    25.677500
2016-01-06    25.174999
2016-01-07    24.112499
2016-01-08    24.240000
"""
close.shape

close.plot()


close.index

close.index=pd.DatetimeIndex(close.index)















