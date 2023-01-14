import heapq


class Solution:
    # 1. Heap
    # Time: O(N * logk) :
    # Space: O(k) : store the heap elements

    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = []

        for num in nums:
            heapq.heappush(max_heap, -num)

        return -max_heap[k-1]


def main():
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(solution.findKthLargest(nums, k))


if __name__ == "__main__":
    main()