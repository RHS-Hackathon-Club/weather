#!/usr/bin/env python
import os
import time
log_file = 'log2.csv'
log_interval = 60 # seconds

def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            return i

def read(s):
    with open(f'/sys/bus/w1/devices/{s}/w1_slave') as f:
        return float(f.read().split('\n')[1].split(' ')[9][2:])/1000*1.8+32

def log(out_file):
    with open(out_file, 'a') as f:
        f.write(f'{int(time.time())}, {int(read(s)*10)/10}\n')

if __name__ == '__main__':
    try:
        s = sensor()
        while True:
            print(f'{time.time()}, {read(s)}')
            log(log_file)
            time.sleep(log_interval)

    except KeyboardInterrupt:
        exit()
