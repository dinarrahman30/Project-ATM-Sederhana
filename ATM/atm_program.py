import random
import datetime
from customer import Customer

atm = Customer(id) 

while True:
    id = int(input("Masukkan Pin Anda: "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin yang Anda Masukan Salah. Silahkan Coba Lagi: "))
        
        trial += 1

    if trial == 3:
        print("Error, Silahkan Ambil Kartu dan Ulangi..")
        exit()

    while True:
        print("Selamat Datang di ATM Bersama...")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        
        selectmenu = int(input("\nSilahkan Pilih Menu: "))
        
        if selectmenu == 1:
             print("\nSaldo Anda Sekarang: RP. " + str(atm.checkBalance()) + "\n")
             
        elif selectmenu == 2:
                nominal = float(input("Masukkan Nominal Saldo: "))
                verify_withdraw = input("Konfirmasi: Anda Akan Melakukan Debet Dengan Nominal Berikut ? \n " + str(nominal) + " ")
                
                if verify_withdraw == "y":
                    print("Saldo Awal Anda Adalah: Rp. " + str(atm.checkBalance()) + "")
                else:
                    break
                if nominal < atm.checkBalance():
                    atm.withdrawBalance(nominal)
                    print("Transaksi Debet Berhasil!")
                    print("Saldo Sisa Sekarang: Rp. " + str(atm.checkBalance()) + "")
                else:
                    print("Maaf. Saldo Anda Tidak Cukup Untuk Melakukan Transaksi!")
                    print("Silahkan Lakukan Penambahan Nominal Saldo")

        elif selectmenu == 3:
                nominal = float(input("Masukkan Nominal Saldo: "))
                verify_deposit = input("Konfirmasi: Anda Akan Melakukan Penyimpanan Dengan Nominal Berikut ? y/n " + str(nominal) + "")

                if verify_deposit == "y":
                    atm.depositBalance(nominal)
                    print("Saldo Anda Sekarang Adalah: Rp. " + str(atm.checkBalance()) + "\n")
                else:
                    break
                
        elif selectmenu == 4:
                verify_pin = int(input("Masukkan Pin Anda: "))

                while verify_pin != int(atm.checkPin()):
                    print("Pin Anda Salah, Silahkan Masukkan Pin: ")
                
                updated_pin = int(input("Silahkan Masukkan Pin Baru: "))
                print("Pin Anda Berhasil Diganti!")

                verify_newpin = int(input("Coba Masukkan Pin Baru: "))

                if verify_newpin == updated_pin:
                    print("Pin Baru Anda Sukses!")
                else:
                    print("Maaf, Pin Anda Salah!")

        elif selectmenu == 5:
                    print("Resi Tercetak Otomatis Saat Anda Keluar. \n Harap Simpan Tanda Terima Ini \n Sebagai Bukti Transaksi Anda.")
                    print("No. Record: ", random.randint(10000, 1000000))
                    print("Tanggal: ", datetime.datetime.nom())
                    print("Saldo Akhir: ", atm.checkBalance())
                    print("Terima Kasih Telah Menggunakan ATM Bersama!")
                    exit()
        else:
            print("Error. Maaf, Menu Tidak Tersedia")