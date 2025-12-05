import network
import socket
import json
from time import sleep
from machine import Pin, Timer
import network_settings

connTimer = 0
led = Pin("LED",Pin.OUT)
wlan = network.WLAN(network.STA_IF)

def connect():
    wlan.active(True)
    wlan.config(pm = 0xa11140) 
    # sets a static ip for this Pico 
    wlan.ifconfig((network_settings.ip, '255.255.255.0', '10.0.0.2', '8.8.8.8')) 
    wlan.connect(network_settings.ssid, network_settings.pwd)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        led.toggle()
        sleep(0.5)
        led.toggle()
    led.on()
    print("Connected")
    connTimer = Timer(-1)
    connTimer.init(mode=Timer.PERIODIC,period=5000,callback=reconnect)

def reconnect(t):
    if(not wlan.isconnected()):
       print("Disconnected, trying again")
       led.off()
       connect()


def serve(f):
    #serve and call function f when called
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    print("listening on ",addr)
    
    while True:
        try:
            cl, addr = s.accept()
            print('client connected from', addr)
            request = cl.recv(1024)
            request = str(request)
            print(request)
            cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
            cl.send(json.dumps(f()))
            cl.close()

        except:
            print("error with request")
