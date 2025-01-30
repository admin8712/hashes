#UNTUK CRAK BCRYPT SILAHKAN CARI NOMOR 6 DAN GANTI HASH,
#PASSWORDNYA DENGAN PASSWORD BCRYPT KALIAN,
#JANGAN LUPA KASIK b DBELAKANG CONTOH SEPERTI DI BAWAH
# b"$2y$10$9o0PxCAeb1FcGRNS3E5rUunj0NW6omq1yIDl3Qt0ogBTJ2zxnD4Lm"
import hashlib,requests,json,os,sys,random,bcrypt
import subprocess,time
from time import sleep
os.system("clear")

def loading():
  os.system("figlet Loading | lolcat")
  for _ in range(6):
    sys.stdout.write("\r\033[36m\033[1mloading " + ["| ", "/ ", "- ", "\\ ", "| ", "/ "][_ % 6])
    sys.stdout.flush()
    time.sleep(0.5)
  print()
while True:
  loading()
  os.system("clear")


  print("🔴🟡🟢")
  print("")
  h=("from mrx_41 cyber indonesia")
  print(f"\033[0;31m\rVersion 1.0.3 {h}")
  os.system("figlet Hashes | lolcat")
  ader=("\033[36m\033[1m[2].Crack-md5 ofline ")
  adar=("\033[36m\033[1m[4].Crack-Md5 Online")
  ador=("\033[36m\033[1m[6].Check Tipe Hash ")
  adir=("\033[36m\033[1m[8].Keluar")
  print(f"\n\033[36m\033[1m[1].Buat-hash md5          {ader}")
  #print("\n\033[36m\033[1m[2].Crack-md5 ofline ")
  print(f"\n\033[36m\033[1m[3].Crack-md5 online       {adar}")
  #print("\n\033[36m\033[1m[4].Crack-Md5 Online")
  print(f"\n\033[36m\033[1m[5].Crack-Bcrypt ofline    {ador}")
  #print("\n\033[36m\033[1m[6].Check Tipe Hash ")
  print(f"\n\033[36m\033[1m[7].Buat Bcrypt            {adir}")
  #print("\n\033[36m\033[1m[8].Keluar")
  ab=("1")
  ba=("2")
  do=("3")
  di=("4")
  co=("5")
  ca=("6")
  cu=("7")
  ci=("8")
  def pilih():
    print("\n")
    cd=input("\n\033[36m\033[1msilahkan pilih : ")
    print("\n")
#___________________________________________________________#
#.1
    if cd==ab:
      def main ():
        os.system("clear")
        os.system("figlet O F L I N E | lolcat")
        msg=input("\n\033[36m\033[1mbuat hash md5: ")
        print("\n")
        hash=hashlib.md5()
        hash.update(msg.encode("utf-8"))
        print("\n")
        os.system("clear")
        os.system("figlet Results | lolcat")
        print("\n\033[0;32m\033[1mResults : {}".format(hash.hexdigest()))
        print("")
        count=0
        for x in range(30):
          time.sleep (0.30)
          print (f"\033[36m\033[1m\rsegera copy hash waktu anda 30 detik {x} :",end =" " ,flush=True)
          count +=1
          if count ==3:
            count=0
        
        subprocess.call("python hash.py", shell=True)
        exit()
        print("\n")
      if __name__=="__main__":
        main()
#___________________________________________________________#
#.2
    if cd ==ba:
      def ofline():
        os.system("clear")
        os.system("figlet O F L I N E | lolcat")
        a=0
        print("\n")
        md=input("\n\033[36m\033[1mcrack-md5: ")
        file=input("\n\033[36m\033[1mmasukan file: ")
        print("\n")
        try:
          print("\n")
          o=open(file,"r")
          print("\n")
        except:
          print("\n")
          print("\n\033[0;31m\033[1mfile not found")
          print("\n")
          quit()
        for word in o:
          dx=word.encode("utf-8")
          xd=hashlib.md5(dx.strip()).hexdigest()
          if xd==md:
            print("\n")
            os.system("clear")
            os.system("figlet Found | lolcat")
            print("\n\033[0;32m\033[1mpassword found : "+word)
            exit()
            a+=1
        if a==0:
          print("\n\033[0;31m\033[1mpassword not found ")
          quit()
      if __name__=="__main__":
        ofline ( )
#___________________________________________________________#
#.3
    if cd==do:
      def online():
        os.system("clear")
        os.system("figlet O N L I N E | lolcat")
        print("\n")
        try:
          md5=input("\n\033[36m\033[1mCrack-Md5: ")
          print("\n")
          url_api=("http://www.nitrxgen.net/md5db/"+md5)
          session=requests.post(url=url_api).text
          print("\n")
          os.system("clear")
          os.system("figlet Found | lolcat")
          print("\n\033[0;32m\033[1mpassword found: "+session+"\n")
          exit()
          print("\n")

        except Exception as ConnectionError:
          print("\n\033[0;31m\033[1mConnection Error !")
          print("")
          time.sleep(1)
          subprocess.call("python hash.py",shell=True)
          exit()
      if __name__=="__main__":
        online()
