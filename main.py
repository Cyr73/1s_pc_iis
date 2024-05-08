#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# вывод списка ПК подключенных к базам 1С согласно журналу IIS
from datetime import datetime
import socket, os.path, time

def get_client_name(device_name):
    return clients[device_name.lower()]

def get_device_name(ip_address):
    try:
        device_name = socket.gethostbyaddr(ip_address)[0]
        return device_name
    except socket.herror:
        return None

today = datetime.now().strftime('%y%m%d')
filename ='C:/inetpub/logs/LogFiles/W3SVC1/u_ex'+today+'.log'
if not os.path.isfile(filename):
    print ('никто сегодня не подключался через IIS')
    time.sleep(3)# ожидание
    exit()
items={} #Словарь
# Чтение лог-файла и загрузка его содержимого
with open(filename, 'r') as f:
    for line in f:
        if line.startswith('#'): continue
        data = line.split()
        URL = data[4]
        base = URL.split('/')[1].lower()
        IP = data[8]
        if 'login' in URL: 
            if (base,IP) not in items: items[base,IP]=1
            else: items[base,IP] +=1
        elif 'logout' in URL:
            if (base,IP) in items: items[base,IP] -=4
            if items[base,IP]<=0: del items[base,IP] 
for i in sorted(items):
        base=i[0]
        IP = i[1]  
        print(base, get_device_name(IP))
print(' Всего:', len(items))
time.sleep(15)# ожидание
