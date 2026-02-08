from prettytable import PrettyTable

# Daftar Tabel Perpustakaan
DB_Perpus = [
    ["BK-NOV-2005-LP7A", "Laskar Pelangi", "Andrea Hirata", 2005, "Novel", 5, "TERSEDIA"],
    ["BK-SAS-1980-BM9C", "Bumi Manusia", "Pramoedya A. Toer", 1980, "Sastra", 3, "TERSEDIA"],
    ["BK-NOV-2009-NM4F", "Negeri 5 Menara", "Ahmad Fuadi", 2009, "Novel", 4, "TERSEDIA"],
    ["BK-FIK-2006-FK0D", "Filosofi Kopi", "Dee Lestari", 2006, "Fiksi", 0, "DIPINJAM"],
    ["BK-SEL-2018-AH6B", "Atomic Habits", "James Clear", 2018, "Self-Help", 6, "TERSEDIA"],
    ["BK-SEL-2016-SU4M", "The Subtle Art of Not Giving a F*ck", "Mark Manson", 2016, "Self-Help", 4, "TERSEDIA"],
    ["BK-SEJ-2011-SA0P", "Sapiens", "Yuval Noah Harari", 2011, "Sejarah", 0, "DIPINJAM"],
    ["BK-SEJ-2015-HD2K", "Homo Deus", "Yuval Noah Harari", 2015, "Sejarah", 2, "TERSEDIA"],
    ["BK-KEU-1997-RD5Q", "Rich Dad Poor Dad", "Robert T. Kiyosaki", 1997, "Keuangan", 5, "TERSEDIA"],
    ["BK-PSI-2011-TF8L", "Thinking, Fast and Slow", "Daniel Kahneman", 2011, "Psikologi", 0, "DIPINJAM"],
    ["BK-TEK-2008-CC3R", "Clean Code", "Robert C. Martin", 2008, "Teknologi", 4, "TERSEDIA"],
    ["BK-TEK-2015-PC9E", "Python Crash Course", "Eric Matthes", 2015, "Teknologi", 3, "TERSEDIA"],
    ["BK-TEK-1999-PP6S", "The Pragmatic Programmer", "Andrew Hunt", 1999, "Teknologi", 2, "TERSEDIA"],
    ["BK-NOV-1949-OR1N", "1984", "George Orwell", 1949, "Novel", 0, "DIPINJAM"],
    ["BK-NOV-1945-AF4G", "Animal Farm", "George Orwell", 1945, "Novel", 4, "TERSEDIA"],
    ["BK-NOV-1960-TK2M", "To Kill a Mockingbird", "Harper Lee", 1960, "Novel", 2, "TERSEDIA"],
    ["BK-NOV-1988-AL7C", "The Alchemist", "Paulo Coelho", 1988, "Novel", 5, "TERSEDIA"],
    ["BK-KEU-2020-PM5H", "The Psychology of Money", "Morgan Housel", 2020, "Keuangan", 4, "TERSEDIA"],
    ["BK-LIF-2016-IK0Y", "Ikigai", "Hector Garcia", 2016, "Lifestyle", 0, "DIPINJAM"],
    ["BK-PRO-2016-DW8J", "Deep Work", "Cal Newport", 2016, "Produktivitas", 4, "TERSEDIA"]
]

# def function tabel
def Tabel_Buku(Data):
    tb = PrettyTable()
    tb.field_names = ['No', 'ID Buku', 'Judul', 'Penulis', 'Tahun Terbit', 'Kategori', 'Stok', 'Status']

    for i in range(len(Data)):
        tb.add_row ([i+1, Data[i][0], Data[i][1], Data[i][2], Data[i][3], Data[i][4], Data[i][5], Data[i][6]])

    return(tb)

# def function generate ID
import random
import string

def generate_id(Kategori, Tahun, DB):
    Kode_Kat = Kategori.strip()[:3].upper()
    Kode_Rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    ID_Baru = f"BK-{Kode_Kat}-{Tahun}-{Kode_Rand}"

    while any(buku[0] == ID_Baru for buku in DB):
        Kode_Rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        ID_Baru = f"BK-{Kode_Kat}-{Tahun}-{Kode_Rand}"

    return ID_Baru

# Variable Bayangan Trash
Trash_Perpus = []

# Import kalender/period
from datetime import date, timedelta