#___________________________________________________________#
#.4
    if cd==di:
      def on():
        os.system("clear")
        os.system("figlet O N L I N E | lolcat")
        print("")
        try:
          pas=input("\n\033[36m\033[1mmasukan pasword : ")
          url = "https://api.onlinehashcrack.com/v2"
          headers = {"Content-Type": "application/json"}
          data = {
        "api_key":"sk_7e490a6da4e4b6c6da5a55633a8f4008",
        "agree_terms": "yes",
        "algo_mode": 0,
        "hashes": [pas]

          }
          response = requests.post(url, json=data,headers=headers)
          print("")
          os.system("clear")
          os.system("figlet Found | lolcat")
          print(f"\n\033[32m\033[1mCrack berhasil periksa di gmail anda : {response}")
          print("")
          exit()
        except Exception as ConnectionError:
          print("\n\033[0;31m\033[1mConnection Error !")
          print("")
        time.sleep(1)
        subprocess.call("python hash.py",shell=True)
        exit()
      if __name__=="__main__":
        on( )
#____________________________________________________________#
#.[5]
    if cd==co:
      os.system("clear")
      os.system("figlet Bcrypt | lolcat")
      print("")
      def main():
        file=input("\n\033[36m\033[1mFile : ")
        os.system("clear")
        with open(file, 'r') as file:
          wordlist = file.read().splitlines()
        hash = b'$2b$12$aPnhQDQ2kTEr3RU4r8YzDeHofkQuWVvSgxQEudSvnVApCJWDupViy'#<--GANTI DENGAN BCRYPT YANG ANDA INGIN CRACK
        for word in wordlist:
          os.system("clear")
          if bcrypt.checkpw(word.encode('utf-8'), hash):
            a=hash.decode()
            print(a)
            os.system("clear")
            print("")
            os.system("figlet Found | lolcat")
            print("")
            print("\033[0;32m\033[1mPassword found: "+word)
            exit()
            print("")
            print("")

            os.system("clear")
          else:
            os.system("clear")
            b=hash.decode()
            print(b)
            os.system("clear")
            print("\n")
            print("\033[0;31mPassword not found : "+word)
            print("\n")
            #time.sleep(0.1)
            print("")

            os.system("clear")
            print(" ")

      if __name__ == "__main__":
        main()

#____________________________________________________________#
#.[6]
    if cd==ca:
      def chek():
        try:
          os.system("clear")
          os.system("figlet Chek Hash | lolcat")
          hash=input("\n\033[36m\033[1mmasukan hash : ")
          url=(f"https://hashes.com/en/api/identifier?hash={hash}")
          req=requests.post(url=url).text
          print("\033[0;32m\033[1m"+req)
          print("\n\033[0;32m\033[1mtipe hash:                     ⬆️")
          print("\033[0;32m\033[1m_____________________________________")
          print("")
          quit()
        except Exception as ConnectionError:
          print("")
          print("\n\033[0;31m\033[1mConnection Error")
          print("")
          time.sleep(1)
          subprocess.call("python hash.py",shell=True)
          exit()
      if __name__=="__main__":
        chek()
#_____________________________________________________________#
#.[7]
    if cd==cu:
      def handex():
        os.system("clear")
        # example password
        os.system("figlet Bcrypt | lolcat")
        pas=input ("\n\033[36m\033[1mbuat pas bcrypt : ")
        print ("\n")
        password = pas
        # converting password to array of bytes
        bytes = password.encode('utf-8')
        # generating the salt
        salt = bcrypt.gensalt()
        # Hashing the password
        hash = bcrypt.hashpw(bytes, salt) 
        print(f"\033[0;32m\033[1m{hash}")
        print("\n")
        count=0
        print("")
        for x in range(30):
          time.sleep (0.30)
          print(f"\r\033[0;36m\033[1mSegera copy hash waktu anda 30 detik {x} :",end =" ",flush=True)
          count+=1
          if count==3:
            count=0
        subprocess.call("python hash.py",shell=True)
        exit()
      if __name__=="__main__":
        handex()

#____________________________________________________________#
#.[8]
    if cd==ci:
      def out():
        def mengetik(s):
          for c in s +"\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random()* 1)
        mengetik("Loading ...")
        print("\n\033[0;31m\033[1mKeluar")
        print("")
        os.system("clear")
        quit()
      if __name__=="__main__":
        out()

  if __name__=="__main__":
    pilih( )
if __name__=="__loading__":
  loading ()

