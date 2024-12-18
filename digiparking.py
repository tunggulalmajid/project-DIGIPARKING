import os
import csv
import termcolor
import datetime as dt
import time
import shutil

def clear():
    os.system("cls")
    
def garis(a,b=107):
    print (a*b)

def cover (b=107):
    garis("═",b)
    print ("")
    print ("██████╗ ██╗ ██████╗ ██╗██████╗  █████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ ".center(b),)
    print ("██╔══██╗██║██╔════╝ ██║██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝ ".center(b),)
    print ("██║  ██║██║██║  ███╗██║██████╔╝███████║██████╔╝█████╔╝ ██║██╔██╗ ██║██║  ███╗".center(b),)
    print ("██║  ██║██║██║   ██║██║██╔═══╝ ██╔══██║██╔══██╗██╔═██╗ ██║██║╚██╗██║██║   ██║".center(b),)
    print ("██████╔╝██║╚██████╔╝██║██║     ██║  ██║██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝".center(b))
    print ("╚═════╝ ╚═╝ ╚═════╝ ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ".center(b))    
    print ("")
    garis("═",b)

def enter (a=""): 
    enter = input (f"{a}tekan [ENTER] untuk melanjutkan >> ") 

def transisi(b=107):
    print ("═"*b)
    print ("")
    print ("LOADING.\n".center(b))
    print ("═"*b)
    time.sleep(0.5)
    clear()
    print ("═"*b)
    print ("")
    print ("LOADING..\n".center(b))
    print ("═"*b)
    time.sleep(0.5)
    clear()
    print ("═"*b)
    print ("")
    print ("LOADING...\n".center(b))
    print ("═"*b)
    time.sleep(0.5)

def exit():
    clear()
    cover()
    print ("\n")
    print ("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI\n\n".center(107))
    garis("═")
    enter()
    clear()

