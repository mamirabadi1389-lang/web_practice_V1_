#for webing two or ... system
import socket
#________________sakht server_____________
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# (socket.AF_INET)-> ma mekhaem az ip hae IPv4 estefadeh konim
# مثلا ایپی 192.168.1.10
#(socket.SOCK_STREAM) -> نوع ارتباط 
#برای ارتباط قابل‌اعتماد مناسبه یعنب داده ها به ترتیب و با کنترل داده میشن 
#________________________________________________________________________________
#socket.socket(
#    socket.AF_INET,
#    socket.SOCK_STREAM
#)
# پس این میشه یه کانال ارتباطی TCP روی IPv4 برای ما میسازه

#___________________bind_________________________________________________________
server.bind(("0.0.0.0",5000))
#اینجا داریم میگیم که اقا این برنامه ما که داریم روی چه ادرس و پورتی منتظر ارتباط باشه
#در قسمت دوم ("0.0.0.0",5000)
#دو بخش داریم که بخش اول 0.0.0.0 روی تمام ادرس های شبکه ای این کامپیوتر گوش یده

# مثلا بیا یه فرضی کنیم که ایپی کامپیوتر همون ipv4 خودت با استفاده از همون چها تا صفر قابل استفاده میشن
#اون دمی هم  مثل ساختمونه مثلا اون شماره واحد ایپ میشه همون پورت
#پس     192.168.1.10:
#_________________listen________________________________________________________________________________________
server.listen(1)
#داره میگه ارههه بیا من امادم که سیستم های دیه به من وصل شن بیاااااااااااااا و اون عدد یکمم ینی اینکه بایئ توی صف قرار بگیری چون خیلی خفنم
print ("wait for connecting...")

#_________________accept__________________________________________________________________________________________________________________________________________
conn, addr = server.accept()

ip = addr[0]
port = addr[1]

print("IP:", ip)
print("Port:", port)
#PC دوم وصل می‌شود
#       ↓
#server.accept()
#       ↓
#('192.168.1.20', 53142)
#       ↓
#      addr
#     /    \
#    IP     Port
#    ↓       ↓
# 192.168  53142

"""
server
   │
   │ منتظر اتصال
   ▼
accept()
   │
   ▼
conn
   │
   │ ارسال / دریافت اطلاعات
   ▼
PC دوم
"""
print("اتصال برقرار شد:", addr)
#حلقه ارسال و دریافت پیام
while True:
    message = conn.recv(1024).decode()


    print("پیام:", message)


    #حداکثر 1024 بایت اطلاعات از کامپیوتر مقابل دریافت کن.
    if not message:
        break


conn.close()
server.close()
"""
1. ابزار شبکه رو وارد کن
        ↓
2. یک Socket بساز
        ↓
3. بگو روی IP و Port مشخص کار کن
        ↓
4. بگو منتظر اتصال باش
        ↓
5. منتظر بمون تا PC دوم وصل بشه
        ↓
6. اتصال PC دوم رو دریافت کن
        ↓
7. از طریق اتصال، پیام دریافت کن
        ↓
8. پیام رو از bytes به متن تبدیل کن
        ↓
9. پیام رو نمایش بده
        ↓
10. دوباره منتظر پیام بعدی باش
        ↓
11. وقتی ارتباط قطع شد، Socket رو ببند
"""
"""
Client
  ↓
Socket بساز
  ↓
به IP و Port سرور وصل شو
  ↓
پیام بساز
  ↓
پیام رو encode کن
  ↓
send()
  ↓
Server دریافت می‌کنه
"""

"""
Python String
     ↓ encode()
    bytes
     ↓ شبکه
    bytes
     ↓ decode()
Python String
"""








#full code

import socket

# ساخت Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# مشخص کردن IP و Port
server.bind(("0.0.0.0", 5000))

# آماده شدن برای دریافت اتصال
server.listen(1)

print("منتظر اتصال یک سیستم...")

# دریافت اتصال
conn, addr = server.accept()

# گرفتن IP و Port کلاینت
client_ip = addr[0]
client_port = addr[1]

print("اتصال برقرار شد!")
print("IP کلاینت:", client_ip)
print("Port کلاینت:", client_port)

# دریافت پیام‌ها
while True:

    message = conn.recv(1024).decode()

    # اگر کلاینت قطع شده باشد
    if not message:
        break

    print("پیام دریافت شد:", message)

# بستن اتصال
conn.close()
server.close()