def solution(numbers, target):
    def dfs(idx, curr_sum):
        if idx == len(numbers):
            if curr_sum == target:
                return 1
            return 0
        return dfs(idx + 1,curr_sum + numbers[idx]) + dfs(idx + 1, curr_sum - numbers[idx])
    return dfs(0,0)