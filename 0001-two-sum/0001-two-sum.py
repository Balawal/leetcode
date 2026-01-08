class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hash map to store value - index mapping
        seen = {}
        
        # iterate through array with index and value
        for i, num in enumerate(nums):
            # calculate what number we need to reach target
            complement = target - num
            
            # check if we've seen the complement before
            if complement in seen:
                # found it, return the complement's index and current index
                return [seen[complement], i]
            
            # haven't found pair yet, store current number with its index
            seen[num] = i