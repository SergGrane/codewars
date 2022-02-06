# The function must accept a non-negative integer. If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

def format_duration(seconds):
    if seconds==0:
        return 'now'
    s2 = ''
    s1 = ['year', 'day', 'hour', 'minute', 'second']
    s =[seconds//31536000,seconds%31536000//86400, seconds%86400//3600,
         seconds%3600//60,seconds % 60]
    z=5 - s.count(0)
    posit=0
    temp=[]
    for i in range(0, len(s)):
        if s[i] > 0:
            res = ''
            if s[i] >= 1:
                s2 = s2 + ' ' + str(s[i]) + ' ' + s1[i]
                temp.append(' ' + str(s[i]) + ' ' + s1[i])
                posit+=1

            if s[i] > 1:
                res = 's'

            if posit == 1 and z == 2 or posit == z-1 and z > 2:
                res = res + ' and'
            elif posit != z :
                res = res + ','
            s2 = s2 + res



#    return s2.lstrip()
    print(temp)
    return ",".join(temp[:-1]) + ' and' + temp[-1] if len(temp) > 1 else temp[0]

if __name__ == '__main__':
    print(format_duration(345634201))