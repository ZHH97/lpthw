# import sys # 导入sys模块
# script, encoding, error = sys.argv


# def main(language_file, encoding, errors):
#     line = language_file.readline()

#     if line:
#         print_line(line, encoding, errors)
#         return main(language_file, encoding, errors)
    

# def print_line(line, encoding, errors):
#     next_lang = line.strip()
#     raw_bytes = next_lang.encode(encoding, errors=errors)
#     cooked_string = raw_bytes.decode(encoding, errors=errors)

#     print(raw_bytes, "<===>", cooked_string)


# languages = open("languages.txt", encoding="utf-8")

# main(languages, encoding, error)


import sys

script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    

def print_line(line, encoding, errors):
    raw_bytes = line.strip()

    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", "rb")

main(languages, encoding, error)