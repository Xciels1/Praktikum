'''
Deskripsi
Lela ingin mencatat berapa banyak dari temannya yang memiliki inisial yang sama. Buatlah fungsi inisial(daftar) yang akan menampilkan nama dari daftar nama. Jika ada nama dengan inisial sudah pernah dicetak, maka akan ditambahkan angka sebanyak jumlah inisial yang sama.

Contoh
Pemanggilan:

daftar = (

             "Michael","Viny","Aurelio","Michael",

             "Felix","Kevin","Vincen","Vincen","Michael")

inisial(daftar)

Output:

Michael

Viny

Aurelio

Michael2

Felix

Kevin

Vincen2

Vincen3

Michael3

 

Batasan
Fungsi anda tidak perlu return, lakukan print() di dalam fungsi.

Output berupa string

Format data berupa tuple of string.
'''
#code
def inisial(daftar):
    inisial_dict = {}
    for nama in daftar:
        inisial_nama = nama[0]
        if inisial_nama in inisial_dict:
            inisial_dict[inisial_nama] += 1
            print(f"{nama}{inisial_dict[inisial_nama]}")
        else:
            inisial_dict[inisial_nama] = 1
            print(nama)
