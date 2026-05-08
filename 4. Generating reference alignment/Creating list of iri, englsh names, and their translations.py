# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:43:33 2022

@author: user
"""

import os
from rdflib import Graph
import rdflib
#import requests
import pandas as pd

# [x[0] for x in os.walk("ont")]

#translations = dict()

pathEng = "2.1 multifarm eng"
pathHindi = "2. hindi ontologies using multifarm"
translations = pd.read_csv("Translations (multifarm).csv", header=None)
#translations.drop([0, 3, 4, 5], axis=1, inplace = True)
#translations.drop_duplicates(subset=None, keep='first', inplace=True)
translations.index = translations.iloc[:, 0]
#translations.drop([1], axis=1, inplace = True)

engHindiAlign = pd.DataFrame()

for (dirpath, dirnames, filenames) in os.walk(pathEng):
    # if dirpath==path:
    #     continue
    # print("dipath = ",dirpath)
    for j in filenames:
        filePathEng = dirpath + "\\" +j
        filePathHindi = "2. hindi ontologies using multifarm\\" + j[:-6] + "hi.owl"
        
#        print(filePath)
        
        graphEng = Graph()
        graphEng.parse(filePathEng)
        
        graphHindi = Graph()
        graphHindi.parse(filePathHindi)
        
        for subEng in graphEng.subjects(predicate = rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')):
            if type(subEng) == type(rdflib.term.URIRef("")):
#                print(sub)
                for label in graphEng.objects(subject = subEng, predicate = rdflib.term.URIRef("http://www.w3.org/2000/01/rdf-schema#label")):
#                   print(label)
                   hindiTranslation = translations.loc[str(label)][1]
#                   print(hindiTranslation)
                   result = graphHindi.query("""SELECT ?subject ?p WHERE { ?subject <http://www.w3.org/2000/01/rdf-schema#label> \"""" + hindiTranslation + """\"@hi }""")
                   for subHindi in result:
                       print(subHindi)
#                       engHindiAlign.at[str(subEng), 0] = str(label)      
#                       engHindiAlign.at[str(subEng), 1] = str(hindiTranslation)      
                       engHindiAlign.at[str(subEng), 0] = str(subHindi[0])                                                                              
