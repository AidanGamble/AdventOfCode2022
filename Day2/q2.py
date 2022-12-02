'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
sum = 0
for f in open("input.txt"):
    if(f[2] == "X"):
        if(f[0] == "A"):
            sum = sum + 3
        elif(f[0] == "B"):
            sum = sum + 1
        elif(f[0] == "C"):
            sum = sum + 2
    elif(f[2] == "Y"):
        if(f[0] == "A"):
            sum = sum + 4
        elif(f[0] == "B"):
            sum = sum + 5
        elif(f[0] == "C"):
            sum = sum + 6
    elif(f[2] == "Z"):
        if(f[0] == "A"):
            sum = sum + 8
        elif(f[0] == "B"):
            sum = sum + 9
        elif(f[0] == "C"):
            sum = sum + 7
print(sum)