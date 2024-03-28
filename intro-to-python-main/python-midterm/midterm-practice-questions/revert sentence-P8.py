text ="Moon is smaller than Sun."
for line in text.split('\n'):
     print (' '.join(line.split()[::-1]))