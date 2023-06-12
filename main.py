def porzadkuj_dane(input_data):
    num_columns = len(input_data[0])

    # szukam sobie maksymalną szerokość
    column_widths = [max(len(str(row[i])) for row in input_data) for i in range(num_columns)]

    formatted_rows = []
    for row in input_data:
        formatted_row = [str(row[i]).rjust(column_widths[i]) for i in range(num_columns)]
        formatted_rows.append(formatted_row)

    output = '['
    for index, row in enumerate(formatted_rows):
        output += (" " if index != 0 else "") + '[' + ', '.join(row) + '],\n'
    output = output.rstrip(',\n') + ']'
    return output


def porzadkuj_do_lewej(input_data):
    num_columns = len(input_data[0])
    column_widths = [max(len(str(row[i])) for row in input_data) for i in range(num_columns)]

    formatted_rows = []
    for row in input_data:
        formatted_row = [str(row[i]).ljust(column_widths[i]) for i in range(num_columns)]
        formatted_rows.append(formatted_row)

    output = '['
    for index, row in enumerate(formatted_rows):
        output += (" " if index != 0 else "") + '[' + ', '.join(row) + '],\n'
    output = output.rstrip(',\n') + ']'
    return output


assert porzadkuj_dane([[5, 5, 5, 150], [4, 4, 4, 2], [100, 1200, 1000, 1000]]) == """[[  5,    5,    5,  150],
 [  4,    4,    4,    2],
 [100, 1200, 1000, 1000]]"""

assert porzadkuj_dane([[500, 450, 5, 150], [4, 4, 4, 11], [1000, 12, 10, 10000], [500, 6000, 1, 2]]) == """[[ 500,  450,  5,   150],
 [   4,    4,  4,    11],
 [1000,   12, 10, 10000],
 [ 500, 6000,  1,     2]]"""

assert porzadkuj_do_lewej([[4, 500, 600], [8000, 1, 60]]) == """[[4   , 500, 600],
 [8000, 1  , 60 ]]"""

assert porzadkuj_do_lewej([[4, 550, 600, 7000], [9999, 1, 50, 11], [750, 11, 99, 68]]) == """[[4   , 550, 600, 7000],
 [9999, 1  , 50 , 11  ],
 [750 , 11 , 99 , 68  ]]"""