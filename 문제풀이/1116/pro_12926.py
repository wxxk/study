# 0. input
s = "AB"
n = 1


# 1. 리스트로 문자열 분리
list_s = list(s)


# 2. 리스트 for문으로 돌면서 chr ord 사용
temp = []
for i in list_s:
    temp.append(chr(ord(i) + n))


# 3. print
result = "".join(temp)

print(result)
