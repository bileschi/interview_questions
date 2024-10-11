# Solution to leetcode problem 3304

charmap = {}
for i in range(26):
    key = chr(i + ord('a'))
    val = chr((i+1) % 26 + ord('a'))
    charmap[key] = val

def extend_str(s: str):
    return s + ''.join([charmap[c] for c in s])

str_500 = 'a'
while len(str_500) < 500:
    str_500 = extend_str(str_500)

class Solution:

    def kthCharacter(self, k: int) -> str:
        return str_500[k-1]
                