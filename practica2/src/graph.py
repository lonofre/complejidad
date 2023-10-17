import random

def decode(in_str: str) -> tuple[dict[int, list[int]], int]:
    tmp_line = ''
    x = []

    for i in range(0, len(in_str), 2):
        c = in_str[i-2:i]
        # print(c)
        if c == "10":
            tmp = in_str[i:]
            x.append(tmp)
            break

        if c == "01":
            x.append(tmp_line)
            tmp_line = ''
            continue

        tmp_line += c

    graph = build_ady(x)
    k = build_k(x)
    return graph, k

def build_ady(ady: list[str]) -> dict[int, list[int]]:
    graph = {}

    for idx, a in enumerate(ady[:-1], start=1):
        graph[idx] = []
        for ele, i in enumerate(range(0, len(a) + 2, 2)):
            match a[i - 2: i]:
                case "00":
                    continue
                case "11":
                    graph[idx].append(ele)

    return graph


def build_k(ady: list[str]) -> int:
    k = ady[-1]
    return int(k, 2)

def random_graph(n: int, e: int) -> dict[int, list[int]]:
    graph = {i: [] for i in range(1, n+1)}
    edges = set()

    while e:
        u = random.randint(1, n)
        v = random.randint(1, n)
        edge = (min(u, v), max(u, v))
        if u == v or edge in edges:
            continue

        edges.add(edge)
        graph[u].append(v)
        graph[v].append(u)

        e -= 1

    return graph
