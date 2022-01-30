from wifiConfg import run_connection
import machine
import machine


## Pin config reset state of json ssid and pasword##

# from time import sleep
# reset_pin = machine.Pin(5, machine.Pin.IN)


# sleep(2)
# while True:
#     if reset_pin.value() == 1:
#         print("pressed")
#     else:
#         print("not pressed")
#     sleep(1)



while True:
    run_connection()



# *******TESTING PURPOSE********** #
# import json
# import network
# import time
# import usocket as socket


# from htmlcontent import html_ap, html_switch
# html_AP= html_ap
# html_STA= html_switch

# wifi = network.WLAN(network.AP_IF)
# # Restarting WiFi
# wifi.active(False)
# time.sleep(0.5)
# wifi.active(True)
# wifi.config(essid='homeAuto',password='12345678')

# wifi.ifconfig(('192.168.0.255', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

# while (not wifi.isconnected()):
#         print("waiting for conect to AP")
#         time.sleep(1) ## 1 second sleep
#         print("connected")


# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Host = '' # Empty means, it will allow all IP address to connect
# Port = 80 # HTTP port
# s.bind((Host,Port)) # Host,Port

# s.listen(5) # It will handle maximum 5 clients at a time
# print("ok1")

# while True:
#         print("ok2")
#         connection_socket,address=s.accept() # Storing Conn_socket & address of new client connected
#         print("Got a connection from ->", address)
#         request=connection_socket.recv(1024) # Storing Response coming from client
#         print("Content bytes--->>>>>", request) # Printing Response 
#         request=str(request) # Coverting Bytes to String
#         # Comparing & Finding Postion of word in String
#         print(request)
#         if (request.find("ssid=") != -1): 
#             fst = request.find("ssid=")+5
#             lst =request.find("&password")
#             sid= request[fst: lst]
#             fst = request.find("password")+8
#             pw= request[fst:]
#             print("ssid: ",sid, "pw: ", pw)
        
    
    
    
#         # Sending HTML document in response everytime to all connected clients  
#         response=html_AP
#         connection_socket.send(response)
    
#         #Closing the socket
#         connection_socket.close()