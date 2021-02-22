import socket
import socks
import struct
import codecs, sys
import threading
import random
import time
import os
import wget
from colorama import init
from colorama import Fore, Back, Style

message1 = codecs.decode("081e77da","hex_codec")
message2 = codecs.decode("081e7eda","hex_codec")
message3 = codecs.decode("081e77da","hex_codec")

messages = [message1, message2, message3]

init()

try:
	os.remove("socks5.txt")
except:
	pass

try:	
	proxy5_download = wget.download("https://raw.githubusercontent.com/DevClancy/proxy/main/socks5.txt")
except:
	print(Fore.RED + "Error!")  

ip = input(Fore.CYAN + "\nEnter IP: ")
port = input(Fore.CYAN + "Enter PORT: ")
threads = int(input(Fore.CYAN + "Enter THREADS: "))

def attack():
	pass

