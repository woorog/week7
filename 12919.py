from collections import deque

# 입력 대신 직접 변수에 할당하는 부분은 생략하고 로직만 구현합니다.
S = input().strip()
T = input().strip()

def bfs(S, T):
    queue = deque([T])
    while queue:
        current = queue.popleft()
        if current == S:
            return 1  # 변환이 가능하다면 1을 반환합니다.

        if len(current) <= len(S):
            continue  # 현재 문자열의 길이가 S보다 짧거나 같으면 더 이상 변환을 수행할 수 없습니다.

        if current[-1] == 'A':
            queue.append(current[:-1])  # 마지막 문자가 'A'인 경우 해당 문자를 제거합니다.
        if current[0] == 'B':
            queue.append(current[:0:-1])  # 첫 문자가 'B'인 경우 문자열을 뒤집고 마지막 문자를 제거합니다.

    return 0  # 모든 가능성을 탐색한 후에도 S를 만들 수 없다면 0을 반환합니다.

print(bfs(S, T))