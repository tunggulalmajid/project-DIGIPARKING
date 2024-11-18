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
                registrasi() 
                break 
            elif pilih == 2 : 
                enter() 
                login_user () 
                break
            elif pilih == 3 :
                enter()
                login_jukir()
                break
            elif pilih == 4 :
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
    global nama,nik,tanggal_lahir,nomor_hp
    nama = []
    nik = []
    tanggal_lahir = []
    nomor_hp = []
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
                if username in list_username[i] and password in list_password[i] :
                    nama.append(user[i])
                    nik.append(nik[i])
                    tanggal_lahir.append(tanggal_lahir[i])
                    nomor_hp.append(nomor_hp[i])
                    indikator += 1 
            if indikator == 1 :  
                termcolor.cprint ("login berhasil", "green") 
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
                peraturan_user ()
                break  
            elif pilih == 2 :
                enter ()
                cek_profil_user() 
                break  
            elif pilih == 3 :
                enter()
                daftarakan_kendaraan_user()
                break  
            elif pilih == 4 :  
                enter()
                booking_parkir_user()           
                break
            elif pilih == 5 :
                enter()
                penitipan_barang_user()        
                break
                 
            elif pilih == 6 :
                enter()
                riwayat_booking_user()
                break 
            elif pilih == 7 :
                enter()
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
                                        NAMA            :   {nama[0]}
                                        NIK             :   {nik[0]}
                                        TANGGAL LAHIR   :   {tanggal_lahir[0]} 
                                        NO TELEPON      :   {nomor_hp[0]}

""")
    garis("=")
    enter ()
    menu_user()

def daftarakan_kendaraan_user():
    pass
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
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    pilih = (int (input("masukkan nomor user yang ingin diupdate >>")) - 1)
    clear()
    border = ["NO","NAMA", "NIK", "TANGGAL LAHIR", "NOMOR HP", "USERNAME", "PASSWORD"]
    while True :
        while True :
            clear()
            cover(b=117)
            garis("=",b=117)
            print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
            garis("=",b=117)
            print (f"|{pilih + 1:^4}|{user[pilih]:^20}|{nik[pilih]:^17}|{tanggal_lahir[pilih]:^17}|{nomor_hp[pilih]:^17}|{list_username[pilih]:^17}|{list_password[pilih]:^17}|")
            garis("=",b=117)
            try :
                bagian = input("bagian mana yang ingin diganti >> ").lower()
                pengganti = input("masukkan kata sebagai pengganti >> ")
                if bagian == "nama":
                    user[pilih] = pengganti
                    break            
                elif bagian == "nik":
                    nik[pilih] = pengganti
                    print ("k")
                    break            
                elif bagian == "tanggal":
                    tanggal_lahir[pilih] = pengganti
                    print ("j")
                    break            
                elif bagian == "nomor":
                    tanggal_lahir[pilih] = pengganti
                    print ("l")
                    break            
                elif bagian == "username":
                    list_username[pilih] = pengganti
                    print ("m")
                    break            
                elif bagian == "password":
                    list_password[pilih] = pengganti
                    print ("n")
                    break            
                else :
                    raise ValueError("bagian yang anda maksid tidak ditemukan")
            except ValueError as error :
                termcolor.cprint(error, "red")
                enter()
                continue
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
            continue

            
       
    
    

    # user[pilih] = f"{ganti}"
    # """
    # hapus tidak hanya satu variabel
    # """
    # with open ("dataadmin/datauser.csv", mode = "w", newline = "\n") as file:
    #     writer = csv.writer(file)
    #     for i in range (len(user)):
    #         writer.writerow ([user[i], nik[i], tanggal_lahir[i],nomor_hp[i],list_username[i],list_password[i]])
    
def hapus_user(): 
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    pilih = int (input ("masukkan nomer user yang ingin dihapus >> "))
    user.pop(pilih - 1)
    nik.pop(pilih - 1)
    tanggal_lahir.pop(pilih - 1)
    nomor_hp.pop(pilih - 1)
    list_username.pop(pilih - 1)
    list_password.pop(pilih - 1)
    with open ("dataadmin/datauser.csv", mode = "w", newline = "\n") as file:
        writer = csv.writer(file)
        for i in range (len(user)):
            writer.writerow ([user[i], nik[i], tanggal_lahir[i],nomor_hp[i],list_username[i],list_password[i]])
    enter()
    clear()
    monitoring_user()
#_________________MONITORING JUKIR________________________
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
    # halaman_awal()
    # menu_admin()
    # menu_user()
    monitoring_user()