import sys

sys.stdin = open("BOJ_5597.txt")

student_list = [i for i in range(1, 31)]

# print(student_list)

for _ in range(28):
    n = int(input())

    student_list.remove(n)

print(min(student_list))
print(max(student_list))
