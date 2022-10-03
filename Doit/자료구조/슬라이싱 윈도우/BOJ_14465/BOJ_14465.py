import sys

sys.stdin = open("input.txt")

N, K, B = map(int, input().split())
signal = [1] * (N)
for _ in range(B):
    signal[int(sys.stdin.readline()) - 1] = 0
result = []

window = sum(signal[:K])
result.append(window)

for i in range(K, N):
    # 연결된 횡단보도 구하기
    window = window + signal[i] - signal[i - K]

    # 고쳐야할 횡단보도 추가
    # K개가 연속되어야 하니까
    # K - window = 고쳐야되는 횡단보도 수
    result.append(K - window)

print(min(result))
