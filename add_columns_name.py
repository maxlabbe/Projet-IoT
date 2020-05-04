# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:10:33 2020

@author: Max
"""

import csv

toAdd = ["pkSeqID","stime","flgs","proto","saddr","sport","daddr","dport","pkts","bytes","state","ltime","seq","dur","mean","stddev","smac","dmac","sum","min","max","soui","doui","sco","dco","spkts","dpkts","sbytes","dbytes","rate","srate","drate","attack","category","subcategory"] 

for file_index in range(1,75):
    file_name = 'Entire Dataset/UNSW_2018_IoT_Botnet_Dataset_' + str(file_index) + '.csv'
    with open(file_name, "r") as infile:
        reader = list(csv.reader(infile))
        reader.insert(0, toAdd)
    with open(file_name, "w", newline='') as outfile:
        writer = csv.writer(outfile)
        for line in reader:
            writer.writerow(line)
    infile.close()
    outfile.close()
    
print("done")