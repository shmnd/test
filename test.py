# lc2032
class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        com=[]
        for i in range(len(nums1)):

            for j in range(len(nums2)):

                for k in range(len(nums3)):
                    
                    if nums1[i]==nums2[j]:
                        com.append(nums1[i])

                    elif nums1[i]==nums3[k]:
                        com.append(nums2[j])

                    elif nums2[j]==nums3[k]:
                        com.append(nums2[j])

                    else:
                        return []
        return com

obj=Solution()
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
a=obj.twoOutOfThree(nums1,nums2,nums3)
print(a)