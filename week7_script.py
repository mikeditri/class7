#!/usr/bin/env python
#find the file
#0. Load data
#0.1   Import data file

#1. Format & Organize
#1.1   Import numpy
#1.2   Import pandas
#1.3   Read data file using pandas library and deternmine if there is a header row or not
#1.3.1      pandas.read_csv(my_csv_file, Header=None)
#1.4   View the shape of the data
from argparse import ArgumentParser

parser= ArgumentParser(description='A CSV reader + stats maker')
parser.add_argument('csvfile', help='path to input file csv file.')

parsed_args = parser.parse_args()

my_csv_file = parsed_args.csvfile

import os

assert os.path.isfile(my_csv_file) , "please give us a real file"

import pandas as pd

#READ CSV

data = pd.read_csv(my_csv_file, header=None)

#View the shape of the data
#Space
print()
print("Data Shape:",data.shape)

#2. Summary Statistics
#2.1   Use Numpy to calculate summary statistics like mean, standard deviation etc
#2.1.1      numpy.mean(data)
#2.1.2      numpy.std(data)
import numpy as np
#Space
#3. Add Headers
data.columns = ["Class","Alcohol","Malic Acid","Ash","Alcalinity of ash", "Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280 OD315 of diluted wines","Proline"]
print()
print("Mean of Each Variable")
print(np.mean(data))
#Space
print()
print("Standard deviation of Each Variable")
print(np.std(data))

#4. Look at it
#4.1 Plot values on histograms
#    import matplotlib
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
#4.1.1  for each column:
#           get values
#           plot histogram
#           save to file as column_name.png
x_label = (list(data.columns.values))

for i in data:
    idx = data.columns.get_loc(i)
    fig = plt.hist(data.iloc[:,idx])
    plt.xlabel(i)
    plt.ylabel("Count")
    plt.savefig(i+'_hist.png')
    plt.clf()

#fig =  plt.hist(data.iloc[:,13])
#plt.xlabel(x_label[13])
#plt.ylabel("Count")
#plt.savefig("xlabel.png")

#
#4.2 Plot pairs
#4.2.1  for each pair of columns:
#           plot scatter
#           save to file as column_name1_vs_column_name2_scatter.png

#shows as a matrix

#axs = pd.scatter_matrix(data)
#n = len(data.columns)
#for i in range(n):
#	for j in range(n):
#		ax = axs[i,j]
#		ax.xaxis.label.set_rotation(90)
#		ax.yaxis.label.set_rotation(0)
#		ax.yaxis.labelpad = 50
#plt.show()		

##n = len(data.columns)
		
##for i in range(n):
##	for j in range(i):
##		plt.scatter(data.iloc[:,i],data.iloc[:,j])
##		i_name = data.columns[i]
##		j_name = data.columns[j]
##		plt.xlabel(i_name)
##		plt.ylabel(j_name)
##		plt.savefig(i_name+'_vs_'+j_name+'scatter_pairs.png')
##		plt.clf()
		
#fig =  plt.scatter(data.iloc[:,0],data.iloc[:,1])
#plt.xlabel(x_label[0])
#plt.ylabel(x_label[1])
#plt.show()

#
#4.3 Plot pair-wise correlation matrix as a heatmap
correlations = data.corr()
names = data.columns
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,14,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names,rotation = 90)
ax.set_yticklabels(names, rotation = 0)
plt.savefig('correlation_matrix.png')

import seaborn as sns
from tqdm import tqdm

n = len(data.columns)

for i in tqdm(range(n)):
	for j in range(i):
		for k in range(j):
			i_name = data.columns[i]
			j_name = data.columns[j]
			k_name = data.columns[k]
			sns.relplot(x=i_name,y=j_name,data=data, hue= 'Class',legend='brief',size=k_name,sizes=(15, 200))
			plt.xlabel(i_name)
			plt.ylabel(j_name)
			plt.savefig(i_name+'_vs_'+j_name+'_size_'+k_name+'_scatter_pairs.png')
			plt.clf()
		


#sns.relplot(x=data.columns[0],y="Alcohol",data=data, hue= 'Class',legend='brief',size='Ash',sizes=(15, 200))
#plt.show()
