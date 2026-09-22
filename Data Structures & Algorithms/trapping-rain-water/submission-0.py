class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
    
    # Step 1: Build prefix max (left max height up to i)
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

    # Step 2: Build suffix max (right max height up to i)
        right_max = [0] * n
        right_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

    # Step 3: Calculate trapped water
        trapped = 0
        for i in range(n):
            trapped += min(left_max[i], right_max[i]) - height[i]

        return trapped
        