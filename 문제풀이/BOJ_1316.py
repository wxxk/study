import sys

sys.stdin = open("BOJ_1316.txt")

# 단어의 개수
n = int(input())

for i in range(n):
    # 단어 입력 받기
    word = input()

    # print(word)

    # 입력 받은 단어 돌기 (다음 글자랑 비교해야되기 때문에 범위 -1)
    for j in range(len(word) - 1):
        # print(word[i])
        # print(word[i + 1])

        # 현재 글자랑 다음 글자랑 같으면 pass
        if word[j] == word[j + 1]:
            pass

        # 현재 글자랑 다음 글자랑 다른경우 elif로
        # 현재 글자가 뒤에 문자열에도 오는지 확인(슬라이싱)
        elif word[j] in word[j + 1 :]:
            # 같은 글자가 온다면 그룹단어가 아니기 떄문에 단어 개수 -1
            n -= 1
            #  현재 단어는 그룹 단어가 아니기 때문에 for문 나가기
            break

print(n)
