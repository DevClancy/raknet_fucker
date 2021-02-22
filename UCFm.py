import socket
import socks
import struct
import codecs,sys
import threading
import random
import time
import os
import wget
from colorama import init
from colorama import Fore, Back, Style

init()

ip = input(Fore.CYAN + "Enter IP: ")
port = input(Fore.CYAN + "Enter PORT: ")
