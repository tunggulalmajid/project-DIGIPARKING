import os
import csv
import termcolor

def clear():
    os.system("cls")
    
def garis(a,b=107):
    print (a*b)

def cover (b=107):
    garis("=",b)
    print ("")
    print("██████╗ ██╗ ██████╗ ██╗██████╗  █████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ ".center(b))
    print("██╔══██╗██║██╔════╝ ██║██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝ ".center(b))
    print("██║  ██║██║██║  ███╗██║██████╔╝███████║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗ ".center(b))
    print("██║  ██║██║██║   ██║██║██╔═══╝ ██╔══██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║ ".center(b))
    print("██████╔╝██║╚██████╔╝██║██║     ██║  ██║██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝ ".center(b))
    print ("")
    garis("=",b)

def enter (): 
    enter = input ("tekan [ENTER] untuk melanjutkan >> ") 

def exit():
    clear()
    cover()
    print ("\n")
    print ("Terima kasih telah menggunakan program ini\n\n".center(107))
    garis("=")

def halaman_awal (): 
    clear() 
    cover () 
    print ("""
                                            1. REGISTRASI
                                            2. LOGIN SEBAGAI USER
                                            3. LOGIN SEBAGAI JUKIR
                                            4. LOGIN SEBAGAI ADMIN
                                            5. EXIT 
""") 
    garis("=") 
    while True : 
        try : 
            pilih = int (input ("Pilih Opsi yang tersedia >> ")) 
            if pilih == 1 : 
                enter()
                clear() 
                registrasi() 
                break 
            elif pilih == 2 : 
                enter() 
                clear() 
                login_user () 
                break
            elif pilih == 3 :
                enter()
                clear() 
                login_jukir()
                break
            elif pilih == 4 :
                enter()
                clear() 
                login_admin()
                break
            elif pilih == 5 :
                exit()
                break
            else : 
                print ("Opsi yang anda pilih tidak tersedia") 
        except ValueError : 
            termcolor.cprint ("masukkan input dalam bentuk angka", "red") 
            enter() 
            halaman_awal () 
#___________________________________REGIST DAN LOGIN USER ____________________________________--
def penampung_user ():
    user = []
    nik = []
    tanggal_lahir = []
    nomor_hp = []
    list_username = [] 
    list_password = [] 
    with open ("dataadmin/datauser.csv", mode = "r") as file : 
        csv_reader = csv.reader(file) 
        for i in csv_reader:  
            user.append(i[0])  
            nik.append(i[1])  
            tanggal_lahir.append(i[2])  
            nomor_hp.append(i[3])  
            list_username.append(i[4])  
            list_password.append (i[5])
    return user,nik,tanggal_lahir,nomor_hp,list_username,list_password   


def registrasi (): 
    clear() 
    cover() 
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()

    while True : 
        nama = input ("masukkan nama lengkap anda >> ")
        nik = int (input ("masukkan NIK anda >>"))
        tanggal_lahir = input ("masukkan tanggal lahir anda (contoh : 02-02-2001)>>") 
        nomorhp = int (input ("Masukkan nomor HP >> ")) 
        while True : 
            try : 
                username = input ("buat username baru >> ")
                if username in list_username: 
                    raise ValueError ("Username sudah digunakan") 
                else : 
                    break 
            except ValueError as erorr:  
                termcolor.cprint (erorr, "red") 
        while True : 
            try : 
                password = input ("buat password baru >> ")
                if password == username or len(password) < 8 : 
                    raise ValueError ("Password harus lebih dari 8 karakter dan tidak sama dengan username") 
                else : 
                    break 
            except ValueError as error: 
                termcolor.cprint (error, "red") 

        while True : 
            try : 
                password2 = input ("konfirmasi password anda >> ") 
                if password2 != password : 
                    raise  ValueError ("password yang anda masukkan tidak sama") 
                else : 
                    break 
            except ValueError as error: 
                termcolor.cprint (error, "red") 
        garis("=") 
        with open ("dataadmin/datauser.csv", mode = "a", newline = "\n") as file : 
            border = ["nama lengkap", "nik","tanggal lahir", "nomor hp", "username", "password"] 
            writer = csv.DictWriter (file, fieldnames=border) 
            writer.writerow ( {"nama lengkap" : nama, "nik" :  nik,"tanggal lahir" : tanggal_lahir,"nomor hp" : nomorhp, "username" : username, "password" : password2} ) 
        termcolor.cprint ("registrasi berhasil, silahkan login", "green") 
        enter()
        halaman_awal() 
        
