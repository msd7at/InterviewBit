link: https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        l=len(A)
        d=0
        for i in range(1,l):
           x=max(abs(A[i-1]-A[i]),abs(B[i-1]-B[i])) 
           d+=x
        return d
