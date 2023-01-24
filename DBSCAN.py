UNASSIGNED = -1
NOSIE = 0

def SCAN(x, e): # x는 지점(data point) e는 거리(neighbor distance)
    Circle = []

    for z in X : # X는 x(data point)집합
        if d(x,z) <= e: # x와 z 사이의 거리 계산하고 그 거리가 e보다 작거나 같으면 x를 원점으로 한 반지름 e안에 들어온다
            Circle.append(z) #그때의 z지점을 Circle list에 넣는다.

    return Circle # 지정된 거리에 있는 data 집합들 반

if __name__ == '__main__':
    X = [] # dataset X 모든 data가 들어가 있는 집합
    e = 10 # neighbor distance 거리가 10 이하로 지정
    n = 5 # 만들어놓은 원안에 최소한 데이터의 갯수가 5 이상이여야 한다

    y = []
    k = 0

    mid_result = [] #중간값
    sub_result = [] #sup로 빼기 위해
    result = [] #결과값

    for x in len(X):
        y[x] = UNASSIGNED # data의 갯수만큼 변수 초기화

    for x in len(X):
        if y[x] == UNASSIGNED: # 아직 정해진 값이 없다면
            mid_result = SCAN(X[x],e) #변수 값이 들어가야 하기때문에 X[x]

            if len(mid_result) >= n : # SCAN 함수를 통해 받아온 데이터들의 총개수가 지정된 최소개수보다 크다면
                k = k+1
                y[x] = k
                for z in mid_result: #초기 x의 원안에있는 데이터들을 확인한다
                    if y[z] == UNASSIGNED:  #정해져있는게 아니라면
                        y[z] = k
                        sub_result = SCAN(z,e) # 초기 x에 대해서 z가 핵심점인지 경계점인지 확인한다
                        if len(sub_result) >= n : # z가 핵심점이라면
                            result.append(X[x])
                            result.append(z) # x와 z를 같은 그룹으로 묶은다 깊은 복사를 해야할거 같습니다
            else:
                y[x] = NOSIE