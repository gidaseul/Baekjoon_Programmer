class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} # 딕셔너리로 기존의 값 저장하고
        num=0
        
        # 문자열의 길이로 돌면서 진행하기 -> 문자열의 길이 자체로 인덱스까지 접근하니까 연결해서 키 값으로 접근까지 가능
        for i in range(len(s)):
            if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]

        return num

