#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Celsius\t | Fahrenheit")
for c in range(-10, 91, 10):
    c = c + 10
    fahrenheit = (c * 9/5) + 32
    print(f'''{c}\t | {fahrenheit}''')


# In[2]:


pi_approx = 0
count = 1

for term in range(16):
    if term == 0:
        continue
        pi_approx += 3
    else:
        sign = (-1)**(term+1)
        d = 2*term
        den = (d)*(d+1)*(d+2)
        pi_approx += (sign)*(4/den)
        count = count + 1
    print(f'Approximation {count - 1} = {pi_approx + 3}')


# In[ ]:




