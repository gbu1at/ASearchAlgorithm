from OrderedSet import OrderedSet


def _direction_function(u: int, v: int) -> int:
    from main import VERTEX_COORD
    """
    :param u: индекс в VERTEX
    :param v: индекс в VERTEX
    :return: оценка минимального расстояния снизу (в данной задача скорее всего будет манхеттенское расстояние)
    """

    x_u, y_u = VERTEX_COORD[u]
    x_v, y_v = VERTEX_COORD[v]

    return abs(x_u - x_v) + abs(y_u - y_v)


def a_search_algorithm(graph: list[list[(int, int)]], s: int, t: int) -> (int, list[int], list[bool]):
    """
    :param graph: список смежности с весами
    :param s: стартовая вершина
    :param t: конечная вершина
    :return: минимальное расстояние, путь, а так же все посещенные вершины (этот параметр необходим для debug)
    """
    inf: int = int(1e9)

    used_vertex: list[bool] = [False] * graph.__len__()

    predict_distances = [inf] * graph.__len__()
    distance_from_s = [inf] * graph.__len__()

    predict_distances[s] = 0
    distance_from_s[s] = 0

    # q = OrderedSet()

    q = set()

    q.add((0, s))

    path_dict: dict[int, (int, int)] = {}

    while q.__len__() != 0:
        el = list(sorted(q))[0]


        # print(q)
        dist, v = el
        q.remove(el)
        # print(dist)
        used_vertex[v] = True

        if v == t:
            break

        for u, weight in graph[v]:
            if predict_distances[u] > distance_from_s[v] + weight + _direction_function(u, t):

                distance_from_s[u] = min(distance_from_s[u], distance_from_s[v] + weight)

                if (predict_distances[u], u) in q:
                    q.remove((predict_distances[u], u))
                predict_distances[u] = distance_from_s[v] + weight + _direction_function(u, t)
                q.add((predict_distances[u], u))

                path_dict[u] = (v, weight)

    if t not in path_dict:
        raise Exception()

    result: int = 0
    x: int = t
    path: list[int] = [x]

    while x != s:
        next_x, weight = path_dict[x]
        result += weight
        x = next_x
        path.append(x)

    return result, path, used_vertex
