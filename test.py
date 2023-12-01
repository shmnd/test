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
class Solution:
    def countElements(self, nums):
        count=0
        s=min(nums)
        l=max(nums)
        for i in range(len(nums)):
            if nums[i]==s or nums[i]== l :
                continue
            else:
                count += 1
        return count


ob=Solution()
nums = [11,7,2,15]
a=ob.countElements(nums)
print(a)