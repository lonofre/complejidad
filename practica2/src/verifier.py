import argparse
from utils.i_o import *
import utils.graph as graph_
import utils.certificate as certificate


if __name__ == "__main__":
    """
    Practice 2
    Computational Complexity 2024-1

    Verifier.
    Given an encoded graph passed as argument,
    and a random encoded certificate of length k
    determines if the problem belongs to the
    simple route problem.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("instance", help="first argument")
    parser.add_argument("certificate", help="second argument")
    args = parser.parse_args()

    instance_file = read_file(args.instance)
    certificate_file = read_file(args.certificate)

    graph, k = graph_.decode(instance_file)
    cert = certificate.decode(certificate_file)

    is_valid = certificate.validate(cert, graph)

    elements = len(graph)

    
    print(f"- k: {k}")
    print(f"- is valid?: {is_valid}")

