# lc2032 correct answer
class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        com=[]
        for i in nums1+nums2+nums3:
            if i in nums1 and i in nums2 or i in nums2 and i in nums3 or i in nums1 and i in nums3:
                com.append(i)
            
        return set(com)
    
obje=Solution()
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
a=obje.twoOutOfThree(nums1,nums2,nums3)
print(a)