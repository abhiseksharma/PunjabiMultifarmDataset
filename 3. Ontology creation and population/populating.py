# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:12:42 2022

@author: user
"""


#import json
import os
from rdflib import Graph
import rdflib
#import requests
import pandas as pd

# [x[0] for x in os.walk("ont")]

#translations = dict()

path = "ontofarm eng"

translations = pd.read_csv("Translations.csv", header=None)
translations.drop([0, 3, 4, 5], axis=1, inplace = True)
#translations.drop_duplicates(subset=None, keep='first', inplace=True)
translations.index = translations.iloc[:, 0]
translations.drop([1], axis=1, inplace = True)
#translations.drop_duplicates(subset=None, keep='first', inplace=True)

allNames = []

for (dirpath, dirnames, filenames) in os.walk(path):
    # if dirpath==path:
    #     continue
    # print("dipath = ",dirpath)
    for j in filenames:
        filePath = dirpath + "\\" +j
#        print(filePath)
        # print(filePath)
        outputFile = "C:/Users/user/OneDrive/PhD (document or files other than dropbox)/Hindi Dataset for Ontology Matching/Ontology creation and population/hindi ontologies using ontofarm ontologies/" +j
        
        graph = Graph()
        graph.parse(filePath)
        done = []
        f = open(filePath, 'r', encoding = "UTF-8")
        data = f.read()
        f.close()
        
        # classCount = 0
        for sub in graph.subjects(predicate = rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')):
            if type(sub) == type(rdflib.term.URIRef("")):
                # for label in graph.objects(subject = rdflib.term.URIRef(sub), predicate = rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label')):
                #     classCount += 1
                #     sourceClassNames.append(str(label.lower().replace('/', ' ')))
                name = (str(sub).split('#'))[-1]
                allNames.append(name)
                if 'http' not in name:
                    if name not in done:
                        try:
                            data = data.replace('\"' + name + '\"', '\"' + translations.loc[name][2].replace(" ", '_') + '\"')
                            data = data.replace('\"#' + name + '\"', '\"#' + translations.loc[name][2].replace(" ", '_') + '\"')
                            data = data.replace('<' + name + ' ', '<' + translations.loc[name][2].replace(" ", '_') + ' ')
                        except(TypeError):
                            data = data.replace('\"' + name + '\"', '\"' + translations.loc[name][2].iloc[0].replace(" ", '_') + '\"')
                            data = data.replace('\"#' + name + '\"', '\"#' + translations.loc[name][2].iloc[0].replace(" ", '_') + '\"')
                            data = data.replace('<' + name + ' ', '<' + translations.loc[name][2].iloc[0].replace(" ", '_') + ' ')
                                                
                    done.append(name)
                
                
                # if classCount == 0:
                #     for classLabel in graph.objects(subject = rdflib.term.URIRef(sub), predicate = rdflib.term.URIRef('http://data.bioontology.org/metadata/prefixIRI')):
                #         if ':' not in label:
                #             sourceClassNames.append(str(label.lower().replace('/', ' ')))
        with open(outputFile, "w", encoding = "UTF-8") as text_file:
            text_file.write(data)
        
        


'''======================================================For ontologies in Multifarm=========================================================='''



import os
from rdflib import Graph
import rdflib
#import requests
import pandas as pd
import random

# [x[0] for x in os.walk("ont")]

#translations = dict()

path = "multifarm eng"

translations = pd.read_csv("Translations (multifarm).csv", header=None, encoding = "UTF-8")
#translations.drop([0, 3, 4, 5], axis=1, inplace = True)
#translations.drop_duplicates(subset=None, keep='first', inplace=True)
translations.index = translations.iloc[:, 0]
translations.drop([0], axis=1, inplace = True)
#translations.drop_duplicates(subset=None, keep='first', inplace=True)


#def CamelCaseSplit(inp_string: str):
#    #s = "CountryOfficialLanguage"
#    string = ""
#    for i in inp_string:
#        if i.isupper():
#            string += " "+i
#        else:
#            string += i
#            
#    words = string.strip().lower()
#    return words


for (dirpath, dirnames, filenames) in os.walk(path):
    # if dirpath==path:
    #     continue
    # print("dipath = ",dirpath)
    for j in filenames:
        filePath = dirpath + "\\" +j
        
        outputFile = "C:/Users/user/OneDrive/PhD (document or files other than dropbox)/Hindi Dataset for Ontology Matching/3. Ontology creation and population/hindi ontologies using multifarm/" + j[:-6] + "hi.owl"
        
        graph = Graph()
        graph.parse(filePath)
        
        done = []
        f = open(filePath, 'r')
        data = f.read()
        f.close()
        
        
        for sub in graph.subjects(predicate = rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')):
            if type(sub) == type(rdflib.term.URIRef("")):
#                print(type(sub))
                for label in graph.objects(subject = sub, predicate = rdflib.term.URIRef("http://www.w3.org/2000/01/rdf-schema#label")):
                    if label not in done:
#                        if '_' in label:
#                            searchLabel = label.replace("_", ' ')
#                        else:
#                            searchLabel = CamelCaseSplit(label)

                        ''' need to search for both conditions either it contains _ or camelcase '''
                        
#                        searchLabel = ''.join(label.title().split())
                        label = str(label)
                        try:
                            data = data.replace('>' + label + '<', '>' + translations.loc[label][1] + '<')
#                            data = data.replace('\"#' + label + '\"', '\"#' + translations.loc[label][1] + '\"')
                        except(TypeError):
                            data = data.replace('>' + label + '<', '>' + translations.loc[label][1].iloc[0] + '<')
#                            data = data.replace('\"#' + label + '\"', '\"#' + translations.loc[label][1].iloc[0] + '\"')
#                        except:
#                            pass
                        done.append(label)
                
        '''  Changing IRI '''
        
        usedIRIID = []
#        data = data.replace(j[:-7]+"_en", j[:-7] + "_hi")
        for sub in graph.subjects(predicate = rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')):
#             if type(sub) == type(rdflib.term.URIRef("")):
            if "http://" + j[:-7] + "_en#" in str(sub):
#                 print(sub)
                 one = random.randrange(1000000, 9999999)
                 two = random.randrange(1000000, 9999999)
                 prevIri = str(sub)
                 iri = prevIri[:-15] + str(one) + "-" + str(two)
                 iri = iri.replace('_en', '_hi')
                 if iri not in usedIRIID:
                     data = data.replace(prevIri, iri)
                 usedIRIID.append(iri)
                 
        data = data.replace("""xml:lang=\"en\"""", """xml:lang=\"hi\"""")       # xml:lang="en"
        data = data.replace(j[:-7] + "_en", j[:-7] + "_hi")                     # cmt_en

                # if classCount == 0:
                #     for classLabel in graph.objects(subject = rdflib.term.URIRef(sub), predicate = rdflib.term.URIRef('http://data.bioontology.org/metadata/prefixIRI')):
                #         if ':' not in label:
                #             sourceClassNames.append(str(label.lower().replace('/', ' ')))
        f = open(outputFile, "w", encoding = "UTF-8")
        f.close()
        with open(outputFile, "w", encoding = "UTF-8") as text_file:
            text_file.write(data)