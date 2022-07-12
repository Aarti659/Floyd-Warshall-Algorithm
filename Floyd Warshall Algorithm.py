nV = 4

INF = 999


def floyd_warshall(G):
    distance = list(map(lambda j: list(map(lambda k: k, j)), G))


    for m in range(nV):
        for j in range(nV):
            for k in range(nV):
                distance[j][k] = min(distance[j][k], distance[j][m] + distance[m][k])
    print_solution(distance)



def print_solution(distance):
    for j in range(nV):
        for k in range(nV):
            if(distance[j][k] == INF):
                print("INF", end=" ")
            else:
                print(distance[j][k], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_warshall(G)




