class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_ = {

        }
        for i in range(len(nums)):

            diff = target-nums[i] 
               
            if diff in hash_:

                return [i, hash_[diff]]

            hash_[nums[i]] = i