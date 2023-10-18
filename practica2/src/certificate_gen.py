from utils.i_o import get_args, read_file, write_file
from utils.graph import decode as grpah_decoder
from utils.certificate import generate, encode

if __name__ == "__main__":
    """
    Practice 2
    Computational Complexity 2024-1

    Certificate generator.
    Given an encoded graph passed as argument,
    generates a random certificate of length k
    and writes it to the argument target file.
    """

    in_file, target = get_args()
    data = read_file(in_file)
    graph, k = grpah_decoder(data)

    cert = generate(k, graph)
    encoded = encode(cert)

    write_file(target, encoded)
