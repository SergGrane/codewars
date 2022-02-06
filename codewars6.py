# Your task is to make a function that can take any non-negative integer as an argument and return
# it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
# Input: 42145 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 123456789 Output: 987654321
inp=123456789
inp=list(str(inp))
print(inp)
inp.sort()
inp.reverse()
s=''
for i in inp:
    s= s+i

print(int(s))
