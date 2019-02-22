if __name__ == "__main__":
    out_file = open("../data/watson.csv", "w")
    first = 0
    with open("../data/competencies.csv", "r") as in_file:
        for line in in_file:
            if first == 0:
                first += 1
                continue
            sep_by_commas = line.split(",")
            text = ""
            length = len(sep_by_commas)
            for i in range(length-1):
                text += sep_by_commas[i] + ","
            lead_style = "Transformational\n" if (sep_by_commas[length-1] == "1\n") else "Transactional\n"
            response_full = text + lead_style
            out_file.write(response_full)
