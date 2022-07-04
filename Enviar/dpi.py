def csv_to_py(file):
    import csv
    lista = list(csv.reader(open(f'{file}', 'r')))
    new_lista = []
    for i in range(len(lista)):
        if i != 0:
            new_row = [float(lista[i][j]) for j in range (len(lista[0]))]
            new_lista.append(new_row)
    return new_lista

def columna(arr, col):
    return [arr[i][col] for i in range(len(arr))]

def nueva_lista(csv_file, valor):
    return [csv_file[i] for i in range(len(csv_file)) if csv_file[i][0] == valor]

def max_min(lista):
    x_max = percentile(lista, 98)
    x_min = percentile(lista, 2)
    return x_max, x_min

def percentile(lista, percentil):
    import math
    lista.sort()
    percentil /= 100
    k = (len(lista) - 1) * percentil
    return (lista[math.floor(k)] + lista[math.ceil(k)]) / 2

def array_max_min(csv_file):
    valores_max = []
    valores_min = []
    for i in range(2, 9):
        x_max, x_min = max_min(columna(csv_file, i))
        valores_max.append(x_max)
        valores_min.append(x_min)
    return valores_max, valores_min

def x_norm(csv_file, fila, col, x_max, x_min):
    import math
    x = csv_file[fila][col]
    if x_max == x_min:
        if x_max == 0:
            x_norm = min(math.floor(2 * x), 1)
        else:
            x_norm = 1 - math.abs(x - x_max) / x_max
    if x_max != x_min:
        x_norm = min(1, max(0, (x - x_min) / (x_max - x_min)))
    if col != 8:
        x_norm = 1 - x_norm
    return x_norm

def dpi(csv_file, fila, valores_max, valores_min):
    dpi_val = sum(x_norm(csv_file, fila, i, valores_max[i - 2], valores_min[i - 2]) for i in range(2, 9))
    dpi_val = dpi_val * 10 / 7
    return dpi_val

def vals(dpi_list):
    import numpy as np
    mean = format(np.mean(dpi_list), ".2f")
    std_dev = format(np.std(dpi_list), ".2f")
    median = format(percentile(dpi_list, 50), ".2f")
    x_min = format(percentile(dpi_list, 2), ".2f")
    x_max = format(percentile(dpi_list, 98), ".2f")
    per25 = format(percentile(dpi_list, 25), ".2f")
    per75th = format(percentile(dpi_list, 75), ".2f")
    return mean, std_dev, median, x_min, x_max, per25, per75th

def main():
    import numpy as np
    csv_file = csv_to_py('device_performance_index.csv')
    for i in range(len(np.unique(columna(csv_file, 0)))):
        new_csv = nueva_lista(csv_file, i + 1)
        valores_max, valores_min = array_max_min(new_csv)
        dpi_list = [dpi(new_csv, i, valores_max, valores_min) for i in range(1, len(new_csv))]
        mean, std_dev, median, x_min, x_max, per25, per75th = vals(dpi_list)
        print(f'{i + 1}: mean: {mean}, std_dev: {std_dev}, median: {median}, min: {x_min}, max: {x_max}, 25th: {per25}, 75th: {per75th}')
    return 0

if __name__ == '__main__':
    main()