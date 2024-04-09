from googleSheets import *
import signal
import subprocess
import time
import os
# config start
account_file = 'client.json'  # расположение json файла с сервис учёткой(см п.4 readme "#см п.3 раздела "Установка бота и клиента(удалённого пк/доски)")
spreadsheet_id = '1y8GEKuaH2vYmerQm_sapIwf1Sf7BnpKSTkF4z5cuEkE' # id таблицы(см п.3 readme "#см п.3 раздела "Установка бота и клиента(удалённого пк/доски)")
delay = '3' #Задержка парсинга таблицы на команды(см п.1 Раздела "Пинкод" и "Задержка клиента")
# config end

processes = subprocess.getoutput("pgrep -f updater_client.py").split()
for pid in processes:
    try:
        os.kill(int(pid), signal.SIGTERM)
    except ProcessLookupError:
        pass

table = Table(account_file=account_file, spreadsheet_id=spreadsheet_id)
while True:
	command = table.read()

	if "terminal" in command:
		command = command.split('=')
		table.write('')
		os.system(command[1])


	elif "image" in command:
		command = command.split('=')
		table.write('')
		os.system('xdg-open '+ 'images/' +command[1])


	elif "run" in command:
		command = command.split('=')
		table.write('')
		os.system(command[1])


	elif "sound" in command:
		command = command.split('=')
		table.write('')
		os.system('mpg123 sounds/' + command[1])

	
	elif 'update=True' in command:
		table.write('')
		os.system('python3 updater_client.py')
		
	time.sleep(int(delay))
