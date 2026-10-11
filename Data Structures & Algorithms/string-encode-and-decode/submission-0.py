class Solution:

    def encode(self, strs: List[str]) -> str:
            code = [str(len(i)) + '#' + i for i in strs ]
            return ''.join(code)
            print(code)

    def decode(self, s: str) -> List[str]:
        total = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            i = j + 1

            total.append(s[i:length + i])

            i += length
        return total