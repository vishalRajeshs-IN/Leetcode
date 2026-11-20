class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        n = len(s)
        
        # An IPv4 address requires between 4 and 12 digits
        if n < 4 or n > 12:
            return res

        def backtrack(start: int, dots: int, path: list[str]):
            # Once 3 dots are placed, check if the remaining substring forms a valid 4th octet
            if dots == 3:
                segment = s[start:]
                if is_valid(segment):
                    path.append(segment)
                    res.append(".".join(path))
                    path.pop()
                return

            # Try placing a dot after 1, 2, or 3 characters
            for length in range(1, 4):
                if start + length >= n:
                    break
                segment = s[start : start + length]
                if is_valid(segment):
                    path.append(segment)
                    backtrack(start + length, dots + 1, path)
                    path.pop()

        def is_valid(segment: str) -> bool:
            # Must be non-empty, <= 3 chars, no leading zeros (unless "0"), and <= 255
            if not segment or len(segment) > 3:
                return False
            if len(segment) > 1 and segment[0] == "0":
                return False
            return int(segment) <= 255

        backtrack(0, 0, [])
        return res      