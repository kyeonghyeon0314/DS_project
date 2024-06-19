# 프로젝트 문제 3번
from collections import deque

input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.
    def bfs():
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(bear_x, bear_y, 0)]) # 곰위치, 이동거리
        visited = [[False] * N for _ in range(N)] # 방문 여부 2차원으로 저장
        visited[bear_x][bear_y] = True # 곰의 초기 위치 방문처리
        possible_honeycombs = [] #먹을수있는 벌집 저장

        while queue: #큐가 비어있지 않으면 반복
            x, y, dist = queue.popleft() #큐에서 위치와 이동거리 추출

            for dx,dy in directions: 
                nx, ny = x + dx, y + dy #다음 위치 계산

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]: #방문하지 않은 곳 중에서
                    if forest[nx][ny] <= bear_size: # 곰 크기 이하인 경우에만 탐색
                        visited[nx][ny] = True #방문처리
                        queue.append((nx, ny, dist + 1)) #큐에 추가 및 거리 계산

                        if 0 < forest[nx][ny] < bear_size: #0보다 크고 곰사이즈보다 작은 겨우 먹을수 있는 벌집에 추가
                            possible_honeycombs.append((dist + 1, nx, ny)) 

        if possible_honeycombs: # 먹을 수 있는 벌집이 있으면
            possible_honeycombs.sort(key=lambda item: (item[0], item[2], item[1])) #거리, 위쪽, 왼쪽 기준으로 정렬 lambda함수 사용 관련 문헌 https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
            return possible_honeycombs[0] #가장 가까운 벌집 반환
        else: # 먹을 수 있는 꿀이 없으면 None 반환
            return None
    
    while True: # 꿀 먹기 반복
        target = bfs() 

        if not target: #먹을 수 있는 벌집이 없으면 종료
            break

        dist, tx, ty = target #벌집까지의 거리, 꿀 위치
        
        if forest[tx][ty] <= bear_size:
            forest[tx][ty] = 0 # 해당 위치에서 벌집 먹기
            bear_x, bear_y = tx, ty #곰이동
            time += dist # 이동시간 추가
            honeycomb_count += 1 #먹은 벌집 개수 증가

            if honeycomb_count == bear_size: # 먹은 벌집수와 곰의 크기랑 같을때 사이즈 증가
                bear_size +=1
                honeycomb_count = 0 #먹은 벌집수 초기화
        else:
            continue

    
    print(bear_size)
    print(honeycomb_count)
    result = 0
    result = time
    return result

result = problem3(input)

print(result)
assert result == 14
print("정답입니다.")
