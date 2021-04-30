import ntplib

a = 1619945220
response = ntplib.NTPClient().request('europe.pool.ntp.org', version=3)
b = response.tx_time

if b < a:
    print("puede acceder")
else:
    print("no puede acceder")

