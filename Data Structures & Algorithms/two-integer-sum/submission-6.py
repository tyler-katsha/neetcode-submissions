class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        
        # loop through each element keeping track of left and right pointer
        for i in range(n):
            difference = target - nums[i]

            if difference  in hashmap:
                return [hashmap[difference],i]
            hashmap[nums[i]] = i


        return [-1,-1] 
        