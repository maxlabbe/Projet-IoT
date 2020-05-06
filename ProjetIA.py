# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:49:53 2020

@author: Max
"""

import pandas as pd
import matplotlib.pyplot as plt 

dataFrame = pd.DataFrame()

for file_index in range(41, 51):
    file_name =  'Entire Dataset/UNSW_2018_IoT_Botnet_Dataset_' + str(file_index) + '.csv'
    dataFrame = pd.concat([dataFrame, pd.read_csv(file_name, sep=',', low_memory=False)], axis = 0)
    print(file_index)

dataFrame_attack = dataFrame[(dataFrame.attack == 1)]

plt.bar(dataFrame_attack.proto.unique(), dataFrame_attack.proto.value_counts())
plt.title("nombre d'attaque par protocole")
plt.xlabel('protocol')
plt.ylabel("nombre d'attaque")
plt.legend()
plt.show()