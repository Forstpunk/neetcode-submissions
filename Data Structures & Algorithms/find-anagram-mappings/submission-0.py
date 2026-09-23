class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_index = {value: index for index, value in enumerate(nums2)}
        result = []
        for num in nums1:
            result.append(num_to_index[num])
        return result 
        