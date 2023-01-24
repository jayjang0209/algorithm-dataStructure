class Solution:

    def maxProduct(self, nums: list[int]) -> int:
        # negative doesn't contribute to the maximize total sum
        maxSub = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub

    # Dynamic programming
    # Time complexity: O(n): single pass
    # Space complexity: O(n): to store memo array
    def maxProductDf(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # store intermediate result
        memo = [0] * len(nums)

        memo[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            memo[i] = max(nums[i], memo[i - 1] + nums[i])
            max_sum = max(max_sum, memo[i])

        return max_sum


def main():
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxProduct(nums))


if __name__ == "__main__":
    main()