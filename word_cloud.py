# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 00:38:38 2026

@author: maddi
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read word counts
word_freq = {}

with open("wordcloud_data.txt", "r") as f:
    for line in f:
        word, count = line.strip().split("\t")
        word_freq[word] = int(count)

# Generate word cloud
wc = WordCloud(
    width=1000,
    height=500,
    background_color="white"
)

wc.generate_from_frequencies(word_freq)

# Display
plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# Optional: save image
wc.to_file("wordcloud.png")

