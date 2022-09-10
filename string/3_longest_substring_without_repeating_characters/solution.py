class Solution:

    @staticmethod
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        longest_len = 0
        substring = ""

        for letter in s:
            if letter not in substring:
                substring += letter
            else:
                duplicate_index = substring.find(letter)
                substring = substring[duplicate_index+1:] + letter

            longest_len = len(substring) if len(substring) >= longest_len else longest_len
        return longest_len


def main():
    """Execute the program."""
    string1 = "abcabcbb"
    string2 = "bbbbb"
    string3 = "pwwkew"
    string4 = "dvdf"

    solution = Solution()
    ans1 = solution.lengthOfLongestSubstring(string1)
    ans2 = solution.lengthOfLongestSubstring(string2)
    ans3 = solution.lengthOfLongestSubstring(string3)
    ans4 = solution.lengthOfLongestSubstring(string4)
    print(ans1)
    print(ans2)
    print(ans3)
    print(ans4)


if __name__ == "__main__":
    main()
