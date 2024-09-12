import sys
sys.stdin = open('input.txt')


def making_tree(node):
    global count
    '''
     전체 노드 수를 채울때까지 조사하는 방법이 유효한 이유
     완전 이진 트리로 만들기 때문 -> 완전 이진 트리로 만드는게 유효한 이유?
     노드의 개수가 3개라고 했을때, 아래와 같이 트리가 그려짐.
            0
        1       2
     노드의 개수가 6개라고 했을 때, 아래와 같이 트리가 그려짐
            0
        1       2
    3      4 5
     모든 노드에 비어 있는 값이 없이, 이진 트리 형태에 값을 더한 것이
     완전 이진 트리이므로, 만약, 지금 조사하려는 노드의 번호가
     N보다 큰 경우,
        ex) 포화 이진 트리로 트리를 구성한다 했을 때,
        3번의 왼쪽, 오른쪽 자식의 노드 번호는
        아마, 7번 8번이 될 것. 즉, N인 6보다 큰 값이 될 것이므로
        조사 대상이 아님. 따라서...
    '''
    if node < V:       # 언제 까지? 전체 노드의 개수를 채울때까지
        making_tree(node*2)     # 왼쪽 자식 탐색
       # 문제에서는 왼쪽 자식부터 중위 순회 순으로
       # 값을 입력하라고 하였으므로, 왼쪽을 조사하고 돌아온 시점인
       # 이곳에서 트리에 값을 삽입하여야 함.
        count += 1      # 값 삽입 전 1증가
        tree[node] = count  # 트리에 현재 노드 번호에 값 삽입
        making_tree(node*2+1)   # 오른쪽 자식 탐색

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 노드의 개수
    V = N + 1           # 0번 노드는 사용하지 않을 것.
    tree = [0] * V      # 노드의 개수 만큼 트리 구성
    count = 0           # 삽입 할 값. 0부터 시작. 삽입 직전 1증가.
    # print(tree)         # [0, 0, 0, 0, 0, 0, 0]
    making_tree(1)      # 1번 노드부터 순회하면서 값을 작성하기 시작.
    # 완성된 트리 모양 출력
    # print(tree)         # [0, 4, 2, 6, 1, 3, 5]
    # 루트 노드 1번, N//2 번째 노드 결과 출력
    print(f'#{tc} {tree[1]} {tree[N//2]}')



