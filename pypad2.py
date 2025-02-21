nums = list(map(int,input().split()))
target = int(input(""))

found = False
for i in nums:
    for j in nums:
        if (i+j) == target:
            print(i,j)
            found = True
            break
    if found:
        break


# from collections import deque
# bfs
# graph = {
#     0:[1, 3, 6],
#     1:[0, 3],
#     2:[3],
#     3:[0, 1, 2, 7],
#     4:[5],
#     5:[4, 6, 7],
#     6:[0, 5],
#     7:[3, 5]
# }

# def bfs(graph,start_v):
#     #시작점 예약
#     q = deque()
#     visited = [False] * len(graph)
#     q.append((start_v, 0))
#     visited[start_v] = True

#     while q:
#         # 현재 노드 방문
#         cur_v, cur_dist = q.popleft()
#         print(cur_v, cur_dist)
#         # 다음 노드 예약
#         for next_v in graph[cur_v]:
#             if not visited[next_v]:
#                 q.append((next_v,cur_dist+1))
#                 visited[next_v] = True

# bfs(graph, start_v=0)



# dfs  방문 -> 현재노드와 연결된 방문안한 노드 찾기 -> 다음노드 방문 

graph = {
    0:[1, 3, 6],
    1:[0, 3],
    2:[3],
    3:[0, 1, 2, 7],
    4:[5],
    5:[4, 6, 7],
    6:[0, 5],
    7:[3, 5]
}
visited = [False] * len(graph)

def dfs(cur_v):
    # 방문
    visited[cur_v] = True
    print(cur_v)
    # 다음노드 dfs
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dfs(next_v)

dfs(0)
