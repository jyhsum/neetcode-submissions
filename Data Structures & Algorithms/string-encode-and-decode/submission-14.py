class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        output = ''
        for s in strs:
            encoded_string = f"{len(s)}#{s}"
            output += encoded_string
        return output

    def decode(self, s: str) -> List[str]:
        print(s)
        import re
        output = []
        pattern = r"(\d+)#"
        str_lens = re.findall(pattern, s)

        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            output.append(s[j:j+length])
            i = j + length

        return output