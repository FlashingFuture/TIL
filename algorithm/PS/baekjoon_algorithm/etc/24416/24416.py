def fib(n):

    if n == 1 or n == 2:
        global recur_cnt
        recur_cnt += 1
        return 1

    return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global dp_cnt
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        dp_cnt += 1
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


N = int(input())
f = [0] * (N + 1)
recur_cnt = 0
dp_cnt = 0
fib_ans = fibonacci(N)
print(fib_ans, dp_cnt)
