class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0:1}
        prefix_sum = 0
        result = 0

        for i in nums:
            prefix_sum += i
            result +=prefix_count.get(prefix_sum - k,0)
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum,0) + 1
        return result
        