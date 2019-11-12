import os
import string
import pandas as pd


def modify_and_output_histogram(input_histogram, file_name):
    output_histogram = sorted(input_histogram.items(), key=lambda kv: kv[1])
    output_histogram.reverse()

    df = pd.DataFrame(columns=["value", "appearances"])

    for index, item in enumerate(output_histogram):
        if item[1] > 5:  # delete words with less then 5 apperances
            df.loc[index] = [item[0], item[1]]

    df.to_csv(os.path.join("outputs", file_name), index=False)


def build_log_string_histogram():
    word_histogram = {}
    line_histogram = {}
    with open(os.path.join("data", "logs_strings.txt"), 'r') as file_content:
        for line in file_content:
            line = line.strip().lower().replace('  ', ' ')
            if len(line) > 200:
                continue
            words = line.split(' ')
            for word in words:
                if len(word) > 1:  # remove single char words
                    if word in word_histogram:
                        word_histogram[word] += 1
                    else:
                        word_histogram[word] = 1
            if len(line) > 1:  # remove single char lines
                if line in line_histogram:
                    line_histogram[line] += 1
                else:
                    line_histogram[line] = 1

    modify_and_output_histogram(word_histogram, file_name="logs_strings_word_histogram.csv")
    modify_and_output_histogram(line_histogram, file_name="logs_strings_line_histogram.csv")
