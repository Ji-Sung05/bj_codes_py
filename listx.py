a, b = map(int, input().split())
list = list(map(int, input().split()))
for i in range(a):
   if b > list[i]:
        print(list[i], end = " ")