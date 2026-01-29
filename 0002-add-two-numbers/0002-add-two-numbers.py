# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val # 값
#         self.next = next # 다음 노드의 주소
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 # 올림수를 저장할 필요가 있는 변수 
        
        a_head = ListNode(0) # 임시 시작 노드
        current = a_head # 현재 노드를 임시 시작 노드로 설정
        
        while l1 or l2 or carry:
            #l1,l2가 None이 아닐 때 값을 가져옴, 아니면 0으로 처리
            val1 = l1.val if l1 else 0
                # if l1 is not None:
                    # val1 = l1.val
                # else:
                    # val=0
            val2 = l2.val if l2 else 0

            # 두 값을 더하고 올림수를 더함.
            total = val1 + val2 + carry
            
            # 현재 자릿수의 값을 계산
            carry = total // 10 
            
            # 새로운 노드에 들어갈 값 (현재 자릿수)
            new_val = total % 10
            
            # 새로운 노드를 생성하고 현재 노드에 연결
            current.next = ListNode(new_val)
            
            # current 포인터를 새로운 노드로 이동
            current = current.next
            
            # l1과 l2가 끝나지 않았으면 다음 노드로 이동
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 결과 연결 리스트의 시작을 반환 (더미 노드 다음부터)
        return a_head.next