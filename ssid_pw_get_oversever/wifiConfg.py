####****get id pw from own server and save it as json to coonect router****####
####****Subham Deb****####

import json
import network
import time
import usocket as socket



from htmlcontent import html_ap, html_sta
html_AP= html_ap
html_STA= html_sta
mode=""

def run_connection():
    savedData = open("wifiData.json")
    wifiData_json = json.loads(savedData.read())
    ssid = wifiData_json["ssid"]
    password = wifiData_json["password"]
    savedData.close()
    global mode
    global html_AP
    global html_STA
    
    
    if ssid != "":
        mode="sta"
        print(mode)
        wifi = network.WLAN(network.STA_IF)
        # Restarting WiFi
        wifi.active(False)
        time.sleep(0.5)
        wifi.active(True)
        wifi.connect(ssid,password)

    else:
        mode="ap"
        wifi = network.WLAN(network.AP_IF)
        # Restarting WiFi
        wifi.active(False)
        time.sleep(0.5)
        wifi.active(True)
        wifi.config(essid='homeAuto',password='12345678')



    wifi.ifconfig(('192.168.10.200', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

    if mode == "sta":
        if not wifi.isconnected():
            print('connecting..')
            while (not wifi.isconnected()):
                time.sleep(1) ## 1 second sleep  

    if mode == "ap":
        while (not wifi.isconnected()):
                print("waiting for conect to AP")
                time.sleep(1) ## 1 second sleep
        print("connected")




    # Initialising Socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol
    time.sleep(2)
    Host = '' # Empty means, it will allow all IP address to connect
    Port = 80 # HTTP port
    s.bind((Host,Port)) # Host,Port

    s.listen(5) # It will handle maximum 5 clients at a time
    print("ok1")


    while mode == "ap":
        print("ok2")
        connection_socket,address=s.accept() # Storing Conn_socket & address of new client connected
        print("Got a connection from ->", address)
        request=connection_socket.recv(1024) # Storing Response coming from client
        print("Content bytes--->>>>>", request) # Printing Response 
        request=str(request) # Coverting Bytes to String
        # Comparing & Finding Postion of word in String
        print(request)
        if (request.find("ssid=") != -1): 
            fst = request.find("ssid=")+5
            lst =request.find("&password")
            sid= request[fst: lst]
            fst = request.find("password")+9
            lst =request.find("&lstprt")
            pw= request[fst:lst]
            print("before save=>> ssid: ",sid, "pw: ", pw)
            savedData = open("wifiData.json", "w")
            jsonData = '{"ssid":' + '"{}","password":'.format(sid)+'"{}"'.format(pw)+'}'
            savedData.write(jsonData)
            savedData.close()

            savedData = open("wifiData.json")
            wifiData_json = json.loads(savedData.read())
            ssid = wifiData_json['ssid']
            password = wifiData_json['password']
            savedData.close()
            print("after save=>> ssid: ",ssid, "pw: ", password)
            return True
    
        # Sending HTML document in response everytime to all connected clients  
        response=html_AP
        connection_socket.send(response)
    
        #Closing the socket
        connection_socket.close()

    while mode == "sta":
        print("on STA mode")
        print("ok2")
        connection_socket,address=s.accept() # Storing Conn_socket & address of new client connected
        print("Got a connection from ->", address)
        request=connection_socket.recv(1024) # Storing Response coming from client
        print("Content bytes--->>>>>", request) # Printing Response 
        request=str(request) # Coverting Bytes to String
        # Comparing & Finding Postion of word in String
        print(request)

        # Sending HTML document in response everytime to all connected clients  
        response=html_STA
        connection_socket.send(response)
    
        #Closing the socket
        connection_socket.close()
