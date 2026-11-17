class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        def reverse(w):
            sep_words = list(w)
            l = 0
            r = len(sep_words)-1

            while l<r:
                sep_words[l], sep_words[r] = sep_words[r], sep_words[l]
                l+=1
                r-=1

            return ''.join(sep_words)

        result = []
        for word in words:
            result.append(reverse(word))

        return ' '.join(result)