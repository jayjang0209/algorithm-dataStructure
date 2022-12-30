class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        for char in s:
            if char in map.keys():
                map[char] += 1
            else:
                map[char] = 1

        for char in s:
            if map[char] == 1:
                return s.find(char)

        return -1


def main():
    solution = Solution()
    string = "leetcode"
    print(solution.firstUniqChar(string))


if __name__ == "__main__":
    main()