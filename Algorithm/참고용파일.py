from collections import deque

def bfs():
    # 큐와 visited 배열 생성
    q = deque([])
    v = [[[0] * M for _ in range(N)] for _ in range(H)]
    dh = [1, -1, 0, 0, 0, 0]
    di = [0, 0, -1, 1, 0, 0]
    dj = [0, 0, 0, 0, -1, 1]

    # 큐에 초기 데이터 삽입, 안 익은 토마토 카운트
    cnt = 0  # 안 익은 토마토 개수
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:  # 익은 토마토
                    q.append([h, i, j])  # i, j 순서 수정
                    v[h][i][j] = 1
                elif arr[h][i][j] == 0:  # 안 익은 토마토
                    cnt += 1

    while q:
        ch, ci, cj = q.popleft()

        # 6방향, 범위내, 미방문, 익지 않은 토마토
        for k in range(6):
            nh = dh[k] + ch
            ni = di[k] + ci
            nj = dj[k] + cj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0 and v[nh][ni][nj] == 0:
                q.append([nh, ni, nj])
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                cnt -= 1

    # 모든 토마토가 익었으면 최종 결과 출력
    if cnt == 0:
        return v[ch][ci][cj] - 1  # 1을 빼서 실제 걸린 일수를 반환
    else:
        return -1  # 안 익은 토마토가 남아있다면 -1 반환


# 입력 처리
M, N, H = map(int, input().split())  # 가로, 세로, 높이 입력
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]  # 3차원 배열 입력

# 결과 출력
ans = bfs()
print(ans)
