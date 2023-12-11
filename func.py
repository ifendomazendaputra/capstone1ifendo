import os, keyboard, time
os.system('color')

def path(filename):
    return '_tugas/capstonemodul1/'+filename+'.txt'

def read(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    lines = [data[:-1].split(', ')
             if i != len(lines)-1 else data.split(', ') 
             for i,data in enumerate(lines)]
    # print(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (lines[i][j].startswith("'") and lines[i][j].endswith("'")) == False:
                lines[i][j] = int(lines[i][j])
            else:
                lines[i][j] = lines[i][j][1:-1]
    return lines

def write(data, filename):
    file = open(filename, 'a')
    for i in range(len(data)-1):
        temp = [str("'" + j + "'") if type(j) == str else str(j) for j in data[i]]
        temp.insert(0, data[-1])
        file.write(','.join(temp))
        file.write('\n')
    file.close()

credit  = ('  _________________________________________  \n' +
           '                                             \n' +
           '     ======= PT. ESCAPE COMPUTER =======     \n' +
           '                                             \n' +
           '                                             \n' +
           '                                             \n' +
           '                   Welcome                   \n' +
           '  _________________________________________  \n' +
           '                                             \n')
credit1 = '==================== PT. ESCAPE COMPUTER ====================\n\n'

def clear():
    os.system('cls')

def error():
    print('\nInputan Tidak Sesuai!')

def etc():
    input('Enter To Continue ...')

def sorotmenu(word, x = 0, y = 30, z = 43):
    return f'\x1b[{x};{y};{z}m' + word + '\x1b[0m'

def pilihmenu(menu, vertical = False, cls = True, header = ''):
    pointer = 0
    print("\n<Gunakan 'Arrow' untuk memilih>  <{empty} + 'enter' untuk mengulang>\n")
    while True:
        if cls : clear()
        print(header, end = '\r')
        for i in menu:
            if vertical:
                print(sorotmenu(i, 6,32,47) if i == menu[pointer] else i, end = '   ')
            else:
                print(sorotmenu(i) if i == menu[pointer] else i)
        print('', end = '\r')
        
        time.sleep(0.2) 
        keyboard.unhook_all()
        key = keyboard.read_key(True)
        if key == 'enter':
            if cls: clear(); print()
            return pointer+1
        elif (key == 'down') or (key == 'right'):
            pointer += 1
        elif (key == 'up') or (key == 'left'):
            pointer -= 1
        
        if pointer == len(menu):
            pointer = 0
        elif pointer == -1 :
            pointer = len(menu)-1

def show(comb, header = ''):
    print(header)
    starts, ends, combT = '', '', list(map(list, zip(*comb))) # print(comb, '\n\n', combT)
    for i, ldata in enumerate(comb):
        if i == len(comb)-1:
            starts = '\x1B[4m'
            ends = '\x1B[0m'
        if i == 0:
            print('|' + sorotmenu(' No '), end = '')
        else:
            space = ' ' if i > 9 else '  '
            print(f'|{starts}{space}{i} {ends}', end = '')
        for j, data in enumerate(ldata):
            maks = len(max([str(i) for i in combT[j]], key = len)) + 2
            if i == 0:
                print('|' + sorotmenu('  ' + data.capitalize() + ' '*(maks-len(data))), end = '')
            else:
                print('|' + starts + '  ' + str(data).capitalize() + ends, end = '')
                print(starts + ' '*(maks - len(str(data))) + ends, end = '')
            if j == len(ldata)-1:
                print('|', end = '')
        print()

def tambahitem(barang, cart):
    try:
        indeks = int(input('\n\nMasukkan Indeks Barang\t\t: '))-1
        if barang[indeks][4] == 0:
            print('\nItem',barang[indeks][0],'Habis Terjual') # del barang[indeks-1]
        else:
            jumlah = int(input('Masukkan Jumlah Barang\t\t: '))
            if barang[indeks][4] >= jumlah:
                barang[indeks][4] -= jumlah

                if any(barang[indeks][1] in item for item in cart):
                    cart[indeks][2] += jumlah
                else:
                    cart.append([barang[indeks][0], barang[indeks][1], jumlah, barang[indeks][5]])
            else:
                print('\nStock Barang Tidak Mencukupi!')
        return barang, cart
    except: return barang, cart

def hapusitem(barang, cart):
    try:
        indeks = int(input('\n\nMasukkan Indeks Keranjang\t\t: '))-1
        if indeks <= len(cart):
            for i in range(len(barang)):
                if cart[indeks][1] == barang[i][1]:
                    barang[i][4] += cart[indeks][2]
                    cart.pop(indeks)
                    break
            return barang, cart
        else:
            print('\nTidak ada barang dengan indeks',indeks + 1)
            return barang, cart
    except: return barang, cart

def updatejumlah(barang , cart):
    try:
        indeks = int(input('\n\nMasukkan Indeks Keranjang\t\t: '))-1
        newjumlah = int(input('Masukkan Jumlah Baru\t\t\t: '))
        if indeks <= len(cart):
            for i in range(len(barang)):
                if cart[indeks][1] == barang[i][1]:         #cari id yang sama antara keranjang dan stock
                    barang[i][4] += cart[indeks][2]         #kembalikan jumlah yang telah diambil
                    if barang[i][4] >= newjumlah:           #jika jumlah baru kecil/sama dg  dari stock
                        barang[i][4] -= newjumlah           #kurangi kembali jumlah dalam stock
                        cart[indeks][2] = newjumlah         #masukkan jumlah baru keranjang
                    else:                                   #kalau jumlah baru tidak cukup
                        barang[i][4] -= cart[indeks][2]     #ambil kembali barang yang direturn
                        print('\nStock Barang Tidak Mencukupi!')
                    break
            return barang, cart
        else:
            print('\nTidak ada barang dengan indeks',indeks + 1)
            return barang, cart
    except: return barang, cart

def lanjut(word):
    lanjut = input(f'Lanjutkan {word}? y/n : ').lower()
    if lanjut == 'y' or lanjut == '': return True
    elif lanjut == 'n': return False
    else: print(f'Input tidak diketahui, lanjutkan {word}..') ; return True

def newcart(barang):
    cart, temp = [], barang
    while True:
        try:
            clear()
            show([['nama', 'id', 'jenis', 'segmen', 'stok', 'harga']] + barang, 'Pembelian\n')
            if cart:
                show([['Nama Barang','ID Barang', 'Jumlah', 'Harga']] + cart, '\nKeranjang\n')
                pilihan = pilihmenu(['|Tambah Item  ', '|Hapus Item  ', '|Update Jumlah  ', '|Pending  ', '|Cancel  ', '|Bayar  '], vertical = True, cls = False)
                if pilihan == 1:
                    barang, cart = tambahitem(barang, cart)
                elif pilihan == 2:
                    barang, cart = hapusitem(barang, cart)
                elif pilihan == 3:
                    barang, cart = updatejumlah(barang, cart)
                elif pilihan == 4:
                    cart.append('p')
                    return barang, cart
                elif pilihan == 5:
                    return temp, []
                elif pilihan == 6: break
            else:
                barang, cart = tambahitem(barang, cart)
                if lanjut('Pembelian') == False: break
        except: error()
    return barang, cart

def pembayaran(cart):
    if cart:
        total = sum(cart[i][2]*cart[i][3] for i in range(len(cart)))
        while True:
            clear()
            print(f'Pembayaran "Cart ID : {len(cart)+1}"')
            show([['Nama Barang','ID Barang', 'Jumlah', 'Harga']] + cart)
            diskon = int(input('Masukkan Persetase Diskon : ')) if input('Lanjut Tanpa Diskon?').lower() == 'y' else 0
            print('\nTotal yang Harus Dibayar =',total)
            if diskon != 0:
                print('Total setelah diskon', total - (total*diskon)/100)
            try:
                x = int(input('Masukkan jumlah uang : '))
                if x >= total:
                    print('\nPembayaran diterima.', end = '')
                    if x > total:
                        print(' Uang kembalian Rp', '{:,}'.format(x - total))
                    print('Menunggu Pengambilan Barang..')
                    return True
                else:
                    print('\nUangnya Anda kurang sebesar Rp', '{:,}'.format(total - x))
                    if lanjut('Pembayaran') == False: 
                        print('\nPembelian dicancel.')
                        return False
            except:
                error(), etc()
    else:
        print('\nTidak Ada Pembelian!')
        return False

def kelolacart(barang, carts):
    print('on progress')


def tambahstock(barang):
    while True:
        try:
            id, found = input('\nMasukkan ID Barang\t\t: '), False
            for i in range(len(barang)):
                if id == barang[i][1]:
                    print('Barang Sudah Ada Dalam Database, silahkan tambah stock..')
                    barang[i][4] += int(input('\nMasukkan Jumlah Tambahan Stock : '))
                    found = True
                    break
            if not found:
                barang.append([input('\nMasukkan Nama Barang\t\t: '), id,
                               input('Masukkan Jenis Barang\t\t: '),
                               input('Masukkan Segmen Barang\t\t: '),
                               int(input('Masukkan Stock Barang\t\t: ')),
                               int(input('Masukkan Harga Barang\t\t: '))])
            if lanjut('Tambah Stock Barang') == False: break
        except:
            error()
    clear()
    show([['nama', 'id', 'jenis', 'segmen', 'stok', 'harga']] + barang, header = 'Stock Terbaru')
    return barang