def login_user ():
    global nama_profil,nik_profil,tanggal_lahir_profil,nomor_hp_profil
    nama_profil = []
    nik_profil = []
    tanggal_lahir_profil = []
    nomor_hp_profil= []
    percobaan = 0
    while True:
        clear () 
        cover ()
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red") 
            enter()
            halaman_awal()
            break
        else:
            user,nik,tanggal_lahir,nomor_hp,list_username,list_password  = penampung_user() 
            username = input ("masukkan username anda >> ") 
            password = input ("masukkan password anda >> ") 
            garis("=")
            indikator = 0 
            for i in range (len(list_username)): 
                if username == list_username[i] and password == list_password[i] :
                    nama_profil.append(user[i])
                    nik_profil.append(nik[i])
                    tanggal_lahir_profil.append(tanggal_lahir[i])
                    nomor_hp_profil.append(nomor_hp[i])
                    indikator += 1 
            if indikator == 1 :  
                termcolor.cprint ("login berhasil", "green")
                if not os.path.exists(f"datauser/{nama_profil[0]}"): 
                    os.makedirs(f"datauser/{nama_profil[0]}")
                enter() 
                menu_user()
                break 
            else : 
                termcolor.cprint ("login tidak berhasil, silahkan masukkan username dan password yang benar", "red") 
                percobaan +=1
                enter () 
                continue
#___________________________LOGIN JUKIR_______________________________            
def penampung_jukir():
    nama_jukir = []
    nik_jukir = []
    telepon_jukir = []
    username_jukir = []
    password_jukir = []
    with open ("dataadmin/loginjukir.csv", mode = "r") as file :
        reader = csv.reader(file)
        for i in reader :
            nama_jukir.append(i[0])
            nik_jukir.append(i[1])
            telepon_jukir.append(i[2])
            username_jukir.append(i[3])
            password_jukir.append(i[4])
    return nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir

def login_jukir():
    percobaan = 0
    while True:
        clear()
        cover()
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red")
            enter()
            halaman_awal()
            break
        else : 
            
            username = input ("masukkan username anda >> ")
            password = input ("masukkan password anda >> ")
            garis("=")
            nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
            for i in range(len(username_jukir)):
                if username == username_jukir[i] and password == password_jukir[i]:
                    termcolor.cprint("LOGIN BERHASIL", "green")
                    enter()
                    menu_jukir()
                    break
                else :
                    termcolor.cprint ("login tidak berhasil, silahkan masukkan username dan password yang benar", "red") 
                    percobaan +=1
                    enter () 
                    continue

