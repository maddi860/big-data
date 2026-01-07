# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 01:26:39 2026

@author: maddi
"""

import pandas as pd

# Load Hadoop output file
df = pd.read_csv(
    "wordcloud_data.txt",
    sep="\t",
    names=["Word", "Count"]
)

# Sort by frequency
df = df.sort_values("Count", ascending=False)

# Top 10 most frequent words
top10 = df.head(10)

# Bottom 10 least frequent words
bottom10 = df.tail(10)

print("\nTop words:")
print(top10)

print("\nBottom 10 words:")
print(bottom10)

# Optional: save tables
top10.to_csv("top10_words.csv", index=False)
bottom10.to_csv("bottom10_words.csv", index=False)
