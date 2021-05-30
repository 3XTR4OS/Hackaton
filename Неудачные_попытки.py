"""Провальные попытки"""
import os

path = 'mypath/path'
files = os.listdir(path)
files_txt = [i for i in files if i.endswith('.txt')]

import requests

file = requests.get('http://192.168.1.5', user='sasdemo00', password='Orion123')
print(file.headers)

import saspy

sas = saspy.SASsession(cfgname='default')

ssh = {'saspath': '/opt/sasinside/SASHome/SASFoundation/9.4/bin/sas_u8',
       'ssh': '/usr/bin/ssh',
       'host': 'remote.linux.host',
       'options': ["-fullstimer"]
       }

sas = saspy.SASsession(cfgname='ssh',
                       options=["-fullstimer", "-autoexec", "/home/my.autoexec.sas"],
                       host="'other.host.with.sas")
