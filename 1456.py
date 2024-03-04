import sys


def eratos_modified(a, b):
    max_num = int(b**0.5) + 1  # B의 제곱근까지만 소수를 찾음
    is_prime = [True] * (max_num + 1)
    is_prime[0] = False  # 0은 소수가 아님
    is_prime[1] = False  # 1은 소수가 아님
    primes = []

    # 에라토스테네스의 체로 소수 찾기
    for number in range(2, max_num + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number*2, max_num + 1, number):
                is_prime[multiple] = False

    # 거의 소수 찾기
    almost_primes = 0
    for prime in primes:
        exponent = 2  # 제곱부터 시작
        while prime**exponent <= b:
            if prime**exponent >= a:
                almost_primes += 1
            exponent += 1

    return almost_primes

a,b=map(int,sys.stdin.readline().split())
prime=eratos_modified(a,b)
print(prime)



