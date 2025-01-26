import os

def tampilkan_pilihan():
    print("Pilih Permainan:")
    print("1. Skibidi Toilet Penjawab Pertanyaan")
    print("2. Cek Khodam")
    print("3. Cek Bau Kentut")
    print("4. TicTacToe #Create By ChatGPT")
    print("5. HangMan #Create By ChatGPT")

def pilihan_terpilih(pilihan):
    if pilihan == 1:
        os.system("python 1.py")
    elif pilihan == 2:
        os.system("python 2.py")
    elif pilihan == 3:
        os.system("python 3.py")
    elif pilihan == 4:
        os.system("python 4.py")
    elif pilihan == 5:
        os.system("python 5.py")
    else:
        print("Pilihan tidak valid.")

# Menampilkan pilihan
tampilkan_pilihan()

# Input dari pengguna
pilihan = int(input("Pilih: "))

# Menampilkan contoh berdasarkan pilihan
pilihan_terpilih(pilihan)