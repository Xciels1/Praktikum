'''
Deskripsi
Vito adalah anak yang sangat tidak teliti. Dia terkadang lupa dengan buku-buku yang ia simpan di dalam lemari bukunya. Oleh sebab itu, kamu harus membatu Vito untuk membuat program yang dapat menjabarkan isi lemarinya!

Contoh
Pemanggilan:

 
buku = (
    "Renungan Harian","Matematika","Sains","Jaringan","Pemrograman",
    "Renungan Harian","Sains","Jaringan","Majalah Perjodohan"
    )
hitung(buku)
Output:

Buku dengan judul Renungan Harian sejumlah 2 buku

Buku dengan judul Matematika sejumlah 1 buku

Buku dengan judul Sains sejumlah 2 buku

Buku dengan judul Jaringan sejumlah 2 buku

Buku dengan judul Pemrograman sejumlah 1 buku

Buku dengan judul Majalah Perjodohan sejumlah 1 buku

Total buku di dalam lemari adalah : 9 buku

 

Batasan
Fungsi anda tidak perlu return, lakukan print() di dalam fungsi.

Output berupa string

Format data berupa tuple of string.
'''
def hitung(buku):
    buku_dict = {}
    for judul in buku:
        if judul in buku_dict:
            buku_dict[judul] += 1
        else:
            buku_dict[judul] = 1
    for judul, jumlah in buku_dict.items():
        print(f"Buku dengan judul {judul} sejumlah {jumlah} buku")
    print(f"Total buku di dalam lemari adalah : {len(buku)} buku")
