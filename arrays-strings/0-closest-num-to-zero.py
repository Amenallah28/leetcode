class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]   # Start with the first number in the array
        for num in nums :
            if abs(num) < abs(closest):  # If the current number is closer to 0
                closest = num
            elif abs(num) == abs(closest) and num > closest :   # Same distance but larger value
                closest = num
        return closest
        