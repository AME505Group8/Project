#importing needed libraries

import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline
import numpy as np
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

#definition of function
def dendrogram(input1, input2):

    #reading data from pkl file
    data = pd.read_pickle('BIRD_STRIKE_REDUCED.pkl')
    text = pd.read_pickle('BIRD_STRIKE_REDUCED.pkl')

    #taking text to have it legible for graph output
    textarray = text.to_numpy()

    data.shape
    data.head()

    #print to check data
    print(data.head())

    #done to show the column names
    print(data.columns.values)

    #list of avaialble columns
    columns = ['INCIDENT_MONTH','TIME_OF_DAY','STATE','AC_CLASS','PHASE_OF_FLIGHT','count']

    i1 = columns.index(input1)

    i2 = columns.index(input2)

    print(i1)

    print(i2)

    #inputs converted to data for graph
    data = data.iloc[:, [0,i1,i2]].values

    print(data)

    #creation of dendrogram
    plt.figure(figsize=(10, 7))
    plt.title("Dendrogram"+' '+input1+' '+"vs" +' '+input2)
    dend = shc.dendrogram(shc.linkage(data, method='ward'))
    plt.axhline(y=450, color='r', linestyle='--')

    #tick marks to make graph more presentable
    my_xticks = textarray[:, i1]
    my_yticks = textarray[:, i2]

    #generation of clusters for plot
    cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    cluster.fit_predict(data)

    #plot definition and printing
    plt.figure(figsize=(10, 7))
    plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow')
    plt.xlabel(input1)
    plt.ylabel(input2)
    plt.xticks(data[:,0], my_xticks)
    plt.yticks(data[:,1], my_yticks)
    plt.show()