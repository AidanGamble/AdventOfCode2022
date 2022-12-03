from collections import Counter
counter = 0
line = 0
string1 = ""
string2 = ""
string3 = ""
for f in open("input.txt"):
    if(line == 0):
        string1 = f.strip()
    elif(line == 1):
        string2 = f.strip()
    else:
        string3 = f.strip()
    
    if(line == 2):
        a=list(set(string1)&set(string2))
        a=list(set(a)&set(string3))
        print(a)
        if(ord(a[0]) < 91):
            counter = counter + ord(a[0]) - 38
        else:
            counter = counter + ord(a[0]) - 96
        line = 0
    else:
        line = line + 1
print(counter)
    