def porzadkuj_dane(input_data):

    num_columns = len(input_data[0])

    # szukam sobie maksymalną szerokość 
    column_widths = [max(len(str(row[i])) for row in input_data) for i in range(num_columns)]

    formatted_rows = []
    for row in input_data:
        formatted_row = [str(row[i]).rjust(column_widths[i]) for i in range(num_columns)]
        formatted_rows.append(formatted_row)
    
    output = '['
    for row in formatted_rows:
        output += '[' + ', '.join(row) + '],\n'
    output = output.rstrip(',\n') + ']'
    return output

input_data = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]

output = porzadkuj_dane(input_data)
print(output)






























def porzadkuj_do_lewej(input_data):

    num_columns = len(input_data[0])
    column_widths = [max(len(str(row[i])) for row in input_data) for i in range(num_columns)]

    formatted_rows = []
    for row in input_data:
        formatted_row = [str(row[i]).ljust(column_widths[i]) for i in range(num_columns)]
        formatted_rows.append(formatted_row)
    
    output = '['
    for row in formatted_rows:
        output += '[' + ', '.join(row) + '],\n'
    output = output.rstrip(',\n') + ']'
    return output

input_data = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
output = porzadkuj_do_lewej(input_data)
print(output)
