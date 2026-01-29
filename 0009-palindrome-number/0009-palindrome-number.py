class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x=x
        x=str(x) # 문자열로 변환하면 '-121'
        list_x = list(x) # 리스트로 변환하면 ['-', '1', '2', '1']
        list_y = list_x[::-1] # 반대로 복사해서 리스트 만들어놓기
        num=1
        for i in range(len(list_x)):
            if list_x[i] != list_y[i]:
                num+=i
        if num > 1:
            return False
        else:
            return True
