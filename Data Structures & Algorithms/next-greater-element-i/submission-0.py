class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Phase 1: monotonic stack on nums2
        stack = []
        next_greater = {}    # value → next greater value
        
        for num in nums2:
            while stack and num > stack[-1]:
                resolved = stack.pop()
                next_greater[resolved] = num    # num is the next greater for resolved
            stack.append(num)
        
        # remaining elements in stack have no next greater
        while stack:
            next_greater[stack.pop()] = -1
        
        # Phase 2: look up each nums1 element
        return [next_greater[num] for num in nums1]