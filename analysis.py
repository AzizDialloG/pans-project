
"""
Thierno Aziz Diallo
Pans Project 2020


"""

import os
import matplotlib.pyplot as plt
import pandas as pd

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



data = pd.read_csv(path + 'iris.csv')
#data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width","species"]
col = data.columns
commutes0 = pd.Series(data[col[0]])
commutes0.plot.hist()
plt.xlabel(col[0])
plt.grid(axis='y', alpha=0.75)
plt.savefig(col[0]+'.png')
plt.show()


commutes1 = pd.Series(data[col[1]])
commutes1.plot.hist()
plt.xlabel(col[1])
plt.grid(axis='y', alpha=0.75)
plt.savefig(col[1]+'.png')
plt.show()

commutes1 = pd.Series(data[col[1]])
commutes1.plot.hist()
plt.xlabel(col[2])
plt.grid(axis='y', alpha=0.75)
plt.savefig(col[2]+'.png')
plt.show()


commutes1 = pd.Series(data[col[1]])
commutes1.plot.hist()
plt.xlabel(col[3])
plt.grid(axis='y', alpha=0.75)
plt.savefig(col[3]+'.png')
plt.show()


colors = (0,0,0)
area = 3.14*2
plt.scatter(data[col[0]], data[col[1]], s=area, c=colors, alpha=0.7)
plt.title('Scatter plot between '+ col[0]+ ' & ' + col[1])
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('Scatter plot between '+ col[0]+ '  ' + col[1]+'.png')
plt.show()

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
