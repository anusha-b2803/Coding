class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        su=0
        pr=1
        while(n>0):
            i=n%10
            su+=i
            pr*=i
            n=n//10
        return pr-su    
