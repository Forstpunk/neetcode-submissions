class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        prefix_sum = 0
        result = 0

        for i in nums:
            prefix_sum +=i
            result += dic.get(prefix_sum-k,0)
            dic[prefix_sum]=dic.get(prefix_sum,0)+1
        return result