def halaman_awal (): 
    clear() 
    cover () 
    print ("""
                                            1. REGISTRASI USER
                                            2. LOGIN SEBAGAI USER
                                            3. LOGIN SEBAGAI JUKIR
                                            4. LOGIN SEBAGAI ADMIN
                                            5. EXIT 
""") 
    garis("═") 
    while True : 
        try : 
            pilih = int (input ("Pilih Opsi yang tersedia >> ")) 
            if pilih == 1 : 
                enter()
                clear() 
                transisi()
                registrasi() 
                break 
            elif pilih == 2 : 
                enter() 
                clear()
                transisi() 
                login_user () 
                break
            elif pilih == 3 :
                enter()
                clear() 
                transisi()
                login_jukir()
                break
            elif pilih == 4 :
                enter()
                clear() 
                transisi()
                login_admin()
                break
            elif pilih == 5 :
                enter()
                clear()
                transisi()
                exit()
                break
            else : 
                raise ValueError ("Opsi yang anda pilih tidak tersedia") 
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
    print("")
    print("REGISTRASI USER\n".center(107))
    garis("═")
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    while True :
        try:
            nama = input ("masukkan nama lengkap anda >> ")
            if len(nama) < 4 :
                raise ValueError ("nama minimal terdiri dari 4 karakter")
            elif nama in user :
                raise ValueError ("nama yang anda pilih sudah digunakan")
            else : 
                break
        except ValueError as error :
            termcolor.cprint (error, "red")
            enter()
            continue
    while True : 
        try : 
            nik = int(input ("masukkan NIK anda >>"))
            nik = str(nik)
            if len (nik) < 6 or len (nik) > 10  :
                raise ValueError ("nik harus terdiri dari minimal 6 dan maksimal 10 karatkter")
            else :
                break
        except ValueError as erorr:  
            termcolor.cprint (erorr, "red")
            enter()
            continue 
    while True : 
        try : 
            tanggal_lahir = input ("masukkan tanggal lahir anda (contoh : 02-02-2001) >>")
            tanggal_lahir = dt.datetime.strptime(tanggal_lahir, "%d-%m-%Y")
            if tanggal_lahir.year < 1920 or tanggal_lahir.year > 2007 :
                raise ValueError ("tanggal lahir harus berada di antara tahun 1920 dan 2007")
            tanggal_lahir = tanggal_lahir.strftime("%d-%m-%Y") 
            break
        except ValueError as erorr:  
            termcolor.cprint (erorr, "red")
            enter()
            continue 

    while True : 
        try : 
            nomorhp =  int(input ("Masukkan nomor HP (8123456789) >> "))
            nomorhp = str(nomorhp)
            if len (nomorhp) < 10:
                raise ValueError ("nomor HP minimal 10  ") 
            elif len (nomorhp) > 12:
                raise ValueError ("nomor HP minimal 10  ") 
            else :
                nomorhp = "+62" + nomorhp
                break 
        except ValueError as erorr:  
            termcolor.cprint (erorr, "red")
            enter()
            continue 
    while True : 
        try : 
            username = input ("buat username baru >> ")
            if len (username) < 4 :
                raise ValueError ("username harus lebih dari sama dengan 4 karakter")
            elif username in list_username: 
                raise ValueError ("Username sudah digunakan") 
            else : 
                break 
        except ValueError as erorr:  
            termcolor.cprint (erorr, "red")
            enter()
            continue 
    while True : 
        try : 
            password = input ("buat password baru >> ")
            if password == username or len(password) < 8 : 
                raise ValueError ("Password harus lebih dari 8 karakter dan tidak sama dengan username") 
            else : 
                break 
        except ValueError as error: 
            termcolor.cprint (error, "red") 
            enter()
            continue
    while True : 
        try : 
            password2 = input ("konfirmasi password anda >> ") 
            if password2 != password : 
                raise  ValueError ("password yang anda masukkan tidak sama") 
            else : 
                break 
        except ValueError as error: 
            termcolor.cprint (error, "red") 
            enter()
            continue
    garis("═") 
    with open ("dataadmin/datauser.csv", mode = "a", newline = "\n") as file : 
        border = ["nama lengkap", "nik","tanggal lahir", "nomor hp", "username", "password"] 
        writer = csv.DictWriter (file, fieldnames=border) 
        writer.writerow ( {"nama lengkap" : nama, "nik" :  nik,"tanggal lahir" : tanggal_lahir,"nomor hp" : nomorhp, "username" : username, "password" : password2} ) 
    os.makedirs(f"datauser/{nama}")
    with open (f"datauser/{nama}/mobil.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/motor.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/riwayat_titip_barang.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/titipbarang.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/booking.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/parkir.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/riwayat_parkir_user.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    termcolor.cprint ("registrasi berhasil, silahkan login", "green")
    enter()
    clear()
    transisi()
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
        print("")
        print("LOGIN USER\n".center(107))
        garis("═")
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red") 
            enter()
            clear()
            transisi()
            halaman_awal()
            break
        else:
            user,nik,tanggal_lahir,nomor_hp,list_username,list_password  = penampung_user() 
            username = input ("masukkan username anda >> ") 
            password = input ("masukkan password anda >> ") 
            garis("═")
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
                enter()
                clear() 
                transisi()
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
    global nama_jukir_profil,nik_jukir_profil,telepon_jukir_profil,username_pasword_jukir_profil
    nama_jukir_profil = []
    nik_jukir_profil = []
    telepon_jukir_profil = []
    username_pasword_jukir_profil = []
    percobaan = 0
    while True:
        clear()
        cover()
        print("")
        print("LOGIN JUKIR\n".center(107))
        garis("═")
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red")
            enter()
            clear()
            transisi()
            halaman_awal()
            break
        else : 
            username = input ("masukkan username anda >> ")
            password = input ("masukkan password anda >> ")
            garis("═")
            login = 0
            nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
            for i in range(len(username_jukir)):
                if username == username_jukir[i] and password == password_jukir[i]:
                    nama_jukir_profil.append(nama_jukir[i])
                    nik_jukir_profil.append(nik_jukir[i]) 
                    telepon_jukir_profil.append(telepon_jukir[i]) 
                    username_pasword_jukir_profil.append([username,password])
                    login +=1
                    break
                else :
                    continue
            if login == 1 :     
                termcolor.cprint("LOGIN BERHASIL", "green")
                enter()
                clear()
                transisi()
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
        print("")
        print("LOGIN ADMIN\n".center(107))
        garis("═")
        useradmin = []
        passadmin = []
        with open("dataadmin/loginadmin.csv", mode="r") as file:
            reader = csv.reader(file)
            for i in reader:
                useradmin.append(i[0])
                passadmin.append(i[1])
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red")
            enter()
            clear()
            transisi()
            halaman_awal()
            break
        else : 
            username = input ("masukkan username >> ")
            password = input ("masukkan password >> ")
            garis("═")
            for i in range(len(useradmin)):
                if username == useradmin[i] and password == passadmin[i] :
                    termcolor.cprint("LOGIN BERHASIL", "green")
                    enter()
                    clear()
                    transisi()
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
                                        1. KETENTUAN DIGIPARKING
                                        2. CEK PROFIL
                                        3. DAFTARKAN KENDARAAN 
                                        4. PARKIR 
                                        5. PENITIPAN BARANG 
                                        6. LOG OUT   
""")
        garis("═")
        try :
            pilih = int(input("masukkan pilihan >> "))
            if pilih == 1 : 
                enter()
                clear()
                transisi()
                ketentuan_digiparking ()
                break  
            elif pilih == 2 :
                enter ()
                clear()
                transisi()
                cek_profil_user() 
                break  
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                daftarakan_kendaraan()
                break  
            elif pilih == 4 :  
                enter()
                clear()
                transisi()
                parkir_user()           
                break
            elif pilih == 5 :
                enter()
                clear()
                transisi()
                penitipan_barang_user()        
                break
            elif pilih == 6 :
                enter()
                clear()
                transisi()
                halaman_awal()
                break
            else :
                raise ValueError ("Opsi Tidak Tersedia")
        except ValueError as error :
            termcolor.cprint (error, "red")
            enter () 
            continue

def ketentuan_digiparking ():
    clear()
    cover()
    penampil_peraturan()
    enter()
    clear()
    transisi()
    menu_user()
    
def cek_profil_user ():
    clear()
    cover()
    print (F"""
                                        NAMA            :   {nama_profil[0]}
                                        NIK             :   {nik_profil[0]}
                                        TANGGAL LAHIR   :   {tanggal_lahir_profil[0]} 
                                        NO TELEPON      :   {nomor_hp_profil[0]}

""")
    garis("═")
    enter ()
    clear()
    transisi()
    menu_user()
#__________________________________________________________________Kendaraan_____________________________________________________
def daftarakan_kendaraan():
    clear()
    cover(b=128)
    print ("\n")
    print ("MOBIL TERDAFTAR\n\n".center(128))
    penampil_mobil()
    print ("\n")
    print ("MOTOR TERDAFTAR\n\n".center(128))
    penampil_motor()
    print ("")
    garis("═", b =128)
    print ("""
        1. TAMBAH KENDARAAN
        2. HAPUS KENDARAAN
        3. KEMBALI KE MENU  
""")
    
    garis("═", b =128)
    while True :
        try :
            pilih = int (input("silahkan masukkan pilihan >> : "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                tambah_kendaraan()
            elif pilih == 2 :
                enter()
                garis("═", b =128)
                print ("""
        1. HAPUS MOBIL
        2. HAPUS MOTOR
""")
                garis("═", b =128)
                mana = int(input ("hapus yang mana 1/2 >> "))
                if mana == 1:
                    enter()
                    clear()
                    transisi()
                    hapus_mobil()
                elif mana == 2 :
                    enter()
                    clear()
                    transisi()
                    hapus_motor()
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                menu_user()
            else :
                raise ValueError("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue

def tambah_kendaraan():
    clear()
    cover()
    print ("\n")
    print ("TAMBAH KENDARAAN\n\n".center(107))
    garis("═")
    print ("""
    1. TAMBAH MOBIL
    2. TAMBAH MOTOR
    3. KEMBALI 
""")
    garis("═")
    while True :
        try :
            pilih = int(input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                jenis_kendaraan = "mobil"
                break
            elif pilih == 2 :
                jenis_kendaraan = "motor"
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                daftarakan_kendaraan()
                break
            else :
                raise ValueError("opsi yang dipilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    while True :
        try:
            plat_nomor = input ("masukkan plat nomor kendaraan (P 1234 VV) >> ").upper()
            if len(plat_nomor) < 7:
                raise ValueError ("plat nomor tidak valid")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    while True :
        try:
            tipe_kendaraan = input ("masukkan tipe kendaraan (Toyota Avanza / Honda Vario) >> ")
            if len (tipe_kendaraan) < 4 :
                raise ValueError ("tipe kendaraan tidak valid")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    while True :
        try:
            tahun_kendaraan = int(input ("masukkan tahun kendaraan (2020) >> "))
            if tahun_kendaraan > 2024 or tahun_kendaraan <= 1980 :
                raise ValueError ("tahun kendaraan tidak valid")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    while True :
        try:
            warna_kendaraan = input ("masukkan warna kendaraan (merah/abu-abu) >> ")
            if len(warna_kendaraan) < 3:
                raise ValueError ("warna kendaraan tidak valid")
            else:
                break
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    garis("═")
    with open (f"datauser/{nama_profil[0]}/{jenis_kendaraan}.csv", mode="a", newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow([nama_profil[0],jenis_kendaraan,plat_nomor, tipe_kendaraan, tahun_kendaraan, warna_kendaraan])
    termcolor.cprint("kendaraan berhasil di inputkan","green")
    enter()
    clear()
    transisi()
    daftarakan_kendaraan()
#_______________________________________ MOBIL__________________________________    
def penampung_mobil():
    atas_nama =[]
    jenis_kendaraan = []
    plat_nomor = []
    tipe_kendaraan = []
    tahun_kendaraan = []
    warna_kendaraan = []
    with open (f"datauser/{nama_profil[0]}/mobil.csv", mode="r") as file :
        reader = csv.reader(file)
        for i in reader:
            if i == []:
                continue
            else :
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
    garis("═",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("═",b=128)
    if len(atas_nama) == 0:
        print ("")
        print("BELUM ADA KENDARAAN TERDAFTAR\n".center(120))
        garis("═",b=128)
    else :
        for i in range (len(jenis_kendaraan)):
            print (f"|{i+1:^3} |{atas_nama[i]:^25}|{jenis_kendaraan[i]:^17}|{plat_nomor[i]:^15}|{tipe_kendaraan[i]:^25}|{tahun_kendaraan[i]:^17}|{warna_kendaraan[i]:^17}|")
            garis("═",b=128)

def hapus_mobil():
    clear()
    cover(b=128)
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_mobil()
    print("")
    print("HAPUS MOBIL\n".center(128))
    penampil_mobil()
    garis("═",b=128)
    if len (atas_nama) == 0:
        termcolor.cprint("kendaraan belum tersedia","red")
        enter()
        clear()
        transisi()
        daftarakan_kendaraan()
    else :
        pilih = (int(input("Masukkan nomor mobil yang ingin dihapus : ")) - 1)
        enter()
        clear()
        cover(b=128)
        print("")
        print("HAPUS MOBIL\n".center(128))
        border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
        garis("═",b=128)
        print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
        garis("═",b=128)
        print (f"|{pilih + 1:^3} |{atas_nama[pilih]:^25}|{jenis_kendaraan[pilih]:^17}|{plat_nomor[pilih]:^15}|{tipe_kendaraan[pilih]:^25}|{tahun_kendaraan[pilih]:^17}|{warna_kendaraan[pilih]:^17}|")
        garis("═",b=128)
        yakin = input ("apkah yakin ingin menghapus data ini [y/n] >> ").lower()
        if yakin == "y":
            atas_nama.pop(pilih)
            jenis_kendaraan.pop(pilih)
            plat_nomor.pop(pilih)
            tipe_kendaraan.pop(pilih)
            tahun_kendaraan.pop(pilih)
            warna_kendaraan.pop(pilih)
        elif yakin == "n":
            enter()
            clear()
            transisi()
            daftarakan_kendaraan()
        with open (f"datauser/{nama_profil[0]}/mobil.csv", mode = "w", newline = "\n") as file:
            writer = csv.writer(file)
            for i in range (len(atas_nama)):
                writer.writerow ([atas_nama[i], jenis_kendaraan[i], plat_nomor[i],tipe_kendaraan[i],tahun_kendaraan[i],warna_kendaraan[i]])
        termcolor.cprint("Data berhasil dihapus", "green")
        enter()
        clear()
        transisi()
        daftarakan_kendaraan()

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
            if i == []:
                continue
            else :
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
    garis("═",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("═",b=128)
    if len(atas_nama) == 0:
        print ("")
        print("BELUM ADA KENDARAAN TERDAFTAR\n".center(120))
        garis("═",b=128)
    else :
        for i in range (len(jenis_kendaraan)):
            print (f"|{i+1:^3} |{atas_nama[i]:^25}|{jenis_kendaraan[i]:^17}|{plat_nomor[i]:^15}|{tipe_kendaraan[i]:^25}|{tahun_kendaraan[i]:^17}|{warna_kendaraan[i]:^17}|")
            garis("═",b=128)

def hapus_motor():
    clear()
    cover(b=128)
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_motor()
    print("")
    print("HAPUS MOTOR\n".center(128))
    penampil_motor()
    garis("═",b=128)
    if len (atas_nama) == 0:
        termcolor.cprint("kendaraan belum tersedia","red")
        enter()
        clear()
        transisi()
        daftarakan_kendaraan()
    else :
        pilih = (int(input("Masukkan nomor motor yang ingin dihapus : ")) - 1)
        enter()
        clear()
        cover(b=128)
        print("")
        print("HAPUS MOTOR\n".center(128))
        border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
        garis("═",b=128)
        print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
        garis("═",b=128)
        print (f"|{pilih + 1:^3} |{atas_nama[pilih]:^25}|{jenis_kendaraan[pilih]:^17}|{plat_nomor[pilih]:^15}|{tipe_kendaraan[pilih]:^25}|{tahun_kendaraan[pilih]:^17}|{warna_kendaraan[pilih]:^17}|")
        garis("═",b=128)
        yakin = input ("apkah yakin ingin menghapus data ini [y/n] >> ").lower()
        if yakin == "y":
            atas_nama.pop(pilih)
            jenis_kendaraan.pop(pilih)
            plat_nomor.pop(pilih)
            tipe_kendaraan.pop(pilih)
            tahun_kendaraan.pop(pilih)
            warna_kendaraan.pop(pilih)
        elif yakin == "n":
            enter()
            clear()
            transisi()
            daftarakan_kendaraan()
        with open (f"datauser/{nama_profil[0]}/motor.csv", mode = "w", newline = "\n") as file:
            writer = csv.writer(file)
            for i in range (len(atas_nama)):
                writer.writerow ([atas_nama[i], jenis_kendaraan[i], plat_nomor[i],tipe_kendaraan[i],tahun_kendaraan[i],warna_kendaraan[i]])
        termcolor.cprint("Data berhasil dihapus", "green")
        enter()
        clear()
        transisi()
        daftarakan_kendaraan()


#___________________________________________________PARKIR__________________________________________________________
def penampung_slot_parkir_mobil():
    slot_parkir_mobil = []
    with open ("dataadmin/slotparkirmobil.csv", mode="r") as file :
        reader = csv.reader(file)
        for i in reader :
            slot_parkir_mobil.append(i)
    return slot_parkir_mobil

def penampil_slot_parkir_mobil():
    slot_parkir_mobil = penampung_slot_parkir_mobil()
    border = ["SLOT PARKIR MOBIL 1","SLOT PARKIR MOBIL 2"]
    garis("═",b=110)
    print (f"|{border[0]:^108}|")
    garis("═",b=110)
    for i in range (len(slot_parkir_mobil[0][0:10])):
        print (f"|{slot_parkir_mobil[0][i]:^9}|", end="")
    print ("")
    garis("═",b=110)
    for i in range (len(slot_parkir_mobil[1][0:10])):
        print (f"|{slot_parkir_mobil[1][i]:^9}|", end="")
    print ("")
    garis("═",b=110)
    print (f"|{border[1]:^108}|")
    garis("═",b=110)
    for i in range (len(slot_parkir_mobil[0][10:20])):
        print (f"|{slot_parkir_mobil[0][i+10]:^9}|", end="")
    print ("")
    garis("═",b=110)
    for i in range (len(slot_parkir_mobil[1][10:20])):
        print (f"|{slot_parkir_mobil[1][i+10]:^9}|", end="")
    print ("")
    garis("═",b=110)

def penampung_slot_parkir_motor():
    slot_parkir_motor = []
    with open ("dataadmin/slotparkirmotor.csv", mode="r") as file :
        reader = csv.reader(file)
        for i in reader :
            slot_parkir_motor.append(i)
    return slot_parkir_motor

def penampil_slot_parkir_motor():
    slot_parkir_motor = penampung_slot_parkir_motor()
    border = ["SLOT PARKIR MOTOR 1","SLOT PARKIR MOTOR 2"]
    garis("═",b=110)
    print (f"|{border[0]:^108}|")
    garis("═",b=110)
    for i in range (len(slot_parkir_motor[0][0:10])):
        print (f"|{slot_parkir_motor[0][i]:^9}|", end="")
    print ("")
    garis("═",b=110)
    for i in range (len(slot_parkir_motor[1][0:10])):
        print (f"|{slot_parkir_motor[1][i]:^9}|", end="")
    print ("")
    garis("═",b=110)
    print (f"|{border[1]:^108}|")
    garis("═",b=110)
    for i in range (len(slot_parkir_motor[0][10:20])):
        print (f"|{slot_parkir_motor[0][i+10]:^9}|", end="")
    print ("")
    garis("═",b=110)
    for i in range (len(slot_parkir_motor[1][10:20])):
        print (f"|{slot_parkir_motor[1][i+10]:^9}|", end="")
    print ("")
    garis("═",b=110)

def parkir_user():
    clear()
    cover(b = 121)
    print ("")
    print ("MENU PARKIR\n".center(121))
    garis("═",b=121)
    print("KENDARAAN TERPARKIR : ")
    penampil_kendaraan_terparkir_user()
    garis("═",b=121)
    print ("""
    1. KETENTUAN PARKIR
    2. CEK KETERSEDIAAN PARKIR
    3. PARKIR INSTANT 
    4. BOOKING PARKIR
    5. CHECKOUT PARKIR
    6. RIWAYAT PARKIR 
    7. KEMBALI KE MENU 
""")
    garis("═",b=121)
    while True :
        try :
            pilih = int (input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                clear()
                cover()
                penampil_peraturan()
                enter()
                clear()
                transisi()
                parkir_user()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                ketersediaan_parkir()
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                parkir_instan_user()
                break
            elif pilih == 4 :
                enter()
                clear()
                transisi()
                menu_booking_parkir_user ()
                break
            elif pilih == 5 :
                enter()
                clear()
                transisi()
                checkout_parkir_user ()
                break
            elif pilih == 6 :
                enter()
                clear()
                transisi()
                riwayat_parkir_user()
                break
            elif pilih == 7 :
                enter()
                clear()
                transisi()
                menu_user()
            else :
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
def ketersediaan_parkir ():
    clear()
    cover(b = 110)
    print ("")
    print ("KETERSEDIAAN PARKIR".center(110))
    garis("═",b=110)
    print ("""
    1. SLOT PARKIR MOBIL
    2. SLOT PARKIR MOTOR
    """)
    garis("═",b=110)
    while True :
        try :
            pilih = int(input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                print ("")
                penampil_slot_parkir_mobil()
                garis("═",b=110)
                enter()
                clear()
                transisi()
                parkir_user()
            elif pilih == 2 :
                print ("")
                penampil_slot_parkir_motor()
                garis("═",b=110)
                enter()
                clear()
                transisi()
                parkir_user()
            else :
                raise ValueError("input yang anda masukkan tidak tersedia, silahkan coba lagi")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue

def parkir_instan_user ():
    clear()
    cover(b=128)
    print ("")
    print ("PARKIR INSTAN\n".center(128))
    garis("═",b=128)
    waktu_sekarang = dt.datetime.now()
    waktu_sekarang = waktu_sekarang.strftime("%d-%m-%Y %H:%M")
    jenis_parkir = "instan"
    print ("""
    1. PARKIR MOBIL
    2. PARKIR MOTOR
    """)
    garis("═",b=128)
    while True:
        try:
            pilih = int (input ("masukkan opsi yang dipilih >> "))
            if pilih == 1  :
                jenis_kendaraan_parkir = "mobil"
                break
            if pilih == 2  :
                jenis_kendaraan_parkir = "motor"
                break
            else :
                raise ValueError("opsi yang dipilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    if jenis_kendaraan_parkir == "mobil" :
        atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_mobil()
        penampil_mobil()
        if len(atas_nama) == 0 :
            print ("silahkan daftarkan kendaraan terlebih dahulu ")
            enter()
            clear()
            transisi()
            daftarakan_kendaraan()
    elif jenis_kendaraan_parkir == "motor" :
        atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_motor()
        penampil_motor()
        if len(atas_nama) == 0 :
            print ("silahkan daftarkan kendaraan terlebih dahulu ")
            enter()
            clear()
            transisi()
            daftarakan_kendaraan()
    while True :
        try:
            pilih_kendaraan = int (input ("pilih kendaraan yang ingin di parkirkan >> ")) - 1
            if pilih_kendaraan < 0 or pilih_kendaraan >= len(atas_nama):
                raise ValueError("inputan tidak valid")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    enter()
    clear()
    transisi()
    clear()
    cover(b=110)
    if jenis_kendaraan_parkir == "mobil" :
        slot_parkir = penampung_slot_parkir_mobil()
        penampil_slot_parkir_mobil()
    elif jenis_kendaraan_parkir == "motor" :
        slot_parkir = penampung_slot_parkir_motor()
        penampil_slot_parkir_motor()
    index_slot_parkir = []
    while True :
        indikator = 0
        try :
            pilih_slot_parkir = input ("masukkan slot parkir yang dipilih >> ").capitalize()
            for i in range (len(slot_parkir[0])) :
                if pilih_slot_parkir == slot_parkir[0][i] and slot_parkir[1][i] == "-":
                    slot_parkir[1][i] = "TERISI"
                    index_slot_parkir.append(i)
                    indikator += 1
                    break
                else :
                    continue
            if indikator == 1 :
                break
            else :
                raise ValueError ("slot tidak tersedia, silahkan pilih slot lain")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    with open (f"dataadmin/slotparkir{jenis_kendaraan_parkir}.csv",mode="w",newline="\n") as file :
        writer = csv.writer(file)
        writer.writerows(slot_parkir)
    with open (f"dataadmin/konfirmasicheckin.csv",mode="a",newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow([atas_nama[pilih_kendaraan],slot_parkir[0][index_slot_parkir[0]],jenis_kendaraan[pilih_kendaraan],plat_nomor[pilih_kendaraan],jenis_parkir,waktu_sekarang])
    termcolor.cprint("registrasi parkir berhasil, silahkan tunggu kondirmasi petugas", "green")
    enter()
    clear()
    transisi()
    parkir_user()

def penampung_kendaraan_terparkir_user ():
    kendaraan_terparkir = []
    with open (f"datauser/{nama_profil[0]}/parkir.csv",mode="r") as file :
        reader = csv.reader(file)
        for i in reader :
            if i == [] :
                continue
            else :
                kendaraan_terparkir.append(i)
    return kendaraan_terparkir

def penampil_kendaraan_terparkir_user():
    kendaraan_terparkir = penampung_kendaraan_terparkir_user()
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "WAKTU CHECK IN"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (kendaraan_terparkir) == 0 :
        print ("BELUM ADA KENDARAAN TERPARKIR".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(kendaraan_terparkir) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)
            
def penampung_booking_user ():
    booking = []
    with open (f"datauser/{nama_profil[0]}/booking.csv",mode="r") as file:
        reader = csv.reader(file)
        for i in reader:
            if i == []:
                continue
            else :
                booking.append(i)
    return booking

def penampil_booking_user():
    booking = penampung_booking_user()
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "TANGGAL TERBOOKING"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (booking) == 0 :
        print ("BELUM ADA KENDARAAN YANG TERDAFTAR".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(booking) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)

def menu_booking_parkir_user ():
    clear()
    cover(b=121)
    print ("")
    print("MENU BOOKING PARKIR\n".center(121))
    penampil_booking_user()
    garis("═",b=121)
    print ("""
    1. BOOKING PARKIR
    2. CHECK IN PARKIR
    3. KEMBALI KE MENU PARKIR
""")
    garis("═",b=121)
    while True :
        try :
            pilih = int(input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                booking_parkir_user()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                checkin_parkir_user()
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                parkir_user()
                break
            else :
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error:
            termcolor.cprint(error,"red")
            enter()
            continue

def booking_parkir_user():
    booking = penampung_booking_user()
    clear()
    cover(b=128)
    print ("")
    print ("BOOKING PARKIR\n".center(128))
    garis("═",b=128)
    waktu_sekarang = dt.datetime.now()
    waktu_sekarang = waktu_sekarang.strftime("%d-%m-%Y")
    waktu_sekarang = dt.datetime.strptime(waktu_sekarang,"%d-%m-%Y")
    batas_booking = dt.datetime.now() + dt.timedelta(days=1)
    batas_booking = batas_booking.strftime("%d-%m-%Y")
    batas_booking = dt.datetime.strptime(batas_booking,"%d-%m-%Y")
    jenis_parkir = "booking"
    print ("""
    1. BOOKING PARKIR MOBIL
    2. BOOKING PARKIR MOTOR
    """)
    garis("═",b=128)
    while True:
        try:
            pilih = int (input("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                jenis_kendaraan_parkir = "mobil"
                break
            elif pilih == 2 :
                jenis_kendaraan_parkir = "motor"
                break
            else :
                raise ValueError("opsi yang dipilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    if jenis_kendaraan_parkir == "mobil" :
        atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_mobil()
        penampil_mobil()
        if len(atas_nama) == 0 :
            print ("silahkan daftarkan kendaraan terlebih dahulu ")
            enter()
            clear()
            transisi()
            daftarakan_kendaraan()
    elif jenis_kendaraan_parkir == "motor" :
        atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_motor()
        penampil_motor()
        if len(atas_nama) == 0 :
            print ("silahkan daftarkan kendaraan terlebih dahulu ")
            enter()
            clear()
            transisi()
            daftarakan_kendaraan()
    while True :
        try :
            pilih_kendaraan = int (input ("pilih kendaraan yang ingin di parkirkan >> ")) - 1
            if pilih_kendaraan < 0 or pilih_kendaraan >= len(atas_nama) :
                raise ValueError ("inputan tidak valid, kendaraan tidak tersedia")
            elif pilih_kendaraan  >= 0 and pilih_kendaraan  < len(atas_nama) :
                a = 0
                for i in booking:
                    if plat_nomor[pilih_kendaraan] in i :
                        a += 1
                    else :
                        continue
            if a == 0:
                break
            else :
                termcolor.cprint("kendaraan yang anda pilih sudah terbooking", "red")
                yakin = input ("apakah anda ingin mencari kendaraan lain ? (y/n) >> ").lower()
                if yakin == "y" :
                    continue
                elif yakin == "n" :
                    clear()
                    transisi()
                    menu_booking_parkir_user()
                    break
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    enter()
    while True : 
        try:
            waktu_booking = input ("masukkan tanggal booking (dd-mm-yyyy) >> ")
            waktu_booking = dt.datetime.strptime(waktu_booking, "%d-%m-%Y")
            waktu_terbooking = waktu_booking.strftime("%d-%m-%Y")
            if waktu_booking < waktu_sekarang :
                raise ValueError("tanggal booking tidak boleh kurang dari hari ini")
            elif waktu_booking > batas_booking :
                raise ValueError("tanggal booking hanya boleh lebih satu hari dari tanggal sekarang")
            else : 
                break
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    if jenis_kendaraan_parkir == "mobil" :
        slot_parkir = penampung_slot_parkir_mobil()
        penampil_slot_parkir_mobil()
    elif jenis_kendaraan_parkir == "motor" :
        slot_parkir = penampung_slot_parkir_motor()
        penampil_slot_parkir_motor()
    index_slot_parkir = []
    while True :
        indikator = 0
        try :
            pilih_slot_parkir = input ("masukkan slot parkir yang ingin di boking >> ").capitalize()
            for i in range (len(slot_parkir[0])) :
                if pilih_slot_parkir == slot_parkir[0][i] and slot_parkir[1][i] == "-":
                    slot_parkir[1][i] = "BOOKED"
                    index_slot_parkir.append(i)
                    indikator += 1
                    break
                else :
                    continue
            if indikator == 1 :
                break
            else :
                raise ValueError ("slot tidak tersedia, silahkan pilih slot lain")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue
    with open (f"dataadmin/slotparkir{jenis_kendaraan_parkir}.csv",mode="w",newline="\n") as file :
        writer = csv.writer(file)
        writer.writerows(slot_parkir)
    with open (f"datauser/{nama_profil[0]}/booking.csv",mode="a",newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow([atas_nama[pilih_kendaraan],slot_parkir[0][index_slot_parkir[0]],jenis_kendaraan[pilih_kendaraan],plat_nomor[pilih_kendaraan],jenis_parkir,waktu_terbooking])
    termcolor.cprint("booking telah berhasil, silahkan checkin di waktu yang telah di tentukan", "green")
    enter()
    clear()
    transisi()
    menu_booking_parkir_user()

def checkin_parkir_user():
    booking = penampung_booking_user()
    clear()
    cover(b=121)
    print ("")
    print("CHECKIN  PARKIR\n".center(121))
    garis("═",b=121)
    penampil_booking_user()
    garis("═",b=121)
    if len(booking) == 0 :
        termcolor.cprint("anda belum melakukan booking", "red")
        enter()
        clear()
        transisi()
        menu_booking_parkir_user()
    else :
        waktu_sekarang = dt.datetime.now() 
        waktu_sekarang = waktu_sekarang.strftime("%d-%m-%Y")
        waktu_sekarang = dt.datetime.strptime(waktu_sekarang,"%d-%m-%Y")
        waktu_checkin = dt.datetime.now()
        waktu_checkin = waktu_checkin.strftime("%d-%m-%Y %H:%M")
        while True :
            try :
                pilih_checkin = int (input ("pilih kendaraan yang ingin di check in kan >> ")) - 1 
                if pilih_checkin < 0 or pilih_checkin >= len(booking) :
                    raise ValueError ("inputan tidak valid, pilihan tidak tersedia")
                tanggal_booking = dt.datetime.strptime(booking[pilih_checkin][5],"%d-%m-%Y")
                if tanggal_booking == waktu_sekarang:
                    break
                elif tanggal_booking < waktu_sekarang :
                    raise ValueError ("tidak bisa melakukan check in, tanggal booking sudah terlewati")
                elif tanggal_booking > waktu_sekarang :
                    raise ValueError ("tidak bisa melakukan check in, tanggal booking belum tiba")
            except ValueError as error :
                termcolor.cprint(error, "red")
                yakin = input ("apakah ingin mencoba lagi? (y/n) >> ").lower()
                enter()
                if yakin == "y" :
                    continue
                elif yakin == "n" :
                    clear()
                    transisi()
                    menu_booking_parkir_user()
        if booking[pilih_checkin][2] == "mobil" :
            slot_parkir = penampung_slot_parkir_mobil()
        elif booking[pilih_checkin][2] == "motor" :
            slot_parkir = penampung_slot_parkir_motor()
        for i in range (len (booking)) :
            if booking[pilih_checkin][1] == slot_parkir[0][i]:
                slot_parkir[1][i] = "TERISI"
        with open (f"dataadmin/slotparkir{booking[pilih_checkin][2]}.csv",mode="w",newline="\n") as file :
            writer = csv.writer(file)
            writer.writerows(slot_parkir)
        with open (f"dataadmin/konfirmasicheckin.csv",mode="a",newline="\n") as file :
            writer = csv.writer(file)
            writer.writerow([booking[pilih_checkin][0],booking[pilih_checkin][1],booking[pilih_checkin][2],booking[pilih_checkin][3],booking[pilih_checkin][4],waktu_checkin])
        booking.pop(pilih_checkin)
        with open (f"datauser/{nama_profil[0]}/booking.csv",mode="w",newline="\n") as file :
            writer = csv.writer(file)
            writer.writerows(booking)
        termcolor.cprint("checkin dalam proses, menunggu konfirrmasi petugas...","green")
        enter()
        clear()
        transisi()
        menu_booking_parkir_user()

def checkout_parkir_user ():
    clear()
    cover(b = 121)
    harga_parkir_motor_5_jam, harga_parkir_motor_harian,harga_parkir_mobil_5_jam, harga_parkir_mobil_harian = penampung_harga_parkir()
    diparkjirkan_jukir_1,diparkjirkan_jukir_2 = penampung_diparkirkan()
    kendaraan_terparkir = penampung_kendaraan_terparkir_user()
    waktu_sekarang = dt.datetime.now()
    waktu_keluar = waktu_sekarang.strftime("%d-%m-%Y %H:%M")
    print ("")
    print ("MENU PARKIR\n".center(121))
    garis("═",b=121)
    print("KENDARAAN TERPARKIR : ")
    penampil_kendaraan_terparkir_user()
    garis("═",b=121)
    if len(kendaraan_terparkir) == 0 :
        termcolor.cprint("tidak ada kendaraan yang terparkir","red")
        enter()
        clear()
        transisi()
        parkir_user()
    else :
        while True :
            try :
                pilih_checkout = int (input ("pilih kendaraan yang ingin di check out >> ")) - 1
                if pilih_checkout < 0 or pilih_checkout >= len (kendaraan_terparkir) :
                    raise ValueError ("inputan tidak valid, silahkan pilih ulang...")
                else :
                    break
            except ValueError as error :
                termcolor.cprint(error, "red")
                enter()
                continue
        if kendaraan_terparkir[pilih_checkout][2] == "mobil" :
            diparkjirkan_jukir_1[0] += 1
            slot_parkir = penampung_slot_parkir_mobil()
            harga_jam = harga_parkir_mobil_5_jam
            harga_harian = harga_parkir_mobil_harian
        elif kendaraan_terparkir[pilih_checkout][2] == "motor" :
            diparkjirkan_jukir_2[0] += 1
            slot_parkir = penampung_slot_parkir_motor()
            harga_jam = harga_parkir_motor_5_jam
            harga_harian = harga_parkir_motor_harian
        for i in range (len (slot_parkir[0])):
            if kendaraan_terparkir[pilih_checkout][1] == slot_parkir[0][i] :
                slot_parkir[1][i] = "-"
                break
            else :
                continue
        enter()
        if kendaraan_terparkir[pilih_checkout][4] == "booking" :
            harga_tambahan = 3000
        elif kendaraan_terparkir[pilih_checkout][4] == "instan" :
            harga_tambahan = 0
        waktu_masuk = dt.datetime.strptime(kendaraan_terparkir[pilih_checkout][5],"%d-%m-%Y %H:%M")
        if (waktu_sekarang - waktu_masuk).days == 0 :
            if ((waktu_sekarang - waktu_masuk).seconds / 3600) <= 5 :
                total_harga = harga_jam + harga_tambahan 
            else : 
                total_harga = harga_harian + harga_tambahan
        else :
            pembulatan_hari = 0
            batas_bawah = 1
            batas_atas = 2
            while True :
                lama_parkir = ((waktu_sekarang - waktu_masuk).total_seconds()/3600)/24
                print (lama_parkir)
                if lama_parkir > batas_bawah and lama_parkir < batas_atas :
                    pembulatan_hari += batas_atas
                    break
                else :
                    batas_atas +=1
                    batas_bawah +=1
            total_harga = harga_harian*pembulatan_hari + harga_tambahan
        clear()
        transisi()
        clear()
        cover ()
        garis("═")
        print (f"""
        PEMILIK KENDARAAN : {kendaraan_terparkir[pilih_checkout][0]} 
        BLOK PARKIR       : {kendaraan_terparkir[pilih_checkout][1]}
        JENIS KENDARAAN   : {kendaraan_terparkir[pilih_checkout][2]}
        PLAT NOMOR        : {kendaraan_terparkir[pilih_checkout][3]}
        JENIS PARKIR      : {kendaraan_terparkir[pilih_checkout][4]}
        WAKTU CHECK IN    : {kendaraan_terparkir[pilih_checkout][5]}
        WAKTU CHECK OUT   : {waktu_keluar}
        TOTAL TAGIHAN     : {total_harga}
        """)
        kendaraan_terparkir[pilih_checkout].append(waktu_keluar)
        kendaraan_terparkir[pilih_checkout].append(total_harga)
        garis("═")
        with open ("datajukir/kendaraan_diparkirkan.csv", mode="w",newline="\n") as file :
            writer = csv.writer(file)
            writer.writerow([diparkjirkan_jukir_1[0],diparkjirkan_jukir_2[0]])
        with open(f"dataadmin/slotparkir{kendaraan_terparkir[pilih_checkout][2]}.csv", mode="w",newline="\n") as file :
            writer = csv.writer(file)
            writer.writerows(slot_parkir)
        with open (f"dataadmin/konfirmasicheckout.csv", mode="a", newline="\n") as file:
            writer = csv.writer(file)
            writer.writerow(kendaraan_terparkir[pilih_checkout])
        kendaraan_terparkir.pop(pilih_checkout)
        with open (f"datauser/{nama_profil[0]}/parkir.csv", mode ="w",newline="\n") as file:
            writer = csv.writer(file)
            writer.writerows(kendaraan_terparkir)
        termcolor.cprint("checkout berhasil, silahkan bayar tagihan secara langsung ke petugas admin", "green")
        enter()
        clear()
        transisi()
        parkir_user()

def penampung_riwayat_parkir_user ():
    riwayat = []
    with open (f"datauser/{nama_profil[0]}/riwayat_parkir_user.csv", mode="r") as file :
        reader = csv.reader(file)
        for i in reader:
            if i == []:
                continue
            else :
                riwayat.append(i)
    return riwayat

def penampil_riwayat_parkir_user():
    riwayat = penampung_riwayat_parkir_user()
    total_harga =[]
    border = ["NO", "PEMILIK", "BLOK", "JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "WAKTU CHECK IN", "WAKTU CHECK OUT", "TOTAL TAGIHAN"]
    garis("═",b=157)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^8}|{border[3]:^20}|{border[4]:^15}|{border[5]:^20}|{border[6]:^20}|{border[7]:^20}|{border[8]:^20}|")
    garis("═",b=157)
    if len(riwayat) == 0:
        print ("BELUM ADA RIWAYAT PARKIR".center(157))
        garis("═",b=157)
    else :
        for i in riwayat:
            total = f"{int(i[7]):,}"
            total_harga.append(total)
        for a,i in enumerate(riwayat):
            print (f"|{a+1:^4}|{i[0]:^20}|{i[1]:^8}|{i[2]:^20}|{i[3]:^15}|{i[4]:^20}|{i[5]:^20}|{i[6]:^20}|{"Rp."+total_harga[a]:^20}|")
            garis("═",b=157)

def riwayat_parkir_user():
    clear()
    cover(b=157)
    print ("")
    print ("RIWAYAT PARKIR\n".center(157))
    garis("═",b=157)
    penampil_riwayat_parkir_user()
    garis("═",b=157)
    enter()
    clear()
    transisi()
    parkir_user()

#__________________________________________________PENITIPAN BARANG USER_____________________________________________________________
def penitipan_barang_user():
    clear()
    cover(b = 110)
    print("")
    print("PENITIPAN BARANG\n".center(110))
    penampil_rak_barang_tersedia()
    print("")
    print("BARANG DITITIPKAN\n".center(110))
    penampil_barang()
    garis("═",b=110) 
    print ("""
        1. TITIPKAN BARANG
        2. AMBIL BARANG
        3. RIWAYAT PENITIPAN  
        4. KEMBALI KE MENU 
    """)
    garis("═",b=110)
    while True :
        try :
            pilih = int (input("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                titipkan_barang_user()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                ambil_barang_user()
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                riwayat_penitipan_user()
                break
            elif pilih == 4 :
                enter()
                clear()
                transisi()
                menu_user()
                break
            else :
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue

# def infokan():
#     rak = []    
#     for i in range (1,21):
#         a = "KOSONG"
#         rak.append(a)
#         # i = str(i)
#         # if len(i) < 2:
#         #     a = f"C0{i}"
#         # elif len(i) == 2 :
#         #     a = f"C{i}"
#         # rak.append(a)
#     with open ("dataadmin/slotparkirmobil.csv",mode="a", newline="\n") as file :
#         writer = csv.writer(file)
#         writer.writerow(rak)
    
def penampung_rak():
    rak_tersedia = []
    status = []
    with open ("dataadmin/rakpenitipanbarang.csv",mode="r") as file:
        reader = csv.reader(file)
        for i in reader :
            rak_tersedia.append(i)
    return rak_tersedia

def penampil_rak_barang_tersedia():
    rak_tersedia= penampung_rak()
    border = "RAK TERSEDIA"
    garis("═",b=110)
    print (f"|{border:^108}|")
    garis("═",b=110)
    for i in range (len(rak_tersedia[0])):
        print (f"|{rak_tersedia[0][i]:^9}|",end= "")
    print ("")
    garis("═",b=110)
    for i in range (len(rak_tersedia[1])):
        print (f"|{rak_tersedia[1][i]:^9}|",end= "")
    print ("")
    garis("═",b=110)

def penampung_barang_user ():
    pemilik = []
    nama_barang = []
    rak = []
    tanggal_masuk = []
    with open(f"datauser/{nama_profil[0]}/titipbarang.csv", mode="r") as file :
        reader = csv.reader(file)
        for i in reader :
            if i == []:
                continue
            else :
                pemilik.append(i[0])
                rak.append(i[1])
                nama_barang.append(i[2])
                tanggal_masuk.append(i[3])
    return pemilik,rak,nama_barang,tanggal_masuk

def penampil_barang():
    pemilik,rak,nama_barang,tanggal_masuk = penampung_barang_user()
    border = ["NO", "PEMILIK","RAK BARANG", "NAMA BARANG", "TANGGAL MASUK"]
    garis("═",b=110)
    print (f"|{border[0]:^6}|{border[1]:^30}|{border[2]:^20}|{border[3]:^28}|{border[4]:^20}|")
    garis("═",b=110)
    if len(pemilik) == 0 :
        tulisan = "TIDAK ADA BARANG YANG DITITIPKAN".center(110)
        print (tulisan)
        garis("═",b=110)
    else:
        for i in range (len(pemilik)):
            print (f"|{i+1:^6}|{pemilik[i]:^30}|{rak[i]:^20}|{nama_barang[i]:^28}|{tanggal_masuk[i]:^20}|")
            garis("═",b=110)
    
def titipkan_barang_user():
    rak_barang = penampung_rak()
    clear()
    cover(b = 110)
    print("")
    print("TITIPKAN BARANG\n".center(110))
    penampil_rak_barang_tersedia()
    garis("═", b =110)
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password  = penampung_user() 
    waktu_sekarang = dt.datetime.now()
    waktu_sekarang = waktu_sekarang.strftime("%d-%m-%Y %H:%M")
    # print (rak_barang)

    index_rak = []
    while True :
        try :
            a = 0
            rak = input("Masukkan nomor rak yang tersedia : ").capitalize()
            for i in range (len(rak_barang[0])):
                if rak == rak_barang[0][i] and rak_barang[1][i] == "-":
                    index_rak.append(i)
                    a += 1 
                    break
            if a == 1 :
                break
            else :
                raise ValueError("Nomor rak yang anda inputkan tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    rak_barang[1][index_rak[0]] = "TERISI"
    while True :
        try :
            nama_barang = input ("masukkan nama barang >> ")
            if len(nama_barang) == 0 or nama_barang == " ":
                raise ValueError ("Nama barang tidak boleh kosong")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    with open (f"datauser/{nama_profil[0]}/titipbarang.csv", mode = "a",newline = "\n") as file :
        border = ["pemilik","rak", "nama barang", "tanggal masuk"]
        writer = csv.DictWriter(file, fieldnames=border)
        writer.writerow({"pemilik" : nama_profil[0],"rak" : rak,"nama barang":nama_barang,"tanggal masuk":waktu_sekarang})
    with open ("dataadmin/rakpenitipanbarang.csv", mode= "w", newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow(rak_barang[0])
    with open ("dataadmin/rakpenitipanbarang.csv", mode= "a", newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow(rak_barang[1])
    termcolor.cprint("barang berhasil di titipkan", "green")
    enter()
    clear()
    transisi()
    penitipan_barang_user()

def ambil_barang_user():
    rak_barang = penampung_rak()
    pemilik,rak,nama_barang,tanggal_masuk = penampung_barang_user()
    waktu_sekarang = dt.datetime.now()
    waktu_sekarang = waktu_sekarang.strftime("%d-%m-%Y %H:%M")
    clear()
    cover(b = 110)
    print("")
    print("AMBIL BARANG\n".center(110))
    garis("═",b=110)
    print ("BARANG DITITIPKAN : ")
    penampil_barang()
    if len(pemilik) == 0 :
        enter()
        clear()
        penitipan_barang_user()
    else :
        while True :
            try :
                pilih = int (input("masukkan nomor barang yang ingin di ambil >> ")) - 1 
                if pilih < 0 or pilih >= len(pemilik) :
                    raise ValueError ("barang tidak tersedia")
                else :
                    break
            except ValueError as error :
                termcolor.cprint(error,"red")
                enter()
                continue
        index_rak = []
        for i in range(len(rak_barang[0])):
            if rak[pilih]==rak_barang[0][i]:
                index_rak.append(i)
        rak_barang[1][index_rak[0]] = "-"
        enter()
        clear()
        cover(b = 110)
        print("")
        print("AMBIL BARANG\n".center(110))
        border = ["NO", "PEMILIK","RAK BARANG", "NAMA BARANG", "TANGGAL MASUK"]
        garis("═",b=110)
        print (f"|{border[0]:^6}|{border[1]:^30}|{border[2]:^20}|{border[3]:^28}|{border[4]:^20}|")
        garis("═",b=110)
        print (f"|{pilih+1:^6}|{pemilik[pilih]:^30}|{rak[pilih]:^20}|{nama_barang[pilih]:^28}|{tanggal_masuk[pilih]:^20}|")
        garis("═",b=110)
        while True :
            try:
                yakin = input("apakah anda yakin ingin mengambil barang ini ? (y/n) >> ").lower()
                if yakin == "y" :
                    with open (f"datauser/{nama_profil[0]}/riwayat_titip_barang.csv", mode="a",newline="\n") as file :
                        border = ["pemilik","rak" ,"nama barang", "tanggal masuk","tanggal keluar"]
                        writer = csv.DictWriter(file, fieldnames=border)
                        writer.writerow({"pemilik" : pemilik[pilih],"rak" : rak[pilih],"nama barang":nama_barang[pilih], "tanggal masuk" : tanggal_masuk[pilih],"tanggal keluar":waktu_sekarang})
                    pemilik.pop(pilih)
                    rak.pop(pilih)
                    nama_barang.pop(pilih)
                    tanggal_masuk.pop(pilih)
                    with open (f"datauser/{nama_profil[0]}/titipbarang.csv", mode = "w",newline="\n")as file:
                        writer = csv.writer(file)
                        for i in range (len(pemilik)):
                            writer.writerow([pemilik[i],rak[i],nama_barang[i],tanggal_masuk[i]])
                    with open ("dataadmin/rakpenitipanbarang.csv", mode = "w",newline="\n") as file :
                        writer = csv.writer(file)
                        writer.writerows(rak_barang)
                    enter()
                    clear()
                    transisi()
                    penitipan_barang_user()
                    break
                elif yakin == "n" :
                    enter()
                    clear()
                    transisi()
                    penitipan_barang_user()
                    break
                elif yakin == "" :
                    raise ValueError("inputan tidak boleh kosong")
                else :
                    raise ValueError("inputan tidak valid")
            except ValueError as error :
                termcolor.cprint(error,"red")
                enter()
                continue

def penampung_riwayat_penitipan_barang_user():
    pemilik = []
    rak = []
    nama_barang = []
    tanggal_masuk = []
    tanggal_keluar = []
    with open (f"datauser/{nama_profil[0]}/riwayat_titip_barang.csv", mode="r",newline="\n") as file :
        reader = csv.reader(file)
        for i in reader:
            if i == []:
                continue
            else :
                pemilik.append(i[0])
                rak.append(i[1])
                nama_barang.append(i[2])
                tanggal_masuk.append(i[3])
                tanggal_keluar.append(i[4])
    return pemilik,rak,nama_barang,tanggal_masuk,tanggal_keluar

def riwayat_penitipan_user():
    clear()
    cover(b = 131)
    pemilik,rak,nama_barang,tanggal_masuk,tanggal_keluar = penampung_riwayat_penitipan_barang_user()
    print("")
    print("RIWAYAT PENITIPAN BARANG\n".center(131))
    border = ["NO", "PEMILIK","RAK BARANG", "NAMA BARANG", "TANGGAL MASUK", "TANGGAL KELUAR"]
    garis("═",b=131)
    print (f"|{border[0]:^6}|{border[1]:^30}|{border[2]:^20}|{border[3]:^28}|{border[4]:^20}|{border[5]:^20}|")
    garis("═",b=131)
    if len(pemilik) == 0 :
        print ("")
        print ("BELUM ADA RIWAYAT PENITIPAN BARANG\n".center(131))
        garis("═",b=131)
    else :
        for i in range (len (pemilik)):
            print (f"|{i+1:^6}|{pemilik[i]:^30}|{rak[i]:^20}|{nama_barang[i]:^28}|{tanggal_masuk[i]:^20}|{tanggal_keluar[i]:^20}|")
            garis("=",b=131)
    garis("═",b=131)
    enter()
    clear()
    transisi()
    penitipan_barang_user()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> JUKIR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu_jukir():
    while True :
        clear()
        cover()
        print ("""
                                        1. CEK PROFIL
                                        2. KEHADIRAN DAN KONTRIBUSI 
                                        3. CEK KETERSEDIAAN PARKIR
                                        4. CEK BOOKING PARKIR
                                        5. CEK KENDARAAN TERPARKIR
                                        6. LOG OUT
""")
        garis("═")
        try :
            pilih = int (input("Masukkan pilihan >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                cek_profil_jukir()
                break
            elif pilih == 2 :
                enter ()
                clear()
                transisi()
                kehadiran_kontribusi_jukir()
                break
            elif pilih == 3 :
                enter ()
                clear()
                transisi()
                cek_parkir_tersedia_jukir()
                break
            elif pilih == 4 :
                enter ()
                clear()
                transisi()
                cek_booking_parkir_jukir()
                break
            elif pilih == 5 :
                enter ()
                clear()
                transisi()
                cek_kendaraan_terparkir_user()
                break
            elif pilih == 6 :
                enter()
                clear()
                transisi()
                halaman_awal()
                break
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue

def cek_profil_jukir():
    clear()
    cover()
    print (f"""
                                    NAMA          : {nama_jukir_profil[0]}
                                    NIK           : {nik_jukir_profil[0]}
                                    NOMOR TELEPON : {telepon_jukir_profil[0]}    
""")
    garis("═")
    enter()
    clear()
    transisi()
    menu_jukir()

def penampung_diparkirkan():
    diparkjirkan_jukir_1 = []
    diparkjirkan_jukir_2 = []
    with open ("datajukir/kendaraan_diparkirkan.csv", mode="r")as file :
        reader = csv.reader(file)
        for i in reader :
            diparkjirkan_jukir_1.append(int(i[0]))
            diparkjirkan_jukir_2.append(int(i[1]))
    return diparkjirkan_jukir_1,diparkjirkan_jukir_2

def kehadiran_kontribusi_jukir():
    tampungan_kehadiran_jukir = penampung_kehadiran_jukir()
    nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
    diparkjirkan_jukir_1,diparkjirkan_jukir_2 = penampung_diparkirkan()
    # username_pasword_jukir_profil = ["jukir1"]
    # nama_profil = ["rohmat alim"]
    if username_pasword_jukir_profil[0][0] == "jukir1" :
        kontribusi = diparkjirkan_jukir_1[0]
    elif username_pasword_jukir_profil[0][0] == "jukir2" :
        kontribusi = diparkjirkan_jukir_2[0]
    clear()
    cover()
    print ("")
    print ("KEHADIRAN DAN KONTRIBUSI JUKIR\n".center(107))
    garis("═")
    border = ["NAMA", "JUMLAH KEHADIRAN", "JUMLAH KONTRIBUSI"]
    garis("═")
    print (f"|{border[0]:^43}|{border[1]:^30}|{border[2]:^30}|")
    garis("═")
    print (f"|{nama_jukir_profil[0]:^43}|{len(tampungan_kehadiran_jukir):^30}|{kontribusi:^30}|")
    garis("═")
    garis("═")
    print ("""
        1. ISI KEHADIRAN
        2. KEMBALI KE MENU
""")
    garis("═")
    while True:
        try:
            pilih = int(input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                kehadiran_jukir()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                menu_jukir()
                break
            else :
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")

def penampung_kehadiran_jukir():
    tampungan_kehadiran_jukir = []
    with open (f"datajukir/kehadiran{username_pasword_jukir_profil[0][0]}.csv", mode="r") as file:
        reader = csv.reader(file)
        for i in reader :
            if i == [] :
                continue
            else :
                tampungan_kehadiran_jukir.append(i)
    return tampungan_kehadiran_jukir

def kehadiran_jukir():
    tampungan_kehadiran_jukir = penampung_kehadiran_jukir()
    clear()
    cover()
    print ("")
    print ("KEHADIRAN JUKIR\n".center(107))
    garis("═")
    tanggal_absen = []
    for i in tampungan_kehadiran_jukir:
            tanggal = dt.datetime.strptime(i[1],"%d-%m-%Y %H:%M")
            tanggal = tanggal.strftime("%d-%m-%Y")
            tanggal_absen.append(tanggal)
    waktu_sekarang = dt.datetime.now()
    waktu_sekarang = waktu_sekarang.strftime("%d-%m-%Y %H:%M")
    waktu_cek = dt.datetime.now()
    waktu_cek = waktu_cek.strftime("%d-%m-%Y")
    if waktu_cek in tanggal_absen :
        print ("KEHADIRAN ANDA SUDAH TERISI HARI INI".center(107))
        garis("═")
        enter()
        clear()
        transisi()
        kehadiran_kontribusi_jukir()
    else :
        while True:
            salah = 0
            if salah >= 3:
                termcolor.cprint("silahkan coba beberapa saat lagi", "red")
                enter()
                clear()
                transisi()
                kehadiran_kontribusi_jukir()
            else :
                try:
                    username = input("masukkan username untuk mengisi kehadiran >>")
                    password = input("masukkan password untuk mengisi kehadiran >>")
                    garis("═")
                    if [username,password] == username_pasword_jukir_profil[0]:
                        with open (f"datajukir/kehadiran{username_pasword_jukir_profil[0][0]}.csv", mode="a",newline="\n") as file :
                            writer = csv.writer(file)
                            writer.writerow([nama_jukir_profil[0],waktu_sekarang])
                        termcolor.cprint("kehasdiran berhasil diperbarui...","green")
                        enter()
                        clear()
                        transisi()
                        kehadiran_kontribusi_jukir()
                        break
                    else :
                        salah +=1
                        raise ValueError ("username atau password salah")
                except ValueError as error :
                    termcolor.cprint(error,"red")
                    enter()
                    continue

def cek_parkir_tersedia_jukir():
    clear()
    cover(b=110)
    print ("")
    print ("KETERSEDIAAN PARKIR".center(110))
    garis("═",b=110)
    penampil_slot_parkir_motor()
    garis("═",b=110)
    print ("""
        1. LIHAT KETERSEDIAAN PARKIR MOBIL
        2. KEMBALI KE MENU
""")
    garis("═",b=110)
    while True :
        try:
            pilih = int(input("masukkan opsi yang dipilih >>"))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                clear()
                cover(b=110)
                print ("")
                print ("KETERSEDIAAN PARKIR".center(110))
                garis("═",b=110)
                penampil_slot_parkir_mobil()
                garis("═",b=110)
                enter()
                break
            elif pilih == 2 :
                enter()
                break
            else : 
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    clear()
    transisi()
    menu_jukir()

def penampung_booking_parkir_seluruh ():
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    booking_parkir_motor = []
    booking_parkir_mobil = []
    for i in user :
        with open (f"datauser/{i}/booking.csv", mode="r") as file :
            reader = csv.reader (file)
            for i in reader:
                if i == []:
                    continue
                elif i[2] == "motor" :
                    booking_parkir_motor.append(i)
                elif i[2] == "mobil" :
                    booking_parkir_mobil.append(i)
    return booking_parkir_motor, booking_parkir_mobil

def penampil_booking_parkir_motor():
    booking_parkir_motor, booking_parkir_mobil = penampung_booking_parkir_seluruh()
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "TANGGAL TERBOOKING"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (booking_parkir_motor) == 0 :
        print ("BELUM ADA KENDARAAN YANG TERDAFTAR".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(booking_parkir_motor) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)

def penampil_booking_parkir_mobil():
    booking_parkir_motor, booking_parkir_mobil = penampung_booking_parkir_seluruh()
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "TANGGAL TERBOOKING"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (booking_parkir_mobil) == 0 :
        print ("BELUM ADA KENDARAAN YANG TERDAFTAR".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(booking_parkir_mobil) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)

def cek_booking_parkir_jukir():
    clear()
    cover(b =121)
    print ("")
    print ("CEK BOOKING PARKIR\n".center(121))
    garis("═",b=121)
    penampil_booking_parkir_motor()
    garis("═",b=121)
    print ("""
        1. CEK BOOKING PARKIR MOBIL
        2. KEMBALI KE MENU
""")
    garis("═",b=121)
    while True :
        try:
            pilih = int(input("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                clear()
                transisi()
                clear()
                cover(b =121)
                print ("")
                print ("CEK BOOKING PARKIR\n".center(121))
                garis("═",b=121)
                penampil_booking_parkir_mobil()
                garis("═",b=121)
                enter()
                clear()
                transisi()
                menu_jukir()
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                menu_jukir()
        except ValueError as error :
            termcolor.cprint(error, "red")

def penampung_parkir_seluruh ():
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    parkir_mobil = []
    parkir_motor = []
    for i in user :
        with open (f"datauser/{i}/parkir.csv", mode="r") as file :
            reader = csv.reader (file)
            for i in reader:
                if i == []:
                    continue
                elif i[2] == "mobil":
                    parkir_mobil.append(i)
                elif i[2] == "motor":
                    parkir_motor.append(i)
    return parkir_mobil,parkir_motor

def penampil_parkir_mobil_seluruh():
    parkir_mobil, parkir_motor = penampung_parkir_seluruh()
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "WAKTU CHECK IN"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (parkir_mobil) == 0 :
        print ("BELUM ADA KENDARAAN TERPARKIR".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(parkir_mobil) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)

def penampil_parkir_motor_seluruh():
    parkir_mobil, parkir_motor = penampung_parkir_seluruh()
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "WAKTU CHECK IN"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (parkir_motor) == 0 :
        print ("BELUM ADA KENDARAAN TERPARKIR".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(parkir_motor) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)

def cek_kendaraan_terparkir_user():
    clear()
    cover(b =121)
    print ("")
    print ("CEK KENDARAAN TERPARKIR\n".center(121))
    garis("═",b=121)
    penampil_parkir_motor_seluruh()
    garis("═",b=121)
    print ("""
        1. CEK MOBIL TERPARKIR
        2. KEMBALI KE MENU
""")
    garis("═",b=121)
    while True :
        try:
            pilih = int(input("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                clear()
                transisi()
                clear()
                cover(b =121)
                print ("")
                print ("CEK KENDARAAN TERPARKIR\n".center(121))
                garis("═",b=121)
                penampil_parkir_mobil_seluruh()
                garis("═",b=121)
                enter()
                clear()
                transisi()
                menu_jukir()
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                menu_jukir()
                break
            else :
                raise ValueError ("opsi yang dipilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue   
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADMIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu_admin():
    while True :
        clear()
        cover()
        print ("""
                                        1. MONITORING PERATURAN
                                        2. MONITORING USER 
                                        3. MONITORING JURU PARKIR
                                        4. MONITORING KENDARAAN USER
                                        5. MONITORING PARKIR
                                        6. MONITORING PENITIPAN BARANG
                                        7. LAPORAN DIGIPARKING 
                                        8. LOG OUT
            
""")
        garis ("═")
        try :
            pilih = int (input("Masukkan pilihan >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                monitoring_peraturan()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                monitoring_user()
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                monitoring_jukir()
            elif pilih == 4 :
                enter()
                clear()
                transisi()
                monitoring_kendaraan_user()
                break
            elif pilih == 5 :
                enter()
                clear()
                transisi()
                monitoring_parkir()
            elif pilih == 6 :
                enter()
                clear()
                transisi()
                monitoring_penitipan_barang()
            elif pilih == 7 :
                enter()
                clear()
                transisi()
                laporan_digiparking()
                break
            elif pilih == 8 :
                enter()
                clear()
                transisi()
                halaman_awal()
                break
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue
#_______________________________________________________________PERATURAN__________________________________________________        

def monitoring_peraturan():
    clear()
    cover()
    print ("")
    print("MONITORING PERATURAN\n".center(107))
    penampil_peraturan()
    print ("""
    1. TAMBAH PERATURAN
    2. UPDATE PERATURAN
    3. HAPUS PERATURAN
    4. ATUR TARIF PARKIR 
    5. KEMBALI KE MENU ADMIN
    """)
    garis("═")
    while True :
        try :
            pilih = int (input("pilih opsi yang tersedia >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                tambah_peraturan()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                update_peraturan()
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                hapus_peraturan()
                break
            elif pilih == 4 :
                enter()
                clear()
                transisi()
                atur_harga_parkir()
                break
            elif pilih == 5 :
                enter()
                clear()
                transisi()
                menu_admin()
                break
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue

def penampung_peraturan():
    isi = []
    with open(f"dataadmin/ketentuan.csv", mode = "r") as file :
        reader = csv.reader(file)
        for a in (reader) :
            if a == [] :
                continue
            else:
                isi.append(a[0])
    return isi

def penampil_peraturan():
    garis("═")
    harga_parkir_motor_5_jam, harga_parkir_motor_harian,harga_parkir_mobil_5_jam, harga_parkir_mobil_harian = penampung_harga_parkir()
    isi = penampung_peraturan()
    print ("TARIF PARKIR :")
    print (f"""
         >. MOTOR KURANG DARI 5 JAM  : Rp.{harga_parkir_motor_5_jam:,}
         >. MOBIL KURANG DARI 5 JAM  : Rp.{harga_parkir_mobil_5_jam:,}
         >. MOTOR HARIAN             : Rp.{harga_parkir_motor_harian:,}
         >. MOBIL HARIAN             : Rp.{harga_parkir_mobil_harian:,}
""")
    print ("KETENTUAN DIGIPARKING :")
    print ("")
    for i in range(len(isi)) :
        print (f"\t >. {isi[i]}")
    garis("═")

def tambah_peraturan():
    clear()
    cover()
    print ("")
    print("TAMBAH PERATURAN\n".center(107))
    garis("═")
    while True : 
        try:
            isi = input ("Isi Peraturan (tidak boleh lebih dari 90 karakter)>> ")
            if len(isi) > 90 or len (isi) < 5 :
                raise ValueError ("isi peraturan minimal terdiri atas 5 karakter dan tidak boleh lebih dari 90 karakter")
            else :
                break
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue
    with open (f"dataadmin/ketentuan.csv", mode="a", newline="\n") as file :
        border = [ "isi"]
        writer = csv.DictWriter(file, fieldnames=border)
        writer.writerow({"isi" : isi})
    termcolor.cprint("peraturan berhasil ditambahkan ","green")
    enter ()
    clear()
    transisi()
    monitoring_peraturan()

def update_peraturan():
    clear()
    cover()
    print ("")
    print("UPDATE PERATURAN\n".center(107))
    isi = penampung_peraturan()
    border = ["NO", "ISI"]
    garis("═")
    print (f"|{border[0]:^5}|{border[1]:^99}|")
    garis("═")
    for i in range (len (isi)):
        print (f"|{i+1:^5}|{isi[i]:^99}|")
        garis("═")
    while True :
        try:
            pilih = int (input ("masukkan peraturan yang ingin di update >> ")) - 1
            if pilih < 0 or pilih >= len(isi):
                raise ValueError ("nomor yang anda pilih tidak tersedia")
            pengganti = input ("masukkan peraturan sebagai pengganti >> ")
            if len (pengganti) < 5 or len(pengganti) > 90:
                raise ValueError ("isi peraturan tidak boleh kurang dari 5 karakter dan tidak boleh lebih dari 90 karakter")
            else : 
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    isi[pilih] = pengganti
    clear()
    cover()
    garis("═")
    print (f"|{border[0]:^5}|{border[1]:^99}|")
    garis("═")
    print (f"|{pilih + 1:^5}|{isi[pilih]:^99}|")
    garis("═")
    with open (f"dataadmin/ketentuan.csv", mode="w", newline="\n") as file:
        writer = csv.writer(file)
        for i in range (len(isi)):
            writer.writerow([isi[i]])
    termcolor.cprint("peraturan berhasil di update", "green")
    enter()
    clear()
    transisi()
    monitoring_peraturan()

def hapus_peraturan():
    clear()
    cover()
    print ("")
    print("HAPUS PERATURAN\n".center(107))
    isi = penampung_peraturan()
    border = ["NO", "ISI"]
    garis("═")
    print (f"|{border[0]:^5}|{border[1]:^99}|")
    garis("═")
    for i in range (len (isi)):
        print (f"|{i+1:^5}|{isi[i]:^99}|")
        garis("═")
    while True :
        try:
            pilih = int (input ("masukkan peraturan yang ingin di hapus >> ")) - 1
            if pilih < 0 or pilih >= len(isi):
                raise ValueError ("nomor yang anda pilih tidak tersedia")
            else : 
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    clear()
    cover()
    garis("═")
    print (f"|{border[0]:^5}|{border[1]:^99}|")
    garis("═")
    print (f"|{pilih + 1:^5}|{isi[pilih]:^99}|")
    garis("═")
    while True:
        try :
            yakin = input ("apakah yakin untuk menghapus peraturan ini (y/n) >> ").lower()
            if yakin == "y" :
                isi.pop(pilih)
                with open (f"dataadmin/ketentuan.csv", mode="w", newline="\n") as file:
                    writer = csv.writer(file)
                    for i in range (len(isi)):
                        writer.writerow([isi[i]])
                termcolor.cprint("peraturan berhasil di hapus", "green")
                enter()
                clear()
                transisi()
                monitoring_peraturan()
                break
            elif yakin == "n" :
                enter()
                clear()
                transisi()
                monitoring_peraturan()
                break
            else :
                raise ValueError ("input yang anda masukkan tidak valid")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue

def atur_harga_parkir():
    clear()
    cover()
    print ("")
    print("ATUR HARGA PARKIR\n".center(107))
    garis("═")
    with open ("dataadmin/harga_parkir.csv", mode="w", newline="\n") as file:
        writer = csv.writer(file)
        while True :
            try :
                harga_parkir_motor_5_jam = int (input("masukkan harga parkir motor dibawah 5 jam >> "))
                if harga_parkir_motor_5_jam < 1000 :
                    raise ValueError ("harga tidak boleh kurang dari 1000")
                else :
                    break
            except ValueError as error:
                termcolor.cprint(error, "red")
                enter()
                continue
        while True :
            try :
                harga_parkir_motor_harian = int (input("masukkan harga parkir motor harian >> "))
                if harga_parkir_motor_harian < 5000:
                    raise ValueError ("harga tidak boleh kurang dari 1000")
                else :
                    break
            except ValueError as error:
                termcolor.cprint(error, "red")
                enter()
                continue

        while True :
            try :
                harga_parkir_mobil_5_jam = int (input("masukkan harga parkir mobil dibawah 5 jam >> "))
                if harga_parkir_mobil_5_jam < 3000 :
                    raise ValueError ("harga tidak boleh kurang dari 3000")
                else :
                    break            
            except ValueError as error:
                termcolor.cprint(error, "red")
                enter()
                continue
            
        while True :
            try :
                harga_parkir_mobil_harian = int (input("masukkan harga parkir mobil harian >> "))
                if harga_parkir_mobil_harian < 10000 :
                    raise ValueError ("harga tidak boleh kurang dari 10000")
                else :
                    break
            except ValueError as error:
                termcolor.cprint(error, "red")
                enter()
                continue
        writer.writerow([harga_parkir_motor_5_jam, harga_parkir_motor_harian,harga_parkir_mobil_5_jam, harga_parkir_mobil_harian])
    garis("═")
    termcolor.cprint("harga parkir berhasil di inputkan", "green")
    enter()
    clear()
    transisi()
    monitoring_peraturan()

def penampung_harga_parkir():
    with open ("dataadmin/harga_parkir.csv", mode="r") as file:
        reader = csv.reader(file)
        for i in reader:
            if i == []:
                harga_parkir_motor_5_jam = 0
                harga_parkir_motor_harian = 0
                harga_parkir_mobil_5_jam = 0
                harga_parkir_mobil_harian = 0
                break
            else :
                harga_parkir_motor_5_jam = int(i[0])
                harga_parkir_motor_harian = int(i[1])
                harga_parkir_mobil_5_jam = int(i[2])
                harga_parkir_mobil_harian = int(i[3])
    return harga_parkir_motor_5_jam, harga_parkir_motor_harian,harga_parkir_mobil_5_jam, harga_parkir_mobil_harian

#______________________________________________________________________MONITORING USER_______________________________________________________________
def penampil_user():
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    border = ["NO","NAMA", "NIK", "TANGGAL LAHIR", "NOMOR HP", "USERNAME", "PASSWORD"]
    garis("═",b=117)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
    garis("═",b=117)
    for i in range (len(user)):
        print (f"|{i + 1:^4}|{user[i]:^20}|{nik[i]:^17}|{tanggal_lahir[i]:^17}|{nomor_hp[i]:^17}|{list_username[i]:^17}|{list_password[i]:^17}|")
        garis("═",b=117)
    garis("═",b=117)

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
        garis("═",b=117)
        try :
            pilih = int(input ("Masukkan pilihan >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                tambah_user()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                update_user()
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                hapus_user()
                break
            elif pilih == 4 :
                enter()
                clear()
                transisi()
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
    garis("═") 
    while True :
        try:
            nama = input ("masukkan nama lengkap user >> ")
            if len(nama) < 4 :
                raise ValueError ("nama minimal terdiri dari 4 karakter")
            elif nama in user :
                raise ValueError ("nama yang anda pilih sudah digunakan")
            else : 
                break
        except ValueError as error :
            termcolor.cprint (error, "red")
            enter()
            continue
    while True : 
        try : 
            nik = int(input ("masukkan NIK user >>"))
            nik = str(nik)
            if len (nik) < 6 or len (nik) > 10  :
                raise ValueError ("nik harus terdiri dari minimal 6 dan maksimal 10 karakter")
            else :
                break
        except ValueError as erorr:  
            termcolor.cprint (erorr, "red")
            enter()
            continue 
    while True : 
        try : 
            tanggal_lahir = input ("masukkan tanggal lahir user (contoh : 02-02-2001)>>")
            tanggal_lahir = dt.datetime.strptime(tanggal_lahir, "%d-%m-%Y") 
            tanggal_lahir = tanggal_lahir.strftime("%d-%m-%Y") 
            break
        except ValueError as erorr:  
            termcolor.cprint (erorr, "red")
            enter()
            continue 

    while True : 
        try : 
            nomorhp =  int(input ("Masukkan nomor HP (8123456789) >> "))
            nomorhp = str(nomorhp)
            if len (nomorhp) < 10:
                raise ValueError ("nomor HP minimal 10  ") 
            elif len (nomorhp) > 12:
                raise ValueError ("nomor HP minimal 10  ") 
            else :
                nomorhp = "+62" + nomorhp
                break 
        except ValueError as erorr:  
            termcolor.cprint (erorr, "red")
            enter()
    
            continue 
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
    garis("═") 
    with open ("dataadmin/datauser.csv", mode = "a", newline = "\n") as file : 
        border = ["nama lengkap", "nik","tanggal lahir", "nomor hp", "username", "password"] 
        writer = csv.DictWriter (file, fieldnames=border) 
        writer.writerow ( {"nama lengkap" : nama, "nik" :  nik,"tanggal lahir" : tanggal_lahir,"nomor hp" : nomorhp, "username" : username, "password" : password2} ) 
    os.makedirs(f"datauser/{nama}")
    with open (f"datauser/{nama}/mobil.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/motor.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/riwayat_titip_barang.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/titipbarang.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/booking.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/parkir.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    with open (f"datauser/{nama}/riwayat_parkir_user.csv", mode="w")as file:
        writer = csv.writer(file)
        writer.writerow("")
    termcolor.cprint ("User berhasil ditambahkan", "green") 
    enter()
    clear()
    transisi()
    monitoring_user()

def update_user():
    clear()
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    while True :
        cover(b=117)
        penampil_user()
        while True :
            try :
                pilih = (int (input("masukkan nomor user yang ingin diupdate >>")) - 1)
                if pilih < 0 or pilih >= len(list_username) :
                    raise ValueError ("inputan tidak valid")
                else :
                    break
            except ValueError as error :
                termcolor.cprint(error, "red")
                enter()
        border = ["NO","NAMA", "NIK", "TANGGAL LAHIR", "NOMOR HP", "USERNAME", "PASSWORD"]
        while True :
            clear()
            cover(b=117)
            garis("═",b=117)
            print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
            garis("═",b=117)
            print (f"|{pilih + 1:^4}|{user[pilih]:^20}|{nik[pilih]:^17}|{tanggal_lahir[pilih]:^17}|{nomor_hp[pilih]:^17}|{list_username[pilih]:^17}|{list_password[pilih]:^17}|")
            garis("═",b=117)
            try :
                bagian = input("bagian mana yang ingin diganti (nama / nik / tanggal / nomor / username / password) >> ").lower()
                if bagian == "nama":
                    raise ValueError ("nama user tidak boleh diganti")
                elif bagian == "nik":
                    while True :
                        try :
                            pengganti = int(input("masukkan kata sebagai pengganti >> "))
                            pengganti = str(pengganti)
                            if len (pengganti) < 6 or len (pengganti) > 10  :
                                raise ValueError ("nik harus terdiri dari minimal 6 dan maksimal 10 karatkter")
                            else :
                                break
                        except ValueError as error :
                            termcolor.cprint(error,"red")
                            enter()
                            continue
                    nik[pilih] = pengganti
                    break            
                elif bagian == "tanggal":
                    while True :
                        try :
                            pengganti = input ("masukkan tanggal lahir sebagai pengganti (contoh : 02-02-2001)>>")
                            pengganti = dt.datetime.strptime(pengganti, "%d-%m-%Y")
                            pengganti = pengganti.strftime("%d-%m-%Y")
                            break 
                        except ValueError as error:
                            termcolor.cprint(error,"red")
                            enter()
                            continue
                    tanggal_lahir[pilih] = pengganti
                    break            
                elif bagian == "nomor":
                    while True :
                        try :
                            pengganti = int(input ("Masukkan nomor HP sebagai pengganti (8123456789) >> "))
                            pengganti = str(pengganti)
                            if len (pengganti) < 10:
                                raise ValueError ("nomor HP minimal 10  ") 
                            elif len (pengganti) > 12:
                                raise ValueError ("nomor HP minimal 10  ") 
                            else :
                                pengganti = "+62" + pengganti
                                enter()
                                break
                        except ValueError as error :
                            termcolor.cprint(error,"red")
                            enter()
                            continue
                    nomor_hp[pilih] = pengganti
                    break            
                elif bagian == "username":
                    while True : 
                        try : 
                            pengganti = input("masukkan username pengganti pengganti >> ")
                            if len (pengganti) < 4 :
                                raise ValueError ("username harus lebih dari sama dengan 4 karakter")
                            elif pengganti in list_username: 
                                raise ValueError ("Username sudah digunakan") 
                            else : 
                                break 
                        except ValueError as erorr:  
                            termcolor.cprint (erorr, "red")
                            enter()
                            continue 
                    list_username[pilih] = pengganti
                    break            
                elif bagian == "password":
                    while True : 
                        try : 
                            pengganti = input("masukkan kata sebagai pengganti >> ")
                            if len(pengganti) < 8 : 
                                raise ValueError ("Password harus lebih dari 8 karakter dan tidak sama dengan username") 
                            else : 
                                break 
                        except ValueError as error: 
                            termcolor.cprint (error, "red") 
                            enter()
                            continue
                    list_password[pilih] = pengganti
                    break            
                else :
                    raise ValueError("bagian yang anda maksud tidak ditemukan")
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
        garis("═",b=117)
        print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
        garis("═",b=117)
        print (f"|{pilih + 1:^4}|{user[pilih]:^20}|{nik[pilih]:^17}|{tanggal_lahir[pilih]:^17}|{nomor_hp[pilih]:^17}|{list_username[pilih]:^17}|{list_password[pilih]:^17}|")
        garis("═",b=117)
        termcolor.cprint("data user telah berhasil di update","green")
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
                enter()
        if indikator == 1 :
            enter()
            clear()
            transisi()
            monitoring_user()
            break
        else :
            clear()
            transisi()
            continue
    
def hapus_user():
    clear()
    cover(b = 117) 
    border = ["NO","NAMA", "NIK", "TANGGAL LAHIR", "NOMOR HP", "USERNAME", "PASSWORD"]
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    print ("\n")
    print ("HAPUS USER\n\n".center(107))
    penampil_user()
    while True :
        try:
            pilih = (int (input ("masukkan nomer user yang ingin dihapus >> ")) - 1)
            if pilih < 0 or pilih >= len(user):
                raise ValueError ("inputan tidak valid")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
    clear()
    cover(b=117)
    garis("═",b=117)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
    garis("═",b=117)
    print (f"|{pilih + 1:^4}|{user[pilih]:^20}|{nik[pilih]:^17}|{tanggal_lahir[pilih]:^17}|{nomor_hp[pilih]:^17}|{list_username[pilih]:^17}|{list_password[pilih]:^17}|")
    garis("═",b=117)
    yakin = input ("apakah yakin ingin menghapus user ? y/n >> ").lower()
    if yakin == "y" :
        shutil.rmtree(f"datauser/{user[pilih]}")
        user.pop(pilih)
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
        transisi()
        monitoring_user()
#_________________MONITORING JUKIR________________________
def penampil_jukir():
    nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
    border = ["NO","NAMA", "NIK", "TELEPON", "USERNAME", "PASSWORD"]
    garis("═")
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^21}|{border[5]:^21}|")
    garis("═")
    for i in range (len(nama_jukir)):
        print (f"|{i+1:^4}|{nama_jukir[i]:^20}|{nik_jukir[i]:^17}|{telepon_jukir[i]:^17}|{username_jukir[i]:^21}|{password_jukir[i]:^21}|")
        garis("═")
def monitoring_jukir():
    clear()
    cover()
    print ("")
    print ("MONITORING JUKIR\n".center(107))
    penampil_jukir()
    print ("")
    garis ("═")
    print ("""   
    1. TAMBAH JUKIR
    2. UPDATE DATA JUKIR
    3. CEK ABSENSI DAN KONTRIBUSI JUKIR
    4. HAPUS DATA JUKIR
    5. KEMBALI KE MENU ADMIN 
    """)
    garis("═")
    while True :
        try :
            pilih = int(input("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                tambah_jukir()
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                update_jukir()
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                cek_absensi_kontribusi_jukir()
            elif pilih == 4 :
                enter()
                clear()
                transisi()
                hapus_jukir()
            elif pilih == 5 :
                enter()
                clear()
                transisi()
                menu_admin()
            else :
                raise ValueError ("opsi yang nada pilih tidak tersedia")
        except ValueError as error:
            termcolor.cprint(error,"red")
            enter()
            continue 

def tambah_jukir ():
    nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
    clear()
    cover()
    while True :
        try :
            nama = input ("masukkan nama jukir >> ")
            if len (nama) < 4 or nama in nama_jukir :
                raise ValueError ("nama jukir tidak tersedia, atau sudah digunakan")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    while True :
        try :
            nik = int(input ("masukkan nik >> "))
            nik = str(nik)
            if len (nik) < 6 or len (nik) > 10  :
                raise ValueError ("nik harus terdiri dari minimal 6 dan maksimal 10 karakter")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    while True :
        try :
            telpon =  input ("masukkan nomor telpon (83812345678) >> ")
            telpon = str(telpon)
            if len (telpon) < 10:
                raise ValueError ("nomor HP minimal 10  ") 
            elif len (telpon) > 12:
                raise ValueError ("nomor HP minimal 10  ") 
            else :
                telpon = "+62" + telpon
                break 
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    while True:
        try:
            username = input ("buat username jukir >> ")
            if len(username) < 5 or username in username_jukir :
                raise ValueError ("username tidak tersedia, atau kurang dari 5 karakter")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    while True :
        try:
            password = input ("buat password jukir >> ")
            if len(password) < 8 :
                raise ValueError ("password kurang dari 8 karakter")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    garis("═")
    with open("dataadmin/loginjukir.csv", mode="a", newline="\n") as file:
        border = ["nama", "nik", "nomor telepon", "username", "password"]
        writer = csv.DictWriter(file, fieldnames=border)
        writer.writerow({"nama" : nama, "nik" : nik, "nomor telepon": telpon,"username":username, "password":password})
    termcolor.cprint("jukir berhasil ditambahkan", "green")
    enter()
    clear()
    transisi()
    monitoring_jukir()

def update_jukir():
    nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
    clear()
    cover()
    print ("")
    print ("UPDATE DATA JUKIR\n".center(107))
    penampil_jukir()
    while True :
        try :
            pilih = (int (input("masukkan nomor user yang ingin diupdate >>")) - 1)
            break
        except ValueError :
            termcolor.cprint("masukkan pilihan berupa angka", "red")
    clear()
    cover()
    border = ["NO","NAMA", "NIK", "TELEPON", "USERNAME", "PASSWORD"]
    garis("═")
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^21}|{border[5]:^21}|")
    garis("═")
    print (f"|{pilih+1:^4}|{nama_jukir[pilih]:^20}|{nik_jukir[pilih]:^17}|{telepon_jukir[pilih]:^17}|{username_jukir[pilih]:^21}|{password_jukir[pilih]:^21}|")
    garis("═")
    while True :
        try:
            bagian = input ("masukkan bagian yang ingin diupdate (nama/nik/telepon/username/password)>> ").lower()
            if bagian not in ["nama", "nik", "telepon", "username", "password"]:
                raise ValueError ("masukkan bagian yang ada")
            elif bagian == "nama" :
                raise ValueError ("nama tidak boleh diganti")
            elif bagian == "nik" :
                while True :
                    try :
                        pengganti = input ("masukkan nik pengganti >> ")
                        pengganti = str(pengganti)
                        if len (pengganti) < 6 or len (pengganti) > 10  :
                            raise ValueError ("nik harus terdiri dari minimal 6 dan maksimal 10 karakter")
                        else :
                            break
                    except ValueError as error :
                        termcolor.cprint(error,"red")
                        enter()
                        continue
                nik_jukir[pilih] = pengganti
                break
            elif bagian == "telepon" :
                while True :
                    try :
                        pengganti = input ("masukkan nomor telepon pengganti  >> ")
                        pengganti = str(pengganti)
                        if len (pengganti) < 10:
                            raise ValueError ("nomor HP minimal 10  ") 
                        elif len (pengganti) > 12:
                            raise ValueError ("nomor HP minimal 10  ") 
                        else :
                            pengganti = "+62" + pengganti
                            break 
                    except ValueError as error :
                        termcolor.cprint(error,"red")
                        enter()
                        continue
                telepon_jukir[pilih] = pengganti
                break
            elif bagian == "username" :
                raise ValueError ("username tidak boleh diganti")
            elif bagian == "password" :
                while True :
                    try:
                        pengganti = input ("masukkan password pengganti  >> ")
                        if len(pengganti) < 8 :
                            raise ValueError ("password kurang dari 8 karakter")
                        else :
                            break
                    except ValueError as error :
                        termcolor.cprint(error,"red")
                        enter()
                        continue
                password_jukir[pilih] = pengganti
                break
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue
    with open ("dataadmin/loginjukir.csv", mode = "w", newline="\n") as file :
        writer = csv.writer(file)
        for i in range (len(nama_jukir)) :
            writer.writerow([nama_jukir[i], nik_jukir[i], telepon_jukir[i], username_jukir[i], password_jukir[i]])
    termcolor.cprint("data berhasil diupdate", "green")
    while True :
        try :
            lagi = input ("apakah ingin mengupdate data jukir lagi (y/n)>> ").lower()
            if lagi == "y":
                enter()
                clear()
                transisi()
                update_jukir()
                break
            elif lagi == "n" :
                enter()
                clear()
                transisi()
                monitoring_jukir()
            else :
                raise ValueError("inputan yang anda masukkan tidak valid")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue

def penampung_kehadiran_jukir_admin():
    tampungan_kehadiran_jukir_1 = []
    tampungan_kehadiran_jukir_2 = []
    nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
    for i in username_jukir:
        with open (f"datajukir/kehadiran{i}.csv", mode="r") as file:
            reader = csv.reader(file)
            for i in reader :
                if i == [] :
                    continue
                elif i[0] == nama_jukir[0]:
                    tampungan_kehadiran_jukir_1.append(i)
                elif i[0] == nama_jukir[1]:
                    tampungan_kehadiran_jukir_2.append(i)
    return tampungan_kehadiran_jukir_1, tampungan_kehadiran_jukir_2


def cek_absensi_kontribusi_jukir():
    nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
    diparkjirkan_jukir_1,diparkjirkan_jukir_2 = penampung_diparkirkan()
    tampungan_kehadiran_jukir_1, tampungan_kehadiran_jukir_2 = penampung_kehadiran_jukir_admin()
    clear()
    cover()
    print ("")
    print ("KEHADIRAN DAN KONTRIBUSI JUKIR\n".center(107))
    garis("═")
    border = ["NO","NAMA JUKIR", "JUMLAH KEHADIRAN", "JUMLAH KONTRIBUSI"]
    garis("═")
    print (f"|{border[0]:^4}|{border[1]:^39}|{border[2]:^29}|{border[3]:^30}|")
    garis("═")
    print (f"|{"1":^4}|{nama_jukir[0]:^39}|{len(tampungan_kehadiran_jukir_1):^29}|{diparkjirkan_jukir_1[0]:^30}|")
    garis("═")
    print (f"|{"2":^4}|{nama_jukir[1]:^39}|{len(tampungan_kehadiran_jukir_2):^29}|{diparkjirkan_jukir_2[0]:^30}|")
    garis("═")
    garis("═")
    print ("""
        1. LIHAT RIWAYAT KEHADIRAN JUKIR
        2. KEMBALI KE MENU 
""")
    garis("═")
    while True :
        try:
            pilih = int (input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                riwayat_kehadiran_jukir()
            elif pilih == 2 : 
                enter()
                clear()
                transisi()
                monitoring_jukir()
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue

def riwayat_kehadiran_jukir ():
    nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
    tampungan_kehadiran_jukir_1, tampungan_kehadiran_jukir_2 = penampung_kehadiran_jukir_admin()
    clear()
    cover()
    print ("")
    print ("RIWAYAT KEHADIRAN JUKIR\n".center(107))
    garis("═")
    border = ["NO","NAMA JUKIR", "USERNAME JUKIR", "WAKTU KEHADIRAN"]
    garis("═")
    print (f"|{border[0]:^4}|{border[1]:^39}|{border[2]:^25}|{border[3]:^34}|")
    garis("═")
    for i in range (len(tampungan_kehadiran_jukir_1)) :
        print (f"|{i+1:^4}|{tampungan_kehadiran_jukir_1[i][0]:^39}|{username_jukir[0]:^25}|{tampungan_kehadiran_jukir_1[i][1]:^34}|")
        garis("═")
    garis("═")
    print ("""
        1. LIHAT KEHADIRAN JUKIR LAIN
        2. KEMBALI KE MENU
""")
    
    garis("═")
    while True:
        try:
            pilih = int (input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                clear()
                cover()
                print ("")
                print ("RIWAYAT KEHADIRAN JUKIR\n".center(107))
                garis("═")
                border = ["NO","NAMA JUKIR", "USERNAME JUKIR", "WAKTU KEHADIRAN"]
                garis("═")
                print (f"|{border[0]:^4}|{border[1]:^39}|{border[2]:^25}|{border[3]:^34}|")
                garis("═")
                for i in range (len(tampungan_kehadiran_jukir_2)) :
                    print (f"|{i+1:^4}|{tampungan_kehadiran_jukir_2[i][0]:^39}|{username_jukir[1]:^25}|{tampungan_kehadiran_jukir_2[i][1]:^34}|")
                    garis("═")
                garis("═")
                enter()
                clear()
                transisi()
                cek_absensi_kontribusi_jukir()
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                cek_absensi_kontribusi_jukir()
            else :
                raise ValueError ("opsi yang dipilih tidak tersedia")
        except ValueError as error:
            termcolor.cprint(error, "red")
            enter()
            continue



def hapus_jukir():
    nama_jukir, nik_jukir, telepon_jukir, username_jukir, password_jukir = penampung_jukir()
    clear()
    cover()
    print ("")
    print ("HAPUS DATA JUKIR\n".center(107))
    penampil_jukir()
    while True :
        try :
            pilih = (int (input("masukkan nomor user yang ingin dihapus >>")) - 1)
            break
        except ValueError :
            termcolor.cprint("masukkan pilihan berupa angka", "red")
    clear()
    cover()
    border = ["NO","NAMA", "NIK", "TELEPON", "USERNAME", "PASSWORD"]
    garis("═")
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^21}|{border[5]:^21}|")
    garis("═")
    print (f"|{pilih+1:^4}|{nama_jukir[pilih]:^20}|{nik_jukir[pilih]:^17}|{telepon_jukir[pilih]:^17}|{username_jukir[pilih]:^21}|{password_jukir[pilih]:^21}|")
    garis("═")
    while True :
        try :
            yakin = input("apakah yakin untuk menghapus data jukir (y/n) >> ").lower()
            if yakin == "y" :
                nama_jukir.pop(pilih)
                nik_jukir.pop(pilih)
                telepon_jukir.pop(pilih)
                username_jukir.pop(pilih)
                password_jukir.pop(pilih)
                with open ("dataadmin/loginjukir.csv", mode = "w", newline="\n") as file :
                    writer = csv.writer(file)
                    for i in range (len(nama_jukir)) :
                        writer.writerow([nama_jukir[i], nik_jukir[i], telepon_jukir[i], username_jukir[i], password_jukir[i]])
                termcolor.cprint("data jukir berhasil dihapus", "green")
                enter()
                clear()
                transisi()
                monitoring_jukir()
                break
            elif yakin == "n":
                enter()
                clear()
                transisi()
                monitoring_jukir()
                break
            else : 
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error:
            termcolor.cprint(error, "red")
            enter()
            continue


#________________________________________________________________MONITOR KENDARAAN MENU ADMIN_______________________________________________________________
def monitoring_kendaraan_user():
    clear()
    cover(b=128)
    print ("")
    print ("DAFTAR MOBIL USER\n".center(128))
    penampil_mobil_admin()
    print ("")
    print ("DAFTAR MOTOR USER\n".center(128))
    penampil_motor_admin()
    print ("")
    garis ("═", b =128)
    print ("""
        1. DAFTARKAN KENDARAAN USER
        2. HAPUS KENDARAAN USER
        3. KEMBALI KE MENU ADMIN
    """)
    garis ("═", b =128)
    pilih = int (input ("masukkan opsi yang dipilih >> "))
    garis ("=", b =128)
    if pilih == 1 :
        enter()
        clear()
        transisi()
        daftarkan_kendaraan_admin()
    elif pilih == 2 :
        enter()
        print ("""
        1. HAPUS DATA MOBIL USER
        2. HAPUS DATA MOTOR USER
        3. KEMBALI KE MENU MONITORING KENDARAAN USER
""")
        garis ("═", b =128)
        pilih = int (input ("masukkan opsi yang dipilih >> "))
        garis ("═", b =128)
        if pilih == 1 :
            enter()
            clear()
            transisi()
            hapus_mobil_admin()
        elif pilih == 2 :
            enter()
            clear()
            transisi()
            hapus_motor_admin()
        elif pilih == 3 :
            enter()
            clear()
            transisi()
            monitoring_kendaraan_user()
    elif pilih == 3 :
        enter()
        clear()
        transisi()
        menu_admin()

def daftarkan_kendaraan_admin():
    clear()
    cover()
    print ("")
    print ("DAFTARKAN KENDARAAN USER\n".center(107))
    garis("═")
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    jenis = ["mobil", "motor"]
    while True:
        try:
            atas_nama = input("masukkan pemilik kendaraan >> ").lower()
            if atas_nama not in user :
                raise ValueError("nama tidak terdaftar")    
            else :
                break
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue
    while True :
        try :
            jenis_kendaraan = input("masukkan jenis kendaraan(mobil/motor) >> ").lower()
            if jenis_kendaraan not in jenis :
                raise ValueError ("jenis kendaraan yang anda masukkan tidak sesuai","red")
            else:
                break
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue
    plat_nomor = input ("masukkan plat nomor kendaraan (P 1234 VV) >> ")
    tipe_kendaraan = input ("masukkan tipe kendaraan (Toyota Avanza / Honda Vario) >> ")
    tahun_kendaraan = input ("masukkan tahun kendaraan (2020) >> ")
    warna_kendaraan = input ("masukkan warna kendaraan (merah/abu-abu) >> ")
    garis("═")
    with open (f"datauser/{atas_nama}/{jenis_kendaraan}.csv", mode="a", newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow([atas_nama,jenis_kendaraan,plat_nomor, tipe_kendaraan, tahun_kendaraan, warna_kendaraan])
    termcolor.cprint("kendaraan berhasil di inputkan","green")
    enter()
    clear()
    monitoring_kendaraan_user()
#__________________________________________________________________________ MOBIL _____________________________________________________________________________________
def penampung_mobil_admin():
    atas_nama =[]
    jenis_kendaraan = []
    plat_nomor = []
    tipe_kendaraan = []
    tahun_kendaraan = []
    warna_kendaraan = []
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    for i in user:
        with open (f"datauser/{i}/mobil.csv", mode="r") as file :
            reader = csv.reader(file)
            for i in reader:
                if i == []:
                    continue
                else :
                    atas_nama.append(i[0])
                    jenis_kendaraan.append(i[1])
                    plat_nomor.append(i[2])
                    tipe_kendaraan.append(i[3])
                    tahun_kendaraan.append(i[4])
                    warna_kendaraan.append(i[5])
    return atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan, warna_kendaraan 

def penampil_mobil_admin():
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_mobil_admin()
    border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
    garis("═",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("═",b=128)
    if len(atas_nama) == 0 :
        print ("BELUM ADA KENDARAAN TERDAFTAR".center(128))
        garis("═",b=128)
    else :
        for i in range (len(jenis_kendaraan)):
            print (f"|{i+1:^3} |{atas_nama[i]:^25}|{jenis_kendaraan[i]:^17}|{plat_nomor[i]:^15}|{tipe_kendaraan[i]:^25}|{tahun_kendaraan[i]:^17}|{warna_kendaraan[i]:^17}|")
            garis("═",b=128)

def hapus_mobil_admin():
    clear()
    cover(b=128)
    indikator_nama = []
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan, warna_kendaraan = penampung_mobil_admin()
    print ("\n")
    print ("HAPUS DATA MOBIL USER\n".center(128))
    penampil_mobil_admin()
    pilih = (int(input("masukkan nomor data yang ingin dihapus >> ")) - 1 )
    garis("═",b=128)
    clear()
    cover(b=128)
    print ("")
    print ("HAPUS DATA MOBIL USER\n".center(128))
    border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
    garis("═",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("═",b=128)
    print (f"|{pilih + 1:^3} |{atas_nama[pilih]:^25}|{jenis_kendaraan[pilih]:^17}|{plat_nomor[pilih]:^15}|{tipe_kendaraan[pilih]:^25}|{tahun_kendaraan[pilih]:^17}|{warna_kendaraan[pilih]:^17}|")
    garis("═",b=128)
    yakin = input ("apkah yakin ingin menghapus data ini [y/n] >> ").lower()
    garis("=",b=128)
    if yakin == "y":
        indikator_nama.append(atas_nama[pilih])
        atas_nama.pop(pilih)
        jenis_kendaraan.pop(pilih)
        plat_nomor.pop(pilih)
        tipe_kendaraan.pop(pilih)
        tahun_kendaraan.pop(pilih) 
        warna_kendaraan.pop(pilih)
    elif yakin == "n":
        enter()
        clear()
        monitoring_kendaraan_user()
    with open (f"datauser/{indikator_nama[0]}/mobil.csv", mode = "w", newline = "\n") as file:
        writer = csv.writer(file)
        for i in range (len(atas_nama)):
            if atas_nama[i] == indikator_nama[0]:
                writer.writerow ([atas_nama[i], jenis_kendaraan[i], plat_nomor[i],tipe_kendaraan[i],tahun_kendaraan[i],warna_kendaraan[i]])
            else :
                continue
    termcolor.cprint("Data mobil berhasil dihapus", "green")
    enter()
    clear()
    transisi()
    monitoring_kendaraan_user()
#______________________________________________________________________________ MOTOR _____________________________________________________________________________________
def penampung_motor_admin():
    atas_nama =[]
    jenis_kendaraan = []
    plat_nomor = []
    tipe_kendaraan = []
    tahun_kendaraan = []
    warna_kendaraan = []
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    for i in user:
        with open (f"datauser/{i}/motor.csv", mode="r") as file :
            reader = csv.reader(file)
            for i in reader:
                if i == [] :
                    continue
                else :
                    atas_nama.append(i[0])
                    jenis_kendaraan.append(i[1])
                    plat_nomor.append(i[2])
                    tipe_kendaraan.append(i[3])
                    tahun_kendaraan.append(i[4])
                    warna_kendaraan.append(i[5])
    return atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan, warna_kendaraan

def penampil_motor_admin():
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan,warna_kendaraan = penampung_motor_admin()
    border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
    garis("═",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("═",b=128)
    for i in range (len(jenis_kendaraan)):
        print (f"|{i+1:^3} |{atas_nama[i]:^25}|{jenis_kendaraan[i]:^17}|{plat_nomor[i]:^15}|{tipe_kendaraan[i]:^25}|{tahun_kendaraan[i]:^17}|{warna_kendaraan[i]:^17}|")
        garis("=",b=128)

def hapus_motor_admin():
    clear()
    cover(b=128)
    indikator_nama = []
    atas_nama,jenis_kendaraan,plat_nomor,tipe_kendaraan,tahun_kendaraan, warna_kendaraan = penampung_motor_admin()
    print ("\n")
    print ("HAPUS DATA MOTOR USER\n".center(128))
    penampil_motor_admin()
    pilih = (int(input("masukkan nomor data yang ingin dihapus >> ")) - 1 )
    garis("═",b=128)
    clear()
    cover(b=128)
    print ("")
    print ("HAPUS DATA MOTOR USER\n".center(128))
    border = ["NO","NAMA PEMILIK","JENIS KENDARAAN","PLAT NOMOR","TIPE KENDARAAN","TAHUN KENDARAAN","WARNA KENDARAAN"]
    garis("═",b=128)
    print (f"|{border[0]:^4}|{border[1]:^25}|{border[2]:^17}|{border[3]:^15}|{border[4]:^25}|{border[5]:^17}|{border[6]:^17}|")
    garis("═",b=128)
    print (f"|{pilih + 1:^3} |{atas_nama[pilih]:^25}|{jenis_kendaraan[pilih]:^17}|{plat_nomor[pilih]:^15}|{tipe_kendaraan[pilih]:^25}|{tahun_kendaraan[pilih]:^17}|{warna_kendaraan[pilih]:^17}|")
    garis("═",b=128)
    yakin = input ("apkah yakin ingin menghapus data ini [y/n] >> ").lower()
    garis("=",b=128)
    if yakin == "y":
        indikator_nama.append(atas_nama[pilih])
        atas_nama.pop(pilih)
        jenis_kendaraan.pop(pilih)
        plat_nomor.pop(pilih)
        tipe_kendaraan.pop(pilih)
        tahun_kendaraan.pop(pilih) 
        warna_kendaraan.pop(pilih)
    elif yakin == "n":
        enter()
        clear()
        transisi()
        monitoring_kendaraan_user()
    with open (f"datauser/{indikator_nama[0]}/motor.csv", mode = "w", newline = "\n") as file:
        writer = csv.writer(file)
        for i in range (len(atas_nama)):
            if atas_nama[i] == indikator_nama[0]:
                writer.writerow ([atas_nama[i], jenis_kendaraan[i], plat_nomor[i],tipe_kendaraan[i],tahun_kendaraan[i],warna_kendaraan[i]])
            else :
                continue
    termcolor.cprint("Data motor berhasil dihapus", "green")
    enter()
    clear()
    transisi()
    monitoring_kendaraan_user()
#____________________________________________________________________BOOKING PARKIR USER_________________________________________________________
def monitoring_parkir():
    clear()
    cover()
    print ("")
    print ("MONITORING PARKIR\n".center(107))
    garis("═")
    print ("""
        1. KONFIRMASI CHECKIN DAN CHECKOUT
        2. BOOKING USER 
        3. KETERSEDIAAN PARKIR
        4. KENDARAAN TERPARKIR
        5. KEMBALI KE MENU 
    """)
    garis("═")
    while True :
        try :
            pilih = int(input("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                konfirmasi_checkin_checkout()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                booking_admin()
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                ketersediaan_parkir_admin()
                break
            elif pilih == 4 :
                enter()
                clear()
                transisi()
                Kendaraan_terparkir_admin()
                break
            elif pilih == 5 :
                enter()
                clear()
                transisi()
                menu_admin()
                break
            else :
                raise ValueError ("opsi yang dipilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue

def konfirmasi_checkin_checkout():
    clear()
    cover(b=121)
    print ("")
    print ("MENU KONFIRMASI\n".center(121))
    garis("═",b=121)
    print ("""
        1. KONFIRMASI CHECKIN
        2. KONFIRMASI CHECKOUT
        3. KEMBALI KE MENU
""")
    garis("═",b=121)
    while True :
        try :
            pilih = int(input("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                konfirmasi_checkin()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                konfirmasi_checkout()
                pass
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                monitoring_parkir()
                pass
            else :
                raise ValueError ("opsi yang dipilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error, "red")
            enter()
            continue

def penampung_konfirmasi_checkin():
    kendaraan_checkin =[]
    with open (f"dataadmin/konfirmasicheckin.csv", mode="r") as file :
        reader = csv.reader(file)
        for i in reader :
            if i == [] :
                continue
            else :
                kendaraan_checkin.append(i)
    return kendaraan_checkin

def penampil_konfirmasi_checkin():
    kendaraan_checkin = penampung_konfirmasi_checkin()
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "WAKTU CHECK IN"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (kendaraan_checkin) == 0 :
        print ("TIDAK ADA YANG PERLU DI KONFIRMASI".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(kendaraan_checkin) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)

def konfirmasi_checkin():
    clear()
    cover(b=121)
    kendaraan_checkin = penampung_konfirmasi_checkin()
    print ("")
    print ("KONFIRMASI CHECKIN\n".center(121))
    garis("═",b=121)
    penampil_konfirmasi_checkin()
    garis("═",b=121)
    if len (kendaraan_checkin) == 0 :
        enter()
        clear()
        transisi()
        konfirmasi_checkin_checkout()
    else :
        while True :
            try :
                pilih_konfirmasi = int(input("pilih nomor kendaraan yang ingin di konfirmasi >> ")) - 1
                if pilih_konfirmasi >= 0 and pilih_konfirmasi < len(kendaraan_checkin):
                    break
                else : 
                    raise ValueError ("inputan yang anda masukkan tidak valid")
            except ValueError as error :
                termcolor.cprint(error, "red")
                enter()
                continue
        while True :
            try :
                yakin = input ("apakah yakin untuk memberikan konfirmasi (y/n) >> ").lower()
                if yakin == "y" :
                    break
                elif yakin == "n" :
                    enter()
                    clear()
                    transisi()
                    konfirmasi_checkin_checkout()
            except ValueError as error :
                termcolor.cprint(error, "red")
                enter()
                continue
        if kendaraan_checkin[pilih_konfirmasi][2] == "mobil":
            slot_parkir = penampung_slot_parkir_mobil()
        elif kendaraan_checkin[pilih_konfirmasi][2] == "motor":
            slot_parkir = penampung_slot_parkir_motor()
        for i in range (len(slot_parkir[0])):
            if kendaraan_checkin[pilih_konfirmasi][1] == slot_parkir[0][i]:
                slot_parkir[1][i] = "TERISI"
        with open (f"dataadmin/slotparkir{kendaraan_checkin[pilih_konfirmasi][2]}.csv",mode="w",newline="\n") as file : 
            writer= csv.writer(file)
            writer.writerows(slot_parkir)
        with open (f"datauser/{kendaraan_checkin[pilih_konfirmasi][0]}/parkir.csv",mode="a",newline="\n") as file : 
            writer= csv.writer(file)
            writer.writerow(kendaraan_checkin[pilih_konfirmasi])
        kendaraan_checkin.pop(pilih_konfirmasi)
        with open (f"dataadmin/konfirmasicheckin.csv",mode="w",newline="\n") as file : 
            writer= csv.writer(file)
            writer.writerows(kendaraan_checkin)
        termcolor.cprint("konfirmasi berhasil", "green")
        enter()
        clear()
        transisi()
        konfirmasi_checkin_checkout()

def penampung_konfirmasi_checkout():
    kendaraan_keluar = []
    with open (f"dataadmin/konfirmasicheckout.csv", mode="r") as file:
        reader = csv.reader(file)
        for i in reader :
            if i == []:
                continue
            else :
                kendaraan_keluar.append(i)
    return kendaraan_keluar

def penampil_konfirmasi_checkout():
    kendaraan_checkout = penampung_konfirmasi_checkout()
    total_harga =[]
    for i in kendaraan_checkout:
        total = f"{int(i[7]):,}"
        total_harga.append(total)
    border = ["NO", "PEMILIK", "BLOK", "JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "WAKTU CHECK IN", "WAKTU CHECK OUT", "TOTAL TAGIHAN"]
    garis("═",b=157)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^8}|{border[3]:^20}|{border[4]:^15}|{border[5]:^20}|{border[6]:^20}|{border[7]:^20}|{border[8]:^20}|")
    garis("═",b=157)
    if len(kendaraan_checkout) == 0:
        print ("TIDAK ADA YANG PERLU DI KONFIRMASI".center(157))
        garis("═",b=157)
    else :
        for a,i in enumerate(kendaraan_checkout):
            print (f"|{a+1:^4}|{i[0]:^20}|{i[1]:^8}|{i[2]:^20}|{i[3]:^15}|{i[4]:^20}|{i[5]:^20}|{i[6]:^20}|{"Rp."+total_harga[a]:^20}|")
            garis("═",b=157)

def konfirmasi_checkout():
    clear()
    cover(b=157)
    kendaraan_checkout = penampung_konfirmasi_checkout()
    print ("")
    print ("KONFIRMASI CHECKIN\n".center(157))
    garis("═",b=157)
    penampil_konfirmasi_checkout()
    garis("═",b=157)
    if len (kendaraan_checkout) == 0 :
        enter()
        clear()
        transisi()
        konfirmasi_checkin_checkout()
    else :
        while True :
            try :
                pilih_konfirmasi = int(input("pilih nomor kendaraan yang ingin di konfirmasi >> ")) - 1
                if pilih_konfirmasi >= 0 and pilih_konfirmasi < len(kendaraan_checkout):
                    break
                else : 
                    raise ValueError ("inputan yang anda masukkan tidak valid")
            except ValueError as error :
                termcolor.cprint(error, "red")
                enter()
                continue
        while True :
            try :
                yakin = input ("apakah yakin untuk memberikan konfirmasi (y/n) >> ").lower()
                if yakin == "y" :
                    break
                elif yakin == "n" :
                    enter()
                    clear()
                    transisi()
                    konfirmasi_checkin_checkout()
            except ValueError as error :
                termcolor.cprint(error, "red")
                enter()
                continue
        if kendaraan_checkout[pilih_konfirmasi][2] == "mobil":
            slot_parkir = penampung_slot_parkir_mobil()
        elif kendaraan_checkout[pilih_konfirmasi][2] == "motor":
            slot_parkir = penampung_slot_parkir_motor()
        for i in range (len(slot_parkir[0])):
            if kendaraan_checkout[pilih_konfirmasi][1] == slot_parkir[0][i]:
                slot_parkir[1][i] = "-"
        with open (f"dataadmin/slotparkir{kendaraan_checkout[pilih_konfirmasi][2]}.csv",mode="w",newline="\n") as file : 
            writer= csv.writer(file)
            writer.writerows(slot_parkir)
        with open ("dataadmin/riwayat_parkir_keseluruhan.csv",mode="a",newline="\n") as file : 
            writer= csv.writer(file)
            writer.writerow(kendaraan_checkout[pilih_konfirmasi])
        with open (f"datauser/{kendaraan_checkout[pilih_konfirmasi][0]}/riwayat_parkir_user.csv",mode="a",newline="\n") as file : 
            writer= csv.writer(file)
            writer.writerow(kendaraan_checkout[pilih_konfirmasi])
        kendaraan_checkout.pop(pilih_konfirmasi)
        with open (f"dataadmin/konfirmasicheckout.csv",mode="w",newline="\n") as file : 
            writer= csv.writer(file)
            writer.writerows(kendaraan_checkout)
        termcolor.cprint("konfirmasi berhasil", "green")
        enter()
        clear()
        transisi()
        konfirmasi_checkin_checkout()

def penampil_booking_parkir_motor_admin():
    booking_parkir_motor, booking_parkir_mobil = penampung_booking_parkir_seluruh()
    booking_parkir_motor.extend(booking_parkir_mobil)
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "TANGGAL TERBOOKING"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (booking_parkir_motor) == 0 :
        print ("BELUM ADA KENDARAAN YANG TERDAFTAR".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(booking_parkir_motor) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)

def booking_admin():
    booking_parkir_motor, booking_parkir_mobil = penampung_booking_parkir_seluruh()
    clear()
    cover(b=121)
    print ("")
    print ("BOOKING PARKIR\n".center(121))
    garis("═",b=121)
    penampil_booking_parkir_motor_admin()
    garis("═",b=121)
    print ("""
        1. HAPUS BOOKING
        2. KEMBALI KE MENU
""")
    garis("═",b=121)
    while True :
        try:
            pilih = int(input("masukkan opsi yang dipilih >>"))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                hapus_booking_admin()
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                monitoring_parkir()
                break
            else : 
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue

def penampung_booking_admin(nama_user):
    booking = []
    with open (f"datauser/{nama_user}/booking.csv",mode="r") as file:
        reader = csv.reader(file)
        for i in reader:
            if i == []:
                continue
            else :
                booking.append(i)
    return booking

def penampil_booking_admin(nama_user):
    booking = penampung_booking_admin(nama_user)
    border = ["NO","PEMILIK", "BLOK","JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "TANGGAL TERBOOKING"]
    garis("═",b=121)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^10}|{border[3]:^19}|{border[4]:^20}|{border[5]:^20}|{border[6]:^20}|")
    garis("═",b=121)
    if len (booking) == 0 :
        print ("BELUM ADA KENDARAAN YANG TERDAFTAR".center(121))
        garis("═",b=120)
    else :
        for a,i in enumerate(booking) :
            print (f"|{a + 1:^4}|{i[0]:^20}|{i[1]:^10}|{i[2]:^19}|{i[3]:^20}|{i[4]:^20}|{i[5]:^20}|")
            garis("═",b=121)

def hapus_booking_admin():
    clear()
    cover(b=121)
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    print ("")
    print ("HAPUS BOOKING PARKIR\n".center(121))
    garis("═",b=121)
    penampil_booking_parkir_motor_admin()
    garis("═",b=121)
    while True :
        try:
            nama_user = input ("masukkan nama pemilik booking >> ").lower()
            if nama_user in user :
                booking = penampung_booking_admin(nama_user)
                break
            else : 
                raise ValueError ("nama pemilik tidak terdaftar")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    garis("═",b=121)
    penampil_booking_admin(nama_user)
    garis("═",b=121)
    while True :
        try:
            pilih_booking = int (input ("masukkan booking yang ingin dihapus >> ")) - 1
            if pilih_booking >= 0 and pilih_booking < len (booking):
                yakin = input ("apakah yakin untuk menghapus data booking (y/n) >> ").lower()
                if yakin == "y" :
                    booking.pop(pilih_booking)
                    with open (f"datauser/{nama_user}/booking.csv",mode="w", newline="\n") as file:
                        writer = csv.writer(file)
                        writer.writerows(booking)
                    termcolor.cprint("booking telah berhasil dihapus", "green")
                    enter()
                    clear()
                    transisi()
                    booking_admin()
                elif yakin == "n" :
                    enter()
                    clear()
                    transisi()
                    booking_admin()
                    break
                else :
                    raise ValueError ("input tidak valid")
            else :
                raise ValueError ("inputan tidak valid")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue

def ketersediaan_parkir_admin():
    clear()
    cover(b=110)
    print ("")
    print ("KETERSEDIAAN PARKIR".center(110))
    garis("═",b=110)
    print ("""
        1. LIHAT KETERSEDIAAN PARKIR MOTOR
        2. LIHAT KETERSEDIAAN PARKIR MOBIL
        3. KEMBALI KE MENU
""")
    garis("═",b=110)
    while True :
        try:
            pilih = int(input("masukkan opsi yang dipilih >>"))
            if pilih == 1 :
                enter()
                slot_parkir = penampung_slot_parkir_motor()
                jenis_kendaraan = "motor"
                penampil_slot_parkir_motor()
                garis("═",b=110)
                break
            elif pilih == 2 :
                enter()
                slot_parkir = penampung_slot_parkir_mobil()
                jenis_kendaraan = "mobil"
                penampil_slot_parkir_mobil()
                garis("═",b=110)
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                monitoring_parkir()
            else : 
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    print ("""
        1. UPDATE SLOT PARKIR 
        2. KEMBALI KE MENU
""")
    garis("═",b=110)
    ulang = 0
    while True :
        try:
            indikator_1 = 0
            pilih = int(input("masukkan opsi yang dipilih >>"))
            if pilih == 1 :
                while True :
                    try :
                        indikator_2 = 0
                        slot = input ("masukkan slot parkir yang ingin di ganti >> ").capitalize()
                        for i in range (len(slot_parkir[0])) :
                            if slot == slot_parkir[0][i] :
                                garis("═",b=110)
                                print ("""
        1. -
        2. BOOKED 
        3. TERISI 
                                """)
                                garis("═",b=110)
                                while True :
                                    try:
                                        pilih = int(input("masukkan opsi yang dipilih >>"))
                                        if pilih == 1 :
                                            pengganti = "-"
                                            break
                                        elif pilih == 2 :
                                            pengganti = "BOOKED"
                                            break
                                        elif pilih == 3 :
                                            pengganti = "TERISI"
                                            break
                                        else :
                                            raise ValueError ("opsi yang anda pilih tidak tersedia")
                                    except ValueError as error :
                                        termcolor.cprint(error,"red")
                                        enter()
                                        continue
                                slot_parkir[1][i] = pengganti
                                indikator_2 += 1
                                with open(f"dataadmin/slotparkir{jenis_kendaraan}.csv", mode="w",newline="\n") as file :
                                    writer = csv.writer(file)
                                    writer.writerows(slot_parkir)
                                break
                            else : 
                                continue
                        if indikator_2 == 1 :
                            indikator_1 += 1
                            break
                        if indikator_2 == 0 :
                            raise ValueError ("slot yang anda masukkan tidak tersedia")
                    except ValueError as error :
                        termcolor.cprint(error,"red")
                        enter()
                        continue
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                monitoring_parkir()
                break
            else : 
                raise ValueError ("opsi yang anda pilih tidak tersedia")

            if indikator_1 == 1 :
                termcolor.cprint("slot parkir berhasil diubah","green")
                enter()
                clear()
                transisi()
                ketersediaan_parkir_admin()
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue

def Kendaraan_terparkir_admin():
    clear()
    cover(b =121)
    print ("")
    print ("KENDARAAN TERPARKIR\n".center(121))
    garis("═",b=121)
    penampil_parkir_motor_seluruh()
    garis("═",b=121)
    print ("""
        1. CEK MOBIL TERPARKIR
        2. KEMBALI KE MENU
""")
    garis("═",b=121)
    while True :
        try:
            pilih = int(input("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                clear()
                transisi()
                clear()
                cover(b =121)
                print ("")
                print ("KENDARAAN TERPARKIR\n".center(121))
                garis("═",b=121)
                penampil_parkir_mobil_seluruh()
                garis("═",b=121)
                enter()
                clear()
                transisi()
                monitoring_parkir()
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                monitoring_parkir()
                break
            else :
                raise ValueError ("opsi yang dipilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue  

#______________________________________________________________________PENITIPAN BARANG__________________________________________________________
def penampung_barang_admin():
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    pemilik = []
    rak = []
    nama_barang = []
    tanggal_masuk = []
    for i in user :
        with open(f"datauser/{i}/titipbarang.csv", mode="r") as file :
            reader = csv.reader(file)
            for a in reader :
                if a == [] :
                    continue
                else :
                    pemilik.append(a[0])
                    rak.append(a[1])
                    nama_barang.append(a[2])
                    tanggal_masuk.append(a[3])
    return pemilik,rak,nama_barang,tanggal_masuk

def penampil_barang_admin():
    pemilik,rak,nama_barang,tanggal_masuk = penampung_barang_admin()
    print("")
    print ("LIST BARANG DALAM RAK\n".center(110))
    border = ["NO","PEMILIK","RAK BARANG","NAMA BARANG", "TANGGAL MASUK"]
    garis("═",b=110)
    print (f"|{border[0]:^6}|{border[1]:^30}|{border[2]:^20}|{border[3]:^28}|{border[4]:^20}|")
    garis("═",b=110)
    if len(pemilik) == 0 :
        print ("BELUM ADA BARANG DITITIPKAN".center(110))
        garis("═",b=110)
    else :
        for i in range (len(pemilik)):
            print (f"|{i+1:^6}|{pemilik[i]:^30}|{rak[i]:^20}|{nama_barang[i]:^28}|{tanggal_masuk[i]:^20}|")
            garis("═",b=110)

def monitoring_penitipan_barang():
    clear()
    cover(b=110)
    print("")
    print("MONITORING PENITIPAN BARANG\n".center(110))
    penampil_rak_barang_tersedia()
    penampil_barang_admin()
    garis("═",b=110)
    print ("""
            1. TAMBAHKAN BARANG
            2. TANDAI BARANG TERAMBIL
            3. KEMBALI KE MENU ADMIN
    """)
    garis("═",b=110)
    while True:
        try :
            pilih = int (input ("masukkan opsi yang dipilih >> ")) 
            if pilih == 1 :
                enter()
                clear()
                transisi()
                tambah_penitipan_barang_admin()
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                tandai_barang_terambil_admin()
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                menu_admin()
            else :
                raise ValueError ("opsi yang anda pilih tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue

def tambah_penitipan_barang_admin():
    clear()
    cover(b=110)
    rak_barang = penampung_rak()
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    waktu_sekarang = dt.datetime.now()
    waktu_sekarang = waktu_sekarang.strftime("%d-%m-%Y %H:%M")
    print("")
    print("TITIPKAN BARANG USER\n".center(110))
    penampil_rak_barang_tersedia()
    garis("═",b=110)
    while True :
        try :
            pemilik = input ("masukkan nama pemilik / user >> ")
            if pemilik in user :
                break
            else :
                raise ValueError ("pemilik tidak terdaftar")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue 
    index_rak = []
    while True :
        a = 0
        try :
            rak = input ("pilih rak kosong yang tersedia >> ").capitalize()
            for i in range (len(rak_barang[0])):
                if rak == rak_barang[0][i] and rak_barang[1][i] == "-":
                    index_rak.append(i)
                    a += 1 
                    break
                else :
                    continue
            if a == 1 :
                break
            else :
                raise ValueError ("rak barang tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    while True :
        try:
            nama_barang = input ("masukkan nama barang >> ")
            if len(nama_barang) <= 2 : 
                raise ValueError ("nama barang tidak boleh kurang dari 3 karakter")
            else :
                break
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    rak_barang[1][index_rak[0]] = "TERISI"
    with open ("dataadmin/rakpenitipanbarang.csv", mode = "w", newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow(rak_barang[0])
    with open ("dataadmin/rakpenitipanbarang.csv", mode = "a", newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow(rak_barang[1])
    with open (f"datauser/{pemilik}/titipbarang.csv", mode = "a", newline="\n") as file :
        writer = csv.writer(file)
        writer.writerow([pemilik,rak,nama_barang,waktu_sekarang])
    termcolor.cprint("barang berhasil ditambahkan", "green")
    enter()
    clear()
    transisi()
    monitoring_penitipan_barang()

def penampung_barang_terambil_admin(nama_user):
    pemilik = []
    rak = []
    nama_barang = []
    tanggal_masuk = []
    with open (f"datauser/{nama_user}/titipbarang.csv", mode="r")as file :
        reader = csv.reader(file)
        for i in reader :
            pemilik.append(i[0])
            rak.append(i[1])
            nama_barang.append(i[2])
            tanggal_masuk.append(i[3])
    return pemilik,rak,nama_barang,tanggal_masuk
        

def tandai_barang_terambil_admin():
    clear()
    cover(b=110)
    rak_barang = penampung_rak()
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    penampil_barang_admin()
    while True :
        try :
            nama_user = input ("masukkan nama user yang barangnya ingin diambil >> ").lower()
            if nama_user in user :
                break
            else :
                raise ValueError ("user tidak ditemukan")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
    clear()
    cover(b=110)
    waktu_sekarang = dt.datetime.now()
    waktu_sekarang = waktu_sekarang.strftime("%d-%m-%Y %H:%M")
    pemilik,rak,nama_barang,tanggal_masuk = penampung_barang_terambil_admin(nama_user)
    print ("")
    print ("LIST BARANG DALAM RAK\n".center(110))
    border = ["NO","PEMILIK","RAK BARANG","NAMA BARANG", "TANGGAL MASUK"]
    garis("═",b=110)
    print (f"|{border[0]:^6}|{border[1]:^30}|{border[2]:^20}|{border[3]:^28}|{border[4]:^20}|")
    garis("═",b=110)
    for i in range (len(pemilik)):
        print (f"|{i+1:^6}|{pemilik[i]:^30}|{rak[i]:^20}|{nama_barang[i]:^28}|{tanggal_masuk[i]:^20}|")
        garis("═",b=110)
    garis("═",b=110)
    pilih = int (input("pilih barang yang ingin diambil >> ")) - 1 
    index_rak = []
    for i in range(len(rak_barang[0])):
        if rak[pilih]==rak_barang[0][i]:
            index_rak.append(i)
    rak_barang[1][index_rak[0]] = "-"
    clear()
    cover(b=110)
    garis("═",b=110)
    print (f"|{border[0]:^6}|{border[1]:^30}|{border[2]:^20}|{border[3]:^28}|{border[4]:^20}|")
    garis("═",b=110)
    print (f"|{pilih+1:^6}|{pemilik[pilih]:^30}|{rak[pilih]:^20}|{nama_barang[pilih]:^28}|{tanggal_masuk[pilih]:^20}|")
    garis("═",b=110)
    while True :
        try :
            yakin = input ("yakin ingin mengambil barang ini? (y/n) >> ").lower()
            if yakin == "y" :
                with open (f"datauser/{nama_user}/riwayat_titip_barang.csv",mode = "a", newline="\n") as file:
                    writer = csv.writer(file)
                    writer.writerow ([pemilik[pilih],rak[pilih],nama_barang[pilih],tanggal_masuk[pilih],waktu_sekarang])
                pemilik.pop(pilih)
                rak.pop(pilih)
                nama_barang.pop(pilih)
                tanggal_masuk.pop(pilih)
                with open (f"datauser/{nama_user}/titipbarang.csv", mode = "w",newline="\n")as file:
                    writer = csv.writer(file)
                    for i in range (len(pemilik)):
                        writer.writerow([pemilik[i],rak[i],nama_barang[i],tanggal_masuk[i]])
                with open ("dataadmin/rakpenitipanbarang.csv", mode = "w",newline="\n") as file :
                    writer = csv.writer(file)
                    writer.writerows(rak_barang)
                termcolor.cprint("barang berhasil ditambahkan","green")
                enter()
                clear()
                transisi()
                monitoring_penitipan_barang()
                break
            elif yakin == "n":
                enter()
                clear()
                transisi()
                monitoring_penitipan_barang()
                break
            else :
                raise ValueError ("inputan tidak valid")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue

#____________________________________________________RIWAYAT PENITIPAN BARANG_____________________________________________________
def penampung_riwayat_barang_admin():
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
    pemilik = []
    rak = []
    nama_barang = []
    tanggal_masuk = []
    tanggal_keluar = []
    for i in user:
        with open(f"datauser/{i}/riwayat_titip_barang.csv",mode="r")as file:
            reader = csv.reader(file)
            for a in reader:
                if a == []:
                    continue
                else :
                    pemilik.append(a[0])
                    rak.append(a[1])
                    nama_barang.append(a[2])
                    tanggal_masuk.append(a[3])
                    tanggal_keluar.append(a[4])
    return pemilik,rak,nama_barang,tanggal_masuk,tanggal_keluar

def laporan_digiparking ():
    parkir_mobil, parkir_motor = penampung_parkir_seluruh()
    booking_parkir_motor, booking_parkir_mobil = penampung_booking_parkir_seluruh()
    pemilik,rak,nama_barang,tanggal_masuk = penampung_barang_admin()
    pemilik_total,rak_total,nama_barang_total,tanggal_masuk_total,tanggal_keluar_total =penampung_riwayat_barang_admin()
    riwayat_parkir_keseluruhan, harga_parkir, penampung_total_harga, total_mobil, total_motor = penampung_riwayat_admin()
    clear()
    cover()
    print ("")
    print("LAPORAN DIGIPARKING\n".center(107))
    garis("═")
    print (f"""
        > BARANG DALAM RAK SAAT INI                   : {len(pemilik)} BARANG
        > RIWAYAT TOTAL PENITIPAN BARANG              : {len(pemilik_total)} BARANG
        > JUMLAH BOOKING MOTOR SAAT INI               : {len(booking_parkir_motor)} MOTOR
        > JUMLAH BOOKING MOBIL SAAT INI               : {len(booking_parkir_mobil)} MOBIL
        > TOTAL BOOKING SAAT INI                      : {len(booking_parkir_motor)+ len(booking_parkir_mobil)} KENDARAAN
        > MOTOR TERPARKIR SAAT INI                    : {len(parkir_motor)} MOTOR
        > MOBIL TERPARKIR SAAT INI                    : {len(parkir_mobil)} MOBIL
        > TOTAL KENDARAAN TERPARKIR SAAT INI          : {len(parkir_motor) + len(parkir_mobil)} KENDARAAN
        > RIWAYAT MOTOR PARKIR KESELURUHAN            : {len(total_motor)} MOTOR
        > RIWAYAT MOBIL PARKIR KESELURUHAN            : {len(total_mobil)} MOBIL
        > RIWAYAT KENDARAAN PARKIR KESELURUHAN        : {len(total_mobil) + len(total_motor)} KENDARAAN
        > TOTAL PENDAPATAN DIGIPARKING                : Rp. {sum(penampung_total_harga)}
    """)
    garis("═")
    print (f"""
    1. LIHAT RIWAYAT PARKIR USER
    2. LIHAT RIWAYAT PENITIPAN BARANG USER
    3. KEMBALI KE MENU
    """)
    garis("═")
    while True :
        try:
            pilih = int (input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                clear()
                transisi()
                riwayat_parkir_admin()
                break
            elif pilih == 2 :
                enter()
                clear()
                transisi()
                riwayat_penitipan_barang_admin()
                break
            elif pilih == 3 :
                enter()
                clear()
                transisi()
                menu_admin()
                break
            else : 
                raise ValueError ("nama pemilik tidak terdaftar")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue
def penampung_riwayat_admin():
    riwayat_parkir_keseluruhan = []
    with open ("dataadmin/riwayat_parkir_keseluruhan.csv", mode = "r")as file :
        reader = csv.reader(file)
        for i in reader :
            riwayat_parkir_keseluruhan.append(i)
    harga_parkir =[]
    for i in (riwayat_parkir_keseluruhan):
        harga = f"{int(i[7]):,}"
        harga_parkir.append(harga)
    penampung_total_harga = []
    for i in riwayat_parkir_keseluruhan :
        harga = int(i[7])
        penampung_total_harga.append(harga)
    total_mobil = []
    total_motor = []
    for i in riwayat_parkir_keseluruhan :
        if i[2] == "mobil":
            total_mobil.append(i[2])
        elif i[2] == "motor":
            total_motor.append(i[2])
    return riwayat_parkir_keseluruhan, harga_parkir, penampung_total_harga, total_mobil, total_motor

def penampil_riwayat_admin():
    riwayat_parkir_keseluruhan, harga_parkir, penampung_total_harga, total_mobil, total_motor = penampung_riwayat_admin()
    border = ["NO", "PEMILIK", "BLOK", "JENIS KENDARAAN", "PLAT NOMOR", "JENIS PARKIR", "WAKTU CHECK IN", "WAKTU CHECK OUT", "TOTAL TAGIHAN"]
    garis("═",b=157)
    print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^8}|{border[3]:^20}|{border[4]:^15}|{border[5]:^20}|{border[6]:^20}|{border[7]:^20}|{border[8]:^20}|")
    garis("═",b=157)
    if len(riwayat_parkir_keseluruhan) == 0:
        print ("BELUM ADA RIWAYAT PARKIR".center(157))
        garis("═",b=157)
    else :
        for a,i in enumerate(riwayat_parkir_keseluruhan):
            print (f"|{a+1:^4}|{i[0]:^20}|{i[1]:^8}|{i[2]:^20}|{i[3]:^15}|{i[4]:^20}|{i[5]:^20}|{i[6]:^20}|{"Rp."+harga_parkir[a]:<20}|")
            garis("═",b=157)

def riwayat_parkir_admin():
    clear()
    cover(b=157)
    print("")
    print("RIWAYAT PARKIR USER\n".center(157))
    garis("═",b=157)
    penampil_riwayat_admin()
    garis("═",b=157)
    enter()
    clear()
    transisi()
    laporan_digiparking()

def riwayat_penitipan_barang_admin():
    pemilik,rak,nama_barang,tanggal_masuk,tanggal_keluar =penampung_riwayat_barang_admin()
    clear()
    cover(b=131)
    print("")
    print("RIWAYAT PENITIPAN BARANG\n".center(131))
    garis("═")
    border = ["NO", "PEMILIK","RAK BARANG", "NAMA BARANG", "TANGGAL MASUK", "TANGGAL KELUAR"]
    garis("═",b=131)
    print (f"|{border[0]:^6}|{border[1]:^30}|{border[2]:^20}|{border[3]:^28}|{border[4]:^20}|{border[5]:^20}|")
    garis("═",b=131)
    for i in range (len (pemilik)):
        print (f"|{i+1:^6}|{pemilik[i]:^30}|{rak[i]:^20}|{nama_barang[i]:^28}|{tanggal_masuk[i]:^20}|{tanggal_keluar[i]:^20}|")
        garis("═",b=131)
    garis("═",b=131)
    enter()
    clear()
    transisi()
    laporan_digiparking()

if __name__ == "__main__":
    halaman_awal()
  
#peh pusing banget in