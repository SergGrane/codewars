# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
def chr_numb(s):

    return ' '.join(str(ord(i)-96) for i in s.lower() if i.isalpha())


print(chr_numb("The sunset sets at twelve o' clock."))
#19 7 4 18 20 13 18 4 19 18 4 19 18 0 19 19 22 4 11 21 4 14 2 11 14 2 10
#20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11