# YWrite a function that will find all the anagrams of a word from a list. You will be given two inputs a
# word and an array with words. You should return an array of all the anagrams or an empty array if there are none.

def anagrams(word, words):
    s=sum(map(ord,word))
    print (s)
    s1=[]
    for i in words:
        s2 = sum(map(ord,i))
        print(s2)
        if s == s2:
            s1.append(i)
    return s1

if __name__ == '__main__':
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))