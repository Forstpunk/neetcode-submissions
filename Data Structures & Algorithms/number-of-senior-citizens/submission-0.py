class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for i in details:
            if int(i[11:13])>60:
                result+=1
        return result
        