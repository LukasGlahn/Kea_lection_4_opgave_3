def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('LUKAS_LABTOP 9701','QWERASDF')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig()[0])
    
do_connect()