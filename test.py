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




# class Solution:
#     def maximumTripletValue(self, nums):
#         f=0
#         m=len(nums)//2
#         k=nums[m]
#         l=nums[-1]
#         print(f,m,l,k)

#         if len(nums)%2==0:
#                 print('outtt')
#                 return 0
#         else:
#                 print('innnnn')
#                 for i in range(1,m):
#                         print('iiiiiiiiiiiiin')
#                         print(nums[0],nums[i])
                        
#                         if nums[0]>nums[i]:
#                                 f=nums[i]
#                                 print(f,'ffffff')
#                                 res= (f-k)*l
#                                 print(res)
#                         else:
#                                 f=nums[0]
#                                 print(f,'ssss')
#                                 res= (f-k)*l
#                                 print(res)
#                 if res>0:
#                         return res
#                 else:
#                         return 0
# obj=Solution()
# nums = [1,10,3,4,19]
# # nums = [12,6,1,2,7]
# # nums = [1,2,3]
# # nums=[1000000,1,1000000]                               

# a=obj.maximumTripletValue(nums)
# print(a)   



#////////////////////////////////////// zeno techonology

shipping=0  
cartTotal =0  

giftWrap={}

productDetails ={
        'productA':20,
        'productB':40,
        'productC':50
}

productQuantity={
        'productA':'',
        'productB':'',
        'productC':''
}

for key,value in productDetails.items():
        quanity=int(input(f'enter the  quantity for {key}:'))
        productQuantity[key]=quanity
           
totalProductPrice={
        'productA':'',
        'productB':'',
        'productC':''
}

DiscountAmounts={
        'DiscountA':'',
        'DiscountB':'',
        'DiscountC':'',
        'DiscountD':''
}

for key,value in productQuantity.items():
        cartTotal+=productDetails[key]*value

# indivual price of products
for key,value in productQuantity.items():
        iPrice=productDetails[key]*value
        totalProductPrice[key]=iPrice
        
for key,value in totalProductPrice.items():
        qnty=productQuantity[key]
        price=productDetails[key]
        print(f'{key}:quantity:{qnty}*{price},total amount:{value}')
        
print('sub total amount:' ,cartTotal)

# flat_10_discount": If cart total exceeds $200, apply a flat $10 discount on the cart total.      
disAmtA=10      
if cartTotal > 200:
        cartA=round(cartTotal-disAmtA)

        DiscountAmounts['DiscountA']=cartA
else:
        DiscountAmounts['DiscountA']=0

        
    
# # "bulk_5_discount": If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price.
per=0
disAmtB=0.05      
finalRes=0 
# countB=0
for key,value in productQuantity.items():
        # if countB==0:
                if value>10:
                        # countB+=1
                        singleprdAmt=productDetails[key]*value
                        totalDisAmtB=disAmtB*singleprdAmt
                        cartB =round(cartTotal-totalDisAmtB)  
                        DiscountAmounts['DiscountB']=cartB 
                        break
                else:
                        DiscountAmounts['DiscountB']=0

totalQuantity=0
qtyoffall=0
for key,value in productQuantity.items():
        totalQuantity+=productQuantity[key]
qtyoffall=totalQuantity

disAmtC=0
if qtyoffall > 20:
        disAmtC=round(0.10 * cartTotal)
        cartC=cartTotal-disAmtC
        DiscountAmounts['DiscountC']=cartC
else:
        DiscountAmounts['DiscountC']=0
             
        
# #"tiered_50_discount": If total quantity exceeds 30 units & any single product quantity greater than 15, then apply a 50% discount on products which are above  15 quantity. The first 15 quantities have the original price and units above 15 will get a 50% discount.           
zero=0
if totalQuantity > 30 :
         print('ssssssss')
         for key,value in productQuantity.items():
                if value>15:
                        print('ccccccccccc')
                        originalPrice=productDetails[key]
                        disAmtD=0.5*originalPrice
                        prdQty=productQuantity[key]-15
                        if prdQty >0:
                                print('kkkkkkkk')
                                totalDisAmt=disAmtD*prdQty
                                
                                cartD=round(cartTotal-totalDisAmt)
                                DiscountAmounts['DiscountD']=cartD
                                print(cartD,'jjjjjj')
                                
                                break
                                                
                        else:
                                DiscountAmounts['DiscountD']=0
                
                else: 
                        DiscountAmounts['DiscountD']=0

else: 
        DiscountAmounts['DiscountD']=0
        
        
#//check best dis                      
for key,value in DiscountAmounts.items():
        print(f'{key}:{value}')
       

filterDic=[]
for key,value in DiscountAmounts.items():
        if value >0:
                filterDic.append(value)
                
        else:
                bestOfffer=0 
if filterDic:                  
        bestOfffer=min(filterDic)
else:
        bestOfffer=0
        
        
max_dis=bestOfffer
print('mmmmmmmmmmmzzzzzzzzzzzz',max_dis)

# for key,value in DiscountAmounts.items():
#         if max_dis:
#                 if max_dis==DiscountAmounts[key]:
#                         dis_amt=cartTotal-max_dis
#                         print('Discount Amount applied:',f'{key}:{dis_amt}')
#         else:
#                 max_dis=0
        
                
                
# print('your total amount:',max_dis)  #need to change into cartTotal








        
        
        
        
        

    
    
    
  
