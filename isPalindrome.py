class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_Str=str(x)
        return x_Str==x_Str[::-1]
