# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:30:31 2022

@author: user
"""


import os
from rdflib import Graph
import rdflib
#import requests
import pandas as pd

# [x[0] for x in os.walk("ont")]

#translations = dict()

path = "1. ref al"

translations = pd.read_csv("Translations (multifarm).csv", header=None)
#translations.drop([0, 3, 4, 5], axis=1, inplace = True)
#translations.drop_duplicates(subset=None, keep='first', inplace=True)
translations.index = translations.iloc[:, 0]
translations.drop([1], axis=1, inplace = True)

for (dirpath, dirnames, filenames) in os.walk(path):
    # if dirpath==path:
    #     continue
    # print("dipath = ",dirpath)
    for j in filenames:
        filePath = dirpath + "\\" +j
#        print(filePath)
        
        outputFile = "3. hindi ref al" + dirpath.replace(path, "").replace("en", "hi") +  "\\"  + j.replace("-en", "-hi")
#        f = open(filePath, 'r')
#        for line in f.readlines():
#            if j[:-6] + "_en" in line:
#                iris.append(line)
#        
#        f.close()
        
        f = open(filePath)
        data = f.read()
        f.close()
        
        for ind in engHindiAlign.index:
#            print(type(ind))
#            break
            data = data.replace(ind, engHindiAlign.loc[ind][0])
        

        f = open(outputFile, "w", encoding = "UTF-8")
        f.close()
        with open(outputFile, "w", encoding = "UTF-8") as text_file:
            text_file.write(data)