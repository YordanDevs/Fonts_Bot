import requests
from bs4 import BeautifulSoup
import sys
import os
import random
import time
import urllib3
import base64
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
totaldown = 0
timed = 0
named = "INDEFINIDO"
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Yi', suffix)
def clear_console():
    os.system("clear")
def download(url, name, up, total_size):
    downloaded = 0
    global totaldown
    global timed
    global named
    try:
        with up.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}, stream=True) as r:
            r.raise_for_status()
            with open(name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        downloaded += 8192
                        totaldown += 8192
                        porcentaje = (totaldown/int(total_size))*100
                        s = round(time.time() - timed)
                        spaces = 17
                        rest = 100/spaces
                        barra = "  \033[32m|\033[0m\033[0m\033[1m\033[30m"+"\033[42m•"*round(porcentaje/rest)+"\033[40m•"*round((100-porcentaje)/rest)+f"\033[0m\033[1m {round(porcentaje,1)}% | {sizeof_fmt(totaldown)}     "
                        print(barra, end="\r")
                        f.write(chunk)
    except:
        print("\n  \033[31m\033[1m|\033[0m\033[41m\033[30m\033[1m + ERROR - CONEXIÓN PERDIDA + \033[0m")
        sys.exit()
directory = "."
url = input('BitZero URL >> ')
url = url.replace("bitzero ", "")
url = url.split(" &&")[0]
print("  \033[1m\033[33m|\033[30m\033[43m + PREPARANDO + \033[0m")
named = url.split("/")[-1]
surl = url.split("/")[-4]
key = url.split("/")[-2]
key = key.split("-")
host = base64.b64decode(key[0].replace("@","==").replace("#","=")).decode("utf-8")
username = base64.b64decode(key[1].replace("@","==").replace("#","=")).decode("utf-8")
password = base64.b64decode(key[2].replace("@","==").replace("#","=")).decode("utf-8")
repo = base64.b64decode(key[3].replace("@","==").replace("#","=")).decode("utf-8")
bitzero = url.split("/")[-3]
k = url.split("/")[-5]
size = k.split("-")[0]
ide = k.split("-")[1]
if "-" in surl:
    urls = surl.split("-")
else:
    urls = [surl]
urla = []
for url in urls:
    urla.append(f"{host}/$$$call$$$/api/file/file-api/download-file?submissionFileId={url}&submissionId={repo}&stageId=1")
urls = urla
index = 0
ide = random.randint(1000,9999)
files = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
up = requests.Session()
getToken = up.get(host+"/login",headers=headers,verify=False)
token = BeautifulSoup(getToken.text,"html.parser").find('input',{'name':'csrfToken'})
login_data = {"password": password,"remember": 1,"source": "","username": username,"csrfToken":token}
login_response = up.post(f"{host}/login/signIn", params=login_data, headers=headers,verify=False)
timed = time.time()
clear_console()
if len(named) > 10:
    namede = named[:7]+"..."
else:
    namede = named
print("  \033[32m|\033[0m\033[1m\033[42m\033[30m + DESCARGANDO + \033[0m "+namede+" | "+str(sizeof_fmt(int(size))))
for url in urls:
    if not url == "":
        download(url,"index_"+str(ide)+"_"+str(index), up, size)
        files.append("index_"+str(ide)+"_"+str(index))
        index += 1
print("\n")
with open(directory+"/"+named, "wb") as file:
    for f in files:
        if bitzero == '1':
            file.write(open(f, "rb").read().replace(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xf6\x178U\x00\x00\x00\x00IEND\xaeB`\x82",b''))
        elif bitzero == '2':
            file.write(base64.b64decode(open(f, "r").read().replace('<!DOCTYPE html>\n<html lang="es">\n<bytes>','').replace('</bytes></html>','')))
        os.unlink(f)
clear_console()
print("\033[32mGUARDADO:\033[0m"+directory+"/"+named)