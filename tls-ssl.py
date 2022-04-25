import socket
import ssl

symb = '''





▄▄▀█▄───▄───────▄
▀▀▀██──███─────███
░▄██▀░█████░░░█████░░
███▀▄███░███░███░███░▄
▀█████▀░░░▀███▀░░░▀██▀
==> SnakeSploit
==> Code By : KrdSploit
==> Version : 0.0.1


													'''

def menu():
	print("[!] Checking TLS Version : [!]")
	print("[!] Checking SSL Version : [!]")
	print("[!] Disable  Cloudflare : [!]")
	print("[!] Bypass Cloudflare : [!]")
	print("[!] Disable SSL Security : ")
	print("[!] Scanning Web Open Port :")

	menu_input = int(input("Select Your Options : "))
	if menu_input==1:
		tls()
	elif menu_input==2:
		ssl()
	elif menu_input==3:
		unb()
	elif menu_input==4:
		byp()
	elif menu_input==5:
		disa()
	elif menu_input==6:
		prt()
	


def tls():

        import time
        from tqdm import tqdm

        m_list = [1,2,3,4]

        for i in tqdm(m_list):
                time.sleep(1)
      
        
        import socket
        import ssl

        print("================================================")


        hostname = input("Enter Yout Target Hostname : ")
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print("The Version Are Detected ===> " + (ssock.version()))
        print("================================================")


def unb():
        import cloudscraper
        import cfscrape
        import requests

        host = input("Enter Target Hostname : ")

        scraper = cloudscraper.create_scraper()  
        scraper = cloudscraper.CloudScraper()  
        print(scraper.get(host).text)

        did = input("Do you wanna disable cloudflare : ")
        if did =="y":
                scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                print(scraper)
                session = requests.session()
                session.headers = ...
                scrapper = cfscrape.create_scraper(sess=session)
                print(scrapper)
        else:
                menu()

def byp():
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)


def disa():
	import requests
	hostname = input("Enter Your Target Hostname : ")
	response = requests.request("GET", hostname, verify=False)
	print(response.text)

def prt():
import threading
import socket
import sys
from datetime import datetime

open_ports = []


def scan_ports(name, start_port, max_port):
    try:
        for port in range(start_port, max_port):
            if (port - 1) == max_port - 1:
                print(name, "is finishing its tasks")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target_ip, port))  # returns an error indicator
            if result == 0:
                open_ports.append(port)
            s.close()
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("Could not connect to server")
        sys.exit()


if __name__ == '__main__':
    print("-" * 50)
    print("Port scanner by Nort721")
    print("-" * 50)

    target_ip = input('Enter target ip: ')
    start_port = int(input('starting port: '))
    max_ports = int(input('ending port: '))
    threads_count = int(input('threads count: '))

    threads = []

    i = 0
    next_max = start_port
    min_port = start_port
    while i < threads_count:
        i += 1
        next_max += ((max_ports - start_port) // threads_count)
        if i == threads_count:
            next_max = max_ports
        print("Thread{} starts: {} ends: {}".format(i, min_port, next_max))
        threads.append(threading.Thread(target=scan_ports, args=("thread{}".format(i), min_port, next_max)))
        min_port = next_max

    print("-" * 50)
    print("Scanning for open ports in range {}-{} . . .".format(start_port, max_ports))
    print("Time started: " + str(datetime.now()))
    print("-" * 50)

    for var in threads:
        var.start()

    for var in threads:
        var.join()

    print("Done scanning")
    print("Time Ended: " + str(datetime.now()))

    if len(open_ports) == 0:
        print("no open ports found in range {}-{}".format(start_port, max_ports))
    else:
        print("open ports found:")
        print("-" * 50)
        for port in open_ports:
            print(port)
        print("-" * 50)

    input("press close to exit . . .")


print(symb)
if __name__ == '__main__':
	menu()
