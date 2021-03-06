class Solution:
 
    def removeDuplicates_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def move_element(arr, i, j):
            if i < 0 or j >= len(arr):
                return
            x = arr[i]
            for k in range(i+1, j+1):
                arr[k-1] = arr[k]
            arr[j] = x

        i = 1
        j = len(nums)-1
        if len(nums) < 1:
            return 0
        a = nums[0]
        n = 1
        while i <= j:
            if nums[i] == a:
                move_element(nums, i, j)
                j -= 1
            else:
                a = nums[i]
                i += 1
                n += 1
        return n
 
    def removeDuplicates(self, nums):
        now=None
        j=0
        for i in range(len(nums)):
            if nums[i]!=now:
                now=nums[i]
                nums[j]=nums[i]
                j+=1
        return j



s = Solution()
arr = [1, 1, 2, 2, 2, 3, 3]
n = s.removeDuplicates(arr)
print(n, arr)
