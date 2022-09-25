
vowels = ('a','i','e','o','u')
def Sld_Window(i, word):
    res = []
    l = r = i # initialize left and right pointer
    while(l <= r and r < len(word) and word[r] in vowels):
        r += 1
    return l , r
    
def VowelList(word):

    res = []
    l = r = 0
    while(l < len(word)):

        if word[l] in vowels:
            l, r = Sld_Window(l, word)
            res.append(word[l:r])
            l = r
        l += 1
            
    return res

if __name__ == "__main__":
    print("Contigous Vowels through sliding window in O(n) Complexity:")

    #words = "cooeeing koauau queeai queeais queueing"

    print(VowelList("coeeing koauau queeai queeais queueing"))