#_____________________________LOGIN ADMIN____________________________________
def login_admin():
    percobaan = 0
    while True:
        clear()
        cover()
        useradmin = []
        passadmin = []
        with open("dataadmin/loginadmin.csv", mode="r") as file:
            reader = csv.reader(file,delimiter=",")
            for i in reader:
                useradmin.append(i[0])
                passadmin.append(i[1])
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red")
            enter()
            halaman_awal()
            break
        else : 
            username = input ("masukkan username >> ")
            password = input ("masukkan password >> ")
            garis("=")
            for i in range(len(useradmin)):
                if username == useradmin[i] and password == passadmin[i] :
                    termcolor.cprint("LOGIN BERHASIL", "green")
                    enter()
                    menu_admin()
                    break
                else :
                    termcolor.cprint ("login tidak berhasil, silahkan masukkan username dan password yang benar", "red") 
                    percobaan +=1
                    enter () 
                    continue

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu_user():
    while True:
        clear()
        cover()
        print ("""
                                        1. PERATURAN DAN KETENTUAN
                                        2. CEK PROFIL
                                        3. DAFTARKAN KENDARAAN 
                                        4. BOOKING PARKIR 
                                        5. PENITIPAN BARANG
                                        6. RIWAYAT BOOKING 
                                        7. LOG OUT   
""")
        garis("=")
        try :
            pilih = int(input("masukkan pilihan >> "))
            if pilih == 1 : 
                enter()
                clear()
                peraturan_user ()
                break  
            elif pilih == 2 :
                enter ()
                clear()
                cek_profil_user() 
                break  
            elif pilih == 3 :
                enter()
                clear()
                daftarakan_kendaraan_user()
                break  
            elif pilih == 4 :  
                enter()
                clear()
                booking_parkir_user()           
                break
            elif pilih == 5 :
                enter()
                clear()
                penitipan_barang_user()        
                break
                 
            elif pilih == 6 :
                enter()
                clear()
                riwayat_booking_user()
                break 
            elif pilih == 7 :
                enter()
                clear()
                halaman_awal()
                break
            else :
                raise ValueError ("Opsi Tidak Tersedia")
        except ValueError as error :
            termcolor.cprint (error, "red")
            enter ()
            continue
def peraturan_user ():
    pass
def cek_profil_user ():
    clear()
    cover()
    print (F"""
                                        NAMA            :   {nama_profil[0]}
                                        NIK             :   {nik_profil[0]}
                                        TANGGAL LAHIR   :   {tanggal_lahir_profil[0]} 
                                        NO TELEPON      :   {nomor_hp_profil[0]}

""")
    garis("=")
    enter ()
    clear()
    menu_user()
#__________________________________________________________________Kendaraan
def daftarakan_kendaraan_user():
    clear()
    cover(b=128)
    print ("\n")
    print ("MOBIL TERDAFTAR\n\n".center(128))
    penampil_mobil()
    print ("\n")
    print ("MOTOR TERDAFTAR\n\n".center(128))
    penampil_motor()
    print ("")
    garis("=", b =128)
    print ("""
        1. TAMBAH KENDARAAN
        2. HAPUS KENDARAAN
        3. KEMBALI KE MENU  
""")
    
    garis("=", b =128)
    pilih = int (input("\tsilahkan masukkan pilihan >> : "))
    if pilih == 1 :
        enter()
        tambah_kendaraan()
    elif pilih == 2 :
        enter()
        print ("""
    1. HAPUS MOBIL
    2. HAPUS MOTOR
""")
        mana = int(input ("\thapus yang mana 1/2 >> "))
        if mana == 1:
            enter()
            clear()
            hapus_mobil()
        elif mana == 2 :
            enter()
            clear()
            hapus_motor()
    elif pilih == 3 :
        enter()
        clear()
        menu_user()
#_______________________________________ MOBIL__________________________________    
def penampung_mobil():
    atas_nama =[]
    jenis_kendaraan = []
    plat_nomor = []
    tipe_kendaraan = []
    tahun_kendaraan = []
    warna_kendaraan = []
    # with open (f"datauser/{nama_profil[0]}/mobil.csv", mode="r") as file :
    with open (f"datauser/ahmad/mobil.csv", mode="r") as file :
        reader = csv.reader(file)
        for i in reader:
            atas_nama.append(i[0])
            jenis_kendaraan.append(i[1])
            plat_nomor.append(i[2])
            tipe_kendaraan.append(i[3])
            tahun_kendaraan.append(i[4])
            warna_kendaraan.append(i[5])
    return atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan

