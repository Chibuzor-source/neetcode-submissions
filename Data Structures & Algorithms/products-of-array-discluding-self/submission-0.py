import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = math.prod(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                new_product = math.prod(nums)
                res.append(int(new_product))
                nums.insert(i,0)
            else:
                res.append(int(product / nums[i]))

        return res
