class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        return next(i for i in count(n) if prod(map(int,str(i)))%t==0)
        