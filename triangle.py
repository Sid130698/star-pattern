n=int(input("enter number of steps :-- "))

k=(n+1)//2 +1
for i in range(n):
    for j in range(k):
        print(end=" ")
    k-=1
    for star in range(i+1):
        print("*",end=" ")
    print(end="\n")