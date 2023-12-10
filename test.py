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




class Solution:
    def mergeTwoLists(self, list1, list2):
        mergedlits=list1+list2
        mergedlits.sort()
        return mergedlits
    
    
    
    
a=Solution()
list1 = [1,2,4]
list2 = [1,3,4]
la=a.mergeTwoLists(list1,list2)
print(la)
