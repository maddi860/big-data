# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 16:43:48 2025

@author: maddi
"""
#importing necassery packages
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib auto

data = pd.read_csv('sub_gal.csv')#reading the data that is needed
data_new = data[(data['zsp'] > 0) & (data['z_best'] > 0)]
#removing zeros and other non-physical values

"""creating the histogram plot"""
plt.figure()#begins the plot
plt.hist(data_new['zsp'], bins = 30, alpha = 0.6, label = 'zsp', 
         density = True, range = (0, 1), histtype="step", linewidth=2,)
#the first histogram for zsp values
plt.hist(data_new['z_best'], alpha = 0.5, bins = 30, label = 'z_best', 
         density = True, range = (0, 1), histtype="step", linewidth=2,)
#the second histogram for z_best values
plt.title('Comparison of zsp and z_best')
"""I have used the labels Redshift and Density because I have used
Density = True which shows the probability density making the plot more easy 
to read. The area under each histogram is equal to one. 
For Redshift, each bin groups the values into ranges."""
plt.xlabel('Redshift')#creates a label for the x-axis
plt.ylabel('Density')#creates a label for the y-axis
plt.legend()#shows which histogram plot is for each data using the labels made
plt.show()#shows the plot
