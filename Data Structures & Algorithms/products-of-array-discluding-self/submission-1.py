import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # First get product of Array
        product = math.prod(nums)
        # for each number in the array divide the product by it
        for i in range(len(nums)):
            # if a zero is encountered remove and take the product 
            if nums[i] == 0:
                nums.pop(i)
                new_product = math.prod(nums)
                res.append(new_product)
                nums.insert(i, 0)
            else:
                res.append(int(product / nums[i]))

        return res
