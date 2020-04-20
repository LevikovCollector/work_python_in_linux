
import os
import re
import subprocess



def do_command(user_command):
    """Выполняет команду и возвращает результат"""
    result = subprocess.run(user_command, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def check_internet_port():
    """Проверка адреса по умолчанию"""
    res = do_command('ifconfig')
    template = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_list = re.findall(template, str(res))
    assert '127.0.0.1' in ip_list


def default_route():
    """Выводит маршрут по умолчанию"""
    res = do_command('route')
    template = 'default\s+\w+\s+0.0.0.0\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+'
    text = str(res).split('\n')
    for line in text:
        def_route = re.findall(template, line)
        if def_route != []:
            print(def_route)
            break


def processor_info():
    """Информация о процессоре"""
    print(do_command('lscpu'))


def all_process():
    """Информация о всех процессах"""
    print(do_command(['ps', '-A']))


def apache_service_status():
    """Состояние сервиса apache"""
    print(do_command(['systemctl', 'status', 'apache2.service']))


def internet_ports_status():
    """Состояние сетевого порта на сервере"""
    print(do_command(['netstat', '-l']))


def pack_version(pack):
    """Выводит версию пакета"""
    info = do_command(['dpkg', '-s', pack])
    template = 'Version: \d+.{1,15}'
    version = re.search(template, info).group(0)
    print('package:{}\n{}'.format(pack, version))


def files_in_dir(path_to_dir):
    """Выводит файлы из папки"""
    if os.path.exists(path_to_dir):
        print(os.listdir(path_to_dir))
    else:
        print('Папка не найдена')


def where_i_am():
    """Выводит текущую директорию"""
    print(do_command('pwd'))


def linux_core():
    """Выводит версию ядра"""
    print(do_command(['uname', '-r']))


def linux_info():
    """Выводит версию linux"""
    print(do_command(['inxi', '-S']).replace('12', ' ').replace('', ' '))


def net_interface():
    """Вывод информации об интерфейсах"""
    print(do_command(['ifconfig', '-a']))
