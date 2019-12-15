def readFile():
    with open('text.txt', 'r') as fin:
        text = fin.read()
        print(text)
        return text


def writeFile(text):
    with open('out.txt', 'w') as fout:
        fout.write(text)

def main():
    writeFile(readFile())


if __name__ == '__main__':
    main()