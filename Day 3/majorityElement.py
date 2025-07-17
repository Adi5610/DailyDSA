class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #using boyer moore voting algo
        x,count = 0,0

        for num in nums:

            if count == 0:
                x = num
            
            count += (1 if x == num else -1)
        return x

        # fast solution using sorting
        mid = len(nums)//2
        return sorted(nums)[mid]