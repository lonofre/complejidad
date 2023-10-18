from utils.i_o import get_args, read_file, write_file
from utils.graph import decode as grpah_decoder
from utils.certificate import generate, encode

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
    rand_graph = graph_.random_graph(n, e)
    print(rand_graph)
    cert = certificate(k, rand_graph)
    print(cert)

    valido = certificate.validate(cert, rand_graph)
    print(valido)
    return rand_graph, cert, valido


if __name__ == "__main__":
    in_file, target = get_args()
    data = read_file(in_file)
    graph, k = grpah_decoder(data)

    cert = generate(k, graph)
    encoded = encode(cert)

    write_file(target, encoded)
