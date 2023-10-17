import random

def encode(raw_content: list[int], int_len: int = 16) -> str:
    """Encode each number of raw_content in its
    `int_len`-bits representation
    
    Parameters
    ----------
    raw_content: list[int]
        the certificate to encode

    int_len: int = 16
        the number of bits to use to encode a number

    Returns
    -------
    str
        a string that joins all the encoded numbers
    """

    return "".join([f"{s:0{int_len}b}" for s in raw_content])


def decode(code: str, int_len: int = 16) -> list[int]:
    """Decode a certificate, which is made up of chunks
    of `int_len`-bits
    
    Parameters
    ----------
    code: str
        the certificate to decode

    int_len: int = 16
        the number of bits to use to decode the certificate

    Returns
    -------
    list[int]
        a list that represents the certificate
    """

    certificate = []
    for i in range(int_len, len(certificate) + int_len, int_len):
        number = int(code[i - int_len : i], 2)
        certificate.append(number)

    return certificate


def generate(k: int, graph: dict[int, list[int]]) -> list[int]:
    """Generates a random certificate
    
    Parameters
    ----------
    k: int
        the number of elements in the certificate

    graph: dict[int, list[int]]
        an adyacency list, to use to build the certificate

    Returns
    -------
    list[int]
        a list that represents the certificate
    """

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

def validate(cert: list[int], graph: dict[int, list[int]]) -> bool:

    if len(cert) == 0 or len(cert) == 1:
        return True

    visited = visit(cert, graph)
    distribution = get_distribution(visited, len(cert))
    
    if distribution[1] == 2 and distribution[1] + distribution[2] == len(cert):
        return True
    return False



def visit(cert: list[int], graph: dict[int, list[int]]) -> dict:
    visited = {}
    for vertex in cert:
        visited[vertex] = 0

    for vertex in cert:
        neighborhood = graph[vertex]
        for neighbor in neighborhood:
            if neighbor in visited:
                visited[neighbor] += 1

    return visited

def get_distribution(visited: dict, elements: int) -> list[int]:
    distribution = [0] * elements
    items = 0
    for vertex in visited:
        times = visited[vertex]
        distribution[times] += 1

    return distribution