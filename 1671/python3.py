class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # calculate LIS and LDS for each index
        n = len(nums)
        if n == 3:
            return 0
        lis = [1]*n
        lds = [1]*n
        for x in range(n):
            # print("x", x)
            for i in range(x):
                # print("i", i)
                #lis
                if nums[i] < nums[x]:
                    lis[x] = max(1 + lis[i], lis[x])
            for d in range(n-1, n-1-x, -1):
                # print("d", d)
                if nums[d] < nums[n-1-x]:
                    lds[n-1-x] = max(1 + lds[d], lds[n-1-x])
            # print(lis)
            # print(lds , "\n")
        summ = [a + b for (a,b) in zip(lis,lds) if a != 1 and b != 1]
        
        return n - max(summ) + 1
        
            
