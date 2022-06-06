# Script to enable wifi on Ceyomur trail camera using bluetooth

```
sudo pacman -S bluez bluez-utils
pip install bluepy

sudo systemctl start bluetooth
echo "power on" | bluetoothctl

python3 enablewifi.py --addr MAC
```

Tested on the Ceyomur CY65 camera.
