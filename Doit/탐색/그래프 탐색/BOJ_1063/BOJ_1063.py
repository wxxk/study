# 대표적인 구현문제

# 알파벳은 열 / 숫자는 행을 상징
# 왼쪽아래 A1
# 킹의 움직임은 8가지 / 돌도 같이 움직임
# 움직임이 체스판 밖으로 나가면 움직임 무시

#  입력
# 첫째줄 : 킹의 위치 / 돌의 위치 / 움직임 횟수
# 둘째줄 부터 ~ : 돌의 움직임

# 델타탐색 / 아스키코드 사용

import sys

sys.stdin = open("input.txt")

# 1. 말이 움직임 정의
# 델타값을 이용 (dxdy / 튜플)
# 8방향 델타값 만드는거 이해(암기 x)
"""
(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)
"""
# 관계를 표현할 때 딕셔너리가 가장 편리
# 알파벳이 많아지면 불편해짐
dict = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1),
}


# # 2. 그래프 만들기
# # 그래프와 좌표 값이 다르기 때문에 전환이 필요함
# for _ in range(8):
#     matrix = [[0] * 8 for i in range(8)]

# 3. 인풋
king, stone, N = input().split()
# print(king, stone, N)

# 4. 그래프 변환(아스키 코드 사용)
# A1 = [열][행] => [행][열]로 변환 필요
# 1->7 / 6->2 / 5->3 / 4->4 / 3->5 / 6->2 / 7->1 : 8을 빼서 계산
kx, ky = 8 - int(king[1]), ord(king[0]) - 65
# ky = ord(king[0]) - 65
sx, sy = 8 - int(stone[1]), ord(stone[0]) - 65
# sy = ord(stone[0]) - 65
"""
A1을 7, 0 으로 변환
k = A1
kx = 8 - int(k[1])
ky = ord(k[0])-64
"""

for i in range(int(N)):
    move = input()
    # 이동
    nkx = kx + dict[move][0]
    nky = ky + dict[move][1]

    # 범위 확인
    if 0 <= nkx < 8 and 0 <= nky < 8:
        # 킹이 돌과 같은곳으로 움직이면 돌도 똑같이 이동
        if nkx == sx and nky == sy:
            nsx = sx + dict[move][0]
            nsy = sy + dict[move][1]
            # 돌이 움직인 범위도 확인
            if 0 <= nsx < 8 and 0 <= nsy < 8:
                # 범위 안에있으면 움직이기
                kx = nkx
                ky = nky
                sx = nsx
                sy = nsy
        # 돌과 킹이 다른 곳
        else:
            # 킹만 움직이기
            kx = nkx
            ky = nky

# 그래프 다시 원래대로 변환
ky = chr(ky + 65)
kx = 8 - kx
sx = 8 - sx
sy = chr(sy + 65)
print(f"{ky}{kx}")
print(f"{sy}{sx}")
