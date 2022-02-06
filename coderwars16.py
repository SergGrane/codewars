# Your task is to construct a building which will be a pile of n cubes.
# The cube at the bottom will have a volume of n^3,
# the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.


def find_nb(m):

    i = 0
    summa = 0
    while summa < m:
        i = i + 1
        summa += i**3
    if summa == m:
        return i
    elif summa > m:
        return -1


if __name__ == '__main__':
    print(find_nb(4183059834009))
