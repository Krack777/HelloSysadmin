import os
import requests
import signal
import subprocess

def read_config_variables(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    config_start = "# config start"
    config_end = "# config end"
    capture = False
    variables = []
    for line in lines:
        if config_start in line:
            capture = True
            continue
        elif config_end in line:
            break
        if capture:
            variables.append(line.strip())
    return variables
def write_config_variables(filename, new_variables):
    with open(filename, 'r') as file:
        lines = file.readlines()

    config_start = "# config start"
    config_end = "# config end"
    inside_config = False
    new_lines = []

    for line in lines:
        if config_end in line and inside_config:
            for var in new_variables:
                new_lines.append(var + '\n')
            inside_config = False

        if not inside_config:
            new_lines.append(line)

        if config_start in line:
            inside_config = True
            continue

    with open(filename, 'w') as file:
        file.writelines(new_lines)
def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response.content)
        print(f"Файл {filename} успешно скачан")

client_script = 'https://raw.githubusercontent.com/Krack777/HelloSysadmin/main/client/main.py'
library = 'https://raw.githubusercontent.com/Krack777/HelloSysadmin/main/client/googleSheets.py'

client_script_file = 'main.py'
library_file = 'googleSheets.py'
config_vars = read_config_variables('main.py')
print(f"Конфиг устаревшего файла прочитан. Debug : {config_vars}")
processes = subprocess.getoutput("pgrep -f main.py").split()
for pid in processes:
    print(f'попытка сбросить pid номера {pid}')
    try:
        os.kill(int(pid), signal.SIGTERM)
        print("С процесса main.py снята задача ")
    except ProcessLookupError:
        print("Процесс main.py не был запущен ранее")

conf1 = config_vars[0].split()
conf2 = config_vars[1].split()
conf3 = config_vars[2].split()
new_vars = [
    f'{conf1[0]} = {conf1[2]}',
    f'{conf2[0]} = {conf2[2]}',
    f'{conf3[0]} = {conf3[2]}'
]

download_file(client_script, client_script_file)
download_file(library, library_file)

write_config_variables('main.py', new_vars)
print("Данные конфига записаны")

print("Клиент main.py успешно запущен после обновления")
os.system('python3 main.py')
