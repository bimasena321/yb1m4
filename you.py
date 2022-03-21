import os
import time
import pywhatkit

os.system('clear')
print("====================================")
print("jenis : search engine khusus youtube")
print("bahasa: python                      ")
print("====================================")

print("[1].mulai")
print("[2].pembuat")
print("[0].keluar")

j = int(input("pilih: "))
if j == 1:
	o = input("Mau Cari Video Apa? : ")
	pywhatkit.playonyt(o)
elif j == 2:
	print("nama : Bima Sena W.p")
else:
	print("ok terimakasih dan jangan recode!!")

	