import sys
sys.stdin = open ('1206.txt')

N = int(input())
list_N = list(map(int, input().split()))

list_R = []
list_L = []

for i in range(2, N-2):
    # 오른쪽 빼기
    list_R.append((list_N[i] - list_N[i+1]))
    list_R.append((list_N[i] - list_N[i+2]))
    # 왼쪽 빼기
    list_L.append((list_N[i] - list_N[i-1]))
    list_L.append((list_N[i] - list_N[i-2]))

print(list_R)
print(list_L)