class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            else :
                seen.add(n)
            total = 0
            temp = n 
            while temp>0:
                m = temp % 10 
                total = total+ (m*m)
                temp=temp//10
            n=total
        if n==1:
            return True
        else :
            return False
        