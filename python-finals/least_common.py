#!/usr/bin/env python
# coding: utf-8

# In[4]:


import word_count 

def least_common(str):
    word_dictionary = word_count.word_cnt(str)
    sort_words = sorted(word_dictionary.items(), key=lambda x: x[1])

    for i in sort_words:
        print(i[0],":",i[1])

