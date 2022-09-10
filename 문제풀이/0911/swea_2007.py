import sys
sys.stdin = open('2007.txt')

T = int(input())

for tc in range(1, T+1):

    words=list(input())
    word = ''

    for i in range(len(words)): # 0~30
        if words[0:i+1] == words[i+1:2*(i+1)]:
            word = ''.join(words[i+1:2*(i+1)])
            break
    print(f"#{tc} {len(word)}")