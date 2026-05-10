import hashlib
import re

def generate_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

def validasi_gmail(email):
    pattern = r'^[a-z0-9](\.?[a-z0-9]){4,}@gmail\.com$'
    return re.match(pattern, email)

def main():
    print("Program Verifikasi Integritas Data (MD5)")
    
    nama = input("Masukkan Nama lu bro = ")
    
    while True:
        email = input("Masukkan Gmail lu bro = ").lower()
        if validasi_gmail(email):
            break
        else:
            print("pliss masukin format Gmail yang valid yah ganteng/cantik 😎😂 (contoh: user@gmail.com)!")

    while True:
        no_hp = input("Masukkan Nomor Handphone lu bro = ")
        if 11 <= len(no_hp) <= 13 and no_hp.isdigit():
            break
        else:
            print("pliss masukin Nomor HP harus angka dan berjumlah 11-13 digit! yahh cantik/ganteng 🫡😎 ")
    
    data_awal = f"{nama}{email}{no_hp}"
    hash_awal = generate_md5(data_awal)
    
    print(f"\nHash Awal Sukeses Disimpan = {hash_awal}")
    print("-" * 45)

    print("\n[VALIDASI] Masukkan Lagi data lu buat pengecekan yah brooo :")
    nama_baru = input("Masukkan Nama = ")
    
    while True:
        email_baru = input("Masukkan Gmail = ").lower()
        if validasi_gmail(email_baru):
            break
        else:
            print("(!) Format Gmail lu gak valid woi 😒!")

    while True:
        no_hp_baru = input("Masukkan Nomor HP = ")
        if 11 <= len(no_hp_baru) <= 13 and no_hp_baru.isdigit():
            break
        else:
            print(">> (!) Nomor HP tidak valid! 😒😒😒😒")
    
    data_baru = f"{nama_baru}{email_baru}{no_hp_baru}"
    hash_baru = generate_md5(data_baru)

    # 5. Output Perbandingan
    print("\n" + "=" * 45)
    print(f"Hash Lama ={hash_awal}")
    print(f"Hash Baru = {hash_baru}")
    print("=" * 45)

    if hash_awal == hash_baru:
        print("STATUS = DATA TIDAK BERUBAH aman aja yekan (INTEGRITAS TERJAMIN)")
    else:
        print("STATUS = DATA BERUBAH/DIMODIFIKASI! waduhhhh")

if __name__ == "__main__":
    main()