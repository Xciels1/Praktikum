def polaular(angka):
    if angka <= 0:
        print("tidak terdefiniskan")
        return
    
    matrix = [[0 for _ in range(angka)] for _ in range(angka)]
    num = 1
    
    for i in range(angka):
        if i % 2 == 0:
            for j in range(angka):
                matrix[i][j] = num
                num += 1
        else:
            for j in range(angka-1, -1, -1):
                matrix[i][j] = num
                num += 1
    
    for row in matrix:
        print(' '.join(f"{x:02d}" for x in row))

# Contoh penggunaan
polaular(4)
polaular(0)
polaular(5)
