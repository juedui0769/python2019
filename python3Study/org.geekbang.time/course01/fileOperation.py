def read_file():
    with open('text.txt', 'r') as fin:
        text = fin.read()
        print(text)
        return text


def write_file(text):
    with open('out.txt', 'w') as file_out:
        file_out.write(text)

def main():
    write_file(read_file())


if __name__ == '__main__':
    main()