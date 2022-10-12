# 1. 말의 움직임 정의
# 2. input
# 3. 그래프 변환
# 4. move(input())
# 4-1. 좌표에 king 움직인거리 추가
# 4-2. 움직인 범위 확인
# 4-3. stone과 같은 위치인지 확인
# 4-4-1. 같으면 stone도 그만큼 움직이기 / 움직인거리 적용
# 4-4-2. 다르면 stone제자리 / 움직인거리 적용
# 5. 그래프 원래대로 변환
# 6. print

import sys

sys.stdin = open("input.txt")

dict = {
    "T": (-1, 0),
    "B": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "TL": (-1, -1),
    "TR": (-1, 1),
    "BL": (1, -1),
    "BR": (1, 1),
}

king, stone, N = input().split()
# k=A1
kx, ky = 8 - int(king[1]), ord(king[0]) - 65
sx, sy = 8 - int(stone[1]), ord(stone[0]) - 65

for i in range(int(N)):
    move = input()
    nkx = kx + dict[move][0]
    nky = ky + dict[move][1]
    if 0 <= nkx < 8 and 0 <= nky < 8:
        if nkx == sx and nky == sy:
            nsx = sx + dict[move][0]
            nsy = sy + dict[move][1]
            if 0 <= nsx < 8 and 0 <= nsy < 8:
                kx = nkx
                ky = nky
                sx = nsx
                sy = nsy
        else:
            kx = nkx
            ky = nky

ky = chr(ky + 65)
kx = 8 - kx
sy = chr(sy + 65)
sx = 8 - sx
print(f"{ky}{kx}")
print(f"{sy}{sx}")
