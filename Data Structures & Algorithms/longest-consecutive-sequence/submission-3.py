class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        my_set = set(nums)

        max_length = 0

        for num in my_set:
            seq_length = 0
            if (num - 1) not in my_set:
                seq_length = 1
                while (num + 1) in my_set:
                    seq_length += 1
                    num += 1
            max_length = max(max_length, seq_length)

        return max_length

      