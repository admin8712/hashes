#UNTUK CRACK BCRYPT SILAHKAN CARI NOMOR [5] DAN GANTI HASH,
#PASSWORDNYA DENGAN PASSWORD BCRYPT KALIAN,
#JANGAN LUPA KASIK b DBELAKANG CONTOH SEPERTI DI BAWAH
# b"$2y$10$9o0PxCAeb1FcGRNS3E5rUunj0NW6omq1yIDl3Qt0ogBTJ2zxnD4Lm"
#____________________ POWER FULL HASHES ____________________#
from itertools import product
import hashlib,requests,json,os,sys,random,bcrypt
import subprocess,time
from time import sleep
from urllib.request import urlopen
import re as r
os.system("clear")
try:
    def getIP():
      d = str(urlopen('http://checkip.dyndns.com/').read())
      return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
      os.system("clear")
    print("\n\033[0;36m\033[1m"+getIP())
    os.system("clear")
    print("")
except Exception as ConnectionError:
  print("")
  print("\n\033[0;31m\033[1mConnection Error")
  print("")
  time.sleep(1)
  exit()

def loading():
  font="""\033[0;32m\033[1m
┓     ┓• 
┃┏┓┏┓┏┫┓┏┓┏┓
┗┗┛┗┻┗┻┗┛┗┗┫   ©©©©©©©©©©
           ┛

  """
  print(font)
  for _ in range(6):
    sys.stdout.write("\r\033[36m\033[1m"+["| ", "/ ", "- ", "\\ ", "| ", "/ "][_ % 6])
    sys.stdout.flush()
    time.sleep(2)
  print()
while True:
  loading()
  os.system("clear")


  #print("🔴🟡🟢")
  try:
    def getIP():
      d = str(urlopen('http://checkip.dyndns.com/').read())
      return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
      os.system("clear")
    print("\n\033[0;31m\033[1m🔴🟡🟢                             "+getIP())
    print("")
  except Exception as ConnectionError:
    print("")
    print("\n\033[0;31m\033[1mConnection Error")
    print("")
    time.sleep(1)
    exit()
  #h=("from mrx_41 cyber indonesia")
  print("\033[0;31m\033[1m🛠️ Version 1.0.3️")
  def banner ():
   font="""\033[0;32m\033[1m
  
  ██░ ██  ▄▄▄        ██████  ██░ ██ ▓█████   ██████ 
 ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓█   ▀ ▒██    ▒ 
 ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒███   ░ ▓██▄   
 ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒▓█  ▄   ▒   ██▒
 ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░▒████▒▒██████▒▒
  ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░▒ ▒▓▒ ▒ ░
  ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░▒  ░ ░
  ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   ░   ░  ░  ░
  ░  ░  ░      ░  ░      ░   ░  ░  ░   ░  ░      ░

  """
   print(font)
  if __name__=="__main__":
    banner()
  ader=("\033[36m\033[1m[2].Crack-md5 ofline ")
  adar=("\033[36m\033[1m[4].Crack-Md5 Online")
  ador=("\033[36m\033[1m[6].Check Tipe Hash ")
  adir=("\033[36m\033[1m[8].Edit Tools")
  adur=("\033[36m\033[1m[10].Exit")
  print(f"\n\033[36m\033[1m[1].Buat-hash md5          {ader}")
  #print("\n\033[36m\033[1m[2].Crack-md5 ofline ")
  print(f"\n\033[36m\033[1m[3].Crack-md5 online       {adar}")
  #print("\n\033[36m\033[1m[4].Crack-Md5 Online")
  print(f"\n\033[36m\033[1m[5].Crack-Bcrypt ofline    {ador}")
  #print("\n\033[36m\033[1m[6].Check Tipe Hash ")
  print(f"\n\033[36m\033[1m[7].Buat Bcrypt            {adir}")
  print(f"\n\033[36m\033[1m[9].Crack Md5 Brute        {adur}")
  ab=("1")
  ba=("2")
  do=("3")
  di=("4")
  co=("5")
  ca=("6")
  cu=("7")
  du=("8")
  ni=("9")
  ci=("10")
  def pilih():
    print("\n")
    cd=input("\n\033[36m\033[1m🟢Silahkan pilih : ")
    print("\n")
