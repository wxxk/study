import sys

sys.stdin = open("BOJ_10807.txt")

n = int(input())
n_list = list(map(int, input().split()))
v = int(input())


print(n_list.count(v))
