class Solution:
    def twoSum(self,nums:list[int],target:int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            diffrence = target - nums[i]
            if diffrence in hashmap:
                return [i, hashmap[diffrence]]
            hashmap[nums[i]] = i    