class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #we will be using a heap, which stores the BIGGEST value on top
        #in this case, it will store the point that is the FARTHEST (greatest distance from the origin)
        #in python, it functions as a minheap, sotirng the SMALLEST value, so we just need to negate the distance values to know that the one at the top, once negated will be the sallest, adhering to minheap module in python 
        max_heap = []

        for x,y in points:

            #calculate the distance from the origin, x^2 + y^2 (just the magnitude for now)
            dist = x*x + y*y

            #push the negation of the distance, along with the coordinates to the heap
            heapq.heappush(max_heap, (-dist, [x,y]))

            #if the length of the heap is greater than k, then we need to kick out the top value, which will by default be the furthest point, leaving the closest value
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        #return only the points, dont need the distance
        return [point for dist, point in max_heap]
        