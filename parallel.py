# -*- coding: utf-8 -*-
'''
Created on Thu Jan  8 12:17:16 2026

@author: maddi
'''
#importing the necessary libraries
from multiprocessing import Pool, cpu_count
import time
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

stars = pd.read_csv('stars.csv')#reading and selecting the data needed
stars_clean = stars.dropna(subset = ['SFR', 'L144', 'E_L144'])#removing the NaN values
stars_clean = stars_clean[stars_clean['L144']>0]#removes bad logs
x = stars_clean['SFR'].values#x = star formation rate
y = stars_clean['L144'].values#y = 144 MHz luminosity
yerr = stars_clean['E_L144'].values#y_err = error on 144 MHz luminosity
n = len(x)#number of data points

logy = np.log10(y)#logging luminosity to base 10
#error propagation:
# σ_z = σ_y / ylog10
#σ_z = log10y_err, σ_y = y_err
log10y_err = yerr / (y * np.log(10)) 

#linear model will be logy =  mx + c
def linear_model(x, m, c):
    return m * x + c

def fit_once(seed):
    np.random.seed(seed)
    idx = np.random.randint(0, n, n)
    popt, _ = curve_fit(
        linear_model,
        x[idx],
        logy[idx],
        sigma=log10y_err[idx],
        absolute_sigma=True
    )
    return popt#returns the fitted slope and intercept

if __name__ == '__main__':#required for multiprocessing
    start = time.time()#start time
    n_bootstrap = 1000#number of bootstrap fits to perform
    n_cores = cpu_count()
    with Pool(processes = n_cores) as pool:#creates a pool of workers
        #divides bootstrap fits across the cpu cores
        results = pool.map(fit_once, range(n_bootstrap))
    results = np.array(results)#makes the results an array
    #seperates the slope and intercept values
    mvals = results[:, 0]
    cvals = results[:, 1]
    end = time.time()#ending time
    running = end - start#finding the run time
    #printing the results:
    print('Parallel Linear Fit Results')
    print('---------------------------')
    print(f'Number of bootstrap fits: {n_bootstrap}')
    print(f'Number of cores: {n_cores}')
    print(f'Slope (m): {np.mean(mvals):.3f} ± {np.std(mvals):.3f}')
    print(f'Intercept (c): {np.mean(cvals):.3f} ± {np.std(cvals):.3f}')
    print(f'Total runtime: {running:.2f} seconds')