#Code from
#https://www.sanfoundry.com/python-program-check-common-letters-string/
#https://stackoverflow.com/questions/4789601/split-a-string-into-2-in-python

from collections import Counter
counter = 0
for f in open("input.txt"):
    firstpart, secondpart = f[:len(f)//2], f[len(f)//2:]
    a=list(set(firstpart)&set(secondpart))
    if(ord(a[0]) < 91):
        counter = counter + ord(a[0]) - 38
    else:
        counter = counter + ord(a[0]) - 96
print(counter)
    