import re

derp = input("Put in the stuff: ")
wifi_interface = "wlx00c0ca961581"
ch = 0
L = [derp]
X = '([a-fA-F0-9]{2}[:|\-]?){6}' # this is the regex
bssid = 0
end_ssid = '(\w+)$'
ssid = 0
def strip_bssid():
    global X
    global L
    global bssid

    for s in L:

        a = re.compile(X).search(s)
        if a:

            bssid = (s[a.start(): a.end()])

def strip_ssid():
    global X
    global L
    global ssid
    for s in L:

        a = re.compile(end_ssid).search(s)
        if a:

            ssid = (s[a.start(): a.end()])

def get_ch():
    global ch
    global derp
    ch_is = (derp.split()[5])
    ch = ch_is





strip_bssid()
strip_ssid()
get_ch()


print("MAC/BSSID of AP is:",bssid)
print("SSID of AP is:",ssid)

print("sudo airodump-ng -w",ssid,"--channel",ch,"--bssid",bssid,wifi_interface)
print("sudo aireplay-ng -0 5 -e",ssid,wifi_interface)
