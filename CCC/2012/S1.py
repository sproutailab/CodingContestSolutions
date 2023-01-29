# i = int(sys.stdin.readline())
# n = int(input()) - 1
# print (int(n*(n-1)*(n-2)/6))


i = int(input())
cnt = 0
for j in range(i-1, 2, -1):
#         print(j)
    for k in range(j-1, 1, -1):
#             print(k)
        for l in range(k-1, 0, -1):
#             print(l,k,j,i)
            cnt += 1
print(cnt)