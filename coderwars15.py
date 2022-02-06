# Duplicate Encoder
# The goal of this exercise is to convert a string to a new string where each character in the new string
# is "(" if that character appears only once in the original string, or ")" if that character appears more
# than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def encode(s2: str):
    """
    :param s2:
    :return s1:
    """
    s1 = ''
    s = s2.lower()
    for item in s:
        if item:
            if s.count(item) > 1:
                s1 += ')'
            else:
                s1 += '('
            print(item, s.count(item))
        else:
            s1 += item
    return s1

if __name__ == '__main__':
    print(encode('UFLxub JbMzIcA(a PdCTDBTxPikr Bl(VTN@eOV'))
