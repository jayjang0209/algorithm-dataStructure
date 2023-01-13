class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        most_freq = -1
        ans = []
        for k, v in counter.items():
            if k % 2 == 0 and v > most_freq:
                most_freq = v
                ans = [k]
            elif k % 2 == 0 and v == most_freq:
                ans.append(k)
        return sorted(ans)[0] if len(ans) != 0 else -1



def main():
    solution = Solution()
    nums = [0,1,2,2,4,4,1]
    print(solution.mostFrequentEven(nums))


if __name__ == "__main__":
    main()