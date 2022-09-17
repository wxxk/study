import sys
sys.stdin = open('70129.txt')

s = input()
cnt = 0
len_s = 0

while s != "1":
    # 횟수 세기
    cnt += 1
    len_s += s.count("0")
    # 0 바꾸기
    s = s.replace("0", "")
    s = len(s)

    tmp = '' 
    
    while s:
        tmp = str(s%2) + tmp
        s//=2
    s=tmp

print(cnt, len_s)
