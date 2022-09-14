# -*- coding: utf-8 -*-
"""Palabras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q4lFqfGsep0mRo1_4YblbJ_bsJOR-aMe
"""

from pyparsing import White
import matplotlib.pyplot as plt
from wordcloud import WordCloud

x = 8 +315 + 156
i = 0
my_list = []
while i < x:
  if i < 8:
    my_list.append("Johnny Depp\n$800K")
  elif i < (315 + 8):
    my_list.append("Keanu Reeves\n$31.5M")
  else:
    my_list.append("Ewan Mcgregor\n$15.6M")
  i+= 1

#convert it to dictionary with values and its occurences
from collections import Counter
word_could_dict=Counter(my_list)
wordcloud = WordCloud(width = 1000, height = 500, background_color="White").generate_from_frequencies(word_could_dict)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
plt.savefig('yourfile.png', bbox_inches='tight')
plt.close()