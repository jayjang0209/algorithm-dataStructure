nums = [358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549]

# Time: O(n * logn)
# Space: max O(n)
def twoSumLessThanK(nums, k) -> int:
    sorted_nums = sorted(nums)
    max = -1

    for i in range(len(sorted_nums)):
        left = i + 1
        right = len(sorted_nums) - 1
        complement = k - sorted_nums[i]
        second_num_max = 0
        while left <= right:
            mid = (left + right) // 2
            if sorted_nums[mid] > second_num_max and sorted_nums[mid] < complement:
                second_num_max = sorted_nums[mid]

            elif sorted_nums[mid] > complement:
                right = mid - 1

            else:
                left = mid + 1
        max_curr = sorted_nums[i] + second_num_max
        if max_curr < k and max_curr > max and second_num_max != 0:
            max = max_curr
    return max

# Time: O(n^2)
# Space: O(1)
def twoSumLessThanKBruteForce(nums,k):
    sorted_nums = sorted(nums)
    max = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            two_sum = sorted_nums[i] + sorted_nums[j]
            if two_sum < k and two_sum > max:
                max = two_sum
    return max


print(twoSumLessThanK(nums, 1800))
print(twoSumLessThanKBruteForce(nums, 1800))