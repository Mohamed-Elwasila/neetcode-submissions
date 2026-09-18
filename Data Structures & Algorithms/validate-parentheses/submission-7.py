class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        p = {"}":"{",
             "]":"[",
             ")":"("}
        
        for i in s:
            if i in p:
                if st and p[i] == st[-1]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        
        if st:
            return False
        
        return True