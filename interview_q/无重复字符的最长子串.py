# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# utf-8


def length_of_longest_substring(s: str):
    if len(s) == 0:
        return 0
    longest = ''
    tmp_s = ''
    for i in range(len(s)):
        if tmp_s == '':
            for j in range(i, len(s)):
                if s[j] not in tmp_s:
                    tmp_s += s[j]
                else:
                    break
            if len(tmp_s) >= len(longest):
                longest = tmp_s
            tmp_s = ''
    return longest


def main():
    # s = "pwwkew"
    # s = 'bbbbb'
    s = "abcabcbb"
    print(length_of_longest_substring(s))


if __name__ == '__main__':
    main()
