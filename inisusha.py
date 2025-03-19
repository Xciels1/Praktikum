def tabel_perkalian_nggak_jelas(baris, kolom):
    if not (isinstance(baris, int) and isinstance(kolom, int)) or baris <= 0 or kolom <= 0 or baris >= 25 or kolom >= 25:
        print("TIDAK VALID")
        return

    if (baris + kolom) % 2 == 0:
        rows_to_print = range(1, baris + 1, 2)
    else:
        rows_to_print = range(2, baris + 1, 2)  

    for i in rows_to_print:
        for j in range(1, kolom + 1):
            if i == j:
                print("miau", end=" ")
            else:
                print(i * j, end=" ")
        print()
