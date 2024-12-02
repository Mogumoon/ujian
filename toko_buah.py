def menu():
    print("""
============================
Selamat Datang Di Toko Buah
============================
1.lihat produk
2.cek stok
3.beli
4.cetak struk
5.exit
""")


def lihat_menu():
        print('\n list buah')
        print('1. apel : 5.000')
        print('2. semangka : 20.000')
        print('3. pisang : 10.000')

def cek_stok(apel, semangka, pisang):
    print('\nstok buah : ')
    print(f'1. apel : {apel}')
    print(f'2. semangka : {semangka}')
    print(f'3. pisang : {pisang}')

def beli(saldo, apel, pisang, semangka):
     lihat_menu()
     pilihan = input('pilih yang akan dibeli : ')
     if pilihan == '1':
          saldo = 100000
          jenis = apel
          harga = 5000
          jumlah = int(input("masukan jumlah buah : "))
          total = jumlah * harga
          pembelian = saldo - total
          if jenis < jumlah:
               print("maaf stok nya kurang")
          else:
               if total > saldo:
                print('Maaf, saldo anda tidak cukup')
               else:
                    print(f"berhasil membeli {jenis} dengan harga {harga}")
                    print(f"sisa saldo anda {pembelian}")
                    try :
                         with open('struk.txt','w') as struk:
                              struk.write('=================\n')
                              struk.write('STRUK PEMBELIAN\n')
                              struk.write('=================\n')
                              struk.write(f'Nama buah {jenis}\n')
                              struk.write(f'Harga buah {harga}\n')
                              struk.write(f'jumlah buah {jumlah}\n')
                              struk.write(f'total {total}\n')
                              struk.write(f'saldo anda {saldo}\n')
                              struk.write(f'kembalian {pembelian}\n')
                    except Exception as e:
                         print(e)
            
     elif pilihan == '2':
          saldo = 100000
          jenis = semangka
          harga = 20000
          jumlah = int(input("masukan jumlah buah : "))
          total = jumlah * harga
          pembelian = saldo - total
          if jenis < jumlah:
               print("maaf stok nya kurang")
          else:
               if total > saldo:
                print('Maaf, saldo anda tidak cukup')
               else:
                    print(f"berhasil membeli {jenis} dengan harga {harga}")
                    print(f"sisa saldo anda {pembelian}")
                    try :
                         with open('struk.txt','w') as struk:
                              struk.write('=================\n')
                              struk.write('STRUK PEMBELIAN\n')
                              struk.write('=================\n')
                              struk.write(f'Nama buah {jenis}\n')
                              struk.write(f'Harga buah {harga}\n')
                              struk.write(f'jumlah buah {jumlah}\n')
                              struk.write(f'total {total}\n')
                              struk.write(f'saldo anda {saldo}\n')
                              struk.write(f'kembalian {pembelian}\n')
                    except Exception as e:
                         print(e)

     elif pilihan == '3':
          saldo = 100000
          jenis = pisang
          harga = 10000
          jumlah = int(input("masukan jumlah buah : "))
          total = jumlah * harga
          pembelian = saldo - total
          if jenis < jumlah:
               print("maaf stok nya kurang")
          else:
               if total > saldo:
                print('Maaf, saldo anda tidak cukup')
               else:
                    print(f"berhasil membeli {jenis} dengan harga {harga}")
                    print(f"sisa saldo anda {pembelian}")
                    try :
                         with open('struk.txt','w') as struk:
                              struk.write('=================\n')
                              struk.write('STRUK PEMBELIAN\n')
                              struk.write('=================\n')
                              struk.write(f'Nama buah {jenis}\n')
                              struk.write(f'Harga buah {harga}\n')
                              struk.write(f'jumlah buah {jumlah}\n')
                              struk.write(f'total {total}\n')
                              struk.write(f'saldo anda {saldo}\n')
                              struk.write(f'kembalian {pembelian}\n')
                    except Exception as e:
                         print(e)
                    else:
                         print("error")

def cetak_struk():
    try:
          with open('struk.txt',"r") as saw:
               lihat = saw.read()
               print(lihat)
    except Exception as e:
         print(e)
        
         
def main():
    saldo = 100000
    apel = 20
    semangka = 15
    pisang = 25
    
    
    while True:

        menu()
        inputan = input("pilih menu : ")
        if inputan == '1':
            lihat_menu()
        elif inputan == '2':
            cek_stok(apel, semangka, pisang)
        elif inputan == '3':
            beli(saldo, apel, pisang, semangka)
        elif inputan == '4':
            cetak_struk()
            break
        else :
            print('error')
         


if __name__ == '__main__':
    main()
