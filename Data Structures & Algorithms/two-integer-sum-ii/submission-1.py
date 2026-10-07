class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]

            if current == target:
                return [l + 1, r + 1]    # 1-indexed
            elif current > target:
                r -= 1                    # sum too big → shrink from right
            else:
                l += 1                    # sum too small → grow from left

        return []