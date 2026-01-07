# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 00:14:50 2026

@author: maddi
"""
#importing the necessary libraries
import re
from collections import Counter

data = 'DOHERTY_PHD_thesis.txt'
with open(data, 'r', encoding = 'utf-8', errors = 'ignore') as file:
#reading the file
    text = file.read().lower()#makes everything lowercase
text = re.sub(r'[^a-z\s]', '', text)
#keeping only the letters a-z, no numbers
#everything else is gonna be replaced with a space
removed = {"section", "sections", "table", "tables", "figure", "figures", "plot", "plots", 
    "panel", "panels", "shows", "show", "present", "presents", "presented", 
    "demonstrates", "demonstrate", "demonstrated","chapter", "chapters", 
    "introduction","conclusion","conclusions","discussion", "abstract", 
    "acknowledgements", "contents", "list", "references", "the", "and", "for", 
    "with", "that", "this", "from", "are", "was", "were", "can", 
    "has", "have", "had", "but", "not", "which", "also", "their", "its", "than",
    "such", "these", "those", "using", "used", "use", "into", "over", "between"}
#removing simple everyday words
words = [w for w in text.split() if len(w) > 2 and w not in removed]
counter = Counter(words)#counting frequency for each word
with open('cleaned_thesis.txt', "w", encoding="utf-8") as file:
    file.write(" ".join(words))
#saving the ouput of program as a txt file that can be used for the word cloud