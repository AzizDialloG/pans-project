#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:51:22 2020

@author: adiallo
Thierno Aziz Diallo
Pans Project 2020
"""

import os #operating system import to get paths
import matplotlib.pyplot as plt #to plot graphs
import pandas as pd #to read/write data


#Reading the dataset
base_path = os.getcwd()
listOfFolders = os.listdir(os.getcwd())
folder = 'Iris-data' 
path = ''
try:
    if folder in listOfFolders:
        path = base_path + folder 
        print('found')
except:
    print('Create folder with Iris-data and put iris.csv in it.')



data = pd.read_csv(path + 'iris.csv') #reading data from disk
#data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width","species"]
col = data.columns #storing columns of data in col list

#computer histogram of speal length
commutes0 = pd.Series(data[col[0]])  #gets data , and make object of histogram
commutes0.plot.hist() #plot histogram
plt.xlabel(col[0]) #writing x label
plt.grid(axis='y', alpha=0.75)
plt.savefig(col[0]+'.png') #saving figure to disk
plt.show() #show graph on runtime

#computer histogram of speal width
commutes1 = pd.Series(data[col[1]])
commutes1.plot.hist()
plt.xlabel(col[1])
plt.grid(axis='y', alpha=0.75)
plt.savefig(col[1]+'.png')
plt.show()

#computer histogram of petal length
commutes1 = pd.Series(data[col[1]])
commutes1.plot.hist()
plt.xlabel(col[2])
plt.grid(axis='y', alpha=0.75)
plt.savefig(col[2]+'.png')
plt.show()

#computer histogram of petal width
commutes1 = pd.Series(data[col[1]])
commutes1.plot.hist()
plt.xlabel(col[3])
plt.grid(axis='y', alpha=0.75)
plt.savefig(col[3]+'.png')
plt.show()


#scatter plot 
colors = (0,0,0) #assign color
area = 3.14*2 #size of circle on scatter plot
plt.scatter(data[col[0]], data[col[1]], s=area, c=colors, alpha=0.7) #ploting scatter plot between two variables
plt.title('Scatter plot between '+ col[0]+ ' & ' + col[1]) #title of scatter plot
plt.xlabel('x') #x-axis label 
plt.ylabel('y') #y-axis label
plt.savefig('Scatter plot between '+ col[0]+ '  ' + col[1]+'.png') #save figure to the disk with column name
plt.show() #show graph

plt.scatter(data[col[2]], data[col[3]], s=area, c=colors, alpha=0.7)
plt.title('Scatter plot between '+ col[2]+ ' & ' + col[3])
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('Scatter plot between '+ col[2]+ '  ' + col[3]+'.png')
plt.show()


plt.scatter(data[col[0]], data[col[2]], s=area, c=colors, alpha=0.7)
plt.title('Scatter plot between '+ col[0]+ ' & ' + col[2])
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('Scatter plot between '+ col[0]+ ' ' + col[2]+'.png')
plt.show()


plt.scatter(data[col[1]], data[col[3]], s=area, c=colors, alpha=0.7)
plt.title('Scatter plot between '+ col[1]+ ' &' + col[3] )
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('Scatter plot between '+ col[1]+ ' ' + col[3]+'.png')
plt.show()

#To Describe data:
for col in data.columns:
    print(col)
    print(data[col].describe())
    print()
