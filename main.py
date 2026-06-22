import time

print("\n=== PROGRAM TIMER BELAJAR FACHRY ===")
print("Brajil, do you redi tu KAIST?")
print("------------------------------------")

menit_belajar = float(input("Mau belajar berapa menit? : "))
total_detik = menit_belajar * 60

print("\nTimer dimulai! Tetap fokus dan jangan buka HP...")

while total_detik > -1:
    menit = int(total_detik // 60)
    detik = int(total_detik % 60)

    print(f"Sisa waktu: {menit:02d}:{detik:02d}", end="\r")
    time.sleep(1)
    total_detik -= 1

print("\n------------------------------------")
print("WAKTU BELAJAR SELESAI! Kerja bagus, Fachry. Istirahat dulu 5 menit.\n")