# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 16:43:48 2025

@author: maddi
"""
#importing necassery packages
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sub_gal.csv')#reading the data that is needed
data_new = data[(data['zsp'] > 0) & (data['z_best'] > 0)]
#removing zeros and other non-physical values

"""creating the histogram plots"""
plt.figure()#begins the plot
#plt.subplot(2, 1, 1)#2 by 1 subplot, the first one
plt.hist(data_new['zsp'],  alpha = 0.6, bins = 40, label = 'zsp')
#the first histogram for zsp values
plt.hist(data_new['z_best'], alpha = 0.5, bins = 40, color = 'red', label = 'z_best')
#the second histogram for z_best values
plt.ylabel('Frequency')
plt.xlabel('zsp and z_best')
plt.title('Comparison of zsp and z_best')#creating the title for the z_best values histogram

plt.show()#shows the plots
