import os

# Clear the console screen
def clear_screen():
    if os.name == 'posix':
        # For Unix and Linux
        os.system('clear')
    elif os.name == 'nt':
        # For Windows
        os.system('cls')

def investasi_modal():
    # Input dari pengguna
    nominal_investasi = float(input("Masukkan nominal uang yang diinvestasikan: "))
    pilihan = input("Pilih jenis persentase (bulan/tahun): ").lower()
    
    while pilihan not in ["bulan", "tahun"]:
        print("Pilihan tidak valid. Silakan pilih 'bulan' atau 'tahun'.")
        pilihan = input("Pilih jenis persentase (bulan/tahun): ").lower()
    
    persentase = float(input(f"Masukkan persentase yang didapat per {pilihan}: "))
    jangka_waktu = int(input(f"Masukkan jangka waktu dalam {pilihan}: "))
    
    # Konversi persentase ke desimal
    persentase = 1 + (persentase / 100)  # Tambahan 1 untuk menambahkan persentase
    
    # Perhitungan hasil investasi setiap bulan
    if pilihan == "bulan":
        for bulan in range(jangka_waktu):
            nominal_investasi *= persentase
            print(f"Bulan ke-{bulan + 1}, uang yang diperoleh: Rp. {nominal_investasi:.0f}")

    # Perhitungan hasil investasi setiap tahun
    elif pilihan == "tahun":
        for tahun in range(jangka_waktu):
            nominal_investasi *= persentase
            print(f"Tahun ke-{tahun + 1}, uang yang diperoleh: Rp. {nominal_investasi:.0f}")

def investasi_rutin():
    # Input dari pengguna
    nominal_investasi = float(input("Masukkan nominal uang yang diinvestasikan: "))
    pilihan = input("Pilih jenis persentase (bulan/tahun): ").lower()
    
    while pilihan not in ["bulan", "tahun"]:
        print("Pilihan tidak valid. Silakan pilih 'bulan' atau 'tahun'.")
        pilihan = input("Pilih jenis persentase (bulan/tahun): ").lower()
    
    persentase = float(input(f"Masukkan persentase yang didapat per {pilihan}: "))
    jangka_waktu = int(input(f"Masukkan jangka waktu dalam {pilihan}: "))
    
    # Konversi persentase ke desimal
    persentase = 1 + (persentase / 100)  # Tambahan 1 untuk menambahkan persentase
    
    # Perhitungan hasil investasi setiap bulan
    if pilihan == "bulan":
        curr_nominal_investasi = float(nominal_investasi)
        for bulan in range(jangka_waktu):
            if bulan == 0:
                curr_nominal_investasi *= persentase
                print(f"Bulan ke-{bulan + 1}, uang yang diperoleh: Rp. {curr_nominal_investasi:.0f}")
            else:
                curr_nominal_investasi += nominal_investasi
                curr_nominal_investasi *= persentase
                print(f"Bulan ke-{bulan + 1}, uang yang diperoleh: Rp. {curr_nominal_investasi:.0f}")

    # Perhitungan hasil investasi setiap tahun
    if pilihan == "tahun":
        bulan = jangka_waktu * 12
        curr_nominal_investasi = float(nominal_investasi)
        for bulan in range(bulan):
            if bulan == 0:
                print(f"Bulan ke-{bulan + 1}, uang yang diperoleh: Rp. {curr_nominal_investasi:.2f}")
            if bulan != 0 and bulan % 12 == 0:
                curr_nominal_investasi += nominal_investasi
                curr_nominal_investasi *= persentase
                print(f"Tahun ke-{int(bulan/12) + 1}, uang yang diperoleh: Rp. {curr_nominal_investasi:.2f}")
            else:
                curr_nominal_investasi += nominal_investasi
                print(f"Bulan ke-{bulan + 1}, uang yang diperoleh: Rp. {curr_nominal_investasi:.2f}")

                


if __name__ == "__main__":
    while True:
        clear_screen()

        print("===================================================")
        print("              Kalkulator Investasi                 ")
        print("            dibuat oleh Anggara kenji              ")
        print("               powered by ChatGPT                  ")
        print("===================================================")

        print("1. investasi satu kali")
        print("2. investai rutin")
        print("3. Keluar")
        pilih = input("pilih jenis investasi yang ingin dihitung: ")
        
        if(pilih == "1"):
            investasi_modal()
            input("Tekan Enter untuk melanjutkan...")
        elif(pilih == "2"):
            investasi_rutin()
            input("Tekan Enter untuk melanjutkan...")
        elif(pilih == "3"):
            print("Terimakasih telah menggunakan program saya!")
            print("Selamat Tinggal!")
            break
        else:
            print("pilihan tidak ada! coba lagi!")


