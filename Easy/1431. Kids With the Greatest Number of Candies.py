class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        boolean = []
        for i in candies:
            boolean.append((i+extraCandies) >= max(candies))
        return boolean