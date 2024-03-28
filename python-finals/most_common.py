#!/usr/bin/env python
# coding: utf-8

# In[2]:

import word_count

#Most common words 
def most_common(str):
    word_dictionary = word_count.word_cnt(str)

    sort_words = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)

    for i in sort_words:
        print(i[0], ":", i[1])


# In[ ]:




