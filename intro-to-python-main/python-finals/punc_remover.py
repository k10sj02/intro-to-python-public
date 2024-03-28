#!/usr/bin/env python
# coding: utf-8

# In[9]:


def punc_remover(str):
    str = str.replace("  ", " ")
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for p in punc:
        str = str.replace(p, " ")

    words = str.split()
    print(words)
    print(str)
    print('\nNumber of words in text file :', len(words))
    return words
