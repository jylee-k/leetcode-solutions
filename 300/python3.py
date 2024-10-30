class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        maxi = 1
        # go backwards
        for i in range(n-1,-1, -1):
            # check if number is smaller than the smallest number of the longest seq
            print(nums[i])
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    # print('update')
                    # update lis
                    lis[i] = max(lis[j] + 1, lis[i])
                    # # update position of smallest number of longest seq
                    # idx = i
                else:
                    continue
            # print("lis", lis)
            maxi = max(maxi,lis[i])
        return maxi
