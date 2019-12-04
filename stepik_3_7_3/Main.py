import sys


def main(argv=sys.argv):
    pattern_count = int(input())
    patterns = list()
    while pattern_count > 0:
        patterns.append(str(input()).lower())
        pattern_count -= 1
    sentence_count = int(input())
    sentences = list()
    while sentence_count > 0:
        sentences.append(str(input()).split())
        sentence_count -= 1
    errors = list()
    for eu in sentences:
        for el in eu:
            if el.lower() not in patterns:
                if el.lower() not in errors:
                    errors.append(el.lower())
    for e in errors:
        print(e)

if __name__ == "__main__":
    main()
