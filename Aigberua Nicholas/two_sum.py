class Solution:
    def twosum(self, nums:list[int], target:int) -> list[int]:
        hashmap = {}
        for i in range (len(nums)):
            dif = target - nums[i]
            if dif in hashmap:
                return (i, hashmap[dif[i]])
            hashmap[dif[i]] = i