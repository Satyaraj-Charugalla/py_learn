# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S,A):
    # Implement your solution here
    ans = ""
    k = 0
    for i in range(len(S)):
        ans = ans + S[k]
        if k == 0:
            break
        return ans


print(solution('cedo',[3,2,0,1]))
print(solution('cdeenetpi',[5,2,0,1,6,4,8,3,7]))
print(solution('bytdag',[4,3,0,1,2,5]))