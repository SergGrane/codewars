# Given a number determine if it Automorphic or not .
# A number is called Automorphic number if and only if its square ends in the same digits as the number itself.

n1=(95,625,225)

for n in n1:

    if str(n) == str(n**2)[0-len(str(n)):]:
        print("Automorphic")
    else:
        print ("Not!!")