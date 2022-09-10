import sys
sys.stdin = open('4375.txt')

while True:
    try:
        n = int(input())
    except: break

    num = 1
    cnt = 1

    while True:
        if num%n == 0:
            print(cnt)
            break
        else:
            num = (num*10)+1
            cnt += 1


    # while True:
    #     if num%n == 0:
    #         print(len(str(num)))
    #         break
    #     else:
    #         num = str(num)
    #         num = num + "1"
    #         num = int(num)
