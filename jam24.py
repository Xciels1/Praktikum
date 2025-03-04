def konversi_waktu(jam, menit, format_24=True):
    if format_24:
        return f"{jam:02d}:{menit:02d}"
    else:
        if jam == 0:
            return f"12:{menit:02d} AM"
        elif jam == 12:
            return f"12:{menit:02d} PM"
        elif jam > 12:
            return f"{jam - 12}:{menit:02d} PM"
        else:
            return f"{jam}:{menit:02d} AM"

# Contoh penggunaan
print(konversi_waktu(3, 45, True))  # 03:45
print(konversi_waktu(15, 30, False)) # 3:30 PM
