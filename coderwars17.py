# You are given an array(list) ar of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.


def con_ca(ar: list, numb: int) -> str:
    a = ''
    for i in range(len(ar)-numb+1):
        if numb <= 0 or len(ar) <= numb:
            return ''
        s = ''.join(ar[i:i+numb])
        if len(s) > len(a):
            a = s
    return a


if __name__ == '__main__':
    print(con_ca(["zone", "abigail", "theta", "form", "libe", "zas", "sfdgasfdgsfdhgasfdhgasfd"], 2))
