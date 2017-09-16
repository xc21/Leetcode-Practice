class Solution:
    # @param a list of integers
    # @return an integer
    def deleteDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                #swap A[i] and A[j+1]
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1