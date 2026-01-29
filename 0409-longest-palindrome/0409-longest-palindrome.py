from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)  # 1. 각 문자의 개수를 센다.
        
        length = 0  # 2. palindrome의 길이를 저장할 변수
        odd_found = False  # 홀수 개수 여부 판단
        
        # 3. 각 문자의 개수를 확인하며 길이 계산
        for count in counts.values():
            if count % 2 == 0:
                length += count  # 짝수 개수는 그대로 더함
            else:
                length += count - 1  # 홀수 개수 중 하나를 제외하고 더함
                odd_found = True
                
        # 4. 홀수 개수가 있으면 가운데에 하나 추가 가능
        if odd_found:
            length += 1
            
        return length
