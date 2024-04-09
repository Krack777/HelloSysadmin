from googleSheets import *
import os
# config start
account_file = 'client.json'
spreadsheet_id = '1y8GEKuaH2vYmerQm_sapIwf1Sf7BnpKSTkF4z5cuEkE' # id гугл таблицы, можно найти в ссылке на таблицу после /d и до /edit
# config end
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

