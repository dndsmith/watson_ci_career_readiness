# version 1: created watson.csv from competencies.csv
# version 2: created watson.csv from set1.csv
# NOTE: README -> doesn't account for entries without proper quotation marks surrounding the text yet
if __name__ == "__main__":
    out_file = open("../data/watson.csv", "w")
    first = 0
    with open("../data/set1.csv", "r") as in_file:
        for line in in_file:
            if first == 0:
                first += 1
                continue
            sep_by_commas = line.split(",")
            text = ""
            length = len(sep_by_commas)
            for i in range(length-3):
                text += sep_by_commas[i] + ","
                print(sep_by_commas[i])
            if sep_by_commas[length-3] == "1":
                lead_style = "transformational\n"
            else:
                lead_style = "transactional\n" if (sep_by_commas[length-2] == "1") else "unknown\n"
            response_full = text + lead_style
            out_file.write(response_full)