# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 16:27:07 2022

@author: user
"""

"""
In this, we are using de-pa reference alignment files to get de-pa mappping 
then de-en files are used to replace de with pa entities that gives us de en reference files

"""



import os
#from rdflib import Graph
#import rdflib
#import requests
import pandas as pd

# [x[0] for x in os.walk("ont")]

#translations = dict()


lang_iden = 'pa'

pathToGetDePaMap = "de-"+lang_iden
pathToChangeDeToPa = lang_iden+"-en"


# renaming files for pa-en ref files
                

def rename_parts(folder_path, old_string, new_string):
    # Iterate over every file in the folder
    for filename in os.listdir(folder_path):
        # Only process if the targeted part is in the filename
        if old_string in filename:
            # Construct full current path
            old_path = os.path.join(folder_path, filename)
            
            # Create new filename and full new path
            new_filename = filename.replace(old_string, new_string)
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: "{filename}" -> "{new_filename}"')
        
        
        
rename_parts(pathToChangeDeToPa, "-de", "-"+lang_iden)        



#count = 0

""" Creating de pa mapping """

for (dirpath, dirnames, filenames) in os.walk(pathToGetDePaMap):
    # if dirpath==path:
    #     continue
    # print("dipath = ",dirpath)
    for j in filenames:
        filePath = dirpath + "\\" +j
        filePathPaEn = pathToChangeDeToPa + "\\" + j.replace("-"+lang_iden, "-en").replace("-de", "-"+lang_iden)
        print(filePath)
#        count += 1
        
        f = open(filePath)
        linesAll = f.readlines()
        f.close()
        
        linesNeeded = []
        for line in linesAll:
            if "entity1" in line or "entity2" in line:
                linesNeeded.append(line)
        dePaAlign = pd.DataFrame()
        ind = 0
        while(ind < len(linesNeeded)):
            if "_de" in linesNeeded[ind]:
                line = linesNeeded[ind]
                start = line.find("=")
                deT = line[start+2: start+2 + line[start+2:].find("\"")]

                line = linesNeeded[ind+1]
                start = line.find("=")
                paT = line[start+2: start+2 + line[start+2:].find("\"")]
                
                
            if "_"+lang_iden in linesNeeded[ind]:
                line = linesNeeded[ind]
                start = line.find("=")
                paT = line[start+2: start+2 + line[start+2:].find("\"")]

                line = linesNeeded[ind+1]
                start = line.find("=")
                deT = line[start+2: start+2 + line[start+2:].find("\"")]
                
            ind += 2
            dePaAlign.at[deT, 0] = paT
        
        
        """ Using dePaAlign to convert de-en to pa-en """
        
        
        f = open(filePathPaEn)
        data = f.read()
        f.close()
        
        for index in dePaAlign.index:
            data = data.replace(index, dePaAlign.loc[index][0])
            
        f = open(filePathPaEn, "w", encoding = "UTF-8")
        f.close()
        with open(filePathPaEn, "w", encoding = "UTF-8") as text_file:
            text_file.write(data) 
            
            
