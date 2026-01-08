### COUNTER SOLUTION ###
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count the frequency of each number in the array
        # ex: [1,1,1,2,2,3] => Counter({1: 3, 2: 2, 3: 1})
        count = Counter(nums)

        # get the k most frequent elements as list of (number, frequency) tuples
        # ex: Counter({1: 3, 2: 2, 3: 1}).most_common(2) => [(1, 3), (2, 2)]
        most_common = count.most_common(k)

        # extract only the numbers from the tuples (ignore frequencies)
        # for each tuple (num, cnt), we only take num
        # ex: [(1, 3), (2, 2)] => [1, 2]
        return [num for num, cnt in most_common]
        