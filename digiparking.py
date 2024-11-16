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
                                        . PERATURAN DAN PEMBERITAHUAN
                                        . CEK PROFIL
                                        . DAFTARKAN KENDARAAN 
                                        . BOOKING PARKIR 
                                        . CEK KETERSEDIAAN PARKIR
                                        . PENITIPAN BARANG
                                        . LAPORKAN KEHILANGAN DAN PENEMUAN BARANG
                                        . RIWAYAT BOOKING 
                                        . EXIT  
""")
        garis("=")
        try :
            pilih = int(input("masukkan pilihan >> "))
            if pilih == 1 : 
                pass  
            elif pilih == 2 :
                enter ()
                cek_profil_user() 
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
                pass  
            elif pilih == 9 :
                enter()
                exit()
                break
            else :
                raise ValueError ("Opsi Tidak Tersedia")
        except ValueError as error :
            termcolor.cprint (error, "red")
            enter ()
            continue
def pemberitahuan_user ():
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
def penitipan_barang_user():
    pass
def laporkan_kehilangan_penemuan_user():
    pass
def riwayat_booking_user():
    pass

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> JUKIR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu_jukir():
    while True :
        clear()
        cover()
        print ("""
                                        . CEK PROFIL
                                        . ABSENSI
                                        . CEK BOOKING PARKIR
                                        . CEK KETERSEDIAAN PARKIR
                                        . CEK PENITIPAN BARANG
                                        . CEK LAPORKAN KEHILANGAN DAN PENEMUAN BARANG
""")
        try :
            pilih = int (input("Masukkan pilihan >> "))
            if pilih == 1 :
                pass
            elif pilih == 2 :
                pass
            elif pilih == 3 :
                pass
            elif pilih == 4 :
                pass
            elif pilih == 5 :
                pass
            elif pilih == 6 :
                pass
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADMIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu_admin():
    while True :
        clear()
        cover()
        print ("""
                                        . TAMBAH PENGUMUMAN ATAU PERATURAN
                                        . MONITORING USER 
                                        . MONITORING JURU PARKIR
                                        . MONITORING KENDARAAN USER
                                        . MONITORING BOOKING PARKIR
                                        . MONITORING LAPORAN KEHILANGAN DAN PENEMUAN BARANG
""")
        garis ("=")
        try :
            pilih = int (input("Masukkan pilihan >> "))
            if pilih == 1 :
                pass
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
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint (error,"red")
            enter()
            continue

def monitoring_user():
    while True :
        clear()
        cover(b=117)
        user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()
        border = ["NO","NAMA", "NIK", "TANGGAL LAHIR", "NOMOR HP", "USERNAME", "PASSWORD"]
        garis("=",b=117)
        print (f"|{border[0]:^4}|{border[1]:^20}|{border[2]:^17}|{border[3]:^17}|{border[4]:^17}|{border[5]:^17}|{border[6]:^17}|")
        garis("=",b=117)
        for i in range (len(user)):
            print (f"|{i + 1:^4}|{user[i]:^20}|{nik[i]:^17}|{tanggal_lahir[i]:^17}|{nomor_hp[i]:^17}|{list_username[i]:^17}|{list_password[i]:^17}|")
            garis("=",b=117)
        print ("""
1. TAMBAH DATA USER
2. UPDATE DATA USER 
3. HAPUS  DATA USER 
""")
        try :
            pilih = int(input ("Masukkan pilihan"))
            if pilih == 1 :
                enter()
                tambah_user()
                break
            elif pilih == 2 :
                enter()
                update_user()
                break
            elif pilih == 3 :
                enter()
                hapus_user()
                break
            else :
                raise ValueError ("opsi tidak tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            continue

def tambah_user():
    clear() 
    cover() 
    user,nik,tanggal_lahir,nomor_hp,list_username,list_password = penampung_user()

   
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
    monitoring_user()

def update_user():
    pass
def hapus_user():
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





if __name__ == "__main__":
    # halaman_awal()
    menu_admin()
    # menu_user()
    # monitoring_user()