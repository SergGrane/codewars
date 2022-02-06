numb_1 = int(input('Number is '))
sum1 = 0

for i in range(1,numb_1+1):
    if i%3==0 or i%5==0 or i%3==0 and i%5==0:
        sum1 = sum1 + i

if numb_1 == 0:
    sum1 = 0

print ('Sum is ',sum1)