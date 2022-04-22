def print_checkboard_header(size):
    line = ['┌']
    for column in range(size):
        line.append('-')
        line.append('+')
    print(''.join(line))


def print_checkboard_footer(size):
    line = ['+']
    for column in range(size):
        line.append('─')
        line.append('─')
    print(''.join(line))


def print_checkboard_row(size):
    line = ['│']
    for column in range(size):
        line.append('  ')
        line.append('│')
    print(''.join(line))


def print_checkboard_row_space(size):
    line = ['├']
    for column in range(size):
        line.append('─')
        line.append('─')
        line.append('┼')
    print(''.join(line))


def print_checkboard(size):
    print_checkboard_header(size=size)
    last_row = size - 1
    for row in range(size):
        print_checkboard_row(size=size)
        if row != last_row:
            print_checkboard_row_space(size=size)
    print_checkboard_footer(size=size)


def main():
    print_checkboard(size=8)


if __name__ == '__main__':
    main()
