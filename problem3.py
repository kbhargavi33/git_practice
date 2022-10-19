#form a matrix by taking input from console

m = int(input("enter number of rows: "))
n = int(input("enter no of cols: "))
res = []
print("enter values rowwise : ")
for i in range(m):
    l = []
    for j in range(n):
        l.append(int(input()))
    res.append(l)
print(res)
print(*res, sep = "\n")


