#!/usr/bin/env python
# coding: utf-8

# In[3]:


def word_count(str):
    counts = dict()
# Given a list of words, returns a dictionary of the word counts.
# Initialize a dictionary to have zero counts.
    words = str.lower().split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1           
# For each word in the text, 
# increment the word's count in the dictionary.

    return counts

# return dictionary

def word_cnt(list):
    counts = dict()
    for word in list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
