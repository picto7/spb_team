import random
N = int(input())
A = []
for i in range(N):
    A.append(random.randint(1,51))
print(A)
A.reverse()
print(A)
