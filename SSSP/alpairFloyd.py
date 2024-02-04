# We should not usethis for negative cycle because we will not go through any vertex
# twice like bellman ford.

INF = 9999


def printSolHere(nv, distance):
    for i in range(nv):
        for j in range(nv):
            if distance[i][j] is INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")


def floydWarshall(nv, G):
    distance = G
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[j][k] + distance[k][i])
    printSolHere(nv, distance)


G = [[0, 8, INF, 1], [INF, 0, 1, INF], [4, INF, 0, INF], [INF, 2, 9, 1]]

floydWarshall(4, G)


# Time complexity: O(v^3)
