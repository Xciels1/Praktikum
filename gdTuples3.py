'''
Deskripsi
Buatlah fungsi databuku(data) yang dapat mencetak data buku. Format data buku yang diterima tidak beraturan tetapi diketahui bahwa setiap data buku yang ada terdiri dari Judul, Tahun terbit dan penulis.

Diketahui juga kondisi berikut:

1.     Sebuah data disebut Judul jika tidak semua karakter merupakan huruf besar.

2.     Sebuah data disebut Penulis jika semua karakter merupakan huruf besar

3.     Sebuah data disebut Tahun terbit, jika data bertipe angka.

Fungsi databuku(data) akan mengeluarkan output berupa semua data buku, dengan format

Judul

Tahun terbit

Penulis

 

Contoh
Pemanggilan:

data = (

            ("Introduction to Python",2022,"SULE RITMA"),

            (2003,"Python for Everybody","DAVID BLEI")

)

databuku(data)

Output:

Introduction to Python

2019

SULE RITMA

Introduction to Assembly

1876

YUSTA CINDY

 

Penjelasan:

Introduction to Assembly merupakan Judul

2019 merupakan Tahun penerbit

YUSTA CINDY merupakan Penulis

 

 Batasan

Fungsi anda tidak perlu return, lakukan print() di dalam fungsi.

Outputnya berupa: semua data buku

Format data yang diterima berupa tuple of ( Judul/Tahun/Penulis, Judul/Tahun/Penulis, Judul/Tahun/Penulis )
'''
def databuku(data):
    for buku in data:
        judul = ""
        tahun = ""
        penulis = ""
        for item in buku:
            if isinstance(item, int):
                tahun = item
            elif item.isupper():
                penulis = item
            else:
                judul = item
        print(judul)
        print(tahun)
        print(penulis)
    print() 
