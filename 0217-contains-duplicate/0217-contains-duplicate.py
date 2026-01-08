class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()    #use a set to track seen numbers

        for num in nums:        #check each number
            if num in seen:     #if we've seen it before, return true
                return True
            
            seen.add(num)       #else, add it to the set
        
        return False            #return false if no duplicate found