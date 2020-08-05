n = int(input())
A = []
for i in range(1, 500):
    a = i * i
    for ii in range(1, 500):
        b = ii * ii
        if a == b + n:
            A.append(i)
            A.append(ii)
print(len(A)//2)