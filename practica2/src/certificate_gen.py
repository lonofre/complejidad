import random


def decoder(in_str: str) -> list[str]:
    parsing_line = True
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
            parsing_line = False
            continue

        tmp_line += c
    print(x, int(x[-1], 2))
    return x


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


# t = "00111100111100011100001111001101110000111111000100111100110011011111111100000001110011000000000100110011000000011011"
# d = decoder(t)
# g = build_ady(d)
# print(g)


def leer():
    # entrada = input("Escribe nombre de archivo de entrada: ")
    entrada = "entrada.txt"
    r = open(entrada, "r").read()
    # ? informacion: Número de vértices, Número de aristas, k

    c = certificado(r)

    # salida = input("Escribe nombre de archivo de salida: ")
    salida = "salida.txt"
    w = open(salida, "w")
    w.write(str(c))


def certificado(s: str):
    n, e, k = map(int, s.split())
    rand_graph = random_graph(n, e)


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


leer()
