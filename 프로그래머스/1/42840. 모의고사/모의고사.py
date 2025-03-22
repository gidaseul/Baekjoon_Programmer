def solution(answers):
    st1 = [1, 2, 3, 4, 5]
    st2 =[2, 1, 2, 3, 2, 4, 2, 5]
    st3 =[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    correct = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == st1[i%5]:
            correct[0] += 1
        if answers[i] == st2[i%8]:
            correct[1] += 1
        if answers[i] == st3[i%10]:
            correct[2] += 1
            
    winner = max(correct)
    for i in range(len(correct)):
        if correct[i] == winner:
            answer.append(i+1)
    return answer