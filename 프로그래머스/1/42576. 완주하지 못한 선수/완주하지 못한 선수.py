from collections import Counter


def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    answer = participant_counter - completion_counter
    return list(answer.keys())[0]
    
    
