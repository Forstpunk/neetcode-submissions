class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
    
    # Step 2: Create buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
    
    # Step 3: Collect from highest frequency to lowest
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result