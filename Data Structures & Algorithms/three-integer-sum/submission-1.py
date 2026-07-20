class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        my_list = []

        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1] :
                continue
            l, r = i + 1, len(nums) - 1
            target = -val
            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    mini_list = [val, nums[l], nums[r]]
                    my_list.append(mini_list)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return my_list
            
