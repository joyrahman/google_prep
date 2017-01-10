'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        #check if length is less then 3
        n = len(nums)
        if n<3:
            return []
        
        result = set()
        nums.sort()
        
        
        #  now we scan for each element from left to right and from right towards left
        #  A[i, j,........k] 
        #  we will check for duplicate as well as run upto length n-2
        #  if a[i]+a[j]+a[k]==0, add i,j,k, 
        #  else if less
        #      increase J 
        #  else if bigger, 
        #      decrease k
        
        for i in xrange(n-2):
            if (i==0 or nums[i]!=nums[i-1]):
                j = i+1
                k = n-1
            
            while (j<k):
                sum = nums[i] + nums[j] + nums[k]
                if sum ==0:
                    result.add((nums[i],nums[j],nums[k]))
                    j+=1 #next position
                    k-=1 #next position
                elif sum <0:
                    j +=1
                else:
                    k -=1
        #end of for
        return list(result)

