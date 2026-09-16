class Solution:
    def isValid(self, s: str) -> bool:
        opn = ["(", "[", "{"]
        clz = [")", "]", "}"]
        closer = {"(" : ")", "[": "]", "{" :"}"}
        arr = []
        length = len(s)
        for i in range(len(s)) :
            if (s[i] in opn):
                arr.append(s[i])
            elif (s[i] in clz):
                if len(arr) == 0:
                    return False
                prev_opn = arr.pop() 
                if (closer[prev_opn] != s[i]):
                    return False
            if (length == (i + 1) and len(arr) != 0):
                return False

        return True