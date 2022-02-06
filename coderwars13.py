# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it
# in the alphabet
# . ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.

def rot13(s):

    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph1 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    s1=''
    for i in s:

        a = alph.find(i)
        a1 = alph1.find(i)
        print(i,a,a1)
        if a != -1:
            s1 += alph[a+13]
        elif a1 != -1:
            s1 += alph1[a1+13]
        else:
            s1 += i
        print(s1)
    return s1


print(rot13('Te1122st'))
