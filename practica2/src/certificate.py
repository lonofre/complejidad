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