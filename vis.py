#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:14:47 2022

@author: mabbbs
"""

import numpy as np
from matplotlib import pyplot as plt

img_array17 = np.load('results/TD3_Walker2d-v2_1_268_1.npy')


seeds = [1,2,3,4,5]

img_array268 = []
for i in seeds:
    img_array268.append(np.load('results/TD3_Walker2d-v2_{}_{}_{}.npy'.format(i, 268, i)))  
    
img_array284 = []
for i in seeds:
    img_array284.append(np.load('results/TD3_Walker2d-v2_{}_{}_{}.npy'.format(i, 284, i)))

    
x2 = []
sum_el2 = 0
for i in range(len(img_array17)):
    x2.append(sum_el2)
    sum_el2+= 5000
    


mean_268 = np.mean(img_array268, axis=0)
std_268 = np.std(img_array268, axis=0)
plt.plot(x2, mean_268, label = 'Swish')
plt.fill_between(x2, mean_268 - (0.5*std_268), mean_268 + (0.5*std_268), alpha=.3)

mean_284 = np.mean(img_array284, axis=0)
std_284 = np.std(img_array284, axis=0)
plt.plot(x2, mean_284, label = 'Swim')
plt.fill_between(x2, mean_284 - (0.5*std_284), mean_284+ (0.5*std_284), alpha=.3)


def func_return(el, els):
    max_re = np.max(el)
    max_ind = np.argmax(el)
    max_std = els[max_ind]
    return max_re, max_std
def func_imp(el1_max, el2_max):
    res = (el2_max - el1_max) / el1_max
    res = res * 100
    return res
    

plt.legend()
plt.xlabel("Time Steps (1e6)")
plt.ylabel("Average Return")
plt.show()