#___________________________________________________________#
#.[1]
    if cd==ab:
      def main ():
        os.system("clear")
        font="""\033[0;32m\033[1m

┏┓  ┏┓  ┓   ┳  ┳┓  ┏┓
┃┃  ┣   ┃   ┃  ┃┃  ┣
┗┛  ┻   ┗┛  ┻  ┛┗  ┗┛


        """
        print(font)
        msg=input("\n\033[36m\033[1mbuat hash md5: ")
        print("\n")
        hash=hashlib.md5()
        hash.update(msg.encode("utf-8"))
        print("\n")
        os.system("clear")
        font="""\033[;32m\033[1m

┏┳┓•      ┳┳┓ ┓┏━
 ┃ ┓┏┓┏┓  ┃┃┃┏┫┗┓
 ┻ ┗┣┛┗   ┛ ┗┗┻┗┛
    ┛

        """
        print(font)
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
#.[2]
    if cd ==ba:
      def ofline():
        os.system("clear")
        font="""\033[0;32m\033[1m

┏┓  ┏┓  ┓   ┳  ┳┓  ┏┓
┃┃  ┣   ┃   ┃  ┃┃  ┣
┗┛  ┻   ┗┛  ┻  ┛┗  ┗┛


        """
        print(font)
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
            font="""\033[0;32m\033[1m

┏┓            ┓  ┏┓       ┓
┃┃┏┓┏┏┓┏┏┏┓┏┓┏┫  ┣ ┏┓┓┏┏┓┏┫
┣┛┗┻┛┛┗┻┛┗┛┛ ┗┻  ┻ ┗┛┗┻┛┗┗┻


            """
            print(font)
            print("\n\033[0;32m\033[1mpassword found : "+word)
            print("")
            exit()
            a+=1
        if a==0:
          print("\n\033[0;31m\033[1mpassword not found ")
          quit()
      if __name__=="__main__":
        ofline ( )
#___________________________________________________________#
#.[3]
    if cd==do:
      def online():
        os.system("clear")
        font="""\033[0;32m\033[1m

┏┓  ┳┓  ┓   ┳  ┳┓  ┏┓
┃┃  ┃┃  ┃   ┃  ┃┃  ┣
┗┛  ┛┗  ┗┛  ┻  ┛┗  ┗┛


        """
        print(font)
        print("\n")
        try:
          md5=input("\n\033[36m\033[1mCrack-Md5: ")
          print("\n")
          url_api=("http://www.nitrxgen.net/md5db/"+md5)
          session=requests.post(url=url_api).text
          print("\n")
          os.system("clear")
          font="""\033[0;32m\033[1m

┏┓            ┓  ┏┓       ┓
┃┃┏┓┏┏┓┏┏┏┓┏┓┏┫  ┣ ┏┓┓┏┏┓┏┫
┣┛┗┻┛┛┗┻┛┗┛┛ ┗┻  ┻ ┗┛┗┻┛┗┗┻


          """
          print(font)
          print("\n\033[0;32m\033[1mpassword found: "+session+"\n")
          print("")
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
#.[4]
    if cd==di:
      def on():
        os.system("clear")
        font="""\033[0;32m\033[1m

┏┓  ┳┓  ┓   ┳  ┳┓  ┏┓
┃┃  ┃┃  ┃   ┃  ┃┃  ┣
┗┛  ┛┗  ┗┛  ┻  ┛┗  ┗┛


        """
        print(font)
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
          font="""\033[0;32m\033[1m

┏┓            ┓  ┏┓       ┓
┃┃┏┓┏┏┓┏┏┏┓┏┓┏┫  ┣ ┏┓┓┏┏┓┏┫
┣┛┗┻┛┛┗┻┛┗┛┛ ┗┻  ┻ ┗┛┗┻┛┗┗┻


          """
          print(font)
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
      font="""\033[0;32m\033[1m

┏┓  ┏┓  ┓   ┳  ┳┓  ┏┓
┃┃  ┣   ┃   ┃  ┃┃  ┣
┗┛  ┻   ┗┛  ┻  ┛┗  ┗┛


      """
      print(font)
      print("")
      def main():
        file=input("\n\033[36m\033[1mFile : ")
        os.system("clear")
        with open(file, 'r') as file:
          wordlist = file.read().splitlines()
        hash = b'$2b$12$qd2YKzJAKWLFmRHLOzj4tufWaNl5S9Gqk4k.uLptxotB1tQtXvx1O'#<--GANTI DENGAN BCRYPT YANG ANDA INGIN CRACK
        for word in wordlist:
          os.system("clear")
          if bcrypt.checkpw(word.encode('utf-8'), hash):
            a=hash.decode()
            print(a)
            os.system("clear")
            print("")
            font="""\033[0;32m\033[1m

┏┓            ┓  ┏┓       ┓
┃┃┏┓┏┏┓┏┏┏┓┏┓┏┫  ┣ ┏┓┓┏┏┓┏┫
┣┛┗┻┛┛┗┻┛┗┛┛ ┗┻  ┻ ┗┛┗┻┛┗┗┻


            """
            print(font)
            print("\033[0;32m\033[1mPassword found: "+word)
            print("")
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
          font="""\033[0;32m\033[1m

┏┓┓   ┓   ┏┳┓•      ┓┏   ┓
┃ ┣┓┏┓┃┏   ┃ ┓┏┓┏┓  ┣┫┏┓┏┣┓
┗┛┛┗┗ ┛┗   ┻ ┗┣┛┗   ┛┗┗┻┛┛┗
              ┛

          """
          print(font)
          hash=input("\n\033[36m\033[1mmasukan hash : ")
          os.system("clear")
          url=(f"https://hashes.com/en/api/identifier?hash={hash}")
          req=requests.post(url=url).text
          font="""\033[0;32m\033[1m

┏┳┓•      ┓┏   ┓
 ┃ ┓┏┓┏┓  ┣┫┏┓┏┣┓
 ┻ ┗┣┛┗   ┛┗┗┻┛┛┗
    ┛

          """
          print(font)
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
        font="""\033[0;32m\033[1m

┏┓  ┏┓  ┓   ┳  ┳┓  ┏┓
┃┃  ┣   ┃   ┃  ┃┃  ┣
┗┛  ┻   ┗┛  ┻  ┛┗  ┗┛


        """
        print(font)
        pas=input ("\n\033[36m\033[1mbuat pas bcrypt : ")
        os.system("clear")
        print ("\n")
        password = pas
        # converting password to array of bytes
        bytes = password.encode('utf-8')
        # generating the salt
        salt = bcrypt.gensalt()
        # Hashing the password
        hash = bcrypt.hashpw(bytes, salt)
        foont="""\033[0;32m\033[1m

┏┳┓•      ┳┓
 ┃ ┓┏┓┏┓  ┣┫┏┏┓┓┏┏┓╋
 ┻ ┗┣┛┗   ┻┛┗┛ ┗┫┣┛┗
    ┛           ┛┛

        """
        print(foont)
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
#___________________________________________________________#
#.[8]
    if cd==du:
      def edit():
        os.system("nano /data/data/com.termux/files/home/hashes/hash.py")

        subprocess.call("python hash.py", shell=True)
        exit()

      if __name__=="__main__":
        edit()
