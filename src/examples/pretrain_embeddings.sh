#!/usr/bin/env bash

fasttext cbow -input ../data/all_student_text.txt -output ../models/student_word_embedding -dim 30 -ws 10 -neg 10 -epoch 30 -thread 6 -wordNgrams 2
