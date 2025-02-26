#if else
def runner_up(a, b, c, d, e):
    # Menentukan juara pertama (waktu terkecil)
    first = min(a, b, c, d, e)

    # Inisialisasi runner-up dengan nilai yang sangat besar
    second = float('inf')

    # Mengecek setiap waktu dan mencari runner-up
    for time in [a, b, c, d, e]:
        if first < time < second:  # Harus lebih besar dari juara pertama, tapi lebih kecil dari runner-up saat ini
            second = time

    return second  # Mengembalikan runner-up

# Contoh penggunaan
print(runner_up(12.5, 11.3, 14.2, 10.8, 13.0))  # Output: 11.3

#sorting
def runner_up(a, b, c, d, e):
    times = [a, b, c, d, e]  # Masukkan semua waktu ke dalam list
    times.sort()  # Urutkan dari terkecil ke terbesar
    return times[1]  # Runner-up adalah elemen kedua setelah sorting

# Contoh penggunaan
print(runner_up(12.5, 11.3, 14.2, 10.8, 13.0))  # Output: 11.3

#Dictionary
def runner_up(times_dict):
    sorted_times = sorted(times_dict.items(), key=lambda x: x[1])  # Urutkan berdasarkan nilai waktu
    return sorted_times[1]  # Runner-up adalah elemen kedua dalam list yang diurutkan

# Contoh penggunaan
times = {
    "pelari_1": 12.5,
    "pelari_2": 11.3,
    "pelari_3": 14.2,
    "pelari_4": 10.8,
    "pelari_5": 13.0
}

print(runner_up(times))  # Output: ('pelari_2', 11.3)
