# Script to enable wifi on Ceyomur trail camera using bluetooth

Just set the bluetooth MAC of the trail camera in the enablewifi.py script then:

```
sudo pacman -S bluez bluez-utils
pip install bluepy

sudo systemctl start bluetooth
echo "power on" | bluetoothctl

python3 enablewifi.py
```
