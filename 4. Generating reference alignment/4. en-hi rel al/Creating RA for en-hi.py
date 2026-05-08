# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 16:27:07 2022

@author: user
"""

import os
#from rdflib import Graph
#import rdflib
#import requests
import pandas as pd

# [x[0] for x in os.walk("ont")]

#translations = dict()

pathToGetDeHiMap = "de-hi"
pathToChangeDeToHi = "hi-en"

#count = 0

""" Creating de hi mapping """

for (dirpath, dirnames, filenames) in os.walk(pathToGetDeHiMap):
    # if dirpath==path:
    #     continue
    # print("dipath = ",dirpath)
    for j in filenames:
        filePath = dirpath + "\\" +j
        filePathHiEn = "hi-en" + "\\" + j.replace("-hi", "-en").replace("-de", "-hi")
        print(filePath)
#        count += 1
        
        f = open(filePath)
        linesAll = f.readlines()
        f.close()
        
        linesNeeded = []
        for line in linesAll:
            if "entity1" in line or "entity2" in line:
                linesNeeded.append(line)
        deHiAlign = pd.DataFrame()
        ind = 0
        while(ind < len(linesNeeded)):
            if "_de" in linesNeeded[ind]:
                line = linesNeeded[ind]
                start = line.find("=")
                deT = line[start+2: start+2 + line[start+2:].find("\"")]

                line = linesNeeded[ind+1]
                start = line.find("=")
                hiT = line[start+2: start+2 + line[start+2:].find("\"")]
                
                
            if "_hi" in linesNeeded[ind]:
                line = linesNeeded[ind]
                start = line.find("=")
                hiT = line[start+2: start+2 + line[start+2:].find("\"")]

                line = linesNeeded[ind+1]
                start = line.find("=")
                deT = line[start+2: start+2 + line[start+2:].find("\"")]
                
            ind += 2
            deHiAlign.at[deT, 0] = hiT
        
        
        """ Using deHiAlign to convert de-en to hi-en """
        
        
        f = open(filePathHiEn)
        data = f.read()
        f.close()
        
        for index in deHiAlign.index:
            data = data.replace(index, deHiAlign.loc[index][0])
            
        f = open(filePathHiEn, "w", encoding = "UTF-8")
        f.close()
        with open(filePathHiEn, "w", encoding = "UTF-8") as text_file:
            text_file.write(data) 
            
            
