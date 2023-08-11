#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i,Len = 0,len(nums)
        L = [0]*Len
        if Len==0:
            return 0
        for i in range(Len-1,-1,-1):
            if i==Len-1:
                L[i]=1
            else:
                L[i] = L[i+1]+1 if nums[i]<nums[i+1] else 1
        return max(L)
            
# @lc code=end

