nums = [1]
i,j,maxValue,Len  = 0,0,0,len(nums)
for i in range(Len):
     for j in range(i,Len,1):
          value = sum(nums[i:j])
          if value>maxValue:
               maxValue=value
print(maxValue)