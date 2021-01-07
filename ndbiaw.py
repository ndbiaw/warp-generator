import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')
print('''1.1.1.1 WARP+ UNLIMITED GENERATION
© Copyright 2021 - Nguyễn Duy Bách (ndbiaw)
├─────────────────────────────────────────────────────┤
Donate: paypal.me/ndbiaw - Momo: 0363608641''')
referrer = input("Nhập 1.1.1.1 Public ID:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		animation = ["[-][■□□□□□□□□□] 10%","[\][■■□□□□□□□□] 20%", "[|][■■■□□□□□□□] 30%", "[/][■■■■□□□□□□] 40%", "[-][■■■■■□□□□□] 50%", "[\][■■■■■■□□□□] 60%", "[|][■■■■■■■□□□] 70%", "[/][■■■■■■■■□□] 80%", "[-][■■■■■■■■■□] 90%", "[✓][■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r Đang cộng lưu lượng... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n Đã cộng lưu lượng vào ID: {referrer}")    
		print(f"≈ {g} GB đã được cộng vào tài khoản của bạn.")
		print(f"Tổng: {g} Thành công {b} Thất bại")
		print("[-]Tiến trình sẽ bắt đầu lại sau 20 giây nữa...", end="\r")
		time.sleep(1)
		print("[\]Tiến trình sẽ bắt đầu lại sau 19 giây nữa...", end="\r")
		time.sleep(1)
		print("[|]Tiến trình sẽ bắt đầu lại sau 18 giây nữa...", end="\r")
		time.sleep(1)
		print("[/]Tiến trình sẽ bắt đầu lại sau 17 giây nữa...", end="\r")
		time.sleep(1)
		print("[-]Tiến trình sẽ bắt đầu lại sau 16 giây nữa...", end="\r")
		time.sleep(1)
		print("[\]Tiến trình sẽ bắt đầu lại sau 15 giây nữa...", end="\r")
		time.sleep(1)
		print("[|]Tiến trình sẽ bắt đầu lại sau 14 giây nữa...", end="\r")
		time.sleep(1)
		print("[/]Tiến trình sẽ bắt đầu lại sau 13 giây nữa...", end="\r")
		time.sleep(1)
		print("[-]Tiến trình sẽ bắt đầu lại sau 12 giây nữa...", end="\r")
		time.sleep(1)
		print("[\]Tiến trình sẽ bắt đầu lại sau 11 giây nữa...", end="\r")
		time.sleep(1)
		print("[|]Tiến trình sẽ bắt đầu lại sau 10 giây nữa...", end="\r")
		time.sleep(1)
		print("[/]Tiến trình sẽ bắt đầu lại sau 9 giây nữa...", end="\r")
		time.sleep(1)
		print("[-]Tiến trình sẽ bắt đầu lại sau 8 giây nữa...", end="\r")
		time.sleep(1)
		print("[\]Tiến trình sẽ bắt đầu lại sau 7 giây nữa...", end="\r")
		time.sleep(1)
		print("[|]Tiến trình sẽ bắt đầu lại sau 6 giây nữa...", end="\r")
		time.sleep(1)
		print("[/]Tiến trình sẽ bắt đầu lại sau 5 giây nữa...", end="\r")
		time.sleep(1)
		print("[-]Tiến trình sẽ bắt đầu lại sau 4 giây nữa...", end="\r")
		time.sleep(1)
		print("[\]Tiến trình sẽ bắt đầu lại sau 3 giây nữa...", end="\r")
		time.sleep(1)
		print("[|]Tiến trình sẽ bắt đầu lại sau 2 giây nữa...", end="\r")
		time.sleep(1)
		print("[/]Tiến trình sẽ bắt đầu lại sau 1 giây nữa...", end="\r")
		time.sleep(1)
		print("[-]Tiến trình sẽ bắt đầu lại sau 0 giây nữa...", end="\r")
		print("[✓]Đang bắt đầu lại tiến trình...", end="\r")
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Đã xảy ra lỗi khi kết nối với máy chủ của CloudFlare")
		print(f"[#] Tổng: {g} Thành công {b} Thất bại")	