import argparse
from utils.i_o import *
import utils.graph as graph_
import utils.certificate as certificate


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("instance", help="first argument")
    parser.add_argument("certificate", help="second argument")
    args = parser.parse_args()

    instance_file = read_file(args.instance)
    certificate_file = read_file(args.certificate)

    graph, k = graph_.decode(instance_file)
    cert = certificate.decode(certificate_file)

    is_valid = certificate.validate(cert, graph)

    print("Total number of elements in S")
    print("Total number of subsets in C")
    print(f"K: {k}")
    print(f"Is valid?: {is_valid}")

