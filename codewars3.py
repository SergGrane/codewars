# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−,
# letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital l
# etters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3
# spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.
#
# NOTE: Extra spaces before or after the code have no meaning and should be ignored.
#
# In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is
# the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···.
# These special codes are treated as single special characters, and usually are transmitted as separate words.
#
# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

MORSE= { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-','SOS' :'···−−−···'}

morze_code='.... . -.--    .--- ..- -.. .'
s1=''
q=morze_code.split('   ')

for item in q:
    a=item.split()
    print(a)
    for j in a:
        for i in  MORSE:
            if MORSE.get(i)==j:
                s1=s1+i
    s1=s1+' '

print (s1.rstrip())