#____________________________________________________________#
#.[9]
    if cd==ni:
      def ofline():
        os.system("clear")
        font="""\033[0;32m\033[1m

┏┓  ┏┓  ┓   ┳  ┳┓  ┏┓
┃┃  ┣   ┃   ┃  ┃┃  ┣
┗┛  ┻   ┗┛  ┻  ┛┗  ┗┛
"""
        print(font)
        print("")
        def computeMD5hash(string):
          m=hashlib.md5()
          m.update(string.encode("utf-8"))
          return m.hexdigest()
        try:
          md5=input("\033[36m\033[1mmasukan hash: ")
          print("")
          max=int(input("\033[36m\033[1mJumlah Salt: ")) +1
          print("")
          chr="""
        1):ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop           qrstuvwxyz1234567890
        2):abcdefghijklmnopqrstuvwxyz1245667890\n
        3):ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\n
        4):1234567890\n
        5):ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop           qrstuvwxyz\n
        6):ABCDFFGHIJKLMNOPQRSTUVWXYZ\n
        7):abcdefghijklmnopqrstuvwxyz\n
        8):Custom\n
         """
          print(chr)
          print("")
          chr_num=int(input("\033[36m\033[1mpilih custom mana: "))
          print("")
          if chr_num == 1:
            chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
          elif chr_num == 2:
            chars="abcdefghijklmnopqrstuvwxyz1245667890"
          elif chr_num == 3:
            chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
          elif chr_num == 4:
            chars="1234567890"
          elif chr_num == 5:
            chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
          elif chr_num == 6:
            chars="ABCDFFGHIJKLMNOPQRSTUVWXYZ"
          elif chr_num == 7:
            chars="abcdefghijklmnopqrztuvwxyz"
          elif chr_num == 8:
            chars="Custom"
            print("")
            chars=input("\033[36m\033[1mIsi Sendiri: ")
            print("")
          found=0
          lines=0
          di=time.time()
          for dini in range(1, max):
            mencoba=product(chars, repeat=dini)
            for hadi in mencoba:
              crypt=computeMD5hash(''.join(hadi))
              if crypt==md5:
                print("")
                os.system("clear")
                font="""\033[0;32m\033[1m

┏┓            ┓  ┏┓       ┓
┃┃┏┓┏┏┓┏┏┏┓┏┓┏┫  ┣ ┏┓┓┏┏┓┏┫
┣┛┗┻┛┛┗┻┛┗┛┛ ┗┻  ┻ ┗┛┗┻┛┗┗┻


                """
                print(font)
                print("")
                print("\033[0;32m\033[1mFound ➡ {} = {}\n".format(crypt, ''.join(hadi)))
                print("")
                do=time.time()
                dn=do-di
                print("\033[0;32m\033[1mselesai {} detik\ndengan {} total hashes".format(str(dn), str(lines)))
                print("")
                exit()
                found=1
              if found== 0:
                print("\033[0;31m\033[1mcracked ➡ {} = {} ".format(crypt, ''.join(hadi)))
        except KeyboardInterrupt:
          print("\n Stooped at line: {}".format(str(lines)))
      if __name__=="__main__":
        ofline()

#____________________________________________________________#
#.[10]
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

 
