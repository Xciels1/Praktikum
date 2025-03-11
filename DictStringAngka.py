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


def angka_ke_kata2(angka):
    angka_dict = {
        0: "nol", 1: "satu", 2: "dua", 3: "tiga", 4: "empat",
        5: "lima", 6: "enam", 7: "tujuh", 8: "delapan", 9: "sembilan"
    }
    kata_list = [angka_dict[int(digit)] for digit in str(angka)]
    return ' '.join(kata_list)


print(angka_ke_kata(3124))

def int_to_string(angka):
  for i in angka: 
    if i == "0":
      print("Nol", end=" ")  
    elif i == "1":
      print("Satu", end=" ")
    elif i == "2":
      print("Dua", end=" ")
    elif i == "3":
      print("Tiga", end=" ")
    elif i == "4":
      print("Empat", end=" ")
    elif i == "5":
      print("Lima", end=" ")
    elif i == "6":
      print("Enam", end=" ")
    elif i == "7":
      print("Tujuh", end=" ")
    elif i == "8":
      print("Delapan", end=" ")
    elif i == "9":
      print("Sembilan", end=" ")
