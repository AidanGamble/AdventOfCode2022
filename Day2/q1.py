'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
sum = 0
for f in open("input.txt"):
    if(f[0] == "A"):
        if(f[2] == "X"):
            sum = sum + 3
            sum = sum + 1
        elif(f[2] == "Y"):
            sum = sum + 6
            sum = sum + 2
        else:
            sum = sum + 3
    elif(f[0] == "B"):
        if(f[2] == "Y"):
            sum = sum + 3
            sum = sum + 2
        elif(f[2] == "Z"):
            sum = sum + 6
            sum = sum + 3
        else:
            sum = sum + 1
    elif(f[0] == "C"):
        if(f[2] == "Z"):
            sum = sum + 3
            sum = sum + 3
        elif(f[2] == "X"):
            sum = sum + 6
            sum = sum + 1
        else:
            sum = sum + 2
    
print(sum)
