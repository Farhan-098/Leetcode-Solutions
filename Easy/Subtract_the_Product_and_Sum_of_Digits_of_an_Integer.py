class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of_digits = 0
        product_of_digits = 1


        while n>0:
            last = n%10

            sum_of_digits+=last
            product_of_digits*=last

            n = n//10

        return product_of_digits - sum_of_digits