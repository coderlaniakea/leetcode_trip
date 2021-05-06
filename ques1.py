class Solution:
    def twoSum(self, nums, target):
        
        # 方法1：
        for i in range(len(nums)):
            left_num = nums[i+1:]
            for j in range(len(left_num)):
                
                if nums[i] + left_num[j] == target:
                    return [i, i+j+1]
        
        # 方法2：
        # for i in range(len(nums)):
        #     b = target - nums[i]
        #     if b in nums:
        #         # 找b
        #         for j in range(len(nums)):
        #             if nums[j] == b and i != j:
        #                 return [i,j]


if __name__ == '__main__':

    nums = [3,3,4]
    target = 6

    s = Solution()
    resu = s.twoSum(nums, target)
    print(resu)