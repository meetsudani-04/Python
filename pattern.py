# space = 4
# for i in range(1,6):
#     for k in range(space):
#         print(" ",end="")
#     space-=1
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

space = 0
for i in range(5,0,-1):
    for k in range(space):
        print("",end="")
    space+=1
    for j in range(i):
        print("*",end=" ")
    print()
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


x=10
print(f'Convert \'x\' to 8 digits number: {x:08d}')