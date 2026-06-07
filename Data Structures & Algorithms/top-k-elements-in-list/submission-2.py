import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Creating a frequency map. The numbers are the keys and their frequencies the values
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
        # Create a minHeap
        minHeap = []
        # Insert the key, value pair in the minHeap, the smallest will be at index zero
        for key, value in my_dict.items():
            heapq.heappush(minHeap,(value, key))
        # Pop from the Heap until the length is equal to K, pop removes the smallest element
        while len(minHeap) != k: 
            heapq.heappop(minHeap)
        # Used List comprehension to create a list from the remaining elements in minHeap
        my_list = [minHeap[i][1] for i in range(len(minHeap))]

        return my_list






        


    
