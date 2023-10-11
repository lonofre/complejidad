def decoder(in_str: str) -> list[str]:
    parsing_line = True
    tmp_line = ''
    x = []

    for i in range(0, len(in_str), 2):
        c = in_str[i-2:i]
        #print(c)
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
    print(x, int(x[-1],2))
    return x

def build_ady(ady: list[str]) -> dict[int, list[int]]:
    graph = {}

    for idx, a in enumerate(ady[:-1], start=1):
        graph[idx] = []
        for ele, i in enumerate(range(0, len(a) + 2, 2)):
            match a[i - 2 : i]:
                case "00":
                    continue
                case "11":
                    graph[idx].append(ele)

    return graph


t = "00111100111100011100001111001101110000111111000100111100110011011111111100000001110011000000000100110011000000011011"
d = decoder(t)
g = build_ady(d)
print(g)
