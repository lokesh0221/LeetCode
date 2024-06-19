class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i==0) or flowerbed[i-1] ==0
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n

# Example usage:
solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
print(solution.canPlaceFlowers([0, 0, 1, 0, 0], 1))  # Output: True
print(solution.canPlaceFlowers([0, 0, 1, 0, 0], 2))  # Output: True