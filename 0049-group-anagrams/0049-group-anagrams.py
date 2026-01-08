class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #create a dictionary that utomatically creates empty lists for keys
        #when acessing a new key, create an empty list
        res = defaultdict(list)

        #going through each word in the input
        for s in strs:

            #create an array with 26 0's, one slot for each letter from a-z
            #we will use this to store how many times each letter appears in the current string 
            count = [0] * 26

            #for each character in the word
            for char in s:

                #we convert each character to its ASCII number (ex: ord(e) - ord(a) = 101-97 = 4)
                #to determine its position in the list of 0's, and then increment it for each time we encounter it in the string
                count[ord(char) - ord("a")] += 1

            #now we convert the count LIST into a TUPLE so we can access the key, which we will use for the dictionary
            #as we append anagram strings for the same tuple value
            key = tuple(count)

            #add the current string to the list of strings with this signature tuple value
            #ex: res[(1,0,0,0,1,0,...)] = ["eat", "tea", "ate"]
            #if the key (tuple) already exists → add to existing list
            #if the key is new, create new list
            res[key].append(s)
        
        #res.values() erturns the values in the key,value dictionary
        #ex: dict_values([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
        # list() converts it to a regular Python list
        # returns: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        return list(res.values())
        


        #words are anagrams if and only if they have the same tuple (character count signature)
        #the dictionary groups them automatically
        #res = {
        #     tuple_A: ["eat", "tea", "ate"],  # all have tuple_A
        #     tuple_B: ["tan", "nat"],          # all have tuple_B
        #     tuple_C: ["bat"]                  # only has tuple_C
        # }