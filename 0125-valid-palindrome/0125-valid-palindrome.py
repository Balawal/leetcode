class Solution:
    def isPalindrome(self, s: str) -> bool:

        #basic two pointer problem, start with 2 points one at the left index and one at the right index
        left = 0
        right = len(s) - 1

        #moving the pointers toward each other
        while left < right:
            
            #we want to skip anything that isnt alphanumeric (a letter or digit). if it isn't alphanumeric, just inrement the left pointer
            while left < right and not s[left].isalnum():
                left += 1
            
            #similarly for the right pointer
            while left < right and not s[right].isalnum():
                right -= 1
            
            #now we compare the characters, if they are not equal, we can immediately return false since it cannot be a palindrome
            if s[left].lower() != s[right].lower():
                return False
            
            #otherwise we increment the pointers further
            left += 1
            right -= 1
        
        #once we make it through, we know every character is the same, so it must be a palindrome
        return True
        