# lc2032 correct answer
# class Solution:
#     def twoOutOfThree(self, nums1, nums2, nums3):
#         com=[]
#         for i in nums1+nums2+nums3:
#             if i in nums1 and i in nums2 or i in nums2 and i in nums3 or i in nums1 and i in nums3:
#                 com.append(i)
            
#         return set(com)
    
# obje=Solution()
# nums1 = [1,1,3,2]
# nums2 = [2,3]
# nums3 = [3]
# a=obje.twoOutOfThree(nums1,nums2,nums3)
# print(a)


# lc2148
# class Solution:
#     def countElements(self, nums):
#         count=0
#         s=min(nums)
#         l=max(nums)
#         for i in range(len(nums)):
#             if nums[i]==s or nums[i]== l :
#                 continue
#             else:
#                 count += 1
#         return count


# ob=Solution()
# nums = [11,7,2,15]
# a=ob.countElements(nums)
# print(a)


# 2000 CORRECT ANSWER
# class Solution:
#     def reversePrefix(self, word, ch):
#         if ch not in word:
#             return word

#         ind = word.find(ch)
#         prefix_to_reverse = word[:ind+1]
#         reversed_prefix = prefix_to_reverse[::-1]
#         result = reversed_prefix + word[ind+1:]

#         return result

# obj = Solution()
# ch = 'd'
# word = 'abcdefg'
# a = obj.reversePrefix(word, ch)
# print(a)


# 2000 also correct answer my logic 
# class Solution: 
#     def reversePrefix(self, word, ch):
#         if ch not in word:
#             return word
        
#         ind=word.find(ch)
#         wtr=word[:ind+1]
#         rev=wtr[::-1]
#         fw=rev+word[ind+1:]
#         return fw
        
# obj = Solution()
# ch = 'd'
# word = 'abcdefg'
# a = obj.reversePrefix(word, ch)
# print(a)



# lc 2176
# class Solution:
#     def countPairs(self, nums, k):
#         c=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     k=i*j
#                     # print(k,'b')
#                     if k%2==0:
#                         c+=1
#                         # print(c,'a')        
#         return c
    
    
# obj=Solution()
# nums = [3,1,2,2,2,1,3]
# k = 2
# a=obj.countPairs(nums,k)
# print(a)


# lc2180
# correct solution
# class Solution:
#     def countEven(self, num: int) -> int:
#         c = 0
#         for i in range(2,num+1):
#             sum=0
#             for j in str(i):
#                 sum+=int(j)
#             if sum%2==0:
#                 c+=1
#         return c

# obj = Solution()
# num = 30
# result = obj.countEven(num)
# print(result)


# # lc2185
# class Solution:
#     def prefixCount(self, words, pref):
#         # c=0
#         # for i in range(len( words)):
#         #   if pref in words[i]:
#         #     for j in range (len(words[i])):
#         #             print(words[i][j],'bb')
#         #             if words[i][j][0]==pref[0]:
                        
#         #                 print(words[i][j][0],pref[0],'iiiiiiiiiii')
#         #                 c+=1
#         # return c
#         c=0
#         for i in words:
#             if i.startswith(pref):
#                 c+=1
#         return c

# ob=Solution()

# # words = ["leetcode","win","loops","success"]
# # pref = "code"

# words = ["pay","attention","practice","attend"]
# pref = 'at'


# a=ob.prefixCount(words,pref)
# print(a)


# lc 2210 correct answer
# class Solution:
#     def countHillValley(self, nums):
#         c=0
        
#         for i in range(1,len(nums)-1) :

#             if nums[i] == nums[i+1]:

#               nums[i] = nums[i-1]

#             if nums[i] > nums[i-1] and nums[i] > nums[i+1]:

#               c+=1

#             if nums[i] < nums[i-1] and nums[i] < nums[i+1]:

#               c+=1
              
#         return c
    
# ob=Solution()
# # nums= [6,6,5,5,4,1]
# nums = [2,4,1,1,6,5]
# a=ob.countHillValley(nums)
# print(a)

# lc2264
# class Solution:
#     def largestGoodInteger(self, num) :
#       #correct answeer
#       max_good = ""
    
#       for i in range(len(num) - 2):
#           current_substring = num[i:i+3]
          
#           # Check if the substring consists of only one unique digit
#           if len(set(current_substring)) == 1:
#               # Update the maximum good integer if the current substring is greater
#               max_good = max(max_good, current_substring)
      
