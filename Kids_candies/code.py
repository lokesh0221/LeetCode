class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res=[]
        max_candies = max(candies)
        for i in candies:
            if i+extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res
solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))  # Output: [True, True, True, False, True]
print(solution.kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [True, False, False, False, False]
print(solution.kidsWithCandies([12, 1, 12], 10))    # Output: [True, False, True]
    