import time

BOLD = "\033[1m"
HIJAU = "\033[92m"
MERAH = "\033[91m"
KUNING = "\033[93m"
RESET = "\033[0m"

def jalankan_timer():
    while True:
        print(f"\n{BOLD}=== PROGRAM TIMER BELAJAR FACHRY ==={RESET}\n")
        print(f"{BOLD}Brajil, do you redi tu KAIST?{RESET}")
        print("------------------------------------")

        while True:
            try:
                menit_belajar = float(input("Mau belajar berapa menit? : "))
                if menit_belajar > 0:
                    break
                else:
                    print(f"{MERAH}{BOLD}Angka harus lebih besar dari 0{RESET}")
            except ValueError:
                print(f"{MERAH}{BOLD}Masukin angka bosku, bukan huruf{RESET}")
        
        total_detik = menit_belajar * 60

        print(f"\n{KUNING}{BOLD}Timer dimulai! Tetap fokus dan jangan buka HP...{RESET}")

        while total_detik > -1:
            menit = int(total_detik // 60)
            detik = int(total_detik % 60)

            print(f"{BOLD}Sisa waktu: {menit:02d}:{detik:02d}{RESET}", end="\r")
            time.sleep(1)
            total_detik -= 1
        print("\n------------------------------------")
        print(f"{HIJAU}{BOLD}WAKTU BELAJAR SELESAI!{RESET}")
        print("------------------------------------")
        
        coba_lagi = input("\nMau lanjut? (y/n) : ").lower().strip()
        if coba_lagi != 'y':
            print(f"\n{BOLD}Ok{RESET}\n")
            break

if __name__ == "__main__":
    jalankan_timer()