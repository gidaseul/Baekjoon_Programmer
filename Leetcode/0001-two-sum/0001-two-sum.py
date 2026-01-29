from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 해시맵 추가
        hash_map = {}

        # 배열 순회하면서 해시 테이블 구성 및 목표 값 확인
        for i, num in enumerate(nums):
            # target에서 현재 숫자를 뺀 값이 해시맵에 있는지 확인
            complement = target - num
            if complement in hash_map:
                # 찾은 거니까 해시맵에 있는 값의 인덱스 반환
                return [hash_map[complement],i]
            # 현재 숫자와 인덱스를 해시맵에 저장
            hash_map[num] = i
        return [] 
