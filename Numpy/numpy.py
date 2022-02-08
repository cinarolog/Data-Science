# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 00:10:23 2022

@author: cinar
"""


#%%

import numpy as np

a=np.array([1,3,6,3,7])

type(a)

np.array([2.45,4,8,5,9])
np.array([2.45,4,8,5,9],dtype="float 32")
np.array([2.45,4,8,5,9],dtype="int")


#%% sifirdan veri olusturma

np.ones(10,dtype="int")

np.zeros((3,5),dtype="int")

np.arange(0,31,3)

np.linspace(0,1,10)

np.random.normal(10,4,(3,4))

np.random.randint(0,10,(3,5))



#%% np array özellikleri

b=np.random.randint(10,size=8)

b.ndim
b.shape
b.size
b.dtype

c=np.random.randint(10,size=(3,5))

c.ndim
c.shape
c.size
c.dtype


#%% yeniden şekillendirme Reshaping

x=np.arange(1,10)
x
x.ndim

y=x.reshape((1,9))
y.ndim



#%% Birleştirme concatenation

m=np.array([1,2,3])
n=np.array([4,5,6])
k=np.concatenate([m,n])
k
w=np.array([7,8,9])

h=np.concatenate([k,w])
h.ndim
h

#2 boyut için

s=np.concatenate([[1,2,3],[4,5,6]])

np.concatenate([[s,s]],axis=0)
np.concatenate([[s,s]],axis=1)



#%%array ayırma splitting

x=np.array([1,2,3,99,99,3,2,1])
np.split(x,[3,5])

a,b,c=np.split(x,[3,5])

a
b
c

# 2 boyutlu ayırma

m=np.arange(16).reshape(4,4)
m

ust,alt=np.vsplit(m,[2])

ust
alt

sag,sol=np.hsplit(m,[2])
sag
sol

#%% sorting sıralama

v=np.array([7,5,2,4,8,9])
np.sort(v)
v

v.sort()
v

#2boyutta sıralama

g=np.random.normal(20,5,(3,3))

np.sort(g,axis=0)

np.sort(g,axis=1)




#%% index ile elemanlara erişmek

a=np.random.randint(10,size=10)
a

a[0]


a[0]=100
a


m=np.random.randint(10,size=(3,5))
m

m[2,2]

m[1,3]=5
m



#%% array alt kume işlemleri slicing


a=np.arange(20,30)

a[0:3]
a[2:5]
a[2:]


a[1::2]
a[0::3]

# 2bbyutlu

m=np.random.randint(10,size=(5,5))
m

m[:,0]
m[:,1:3]


m[0,:]
 
m[0:2,0:3]

m[:,0:2]


m[1:3,0:2]

#%%alt kume uzerinde işlem yapmak


a=np.random.randint(10,size=(5,5))
a
a_x=a[0:2,:2]
a_x
a_x[0,0]=111
a_x[1,1]=2222
a_x

a_y=a[0:3,0:2]
a_y


a_y[0,1]=3333
a_y[1,2]=4444


#%% fancy index slice

v=np.arange(0,30,3)
v

al_getir=[1,3,5]
v[al_getir]

# 2boyutta fancy

m=np.arange(9).reshape(3,3)
m
m[0:,[1,2]]



#%% koşullu eleman işlkemleri

v=np.array([1,2,3,4,5])
v

v<3
v>2

v[v<3]
v[v>=2]

v*2

#(matematıksel işlemleri yapabılrıxz)


#%% matematıksel işlemler

v=np.array([1,2,3,4,5])
v
v-1

#ufunc

?np


#cheetsheet

  