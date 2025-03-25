class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        F,TM,BM = {0:1,1:1} , {1:0},{1:0}
        for i in range(2,n+1):
            F[i] = F[i-1]+F[i-2]+TM[i-1] + BM[i-1]
            TM[i] = BM[i-1] + F[i-2]
            BM[i] = TM[i-1] + F[i-2]
        return F[n] % (10**9+7)