#       return max_good
        
      
# wrong answerrrr 
#         com=[]
#         for i in range(len(num)):
#             for j in range(i,len(num)):
#                 if num[i]==num[j]==num[j+1]:
#                     com.append(num[i:j+2])
#                     print(com,'aa')
                    
                    
# ob=Solution()
# num = "6777133339"
# # num = "2300019"
# # num = "42352338"
# a=ob.largestGoodInteger(num)
# print(a)

# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         mergedlits=list1+list2
#         mergedlits.sort()
#         return mergedlits
    
# a=Solution()
# list1 = [1,2,4]
# list2 = [1,3,4]
# la=a.mergeTwoLists(list1,list2)
# print(la)



# correct answer
# lc2016g
# class Solution:
#     def maximumDifference(self, nums) :
#         p=0
#         d=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j] > nums[i]:
                
#                     d=nums[j]-nums[i]
#                     print(nums[j],'aaa')
#                     print(nums[i],'bbb')
#                     print(nums[j]-nums[i],'cccccc')
                    
#                     if d>=p:
#                         print(d,p,'oo')
#                         p=d
#                         print(p,'joooooo')
   
                    
#         return p

# ov=Solution()
# nums = [1,5,2,10]
# # nums = [7,1,5,4]
# o=ov.maximumDifference(nums)
# print(o)


# lc 2283
# class Solution:
#     def digitCount(self, num: str) -> bool:
#         count = [0] * 10  # To store the count of each digit

#         for digit in num:
#             count[int(digit)] += 1  # Count occurrences of each digit

#         for i in range(len(num)):
#             if int(num[i]) != count[i]:
#                 return False

#         return True

# ob=Solution()
# num='1210'
# # num='030'
# a=ob.digitCount(num)
# print(a)


# 2357. Make Array Zero by Subtracting Equal Amounts
# class Solution:
#     def minimumOperations(self, nums) :
#         num=set(nums)
#         print(num,'aaaaaa')

#         if 0 in num:
            
#             num.remove(0)
#             print(num)
            
#         return len(num)
        
                
                
#         # x=1
#         # c=0
#         # if nums == 0:
#         #     return 0
#         # else:
#         #     for i in range(len(nums)):
#         #         if nums[i]-x==0:
#         #             print(nums[i],'aaa')
#         #             c+=1
#         #         x+=1
#         #     return c
                

# ob=Solution()
# nums = [1,5,0,3,5]
# a=ob.minimumOperations(nums)
# print(a)


# 2351. First Letter to Appear Twice
# class Solution:
#     def repeatedCharacter(self, s):
#         d=''
#         for i in range(len(s)):
#             if s[i] in d:
#                return s[i]
#             d=d+s[i]
#             print(d,'aaaa')
#         return d 
        
        
        
#         # for i in range(len(s)-1):
#         #     if s[i]==s[i+1]:
#         #         return s[i]
            
            
# ob=Solution()
# # s = "abccbaacz"
# s = "abcdde"
# a=ob.repeatedCharacter(s)
# print(a)


# 2413. Smallest Even Multiple
# class Solution:
#     def smallestEvenMultiple(self, n) :
#         if n%2==0:

#             return n 
            
#         return n*2

# obj=Solution()
# n=5
# # n=6
# a=obj.smallestEvenMultiple(n)
# print(a)



# lc 2418
# 2418. Sort the People
# Example 1:
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.


# class Solution:
#     def sortPeople(self, names, heights):
#         for i in range(len(heights)):
#             for j in range(len(heights)):
#                 if heights[i]<heights[j]:
#                     heights[i],heights[j]=heights[j],heights[i]
#                     names[i],names[j]=names[j],names[i]
#         return names
        
# obj=Solution() 
# names = ["Mary","John","Emma"]
# heights = [180,165,170]
# a=obj.sortPeople(names,heights)     
# print(a)  

# 2475. Number of Unequal Triplets in Array

# class Solution:
#     def unequalTriplets(self, nums):
#         count=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]!=nums[j]:
#                     for k in range(j+1,len(nums)):
#                         if nums[i]!=nums[k] and nums[j]!= nums[k]:
#                             count+=1
#         return count
    
# obj=Solution()
# nums=[4,4,2,4,3]
# a=obj.unequalTriplets(nums)
# print(a)
