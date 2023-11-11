- `agrCtlRSSI`: Kontrol edilen alıcı sinyal gücü seviyesi (RSSI).
- `agrExtRSSI`: Genişletilmiş alıcı sinyal gücü seviyesi (RSSI).
- `agrCtlNoise`: Kontrol edilen gürültü seviyesi.
- `agrExtNoise`: Genişletilmiş gürültü seviyesi.
- `state`: Wi-Fi bağlantısının durumu (örneğin, "running" bağlı demek olabilir).
- `op mode`: İşletim modu (örneğin, "station" kablosuz ağa istemci olarak bağlı olduğunu gösterebilir).
- `lastTxRate`: Son veri iletim oranı.
- `maxRate`: Maksimum veri iletim hızı.
- `lastAssocStatus`: Son bağlantı durumu (0 genellikle başarılı bir bağlantıyı temsil eder).
- `802.11 auth`: 802.11 kimlik doğrulama türü (örneğin, "open" açık bir ağa bağlandığını gösterebilir).
- `link auth`: Link (bağlantı) kimlik doğrulama türü (örneğin, "wpa2" WPA2 kullanıldığını gösterebilir).
- `BSSID`: Erişim noktasının BSSID'si (MAC adresi).
- `SSID`: Erişim noktasının adı (örneğin, "eduroam").
- `MCS`: Modülasyon ve Kodlama Şeması (MCS).
- `guardInterval`: Koruma aralığı süresi.
- `NSS`: Uygun Uzay Sinyali (NSS).
- `channel`: Kullanılan kablosuz kanal numarası.

## To Activate airport

> sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport

## Test results
![](Test_results/second_with_10k_val.png)