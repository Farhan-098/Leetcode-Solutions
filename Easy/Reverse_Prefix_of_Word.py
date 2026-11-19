class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)

        res = ""

        for i in range(len(word)):

            if i > index:
                res = res + word[i]

            else:
                res = word[i] + res

        return res