class Solution:
    def kk(self,A):
        if not A:
            return 
        self.kk(A.left)
        self.B-=1
        if self.B==0:
            self.res=A.val
            return 
        self.kk(A.right)
        
    def kthsmallest(self, A,B) -> int:
        self.B=B
        self.res=None
        self.kk(A)
        return self.res   
