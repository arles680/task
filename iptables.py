#!/usr/bin/env python3
import subprocess

# Очистка правил
subprocess.run(['iptables', '-F'])
subprocess.run(['iptables', '-X'])

# Создание цепочек
chains = ['ALLOW_ALL', 'DB_SERVERS', 'ON_DEMAND', 'TEMP_ACCESS', 'TO_THE_WORLD', 'LOGGING']
for chain in chains:
    subprocess.run(['iptables', '-N', chain])

# Разрешение всего трафика для ALLOW_ALL
subprocess.run(['iptables', '-A', 'ALLOW_ALL', '-j', 'ACCEPT'])

# Разрешение всего трафика для DB_SERVERS
subprocess.run(['iptables', '-A', 'DB_SERVERS', '-j', 'ACCEPT'])

# Добавление правил для ON_DEMAND
subprocess.run(['iptables', '-A', 'ON_DEMAND', '-j', 'ACCEPT'])

# Добавление правил для TEMP_ACCESS
subprocess.run(['iptables', '-A', 'TEMP_ACCESS', '-p', 'tcp', '--dport', '22,80,443', '-j', 'ACCEPT'])

# Добавление правил для TO_THE_WORLD
subprocess.run(['iptables', '-A', 'TO_THE_WORLD', '-j', 'ACCEPT'])

# Блокировка остального трафика и логирование
subprocess.run(['iptables', '-A', 'INPUT', '-j', 'LOGGING'])
subprocess.run(['iptables', '-A', 'FORWARD', '-j', 'LOGGING'])
subprocess.run(['iptables', '-A', 'LOGGING', '-j', 'DROP'])

# Вывод текущих правил
subprocess.run(['iptables', '-L', '-n', '-v'])
