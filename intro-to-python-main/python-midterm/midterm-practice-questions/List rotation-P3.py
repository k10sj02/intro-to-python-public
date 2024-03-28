lst=[3,4,6,12,8,9,14]
n=2
ln=len(lst)
lst=lst[-n::]+lst[0:ln-2]
print (lst)