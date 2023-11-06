#https://medium.com/macoclock/getting-a-list-of-nearby-wifi-access-points-in-python-on-macos-726d9fb59001
#https://python.plainenglish.io/estimating-distance-using-rssi-python-8f3d44c38108

import subprocess


scan_cmd = subprocess.Popen(['airport', '-I'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
scan_out, scan_err = scan_cmd.communicate()

print(scan_out)
print(scan_err)
