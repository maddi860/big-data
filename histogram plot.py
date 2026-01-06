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

"""creating the histogram plots"""
plt.figure()#begins the plot
plt.subplot(2, 1, 1)
plt.hist(data_new['zsp'], bins = 30, alpha = 0.6)
#the first histogram for zsp values
plt.title('zsp')



plt.subplot(2, 1, 2)
plt.hist(data_new['z_best'], alpha = 0.5, bins = 30, color = 'red')
#the second histogram for z_best values
plt.title('z_best')


plt.show()#shows the plots
