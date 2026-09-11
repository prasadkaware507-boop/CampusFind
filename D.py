t = int(input())
for _ in range(t):
    n,m,h=map(int,input().split())
    arr = list(map(int,input().split()))
    mapii = {
        -1:arr[:]
    }
    for q in range(m):
        b,c = map(int,input().split())
        isvalid = mapii[q-1][b-1]+c
        if isvalid <= h:
            mapii[q] = mapii[q-1][:]
            mapii[q][b-1] +=c 
        else:
            mapii[q] = arr[:]
    print(*mapii[m-1])           
        