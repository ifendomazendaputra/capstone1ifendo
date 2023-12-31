from func import *

barang = read(path('barang'))
# carts = read(path('carts'))

clear(), print(sorotmenu(credit))
while True:
    try:
        etc()
        pilihan = pilihmenu(['| New Cart    |', '| Open Cart   |', '| Add Stock   |',
                                '| Exit        |'], vertical = False, header = credit1)
        
        if pilihan == 1:                    #new cart
            print('Pembelian\n')
            barang, cart = newcart(barang)
    
            if len(cart)!= 0 and cart[-1] == 'p':
                cart.pop(-1)
                write(cart, path('carts'), note = "'" + input('\nMasukkan Nama Pembeli : ') + "'")
                os.system('notepad.exe ' + path('carts'))
                continue
            
            if pembayaran(cart):
                write(cart, path('transactions'), note = "'paid'")
                os.system('notepad.exe ' + path('transactions'))
    
                os.remove(path('barang'))
                write(barang, path('barang'))
                os.system('notepad.exe ' + path('barang'))
        
        elif pilihan == 2:                  #kelola cart
            print('Kelola Keranjang\n')
            # print(carts)
            # barang, cart = kelolacart(barang, carts)
        
        elif pilihan == 3:                  #Tambah stock
            barang = tambahstock(barang)

            os.remove(path('barang'))
            write(barang, path('barang'))
            os.system('notepad.exe ' + path('barang'))
        
        elif pilihan == 4:                  #exit
            print('Terima Kasih')
            break
        else: error()
    except: error()
