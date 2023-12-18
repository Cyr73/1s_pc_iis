#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# вывод списка ПК подключенных к базам 1С согласно журналу IIS
from datetime import datetime
import socket

def get_device_name(ip_address):
    try:
        device_name = socket.gethostbyaddr(ip_address)[0]
        return device_name
    except socket.herror:
        return None

today=datetime.now().strftime('%y%m%d')
filename ='C:/inetpub/logs/LogFiles/W3SVC1/u_ex'+today+'.log'
items={} #Словарь
# Чтение лог-файла и загрузка его содержимого
with open(filename, 'r') as f:
    for line in f:
        if line.startswith('#'): continue
        data = line.split()
        URL = data[4]
        base= URL.split('/')[1]
        IP =  data[8]
        if 'login' in URL: 
            items[base,IP]='login'    
        elif 'logout' in URL:
            items[base,IP]='logout'
for i in items:
    if items[i]=='login':
        base=i[0]
        IP = i[1]  
        print(base, get_device_name(IP))
 
input() # ожидание нажатия любой кнопки
