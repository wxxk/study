import sys
sys.stdin = open('1244.txt')

n = int(input())
switch = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    x, y = map(int, input().split())

    if x == 1:
        for i in range(1, len(switch)//y + 1):
            if switch[(y * i) - 1] == 0:
                switch[(y * i) - 1] = 1
            else:
                switch[(y * i) - 1] = 0
    
    elif x == 2:
        if switch[y -1] == 0:
            switch[y-1] = 1
        else:
            switch[y -1] = 0
        l = y - 2
        r = y
        while l >= 0 and r < n and switch[l] == switch[r]:
            if switch[l] == 0:
                switch[l], switch[r] = 1, 1
            else:
                switch[l], switch[r] = 0, 0
            l -= 1
            r += 1
            if l<0 and r>=n:
                break

cnt = 0
ans = ''
for i in range(n):
    ans += (str(switch[i]) + ' ')
    cnt += 1
    if cnt == 20:
        print(ans)
        ans=''
        cnt =  0
if len(ans) != 0:
    print(ans)
