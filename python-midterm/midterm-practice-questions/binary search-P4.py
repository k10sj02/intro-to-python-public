alist=[4,5,7,9,13,45,34,58,99,125,145]
key=145
"""Search key in alist[start... end - 1]."""
start = 0
end = len(alist)
while start < end:
    mid = (start + end)//2
    if alist[mid] > key:  # this is where we check if the guess is bigger than the key
            end = mid
    elif alist[mid] < key:
            start = mid + 1
    elif alist[mid] == key:
                print (f"you searched for {alist[mid]} and we found it in the index number {alist.index(125)} of the list")
                break
else:
    print ("Not Found!")
