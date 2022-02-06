# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more
# than one digit, continue reducing in this way until a single-digit
# number is produced. The input will be a non-negative integer.
summa = 0


def s_summa (s1: str):
    summ = sum(list(map(int, s1)))
    print(s1, summ)
    return summ


n = input('N = ')

if int(n) > 0:
    summa = s_summa(n)
    if summa > 9:
        summa = s_summa(str(summa))
        if summa > 9:
            summa = s_summa(str(summa))

print(summa)
