class FindTheDifference:

    def findTheDifference(self, s: str, t: str) -> str:
        charCount = {}

        for ch in s:
            if ch in charCount:
                charCount[ch] = charCount[ch] + 1
            else:
                charCount[ch] = 1

        for ch in t:
            if ch not in charCount or charCount[ch] == 0:
                return ch
            else:
                charCount[ch] = charCount[ch] - 1

        return ""