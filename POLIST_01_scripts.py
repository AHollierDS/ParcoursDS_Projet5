import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
  
#-----------------------------------------------------------------------------
def plot_df_sizes(df_list):
    """ Function returning a visualisation showing the number of elements and 
    availiable data for each data set in df_list """
    
    # Initialization
    missing_data = []
    availiable_data = []
    dataset_percent_missing = []
    datasets = []
    dataset_sizes = []

    # Calculating availiable and missing data
    for df in df_list:
        count_NaN = df.isnull().sum().sum()
        percent_NaN = 100 * round(count_NaN / df.size,3)
    
        missing_data.append(count_NaN)
        availiable_data.append(df.size - count_NaN)
        dataset_percent_missing.append(percent_NaN)
        datasets.append(df.name)
        dataset_sizes.append(df.size)
        
    # Visual representation
    pivot = pd.DataFrame({'Dataset sizes':dataset_sizes,
                          'Availiable data':availiable_data},
                        index = datasets)
    pivot.plot.bar(figsize = (10,7), rot = 0)
    plt.yscale('log')
    plt.title("Elements in datasets")
    plt.ylabel("Number of elements")
    plt.gca().yaxis.grid(True)
    
#-----------------------------------------------------------------------------
def check_keys(left, right, key=None, l_key = None, r_key = None):
    """ Returns the number of keys in right absent from left and number of 
    keys in left absent from right """
    
    if (l_key !=None) and (r_key !=None):
        nb_miss_right = len(right[~right[r_key].isin(left[l_key])])
        nb_miss_left = len(left[~left[l_key].isin(right[r_key])])
    elif key != None:
        nb_miss_right = len(right[~right[key].isin(left[key])])
        nb_miss_left = len(left[~left[key].isin(right[key])])
    else:
        pass

    return(nb_miss_right, nb_miss_left)

#-----------------------------------------------------------------------------
def plot_cluster_descr(data, columns, clusters, title):
    
    df_ = data.groupby(by = clusters).mean()[columns]
    df_.plot(kind = 'bar', figsize = (20,5), rot = 0)
    
    plt.legend(bbox_to_anchor=(1,1,0,0))
    plt.grid(True)
    plt.xlabel('Clusters', backgroundcolor = 'lightgrey')
    plt.title(title, fontweight = 'bold')
    
    plt.show()
