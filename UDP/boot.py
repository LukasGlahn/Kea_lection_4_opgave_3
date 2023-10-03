def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('','') # put nætvrks novn og så nætværks kode her
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig()[0])
    
do_connect()