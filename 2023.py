def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False  # 0과 1은 소수가 아님

    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n+1) if primes[i]]
primes=[]
# 1자리부터 8자리까지의 소수 구하기
for i in range(1, 9):
    a=sieve_of_eratosthenes(10**i)
    primes.append(a)

print(primes[3])