class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)

        l, r = 0, len(nums) - 1

        while r >= 0 and l < len(nums):
            l_arr[l] = l_mult
            r_arr[r] = r_mult
            l_mult *= nums[l]
            r_mult *= nums[r]
            l += 1
            r -= 1

        return [x * y for x, y in zip(l_arr, r_arr)]

