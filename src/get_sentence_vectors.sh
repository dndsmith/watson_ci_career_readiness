#!/usr/bin/env bash
# get the sentence vectors using fasttext
fasttext print-sentence-vectors ../models/student_word_embedding.bin < ../data/labelled_data_text.txt > ../data/labelled_data_text_with_vectors.txt

# replace all ^M with \t
sed 's/\/\t/g' ../data/labelled_data_text_with_vectors.txt > ../data/labelled_data_text_with_vectors.tsv
