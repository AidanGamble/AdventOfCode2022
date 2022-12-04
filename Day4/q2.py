count = 0
for f in open("input.txt"):
    input = f.strip().split(',')
    input[0] = input[0].split("-")
    input[1] = input[1].split("-")
    if(int(input[0][0]))<=(int(input[1][0])):
        if(int(input[0][1]))>=(int(input[1][0])):
            count += 1
    elif(int(input[1][0]))<=(int(input[0][0])):
        if(int(input[1][1]))>=(int(input[0][0])):
            count += 1
print(count)