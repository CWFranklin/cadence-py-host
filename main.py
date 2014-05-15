#!/usr/bin/env python3

import requests
import os, configparser, json, threading, time
from Pubnub import Pubnub
import psutil as ps

configFile = 'CONFIG.INI'
#pubKey = 'pub-c-0c1983e0-4b1d-4856-a5ee-30016247de60'
pubKey = 'pub-c-18bc7bd1-2981-4cc4-9c4e-234d25519d36'
#subKey = 'sub-c-79ce0714-db54-11e3-8c07-02ee2ddab7fe'
subKey = 'sub-c-5782df52-d147-11e3-93dd-02ee2ddab7fe'
timeout = 10
channelName = 'test'
authUser = "brandon@brandonscott.co.uk"
authPassword = "Cadenc3!"
pulseInterval = 4

config = configparser.ConfigParser()
config.read(configFile)

pubnub = Pubnub( pubKey, subKey, False )

def getCpuUsage():
        return ps.cpu_percent(interval=1)

def getRamUsage():
        mem = ps.phymem_usage()
        return mem.percent

def getDiskUsage():
        disks = ps.disk_partitions()
        return int(ps.disk_usage(disks[0].mountpoint).percent)

def getTimestamp():
        return int(time.time())

def getUptime():
        bootTime = int(ps.get_boot_time())
        return int(getTimestamp() - bootTime)

def sendPulse():
        while True:
                time.sleep(pulseInterval)
                pulseData = {"server_id": int(config['DEFAULT']['ServerId']), "ram_usage": getRamUsage(), "cpu_usage": getCpuUsage(), "disk_usage": getDiskUsage(), "uptime": getUptime(), "timestamp": getTimestamp()}
                resp = requests.post("http://cadence-bu.cloudapp.net/pulses", data=pulseData, auth=(authUser, authPassword))
                print(resp)

def receive(message):
        print(message)
        return false

def subscribe():
        pubnub.subscribe({'channel': channelName, 'callback': receive, 'heartbeat': 30})

print(config['DEFAULT']['Activated'])
osDetails = os.uname()
mem = ps.phymem_usage()
disks = ps.disk_partitions()

osName = osDetails.sysname + " " + osDetails.release
osVersion = osDetails.version
cpuMaxSpeed = 0 #CPU Speed in MHz
ramTotal = int(mem.total / 1000000) #RAM in MB
diskSize = int(ps.disk_usage(disks[0].mountpoint).total / 1000000) #Disk Size in MB

fr = open('/proc/cpuinfo', 'r')
cpuInfo = fr.readlines()
fr.close()
for line in cpuInfo:
        if 'MHz' in line:
                cpuMaxSpeed = int(float(line.split(':')[1].strip()))

if config['DEFAULT']['Activated'] == 'no':
        payload = {"servergroup_id": 0, "name": osDetails.nodename, "available_disk": diskSize, "available_ram": ramTotal, "cpu_speed": cpuMaxSpeed, "os_name": osName, "os_version": osVersion, "guid": pubnub.uuid}
        resp = requests.post("http://cadence-bu.cloudapp.net/servers", data=payload, auth=(authUser, authPassword))
        print (resp)
        config['DEFAULT'] = {'ServerId': resp.json()['id'], 'Activated': 'yes', 'Uuid': pubnub.uuid}
        with open(configFile, 'w') as configfile:
                config.write(configfile)
else:
        payload = {"servergroup_id": 0, "name": osDetails.nodename, "available_disk": diskSize, "available_ram": ramTotal, "cpu_speed": cpuMaxSpeed, "os_name": osName, "os_version": osVersion, "guid": pubnub.uuid}
        resp = requests.put("http://cadence-bu.cloudapp.net/servers/" + config['DEFAULT']['Uuid'], data=payload, auth=("brandon@brandonscott.co.uk", "Cadenc3!"))
        print(resp)

pubnub.uuid = config['DEFAULT']['Uuid']

sub_thread = threading.Thread(target=subscribe)
sub_thread.start()

pulse_thread = threading.Thread(target=sendPulse)
pulse_thread.start()

print(pubnub.uuid)
print(config['DEFAULT']['UUID'])