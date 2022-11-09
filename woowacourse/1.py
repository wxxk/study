import sys

sys.stdin = open("input.txt")

pobi = list(map(str, input().split()))
crong = list(map(str, input().split()))

if (
    (int(pobi[1]) - int(pobi[0])) != 1
    or (int(crong[1]) - int(crong[0])) != 1
    or 0 < int(pobi[1]) < 400
    or 0 < int(pobi[0]) < 400
    or 0 < int(crong[1]) < 400
    or 0 < int(crong[0]) < 400
    or int(pobi[0]) % 2 != 1
    or int(pobi[1]) % 2 != 0
    or int(crong[0]) % 2 != 1
    or int(crong[1]) % 2 != 0
):
    print(-1)
else:
    for i in range(2):
        for j in range(2):

            pl_1 = int(pobi[0][0])
            pl_2 = int(pobi[0][1])

            pr_1 = int(pobi[1][0])
            pr_2 = int(pobi[1][1])

            cl_1 = int(crong[0][0])
            cl_2 = int(crong[0][1])

            cr_1 = int(crong[1][0])
            cr_2 = int(crong[1][1])

    pl_sum = pl_1 + pl_2
    pr_sum = pr_1 * pr_2
    p_max = 0

    if pl_sum > pr_sum:
        p_max = pl_sum
    else:
        p_max = pr_sum

    cl_sum = cl_1 + cl_2
    cr_sum = cr_1 * cr_2
    c_max = 0

    if cl_sum > cr_sum:
        c_max = cl_sum
    else:
        c_max = cr_sum

    result = 0

    if p_max > c_max:
        result = 1
    elif c_max > p_max:
        result = 2
    else:
        result = 0

    print(result)
