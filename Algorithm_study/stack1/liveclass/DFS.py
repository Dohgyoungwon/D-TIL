# Depth First Search, DFS
# Breadth First Search, BFS

# DFS 연습문제

def DFS(s, V):              # s 시작정점, V 정점개수(1번부터인 정점의 마지막 정점)
    visited = [0] * (V+1)   # 방문한 정점을 표시
    stack = []              # 스택생성
    print(s)
    visited[s] = 1          # 시작정점 방문표시
    v = s
    while True:
        for w in adjL[v]:   # v에 인접하고, 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # push(v) 현재 정점을 push하고
                v = w            # w에 방문
                print(v)
                visited[w] = 1   # w에 방문 표시
                break            # v부터 다시 탐색
        else:                    # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if stack:            # 이전 갈림길을 스택ㅇ서 꺼내서 ... if TOP > -1
                v = stack.pop()
            else:                # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색 종료
                break            # While True:


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    print(adjL)

    DFS(1, V)




