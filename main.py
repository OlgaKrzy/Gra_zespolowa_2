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

def znajdz_brakujacy_wierzcholek(wierzcholki):
    t_wierzcholki = [tuple(wierzch) for wierzch in wierzcholki]
    #Znalezienie wierzchołka trójkąta przy którym kąt wynosi 90 stopni
    symetryczny = None
    for i in range(3):
        wierzch1 = t_wierzcholki[i]
        wierzch2 = t_wierzcholki[(i + 1) % 3]
        wierzch3 = t_wierzcholki[(i + 2) % 3]

        #Obliczenie długości boków trójkąta
        bok1 = ((wierzch2[0] - wierzch1[0])**2 + (wierzch2[1] - wierzch1[1])**2)**0.5
        bok2 = ((wierzch3[0] - wierzch2[0])**2 + (wierzch3[1] - wierzch2[1])**2)**0.5
        bok3 = ((wierzch1[0] - wierzch3[0])**2 + (wierzch1[1] - wierzch3[1])**2)**0.5
        #Sprawdzenie czy kąt wynosi 90 stopni
        if round(bok1**2 + bok2**2, 2) == round(bok3**2, 2):
            #Zwrócenie brakującego wierzchołka
            symetryczny = wierzch2

    #znalezienie punktu środkowego przekątnej
    wierzcholki_przekatnej = set(t_wierzcholki) - set([symetryczny])
    wierzch1 = list(wierzcholki_przekatnej)[0]
    wierzch2 = list(wierzcholki_przekatnej)[1]
    srodek = ((wierzch1[0] + wierzch2[0]) / 2, (wierzch1[1] + wierzch2[1]) / 2)

    #wektor od symetrycznego do środka
    wektor = (srodek[0] - symetryczny[0], srodek[1] - symetryczny[1])
    #brakujacy wierzcholek
    brakujacy = (symetryczny[0] + wektor[0] * 2, symetryczny[1] + wektor[1] * 2)

    return brakujacy
# Przykładowe wejście
wierzcholki = [[1,1], [2,3], [4,2]]
brakujacy_wierzch = znajdz_brakujacy_wierzcholek(wierzcholki)
print(brakujacy_wierzch)
