import random


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


def decoder(in_str: str) -> tuple[dict[int, list[int]], int]:
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

    graph = build_ady(x)
    k = build_k(x)
    return graph, k


def encoder(raw_content: list[str], int_len: int = 16) -> str:
    return "".join([f"{s:0{int_len}b}" for s in raw_content])


def certificate(k: int, graph: dict[int, list[int]]) -> list[int]:
    perm = []
    count = 0
    size = len(graph.keys()) + 1
    complete = False

    while count != k:
        e = random.randrange(size)
        if e in perm or e == 0:
            continue

        perm.append(e)
        count += 1

    return perm


# t = "0000001111110100001111111101000000111111011111110011000111111100000001111111000000011011"
# d, k = decoder(t)
# print(d, k)
# print()

# p = certificate(k, d)
# print(f"Certificate of length {k}: {p}")


def run():
    """
    Funcion que se encarga de gestionar archivos de entrada, salida y correr el programa.
    """

    # entrada = input("Escribe nombre de archivo de entrada: ")
    entrada = "entrada.txt"
    r = open(entrada, "r").read()
    # ? informacion: Número de vértices, Número de aristas, k

    graph, cert, valido = certificado(r)

    # salida = input("Escribe nombre de archivo de salida: ")
    salida = "salida.txt"
    w = open(salida, "w")
    w.write("Grafo: " + str(graph) + "\n")
    w.write("Certificado: " + str(cert) + "\n")
    w.write("Validez: " + str(valido) + "\n")


def certificado(s: str):
    """
    Recibe del archivo num_nodos, num_aristas, k.
    Crea grafo aleatorio y genera certificado.
    Valida certificado.
    """
    n, e, k = map(int, s.split())
    rand_graph = random_graph(n, e)
    print(rand_graph)
    cert = certificate(k, rand_graph)
    print(cert)

    valido = validate(cert, rand_graph)
    print(valido)
    return rand_graph, cert, valido


def validate(cert: list[int], graph: dict[int, list[int]]) -> bool:
    """
    Función explicada por Malinali, valida que el certificado sea válido.

    Obteniendo una ruta al azar, checa que las aristas se encuentren en la gráfica.
    """
    for i in range(len(cert)-1):
        if cert[i+1] not in graph[cert[i]]:
            return False
        for j in range(i+2, len(cert)):
            if cert[i] in graph[cert[j]]:
                return False

    return True


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


run()