Cart_Peminjaman = []   # isi: list ID buku (maks 2)
Riwayat_Pinjam = []    # list transaksi

# def function cari buku by id untuk pinjam
def cari_index_buku_by_id(DB, ID_Buku):
    for idx in range(len(DB)):
        if DB[idx][0] == ID_Buku:
            return idx
    return -1

# def function cart
def tampil_cart(DB, Cart_IDS):
    if not Cart_IDS:
        print("🛒 Cart masih kosong.")
        return []

    data_cart = []
    for id_buku in Cart_IDS:
        idx = cari_index_buku_by_id(DB, id_buku)
        if idx != -1:
            data_cart.append(DB[idx])

    print("\n🛒 Isi Cart:")
    print(Tabel_Buku(data_cart))
    return data_cart




# Mulai program
while True:
    # Menampilkan menu
    print('Selamat Datang di Perpustakaan Umum Rumah Buku')
    print('\nPilihan Menu:')
    print('1. Tampilkan Daftar Koleksi')
    print('2. Menambahkan Daftar Koleksi')
    print('3. Update Data Koleksi')
    print('4. Hapus Data Koleksi')
    print('5. Sewa Koleksi')
    print('0. Keluar')
    
    # Input pilihan menu
    Menu = input('\nMasukkan pilihan menu yang Anda inginkan: ')

    # Pilihan Menu 1
    if Menu == '1':
        # Input untuk pilihan di menu 1
        while True:
            print('\nPilih data yang ingin ditampilkan:')
            print('1. Tampilkan semua buku')
            print('2. Tampilkan buku berdasarkan kategori')
            print('3. Tampilkan buku yang tersedia')
            print('4. Cari buku berdasarkan penulis/judul')
            print('0. Kembali')

            # Input Pilihan Menu Tampilkan Koleksi
            Menu_1 = input('\nMasukkan pilihan menu (1-4): ')
            # Tampilkan semua koleksi
            if Menu_1 == '1':
                print(Tabel_Buku(DB_Perpus))

            # Tampilkan koleksi berdasarkan kategori
            elif Menu_1 == '2':
                Kategori = input('Masukkan kategori yang ingin dicari: ').strip().lower()
                Hasil_Pencarian = []

                for i in range(len(DB_Perpus)):
                    if DB_Perpus[i][4].lower() == Kategori:
                        Hasil_Pencarian.append(DB_Perpus[i])

                if len(Hasil_Pencarian) == 0:
                    print('❌ Tidak ada buku dengan kategori tersebut.')

                else:
                    print(Tabel_Buku(Hasil_Pencarian))

            # Tampilkan buku yang tersedia
            elif Menu_1 == '3':
                Hasil_Pencarian = []

                for i in range(len(DB_Perpus)):
                    if DB_Perpus [i][5] > 0:
                        Hasil_Pencarian.append(DB_Perpus[i])

                if len(Hasil_Pencarian) == 0:
                    print('❌ Tidak ada buku yang tersedia.')
                 
                else:
                    print(Tabel_Buku(Hasil_Pencarian))

            # Tampilkan buku sesuai nama penulis atau judul yang dicari
            elif Menu_1 == '4':
                Cari = input('Masukkan nama penulis/judul buku yang ingin dicari: ').strip().lower()
                Hasil_Pencarian = []

                for i in range(len(DB_Perpus)):
                    Judul = DB_Perpus[i][1].lower()
                    Penulis = DB_Perpus[i][2].lower()

                    if Cari in Judul or Cari in Penulis:
                        Hasil_Pencarian.append(DB_Perpus[i])

                if len(Hasil_Pencarian) == 0:
                    print('❌ Buku yang Anda cari tidak ada.')
                else:
                    print(Tabel_Buku(Hasil_Pencarian))

            elif Menu_1 == '0':
                break

            else:
                print('❌ Input yang Anda masukkan salah.')
                break

    # Pilihan menu 2 - tambahkan koleksi
    elif Menu == '2':
        Judul_Baru = input('Masukkan judul buku yang ingin ditambahkan: ').strip()
        Penulis_Baru = input('Masukkan nama penulis: ').strip()

        while True:
            try:
                Tahun_Terbit = int(input('Masukkan tahun terbit buku: ').strip())
                break
            except:
                print('❌ Tahun harus angka. Coba lagi.')

        Kategori = input('Masukkan kategori buku: ')

        while True:
            try:
                Stok_Buku = int(input('Masukkan jumlah buku baru: ').strip())
                if Stok_Buku < 0:
                    print('❌ Stok tidak boleh negatif')
                    continue
                break
            except:
                print('❌ Stok harus angka')

        Status_Buku = 'TERSEDIA' if Stok_Buku > 0 else 'DIPINJAM'
        ID_Buku = generate_id(Kategori, Tahun_Terbit, DB_Perpus)
       
        Buku_Baru = [ID_Buku, Judul_Baru, Penulis_Baru, Tahun_Terbit, Kategori, Stok_Buku, Status_Buku]
        DB_Perpus.append(Buku_Baru)

        print('\n✅ Buku berhasil ditambahkan!')
        print('📌 Buku baru yang ditambahkan:')
        print(Tabel_Buku([Buku_Baru]))

    # Menu 3 Update Data
    elif Menu == '3':
        print(Tabel_Buku(DB_Perpus))

        Judul_Update = input('\nMasukkan judul buku yang ingin di-update: ').strip().lower()
        Ditemukan = False

        for i in range(len(DB_Perpus)):
            if DB_Perpus[i][1].strip().lower() == Judul_Update:
                Ditemukan = True

                print('\n📌 Buku yang akan di-update')
                print(Tabel_Buku([DB_Perpus[i]]))

                print('\nPilih jenis update data yang diinginkan: ')
                print('1. Update semua data (Kecuali ID Buku)')
                print('2. Update judul buku saja')
                print('3. Update nama penulis')
                print('4. Update tahun terbit')
                print('5. Update kategori buku')
                print('6. Update stok buku')
                print('0. Batal')

                Pilihan = input('Pilih (0-6): ').strip()

                if Pilihan == '0':
                    print('❌ Update dibatalkan.')
                    break

                elif Pilihan == '1': # Update semua data
                    Judul_New = input('Judul baru: ').strip()
                    Penulis_New = input('Nama penulis baru: ').strip()

                    while True:
                        try:
                            Tahun_New = int(input('Tahun terbit baru: ').strip())
                            break
                        except:
                            print('❌ Tahun harus angka')

                    Kategori_New = input('Kategori baru: ').strip()

                    while True:
                        try:
                            Stok_New = int(input('Stok baru: ').strip())
                            if Stok_New < 0:
                                print('❌ Stok tidak boleh negatif!')
                                continue
                            break
                        except:
                            print('❌ Stok harus angka')

                    Status_New = 'TERSEDIA' if Stok_New > 0 else 'DIPINJAM'

                    DB_Perpus[i][1] = Judul_New
                    DB_Perpus[i][2] = Penulis_New
                    DB_Perpus[i][3] = Tahun_New
                    DB_Perpus[i][4] = Kategori_New
                    DB_Perpus[i][5] = Stok_New
                    DB_Perpus[i][6] = Status_New

                elif Pilihan == '2': # Update judul aja
                    DB_Perpus[i][1] = input('Masukkan judul baru: ').strip()

                elif Pilihan == '3': # Update nama penulis aja
                    DB_Perpus[i][2] = input('Masukkan nama penulis baru: ').strip()

                elif Pilihan == '4': # Update tahun terbit
                    while True:
                        try:
                            DB_Perpus[i][3] = int(input('Masukkan tahun terbit baru: ').strip())
                            break
                        except:
                            print('❌ Tahun harus angka')

                elif Pilihan == '5': # Update kategori
                    DB_Perpus[i][4] = input('Masukkan kategori baru: ').strip()

                elif Pilihan == '6': # Update jumlah stok
                    while True:
                        try:
                            Stok_New = int(input('Masukkan jumlah stok baru: ').strip())
                            if Stok_New < 0:
                                print('❌ Stok tidak boleh negatif')
                                continue

                            DB_Perpus[i][5] = Stok_New
                            DB_Perpus[i][6] = 'TERSEDIA' if Stok_New > 0 else 'DIPINJAM'
                            break
                        except:
                            print('❌ Stok harus angka')

                else:
                    print('❌ Pilihan tidak valid')
                    break

                print('✅ Data berhasil di-update!')
                print(Tabel_Buku([DB_Perpus[i]]))
                break  # keluar dari loop for karena buku sudah ketemu & diproses

        if not Ditemukan:
            print("❌ Buku dengan judul tersebut tidak ditemukan.")


    # Menu 4 hapus koleksi
    elif Menu == '4':
        while True:
            print('\nPilihan Menu Hapus Koleksi: ')
            print('1. Hapus koleksi buku')
            print('2. Lihat isi Keranjang Sampah')
            print('0. Kembali ke menu utama')

            Pilih = input('Pilih menu (0/1/2): ')

            if Pilih == '1':
                print(Tabel_Buku(DB_Perpus))

                Judul_Del = input('Masukkan judul buku yang ingin dihapus: ').strip().lower()

                Ditemukan = False
                for i in range(len(DB_Perpus)):
                    if DB_Perpus[i][1].strip().lower() == Judul_Del:
                        Ditemukan = True
                        print(Tabel_Buku([DB_Perpus[i]]))
                        Konfirmasi = input(f'Pindahkan {DB_Perpus[i][0]} - {DB_Perpus[i][1]} ke Keranjang Sampah? (Y/N): ').strip().lower()
                        if Konfirmasi == 'y':
                            Trash_Perpus.append(DB_Perpus.pop(i))
                            print('✅ Data berhasil dipindahkan ke Keranjang Sampah!')

                        else:
                            print('❌ Penghapusan data dibatalkan.')

                        break

                if not Ditemukan:
                    print('❌ Data tidak ditemukan')

            elif Pilih == '2':
                while True:
                    print('\nPilihan menu Keranjang Sampah:')
                    print('1. Lihat data Keranjang Sampah')
                    print('2. Restore koleksi')
                    print('3. Hapus permanen koleksi')
                    print('0. Kembali')

                    T = input('Masukkan pilihan menu (0-3): ')

                    if T == '1':
                        if not Trash_Perpus:
                            print("🗑️ Trash kosong")

                        else:
                            print(Tabel_Buku(Trash_Perpus))

                    elif T == '2':
                        if not Trash_Perpus:
                            print("🗑️ Trash kosong")
                            continue

                        print(Tabel_Buku(Trash_Perpus))
                        ID_R = input('\nMasukkan ID Buku: ').strip().upper()

                        Ditemukan = False
                        for j in range(len(Trash_Perpus)):
                            if Trash_Perpus[j][0] == ID_R:
                                DB_Perpus.append(Trash_Perpus.pop(j))
                                print('✅ Data berhasil di-restore!')
                                Ditemukan = True
                                break

                        if not Ditemukan:
                            print('❌ ID Buku tidak ditemukan')

                    elif T == '3':
                        if not Trash_Perpus:
                            print("🗑️ Trash kosong")
                            continue

                        print(Tabel_Buku(Trash_Perpus))
                        ID_D = input('\nMasukkan ID Buku: ').strip().upper()
                        Konfirmasi = input('Yakin ingin hapus permanen koleksi? (Y/N): ').strip().lower()

                        if Konfirmasi != 'y':
                            print('❌ Batal!')
                            continue

                        Ditemukan = False
                        for j in range(len(Trash_Perpus)):
                            if Trash_Perpus[j][0] == ID_D:
                                Trash_Perpus.pop(j)
                                print('✅ Dihapus permanen.')
                                Ditemukan = True
                                break

                        if not Ditemukan:
                            print('❌ ID Buku tidak ditemukan')

                    elif T == '0':
                        break

            elif Pilih == '0':
                break

            else:
                print('❌ Input yang Anda masukkan salah.')
                continue                  

    elif Menu == '5':
        while True:
            print('\nPilihan menu Pinjam Buku: ')
            print('1. Tambah buku ke Cart')
            print('2. Lihat Cart')
            print('3. Hapus buku dari Cart')
            print('4. Checkout')
            print('0. Kembali ke menu utama')

            Pilih = input('Masukkan pilihan (0-4): ').strip()

            # Tambah ke cart
            if Pilih == '1':
                if len(Cart_Peminjaman) >= 2:
                    print('❌ Maksimal pinjam 2 buku')
                    continue

                print('📚 Daftar buku: ')
                print(Tabel_Buku(DB_Perpus))

                ID_Buku = input('Masukkan ID Buku yang ingin dipinjam: ').strip().upper()

                idx = cari_index_buku_by_id(DB_Perpus, ID_Buku)
                if idx == -1:
                    print('❌ ID Buku tidak ditemukan')
                    continue

                # Cek stok buku
                if DB_Perpus[idx][5] <= 0:
                    print('❌ Stok buku kosong, tidak bisa dipinjam')
                    continue

                # Cek buku sudah ada di cart/belum
                if ID_Buku in Cart_Peminjaman:
                    print('❌ Buku ini sudah ada di cart')
                    continue

                Cart_Peminjaman.append(ID_Buku)
                print('✅ Buku berhasil ditambahkan ke Cart')
                tampil_cart(DB_Perpus, Cart_Peminjaman)

            # Lihat Cart
            elif Pilih == '2':
                tampil_cart(DB_Perpus, Cart_Peminjaman)

            # Hapus buku dari cart
            elif Pilih == '3':
                if not Cart_Peminjaman:
                    print('🛒 Cart kosong')
                    continue

                tampil_cart(DB_Perpus, Cart_Peminjaman)
                ID_Remove = input('Masukkan ID Buku yang mau dihapus dari cart: ').strip().upper()

                if ID_Remove in Cart_Peminjaman:
                    Cart_Peminjaman.remove(ID_Remove)
                    print('✅ Buku dihapus dari cart')
                else:
                    print('❌ ID tersebut tidak ada di cart')

                tampil_cart(DB_Perpus, Cart_Peminjaman)

            # Checkout
            elif Pilih == "4":
                if not Cart_Peminjaman:
                    print("🛒 Cart kosong. Tambahkan buku dulu.")
                    continue

                # tampilkan cart dulu
                Data_Cart = tampil_cart(DB_Perpus, Cart_Peminjaman)

                print("\n🛒 Isi Cart:")
                print(Tabel_Buku(Data_Cart))

                Nama_Peminjam = input("Nama peminjam: ").strip()
                if not Nama_Peminjam:
                    print("❌ Nama peminjam tidak boleh kosong.")
                    continue

                Konfirmasi = input("Konfirmasi pinjam semua buku di cart? (Y/N): ").strip().lower()
                if Konfirmasi != "y":
                    print("❌ Checkout dibatalkan.")
                    continue

                tgl_pinjam = date.today()
                tgl_jatuh_tempo = tgl_pinjam + timedelta(days=7)

                Buku_Dipinjam = []
                Data_Update = []

                # ✅ proses semua ID di cart (jangan clear cart di dalam loop)
                for ID_Buku in Cart_Peminjaman:
                    idx = cari_index_buku_by_id(DB_Perpus, ID_Buku)
                    if idx == -1:
                        continue

                    if DB_Perpus[idx][5] <= 0:
                        print(f"❌ Stok habis saat checkout untuk: {DB_Perpus[idx][0]} - {DB_Perpus[idx][1]}")
                        continue

                    DB_Perpus[idx][5] -= 1
                    DB_Perpus[idx][6] = "TERSEDIA" if DB_Perpus[idx][5] > 0 else "DIPINJAM"

                    Buku_Dipinjam.append(ID_Buku)
                    Data_Update.append(DB_Perpus[idx])

                if not Buku_Dipinjam:
                    print("❌ Tidak ada buku yang berhasil dipinjam (stok habis / data tidak valid).")
                    continue

                # simpan riwayat
                Riwayat_Pinjam.append({
                    "Nama": Nama_Peminjam,
                    "Tanggal Pinjam": str(tgl_pinjam),
                    "Jatuh Tempo": str(tgl_jatuh_tempo),
                    "Items": Buku_Dipinjam[:]  # copy biar aman
                })

                # kosongkan cart setelah semua diproses
                Cart_Peminjaman.clear()

                print("\n✅ Peminjaman berhasil!")
                print(f"Nama          : {Nama_Peminjam}")
                print(f"Tanggal Pinjam: {tgl_pinjam}")
                print(f"Jatuh Tempo   : {tgl_jatuh_tempo}")

                print("\n📌 Buku yang berhasil dipinjam (stok setelah update):")
                print(Tabel_Buku(Data_Update))

            elif Pilih == '0':
                break

            else:
                print('❌ Input tidak valid')

    elif Menu == '0':
        break

    else:
        print('❌ Input tidak valid')
