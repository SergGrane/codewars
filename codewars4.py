# For this kata we assume the message receiving is performed automatically by the hardware that checks the line
# periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, and if the
# line is not connected (remote key is up), 0 is recorded. After the message is fully received,
# it gets to you for decoding as a string containing only symbols 0 and 1.
#
# For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:
#
# 1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011
#
# As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".


bits='1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
q1=bits.split('00000000000000')
print (q1)

s2=''
for i in q1:
    a1=i.split('000000')
    print(a1)
    for j in a1:
        dot=0
        dash=0
        pos=0
        j1 = j.split('00')
        print('dot ', dot, 'dash', dash, 'j' ,j,j1)
        for x in j1:
            if x == '11':
                s2= s2 + '.'
            else:
                s2 = s2 + '-'

        s2= s2 + ' '
    s2=s2 + '   '


print(s2)

