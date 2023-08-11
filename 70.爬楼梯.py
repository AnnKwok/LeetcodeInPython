#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        L = [0]*(n+1)
        if n==0:
            return 0
        for i in range(1,n+1,1):
            if i==1:
                L[i] =1
            elif i==2:
                L[i] = 2
            # elif i-1>=0 and i-2<0:
            #     L[i] = L[i-1]
            else:# i-2>=0:
                L[i] = L[i-1]+L[i-2]
        return L[n]
# @lc code=end

