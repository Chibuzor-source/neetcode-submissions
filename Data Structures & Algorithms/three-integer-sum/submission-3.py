class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        my_list = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                my_sum = nums[l] + nums[r]
                if my_sum == target:
                    my_list.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif my_sum < target:
                    l += 1
                else:
                    r -= 1
        return my_list
                
                

