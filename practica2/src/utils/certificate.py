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
    code = code.strip()
    certificate = []
    for i in range(int_len, len(code) + int_len, int_len):
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

    while count != k:
        e = random.randrange(size)
        if e in perm or e == 0:
            continue

        perm.append(e)
        count += 1

    return perm

def validate(cert: list[int], graph: dict[int, list[int]]) -> bool:
    """Verifiy the given certificate is a correct answer to the
    induced path problem
    
    Returns
    -------
    bool
        whether the certificate is a correct answer or not
    """

    if len(cert) == 0 or len(cert) == 1:
        return True

    visited = visit(cert, graph)
    distribution = get_distribution(visited, len(cert))
    
    if distribution[1] == 2 and distribution[1] + distribution[2] == len(cert):
        return not is_disconnected(visited, cert, graph)
    return False

def is_disconnected(visited:  dict[int, int], cert: list[int], graph:  dict[int, list[int]]) -> bool:
    """Check whether exists a path from the given
    certificate in the graph.

    Returns
    -------
    bool
        is True if the graph is disconnected, False otherwise
    """

    start = 0
    for key in visited:
        if visited[key] == 1:
            start = key
            break
    
    path = { start }
    cert_set = set(cert)
    
    current = start
    while len(path) < len(visited):
       neighborhood = graph[current]
       search_set = set(neighborhood).intersection(cert_set).difference(path)
       next_vertex = next((v for v in search_set), 0)
       if not next_vertex:
           return True
       else:
           path.add(next_vertex)
           current = next_vertex

    return False

def visit(cert: list[int], graph: dict[int, list[int]]) -> dict:
    """For each vertex in the certificate, explores its neighborhood
    and marks a neighbor as visited if it is in the certificate 
    
    Returns
    -------
    dict
        where the keys are the vertices and their values
        how many times were visited
    """
    
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
    """Gets the distribution of visited vertex"""

    distribution = [0] * elements
    for vertex in visited:
        times = visited[vertex]
        distribution[times] += 1

    return distribution
