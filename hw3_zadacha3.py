#Составить список простых множителей натурального числа N

def prime_factors(N):
    spisok_factors = []
    prime_num = 2
    while prime_num * prime_num <= N:
        if N % prime_num == 0:
            spisok_factors.append(prime_num)
            N //= prime_num
        else:
            prime_num += 1
    if N > 1:
        spisok_factors.append(N)
    return spisok_factors

print(prime_factors(15))
