#problem 1: input numbers and sort them

#n = int(input("enter number of integers n to be sorted: ").strip())

#a = list(map(int, input("enter n space separated integer values: ").rstrip().split()))

a = [5,4,3,2,1,1]
for i in range(5):
    for i in range(0,len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

print(a)




