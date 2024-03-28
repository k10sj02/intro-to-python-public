lst = [1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,6,6]
key=5
# find_low_index
low = 0
high = len(lst)-1
mid = high//2

while low <= high:
  mid_elem = lst[mid]
  if mid_elem < key:
   low = mid+1
  else:
   high = mid-1
  mid = low + (high-low)//2
  if lst[low] == key:
   print("Low Index of " + str(key) + ": " + str(low))
   break

# find_high_index
low = 0
high = len(lst) - 1
mid = high//2

while low <= high:
  mid_elem = lst[mid]
  if mid_elem <= key:
     low = mid+1
  else:
     high = mid-1
  mid = low + (high-low)//2;
if lst[high] == key:
  print ("High Index of " + str(key) + ": " + str(high))