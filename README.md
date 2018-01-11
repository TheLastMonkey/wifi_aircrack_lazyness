### Read Me
# WiFi aircrack laziness
WiFi aircrack laziness is a lazy ass script to take the output for a given Target from airodump-ng (see output example below) and generate all the necessary aircrack commands for listening for handshakes and doing replays for DeAuthentication. 

The script is designed to take an input from the user which can be typed out or copy and pasted in and if everything goes accordingly and if the inputs is clean meaning nothing anything out of the ordinary it should generate the commands and print them out to the terminal. It also additionally outputs the Mac address or bssid as well as the SSID so that you can visually confirm that it grab them correctly. I would suggest also confirming that the channel is correct in the outputted commands.

As stated before the script is for pure laziness purposes although it might speed up a workflow. I'm using this project to learn stuff so it's far from perfect I'm sure. If you see any issues or have any suggestions feel free to let me know.

# One More Thing!
Very Important!  
The WiFi Interface is HARD-CODED!  
So you will need to change that line of code manually.  
(See Variable) `wifi_interface`  
*This may get a update in the future.*

## Output from airodump-ng example:

    24:6F:20:41:FA:FA  -77       58      421    0   6  54e  WPA2 CCMP   PSK  1.0 LAB,DISP       The_ssid
## Output of this script example:

    Put in the stuff: <paste the stuff here>
    MAC/BSSID of AP is: 24:6F:20:41:FA:FA
    SSID of AP is: The_ssid
    sudo airodump-ng -w The_ssid --channel 6 --bssid 24:6F:20:41:FA:FA wlx00c0ca961581
    sudo aireplay-ng -0 5 -e The_ssid wlx00c0ca961581


