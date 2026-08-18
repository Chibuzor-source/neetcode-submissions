class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        my_list = []
        product, count = 1, 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                count += 1
        if count >= 2:
            return [0] * len(nums)
        for num in nums:
            if num == 0:
                my_list.append(product)
            elif count == 1:
                my_list.append(0)
            else:
                my_list.append(product // num)
        return my_list