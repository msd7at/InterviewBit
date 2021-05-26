#link : https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        msh=0
        mstn=min(A)
        for i in A:
            msh=msh+i
            if msh>mstn:
                mstn=msh
            if msh<0:
                msh=0
        return mstn
