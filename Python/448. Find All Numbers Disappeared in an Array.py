class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            # for input [4,3,2,7,8,2,3,1] num
            #     index  0,1,2,3,4,5,6,7
            # should be  1,2,3,4,5,6,7,8
            # after the first for loop:
            #            [4,3,2,-7,8,2,3,1]
            # after the second for loop:
            #            [4,3,-2,-7,8,2,3,1]
            # after going over the whole arrary
            # num becomes [-4,-3,-2,-7,8,2,-3,-1]
            #               0,1, 2  3  4 5  6 7
            # the index 4 5 have never been change to negative
            # so the corresponding "should be" 5 6 is the disappeared number



            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        return [i + 1 for i, n in enumerate(nums) if n > 0]

    #Arrary type of problem
    #methods: turning to negative
    #time: O(n), space: O(n)
