class Solution:
    def isValid(self, s: str) -> bool:
        s_new = s.replace("()", "").replace("[]", "").replace("{}", "")
        while len(s_new) < len(s):
            s = s_new
            s_new = s.replace("()", "").replace("[]", "").replace("{}", "")
        return not s_new