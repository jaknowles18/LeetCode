class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        lena = len(a)
        lenb = len(b)
        max_len = None
        diff_len = 0

        if lena >= lenb:
            max_len = lena
            diff_len = lena - lenb

            for i in range(diff_len):
                b = "0" + b

        else:
            max_len = lenb
            diff_len = lenb - lena
            for i in range(diff_len):
                a = "0" + a

        output = ""
        carry = 0
        for i in range(max_len - 1, -1, -1):
            numa = a[i] 
            numb = b[i]

            if numa == "0" and numb == "0":
                if carry == 1:
                    carry = 0
                    output = "1" + output
                else:
                    output = "0" + output

            elif numa == "1" and numb == "1":
                if carry == 1:
                    carry = 1
                    output = "1" + output
                else:
                    output = "0" + output
                    carry = 1

            else:
                if carry == 1:
                    output = "0" + output
                    carry = 1
                else:
                    output = "1" + output

        if carry == 1:
            output = str(carry) + output
        
        return output




        

