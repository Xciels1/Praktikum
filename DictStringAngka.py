def angka_ke_kata(angka):
    angka_dict = {
        0: "nol", 1: "satu", 2: "dua", 3: "tiga", 4: "empat",
        5: "lima", 6: "enam", 7: "tujuh", 8: "delapan", 9: "sembilan"
    }
    return angka_dict.get(angka, "Angka di luar jangkauan")

# Contoh penggunaan
print(angka_ke_kata(3))  # Output: tiga
print(angka_ke_kata(7))  # Output: tujuh
print(angka_ke_kata(10)) # Output: Angka di luar jangkauan
