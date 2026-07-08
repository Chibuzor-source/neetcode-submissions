class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_sequence = 0

        for num in num_set:
            min_sequence = 0
            if (num - 1) not in num_set:
                min_sequence += 1
                while (num + 1) in num_set:
                    min_sequence += 1
                    num += 1
            
            longest_sequence = max(min_sequence, longest_sequence)

        return longest_sequence

      