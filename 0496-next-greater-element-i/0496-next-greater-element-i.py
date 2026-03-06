class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        d={}
        d[nums2[-1]]=-1
        stack.append(nums2[-1])
        for i in range(len(nums2)-2,-1,-1):
            if (nums2[i]<stack[-1]):
                d[nums2[i]]=stack[-1]
                stack.append(nums2[i])
                continue
            while(stack and nums2[i]>stack[-1]):
                stack.pop()
            if not stack:
                d[nums2[i]]=-1
                stack.append(nums2[i])
            else:
                d[nums2[i]]=stack[-1]
                stack.append(nums2[i])
        for i in range(len(nums1)):
                nums1[i]=d[nums1[i]]
        return nums1


           
