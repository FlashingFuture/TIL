def main():
    lines = [input() for _ in range(5)]
    answer = ''
    for position in range(len(lines)):
        for i in range(5):
            answer += lines[i][position]

    print(answer)


if __name__ == '__main__':
    main()
