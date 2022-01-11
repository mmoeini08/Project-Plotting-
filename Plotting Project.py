# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 11:48:27 2022

@author: mmoein2
"""

#Libraries needed to run the tool
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Ask for file name
file_name = 'TSS'
file_header = input("File has labels and header (Y):")

#Create a pandas dataframe from the csv file.      
if file_header == 'Y' or file_header == 'y':
    data = pd.read_csv(file_name + '.csv', header=0, index_col=0) #Remove index_col = 0 if rows do not have headers
else:
    data = pd.read_csv(file_name + '.csv', header=None)

#Print number of rows and colums read
print("{0} rows and {1} columns".format(len(data.index), len(data.columns.values)))
print('')

#Mean, median, and standard deviation
variable = data.TSS
print("Count: {0}".format(len(variable)))
print("Mean: {0}".format(round(variable.mean(),2)))
print("Median: {0}".format(round(variable.median(),2)))
print("Std Dev: {0}".format(round(variable.std(),2)))
print("Min: {0}".format(round(variable.min(),2)))
print("25th perc: {0}".format(round(variable.quantile(0.25), 2)))
print("50th perc: {0}".format(round(variable.quantile(0.5), 2)))
print("75th perc: {0}".format(round(variable.quantile(0.75), 2)))
print("Max: {0}".format(round(variable.max(),2)))
print("")

print(data.describe()) #See the difference betweent the count above and the count in Pandas.
print("")

#Plot a boxplot
boxplot = input("Plot a boxplot (Y):")
if boxplot == 'Y' or boxplot == 'y':
    sns_boxplot = sns.boxplot(x=data.IP, y=data.TSS) #Boxplot of selected variable over categories
    sns_boxplot.get_figure().savefig(file_name + "_boxplot.png")
    plt.show()
    
#Plot a pairplot
pairplot = input("Plot a pairplot (Y):")
if pairplot == 'Y' or pairplot == 'y':
    sns_pairplot = sns.pairplot(data, diag_kind="hist")
    # sns_pairplot = sns.pairplot(data, vars=['DA', 'PR'], hue='TSS')
    sns_pairplot.savefig(file_name + "_pairplot.png")
    plt.show()

#Plot a jointplot
jointplot = input("Plot a jointplot (Y):")
if jointplot == 'Y' or jointplot == 'y':
    print(data.columns.values)
    x_var = input("X variable:")
    y_var = input("Y variale:")
    sns_jointplot = sns.jointplot(x=data[x_var], y=data[y_var]) #, kind="kde")
    sns_jointplot.savefig(file_name + "_jointplot.png")
    plt.show()

#Goodbye message
print('')
print("Good Bye")
