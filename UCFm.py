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

