#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    # 200/210 超时了
    '''def maxSubArray(self, nums: List[int]) -> int:
        i,j,maxValue,Len  = 0,0,0,len(nums)
        if Len==0:
            return 0
        else:
            maxValue = nums[0]
        for i in range(Len):
            for j in range(i,Len,1):
                value = sum(nums[i:j+1])
                if value>maxValue:
                    maxValue=value
        return maxValue'''
    def maxSubArray(self, nums: List[int]) -> int:
        i,j,Len  = 0,0,len(nums)
        if Len==0:
            return 0
        L = [0]*Len
        for i in range(Len-1,-1,-1):
            if i==Len-1:
                L[i]=nums[i]
            else:
                L[i] =max(nums[i]+L[i+1],nums[i])
        return max(L)

# @lc code=end

