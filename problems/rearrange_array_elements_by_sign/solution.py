class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1 , l2 ,l3= [] , [] , []
        for i in range(len(nums)):
            if(nums[i]>=0):
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        for i in range(len(nums)//2):
            l3.append(l1[i])
            l3.append(l2[i])
        return l3