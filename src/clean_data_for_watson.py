# version 1: created watson.csv from competencies.csv
# version 2: created watson.csv from set1.csv
# NOTE: README -> doesn't account for entries without proper quotation marks surrounding the text yet
# version 3: changing this code to be more generic NOTE DONE YET


# *** # *** # DO NOT USE 10-9-19 # *** # *** #s


import sys

if __name__ == "__main__":
    in_file = open(sys.argv[1], "r")
    out_file = open("../data/watson.csv", "w")
    first = 0
    for line in in_file:
        if first == 0:
            first += 1
            continue
        sep_by_commas = line.split("|")
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
