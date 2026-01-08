class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #empty array, return empty string
        if not strs:
            return ""

        #we will check each character position, using the first string as reference
        for i in range(len(strs[0])):

            # get the character at position i from first string
            char = strs[0][i]
            
            #check if this character matches in all subsequent strings
            for string in strs[1:]:
                
                #if we've reached the end of the current string or the character at doesnt match, we terminate and just return the current prefix from the first string, up till i
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        
        #if we make it through all matches, the first string is the common prefix
        return strs[0]