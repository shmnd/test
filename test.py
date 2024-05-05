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

class Solution():
    def target(self, nums, t):
        d={}

        for i in range(len(nums)):
            k=t-nums[i]

            if k in d:
                return [d[k],i]
            d[nums[i]]=i
        return d

obj = Solution()
nums = [2, 7, 11, 15]
t = 9
a = obj.target(nums, t)
print(a)

