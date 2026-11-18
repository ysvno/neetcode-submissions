class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        val = 0 
        for i in range(n):
            for j in range(i+1,n):
                if arr[j] > val:
                    val = arr[j]
            arr[i] = val
            val = 0
        arr[-1] = -1
        return arr