def penampil_mobil():
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_mobil()
    border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
    garis("=",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("=",b=128)
    for i in range (len(jenis_kendaraan)):
        print (f"|{i+1:^3} |{atas_nama[i]:^25}|{jenis_kendaraan[i]:^17}|{plat_nomor[i]:^15}|{tipe_kendaraan[i]:^25}|{tahun_kendaraan[i]:^17}|{warna_kendaraan[i]:^17}|")
        garis("=",b=128)

def hapus_mobil():
    clear()
    cover(b=128)
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_mobil()
    print("")
    print("HAPUS MOBIL\n".center(128))
    penampil_mobil()
    garis("=",b=128)
    pilih = (int(input("Masukkan nomor mobil yang ingin dihapus : ")) - 1)
    border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
    garis("=",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("=",b=128)
    print (f"|{pilih + 1:^3} |{atas_nama[]:^25}|{jenis_kendaraan[i]:^17}|{plat_nomor[i]:^15}|{tipe_kendaraan[i]:^25}|{tahun_kendaraan[i]:^17}|{warna_kendaraan[i]:^17}|")
    garis("=",b=128)
    
    

#__________________________________________________MOTOR_____________________________________________________
def penampung_motor():
    atas_nama =[]
    jenis_kendaraan = []
    plat_nomor = []
    tipe_kendaraan = []
    tahun_kendaraan = []
    warna_kendaraan = []
    with open (f"datauser/{nama_profil[0]}/motor.csv", mode="r") as file :
        reader = csv.reader(file)
        for i in reader:
            atas_nama.append(i[0])
            jenis_kendaraan.append(i[1])
            plat_nomor.append(i[2])
            tipe_kendaraan.append(i[3])
            tahun_kendaraan.append(i[4])
            warna_kendaraan.append(i[5])
    return atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan
def penampil_motor():
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_motor()
    border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
    garis("=",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("=",b=128)
    for i in range (len(jenis_kendaraan)):
        print (f"|{i+1:^3} |{atas_nama[i]:^25}|{jenis_kendaraan[i]:^17}|{plat_nomor[i]:^15}|{tipe_kendaraan[i]:^25}|{tahun_kendaraan[i]:^17}|{warna_kendaraan[i]:^17}|")
        garis("=",b=128)
def hapus_motor():
    pass 

def tambah_kendaraan():
    clear()
    cover()
    print ("\n")
    print ("TAMBAH KENDARAAN\n\n".center(107))
    garis("=")
    jenis_kendaraan = input("masukkan jenis kendaraan (mobil/motor) >> ").lower()
    plat_nomor = input ("masukkan plat nomor kendaraan (P 1234 VV) >> ")
    tipe_kendaraan = input ("masukkan tipe kendaraan (Toyota Avanza / Honda Vario) >> ")
    tahun_kendaraan = input ("masukkan tahun kendaraan (2020) >> ")
    warna_kendaraan = input ("masukkan warna kendaraan (merah/abu-abu) >> ")
    garis("=")
    if not os.path.exists(f"datauser/{nama_profil[0]}") :
        os.makedirs(f"datauser/{nama_profil[0]}")
    with open (f"datauser/{nama_profil[0]}/{jenis_kendaraan}.csv", mode="a", newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow([nama_profil[0],jenis_kendaraan,plat_nomor, tipe_kendaraan, tahun_kendaraan, warna_kendaraan])
    termcolor.cprint("kendaraan berhasil di inputkan")
    enter()
    daftarakan_kendaraan_user()


def booking_parkir_user():
    pass
    """
    user diberi pilihan mobil atau motor
    user diberi ketersediaan parkir selama seminggu kedepan, hanya blok parkir
    A = Mobil
    B = Motor
    User memilih tanggal dan blok parkir
    user memilih kendaraan mana yang di bookingkan
    user memilih parkir kurang dari 5 jam atau lebih, jika lebih masuk parkir harian
    jika harian maka berapa hari 
    jika sudah maka booking sudah terdaftar dan dilanjut ke pembayaran
    """
def penitipan_barang_user():
    pass
def riwayat_booking_user():
    pass

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> JUKIR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu_jukir():
    while True :
        clear()
        cover()
        print ("""
                                        1. CEK PROFIL
                                        2. ABSENSI
                                        3. CEK KETERSEDIAAN PARKIR
                                        4. CEK BOOKING PARKIR
                                        5. CEK PENITIPAN BARANG
                                        6. LOG OUT
""")
        try :
            pilih = int (input("Masukkan pilihan >> "))
            if pilih == 1 :
                enter()
                cek_profil_jukir()
                break
            elif pilih == 2 :
                enter ()
                absensi_jukir()
                break
            elif pilih == 3 :
                enter ()
                cek_parkir_tersedia_jukir()
                break
            elif pilih == 4 :
                enter ()
                cek_booking_parkir_jukir()
                break
            elif pilih == 5 :
                enter ()
                cek_penitipan_barang_jukir()
                break
            elif pilih == 6 :
                enter()
                halaman_awal()
                break
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue

def cek_profil_jukir():
    pass
def absensi_jukir():
    pass
def cek_parkir_tersedia_jukir():
    pass
def cek_booking_parkir_jukir():
    pass
def cek_penitipan_barang_jukir():
    pass
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADMIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu_admin():
    while True :
        clear()
        cover()
        print ("""
                                        1. TAMBAH PENGUMUMAN ATAU PERATURAN
                                        2. MONITORING USER 
                                        3. MONITORING JURU PARKIR
                                        4. MONITORING KENDARAAN USER
                                        5. MONITORING KETERSEDIAAN PARKIR   
                                        6. MONITORING BOOKING PARKIR
                                        7. MONITORING PENITIPAN BARANG
                                        8. LOG OUT
            
""")
        garis ("=")
        try :
            pilih = int (input("Masukkan pilihan >> "))
            if pilih == 1 :
                enter()
                tambah_peraturan()
                break
            elif pilih == 2 :
                enter()
                monitoring_user()
                break
            elif pilih == 3 :
                pass
            elif pilih == 4 :
                pass
            elif pilih == 5 :
                pass
            elif pilih == 6 :
                pass
            elif pilih == 7 :
                pass
            elif pilih == 8 :
                enter()
                halaman_awal()
                break
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue

def tambah_peraturan():
    pass

#_________________MONITORING USER________________________
def penampil_user():
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    border = ["NO","NAMA", "NIK", "TANGGAL LAHIR", "NOMOR HP", "USERNAME", "PASSWORD"]
    garis("=",b=117)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
    garis("=",b=117)
    for i in range (len(user)):
        print (f"|{i + 1:^4}|{user[i]:^20}|{nik[i]:^17}|{tanggal_lahir[i]:^17}|{nomor_hp[i]:^17}|{list_username[i]:^17}|{list_password[i]:^17}|")
        garis("=",b=117)
    garis("=",b=117)

def monitoring_user():
    while True :
        clear()
        cover(b=117)
        print ("\n")
        print ("MONITORING USER\n\n".center(117))
        penampil_user()
        print ("""
                                                1. TAMBAH DATA USER
                                                2. UPDATE DATA USER
                                                3. HAPUS DATA USER
                                                4. KEMBALI KE MENU
""")
        garis("=",b=117)
        try :
            pilih = int(input ("Masukkan pilihan >> "))
            if pilih == 1 :
                enter()
                clear()
                tambah_user()
                break
            elif pilih == 2 :
                enter()
                clear()
                update_user()
                break
            elif pilih == 3 :
                enter()
                clear()
                hapus_user()
                break
            elif pilih == 4 :
                enter()
                clear()
                menu_admin()
                break
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            continue

def tambah_user():
    clear()
    cover()
    print ("\n")
    print ("TAMBAH USER\n\n".center(107)) 
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    garis("=")
    nama = input ("masukkan nama lengkap User >> ")
    nik = int (input ("masukkan NIK User >>"))
    tanggal_lahir = input ("masukkan tanggal lahir User (contoh : 02-02-2001)>>") 
    nomorhp = int (input ("Masukkan nomor HP User >> ")) 
    while True : 
        try : 
            username = input ("buat username User >> ")
            if username in list_username: 
                raise ValueError ("Username sudah digunakan") 
            else : 
                break 
        except ValueError as erorr:  
            termcolor.cprint (erorr, "red") 
    while True : 
        try : 
            password = input ("buat password User >> ")
            if password == username or len(password) < 8 : 
                raise ValueError ("Password harus lebih dari 8 karakter dan tidak sama dengan username") 
            else : 
                break 
        except ValueError as error: 
            termcolor.cprint (error, "red") 

    while True : 
        try : 
            password2 = input ("konfirmasi password User >> ") 
            if password2 != password : 
                raise  ValueError ("password yang anda masukkan tidak sama") 
            else : 
                break 
        except ValueError as error: 
            termcolor.cprint (error, "red") 
    garis("=") 
    with open ("dataadmin/datauser.csv", mode = "a", newline = "\n") as file : 
        border = ["nama lengkap", "nik","tanggal lahir", "nomor hp", "username", "password"] 
        writer = csv.DictWriter (file, fieldnames=border) 
        writer.writerow ( {"nama lengkap" : nama, "nik" :  nik,"tanggal lahir" : tanggal_lahir,"nomor hp" : nomorhp, "username" : username, "password" : password2} ) 
    termcolor.cprint ("User berhasil ditambahkan", "green") 
    enter()
    clear()
    monitoring_user()

def update_user():
    clear()
    cover(b=117)
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    while True :
        penampil_user()
        pilih = (int (input("masukkan nomor user yang ingin diupdate >>")) - 1)
        border = ["NO","NAMA", "NIK", "TANGGAL LAHIR", "NOMOR HP", "USERNAME", "PASSWORD"]
        while True :
            clear()
            cover(b=117)
            garis("=",b=117)
            print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
            garis("=",b=117)
            print (f"|{pilih + 1:^4}|{user[pilih]:^20}|{nik[pilih]:^17}|{tanggal_lahir[pilih]:^17}|{nomor_hp[pilih]:^17}|{list_username[pilih]:^17}|{list_password[pilih]:^17}|")
            garis("=",b=117)
            try :
                bagian = input("bagian mana yang ingin diganti (nama / nik / tanggal / nomor / username / password) >> ").lower()
                if bagian == "nama":
                    pengganti = input("masukkan kata sebagai pengganti >> ")
                    user[pilih] = pengganti
                    break            
                elif bagian == "nik":
                    pengganti = int(input("masukkan kata sebagai pengganti >> "))
                    nik[pilih] = pengganti
                    break            
                elif bagian == "tanggal":
                    pengganti = input("masukkan kata sebagai pengganti >> ")
                    tanggal_lahir[pilih] = pengganti
                    break            
                elif bagian == "nomor":
                    pengganti = int(input("masukkan kata sebagai pengganti >> "))
                    tanggal_lahir[pilih] = pengganti
                    break            
                elif bagian == "username":
                    pengganti = input("masukkan kata sebagai pengganti >> ")
                    list_username[pilih] = pengganti
                    break            
                elif bagian == "password":
                    pengganti = input("masukkan kata sebagai pengganti >> ")
                    list_password[pilih] = pengganti
                    break            
                else :
                    raise ValueError("bagian yang anda maksid tidak ditemukan")
            except ValueError as error :
                termcolor.cprint(error, "red")
                enter()
                continue
        with open ("dataadmin/datauser.csv", mode = "w", newline = "\n") as file:
            writer = csv.writer(file)
            for i in range (len(user)):
                writer.writerow ([user[i], nik[i], tanggal_lahir[i],nomor_hp[i],list_username[i],list_password[i]])
        clear()
        cover(b=117)
        garis("=",b=117)
        print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
        garis("=",b=117)
        print (f"|{pilih + 1:^4}|{user[pilih]:^20}|{nik[pilih]:^17}|{tanggal_lahir[pilih]:^17}|{nomor_hp[pilih]:^17}|{list_username[pilih]:^17}|{list_password[pilih]:^17}|")
        garis("=",b=117)
        indikator = 0
        while True :         
            try :
                pilih = input("apakah ingin mengubah lagi ? y/n >> ").lower()
                if pilih == "y":
                    indikator +=0
                    break
                elif pilih == "n":
                    indikator +=1
                    break
                else :
                    raise ValueError("inputan yang anda masukkan tidak valid")
            except ValueError as error :
                termcolor.cprint(error, "red")
        if indikator == 1 :
            enter()
            clear()
            monitoring_user()
            break
        else :
            clear()
            continue
    
def hapus_user():
    clear()
    cover(b = 117) 
    border = ["NO","NAMA", "NIK", "TANGGAL LAHIR", "NOMOR HP", "USERNAME", "PASSWORD"]
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    print ("\n")
    print ("HAPUS USER\n\n".center(107))
    penampil_user()
    pilih = (int (input ("masukkan nomer user yang ingin dihapus >> ")) - 1)
    clear()
    cover(b=117)
    garis("=",b=117)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
    garis("=",b=117)
    print (f"|{pilih + 1:^4}|{user[pilih]:^20}|{nik[pilih]:^17}|{tanggal_lahir[pilih]:^17}|{nomor_hp[pilih]:^17}|{list_username[pilih]:^17}|{list_password[pilih]:^17}|")
    garis("=",b=117)
    yakin = input ("apakah yakin ingin menghapus user ? y/n >> ").lower()
    if yakin == "y" :
        user.pop(pilih )
        nik.pop(pilih)
        tanggal_lahir.pop(pilih)
        nomor_hp.pop(pilih)
        list_username.pop(pilih)
        list_password.pop(pilih)
        with open ("dataadmin/datauser.csv", mode = "w", newline = "\n") as file:
            writer = csv.writer(file)
            for i in range (len(user)):
                writer.writerow ([user[i], nik[i], tanggal_lahir[i],nomor_hp[i],list_username[i],list_password[i]])
        enter()
        clear()
        monitoring_user()
    else :
        enter()
        clear()
        monitoring_user()
#_________________MONITORING JUKIR________________________
def penampil_jukir():
    pass
def monitoring_jukir():
    pass

def tambah_jukir ():
    clear()
    cover()
    nama = input ("masukkan nama jukir >> ")
    nik = input ("masukkan nik >> ")
    telpon = int (input ("masukkan nomor telpon >> "))
    username = input ("buat username jukir >> ")
    password = input ("buat password jukir >> ")
    garis("=")
    with open("dataadmin/loginjukir.csv", mode="a", newline="\n") as file:
        border = ["nama", "nik", "nomor telepon", "username", "password"]
        writer = csv.DictWriter(file, fieldnames=border)
        writer.writerow({"nama" : nama, "nik" : nik, "nomor telepon": telpon,"username":username, "password":password})
    termcolor.cprint("jukir berhasil ditambahkan", "green")
    enter()
    menu_admin()

def monitoring_kendaraan_user():
    pass
def monitoring_ketersediaan_parkir():
    pass
def monitoring_booking_parkir():
    pass
def monitoring_penitipan_barang():
    pass




if __name__ == "__main__":
    login_user()
    # penampil_mobil()
    # halaman_awal()
    # menu_admin()
    # menu_user()
    # monitoring_user()
    # penampil_user()
    # print (a)