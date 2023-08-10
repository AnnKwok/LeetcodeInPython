#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        i,Len = 0,len(nums)
        if Len==0:
            return 0
        else:
            L = [0]*Len
            for i in range(Len-1,-1,-1):
                if i==Len-1:
                    L[i] = 1
                else:
                    # 遍历i后面的每个值，判断是否能构成最大子序列，如果可以就加1
                    maxValue = 1# 一定要理解L的含义，是从i开始的最长序列的长度，是必须包含i这个数值的，否则后续无法计算
                    for j in range(i+1,Len,1):
                        if nums[i]<nums[j]:
                            if L[j]+1>maxValue:
                                maxValue = L[j]+1
                    L[i] = maxValue
            # print(L)
            return max(L)
# @lc code=end

