# ESP32 can use 2.4GHz only
# Turn on the router before use
# 学校用のS変数、SSIDからMYGATEWAYまでをコピペして、学校用をコメントアウトする。
#SSID = "AI-IoT-G"
#PASS = "WECWECWECWECWEC"
SSID = "7885F47DBABE-2G"
PASS = "anefzxzcragd21"
# Change MYIP and MYHOSTNAME to your own ones
#MYIP = b"172.22.1.40"
#MYHOSTNAME = "0P01050"
#MYNETMASK = b"172.22.1.255"
#MYDNS = b"1.1.1.1"
#MYGATEWAY = b"172.22.1.254"
MYIP = b"192.168.3.50" # X.250の部分は自宅環境で使われていないIPアドレスを指定
MYHOSTNAME = "0P01011"
MYNETMASK = b"255.255.255.0"    # Xの部分は自宅環境によって異なる
MYDNS = b"1.1.1.1"
MYGATEWAY = b"192.168.3.1"      # X,Yの部分は自宅環境によって異なる