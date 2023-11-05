

import rssi

interface = 'en0'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = [b"FiberHGV_ZTNZ43_2.4GHz"]

ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

print(ap_info)

