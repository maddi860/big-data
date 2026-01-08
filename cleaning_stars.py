# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 10:15:37 2026

@author: maddi
"""
#importing the libraries needed
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

stars = pd.read_csv('stars.csv')#reading and selecting the data needed
stars_clean = stars.dropna(subset = ['SFR', 'L144', 'E_L144'])#removing the NaN values
stars_clean = stars[stars['L144']>0]#removes bad logs
x = stars_clean['SFR']#x = star formation rate
y = stars_clean['L144']#y = 144 MHz luminosity
yerr = stars_clean['E_L144']#y_err = error on 144 MHz luminosity

logy = np.log10(y)#logging luminosity to base 10
#error propagation:σ_z = σ_y / ylog10, σ_z = log10y_err, σ_y = y_err
log10y_err = yerr / y * np.log(10) 

#linear model will be logy =  mx + c
def linear_model(x, m, c):
    return m * x + c

#fitting the linear model
popt, pcov = curve_fit(linear_model, x, logy, sigma = log10y_err, absolute_sigma = True)
m , c = popt
m_err, c_err = np.sqrt(np.diag(pcov))
n = len(x)#number of data points

#creating the line of best fit
xfit = np.linspace(min(x), max(x), n)
yfit = linear_model(xfit, m, c)

plt.figure()#beginning the plot
plt.scatter(x, logy, label = 'Star data', alpha = 0.3, s = 10)#plotting the scatter graph
plt.plot(xfit, yfit, label = 'line of best fit', alpha = 0.6, color = 'orange')#plotting the line of best fit
plt.xlabel('Star Formation Rate')#labelling the x-axis
plt.ylabel(r'$\log_{10}(L_{144})$')#labelling the y-axis
plt.legend()#creates legend
plt.show()#prints the plot
#printing the results
print('Results:')
print(f"Slope = {m:.3f} ± {m_err:.3f}")
print(f"Intercept = {c:.3f} ± {c_err:.3f}")
print(f"Number of data points = {n}")