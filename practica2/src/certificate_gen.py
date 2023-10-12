import random

def build_ady(ady: list[str]) -> dict[int, list[int]]:
    graph = {}

    for idx, a in enumerate(ady[:-1], start=1):
        graph[idx] = []
        for ele, i in enumerate(range(0, len(a) + 2, 2)):
            match a[i - 2 : i]:
                case "00":
                    continue
                case "11":
                    graph[idx].append(ele)

    return graph

def build_k(ady: list[str]) -> int:
    k = ady[-1]
    return int(k, 2)

def decoder(in_str: str) -> tuple[dict[int, list[int]], int]:
    parsing_line = True
    tmp_line = ''
    x = []

    for i in range(0, len(in_str), 2):
        c = in_str[i-2:i]
        #print(c)
        if c == "10":
            tmp = in_str[i:]
            x.append(tmp)
            break

        if c == "01":
            x.append(tmp_line)
            tmp_line = ''
            parsing_line = False
            continue

        tmp_line += c

    graph = build_ady(x)
    k     = build_k(x)
    return graph, k

def certificate(k: int, graph) -> list[int]:
    perm = []
    count = 0
    size = len(graph.keys()) + 1
    complete = False

    while count != k:
        e = random.randrange(size)
        if e in perm:
            continue

        perm.append(e)
        count += 1

    return perm

t = "0000001111110100001111111101000000111111011111110011000111111100000001111111000000011011"
d, k = decoder(t)
print(d, k)
print()

p = certificate(k, d)
print(f"Certificate of length {k}: {p}")