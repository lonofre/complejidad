import sys
from dataclasses import dataclass

@dataclass
class MatrixEncoding:
    encoding: str
    pretty_encoding : str
    vertex_count: int
    edge_count: int
    k: int


def count_character(text: str, query: str) -> int:
    """Counts the total times a character appears in a given
    text

    Parameters:
    -----------
    text: str
        the text to parse
    query: str
        character to search

    Returns:
    --------
    int
        the number of the appearences of the given character
    """
    times = 0
    for char in text:
        if char == query:
            times += 1

    return times


def repeat_character(char: str, n: int) -> str:
    """
    Repeats a character a number of times.

    Parameters:
    -----------
    char: str
        the character to repeat
    n: int
        the number of times to repeat a char

    Returns:
    --------
    str
        a string with n repetitions of char
    """
    string = []
    for i in range(0, n):
        string.append(char)

    return "".join(string)


def fill_empty_positions(start: int, end: int) -> str:
    """Fills with 00 the positions between start and end,
    for our binary matrix encoding

    Parameters:
    -----------
    start: int
        the start position
    end: int
        the end position

    Returns:
    --------
    str
        a string of zeroes
    """
    return repeat_character("00", end - start)

def decimal_to_binary(decimal_number: int) -> str:
    """Given a decimal number, turns into its binary
    representation

    Parameters:
    -----------
    decimal_number: int
        the decinal number to transform

     Returns:
    --------
    str
        the corresponding binary string representation.
    """
    if decimal_number == 0:
        return '0'

    binary_digits = []

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_digits.append(str(remainder))
        decimal_number //= 2

    binary_digits.reverse()
    binary_representation = ''.join(binary_digits)
    return binary_representation


def encode(encoding: str) -> MatrixEncoding:
    """Turns a given coding into its matrix representation using only
    binary numbers
    
    Parameters:
    -----------
    encoding: str
        A string using the adjacencie list coding. For example:
        1:2,3
        2:1
        3:1
    
    Returns:
    MatrixEncoding
        that represents the matrix encoding plus additional data. For example:
        0110110001100
    """
    total_vertices = count_character(encoding.strip()[:-1], "\n")
    row = []
    is_parsing_adjacencies = False
    matrix = []
    pretty = []
    k = ""
    # it helps to write zeros
    last_position = 1
    edge_count = 0

    # Counts the line breaks to read "k"
    break_couting = 0

    for char in encoding:
        if break_couting == total_vertices:
            k += char
        elif char == "\n":
            row.append(fill_empty_positions(last_position - 1, total_vertices))
            # For pretty print
            pretty.append("".join(row))
            pretty.append("\n")
            # Divides a row, for debug change it to \n
            row.append("01")
            matrix.append("".join(row))
            
            row = []
            is_parsing_adjacencies = False
            last_position = 1
            break_couting += 1

        # Parsing the adjacencies, that are given like this:
        # <vertex>:<adj_1><adj_2>
        elif char == ":":
            is_parsing_adjacencies = True

        elif is_parsing_adjacencies and char != ",":
            adjacency = int(char)
            edge_count += 1
            # Writes zeros til it reaches the adjacency position
            fill = fill_empty_positions(last_position, adjacency) + "11"
            row.append(fill)
            last_position = adjacency + 1

    # Divides k from the matrix
    matrix.append("10")
    matrix.append(decimal_to_binary(int(k)))
    pretty.append(decimal_to_binary(int(k)))
    pretty.append("\n")
    
    # join uses at worst O(n), while + is O(n^2)
    return MatrixEncoding(encoding = "".join(matrix),
                          pretty_encoding= "".join(pretty),
                          vertex_count = total_vertices, 
                          edge_count = edge_count//2,
                          k = int(k))



if __name__ == "__main__":

    input_file = ""
    output_file = ""
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    except IndexError:
        print("Not enough arguments")
        sys.exit(1)

    try:
        with open(input_file, "r") as file:
            encoding = file.read()
            matrix = encode(encoding)

        with open(output_file, "w") as file:
            if len(sys.argv) > 3 and sys.argv[3] == '--v':
                print(f"Codificación (formateada): \n{matrix.pretty_encoding}")
                print(f"Codificación (en archivo): \n{matrix.encoding}\n")
            print(f"Número de vértices: {matrix.vertex_count}")
            print(f"Número de aristas: {matrix.edge_count}")
            print(f"k: {matrix.k}")
            file.write(matrix.encoding)
    except IOError:
        print('Error reading file\nIt exists?')
        sys.exit(1)
