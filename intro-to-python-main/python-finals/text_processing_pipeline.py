#!/usr/bin/env python
# coding: utf-8

# In[1]:


import lower_case
import punc_remover
import word_count
import most_common
import least_common
import report


# In[2]:


file_txt = """Python is easy to learn and enjoyable. Like other languages, Python provides a complete set of control flow elements, including while and for loops, and conditionals. .
In python,  the indent is important !  Things can easily go wrong if you do not follow indentation. 
PythoN uses the level of indentation to group blocks of code with control elements."""

print(file_txt)


# In[3]:


file_txt = lower_case.lower_case(file_txt)
print(file_txt)


# In[4]:


file_txt = punc_remover.punc_remover(file_txt)


# In[5]:


print(word_count.word_cnt(file_txt))


# In[6]:


print(most_common.most_common(file_txt))


# In[7]:


print(least_common.least_common(file_txt))


# In[8]:


report.report(file_txt)


# In[ ]:




