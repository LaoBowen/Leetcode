from math import sqrt


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
        # robust
        if (num <= 1):
            return False

        is_perfect_number = False
        sum = 0
        for factor in range(1, int(sqrt(num)) + 1):
            # 判断是否是因子
            if num % factor == 0:
                sum += factor
                # 对应的另一个因子且剔除相同因子重复情况
                if factor > 1 and num // factor != factor:
                    sum += num // factor
        if num == sum:
            is_perfect_number = True
        return is_perfect_number