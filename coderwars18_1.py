# YWrite a function that will find all the anagrams of a word from a list. You will be given two inputs a
# word and an array with words. You should return an array of all the anagrams or an empty array if there are none.

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

if __name__ == '__main__':
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))