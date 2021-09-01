n=int(input("Enter number of steps :- "))
k=2*n-2
for i in range(n):
    for j in range(k):
        print(end=" ")
    k-=2
    for star in range(i+1):
        print("*",end=" ")
    
    print(end="\n")

