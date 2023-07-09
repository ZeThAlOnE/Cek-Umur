  GNU nano 6.2                                                                    cekumur.py                                                                             
import datetime as dt
# module
from os import system
from time import sleep

# program
def logo():
   print("""
 ▄████▄  ▓█████ ██ ▄█▀ █    ██  ███▄ ▄███▓ █    ██  ██▀███  
▒██▀ ▀█  ▓█   ▀ ██▄█▒  ██  ▓██▒▓██▒▀█▀ ██▒ ██  ▓██▒▓██ ▒ ██▒
▒▓█    ▄ ▒███  ▓███▄░ ▓██  ▒██░▓██    ▓██░▓██  ▒██░▓██ ░▄█ ▒
▒▓▓▄ ▄██ ▒▓█  ▄▓██ █▄ ▓▓█  ░██░▒██    ▒██ ▓▓█  ░██░▒██▀▀█▄  
▒ ▓███▀ ▒░▒████▒██▒ █▄▒▒█████▓ ▒██▒   ░██▒▒▒█████▓ ░██▓ ▒██▒
░ ░▒ ▒  ░░░ ▒░ ▒ ▒▒ ▓▒ ▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░
  ░  ▒  ░ ░ ░  ░ ░▒ ▒░ ░▒░ ░ ░ ░  ░      ░░░▒░ ░ ░   ░▒ ░ ▒ 
░           ░  ░ ░░ ░   ░░ ░ ░ ░      ░    ░░░ ░ ░   ░░   ░ 
░ ░     ░   ░  ░  ░      ░            ░      ░        ░     
""")

logo()
print("Silahkan masukkan tanggal, \nbulan dan tahun, \nlahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir:%A}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(umur_hari)
print(f"Umur anda adalah : {umur_tahun} tahun")

