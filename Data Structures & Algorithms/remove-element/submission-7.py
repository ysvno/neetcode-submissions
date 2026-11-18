class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                n -= 1
                for j in range(i,n):
                    nums[j] = nums[j+1]
                nums[n] = -1
            else:
                i += 1
        return n