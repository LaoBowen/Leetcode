class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """[summary]
        
        Parameters
        ----------
        num : int
            [description]
        
        Returns
        -------
        bool
            [description]
        """
        if (num <= 1):
            return False
        sum = 0
        i = 2
        while (i * i < num):
            if (num % i == 0):
                sum += i
                sum += num / i
            i += 1
        if (i * i == num):
            sum += i
        sum += 1
        return sum == num