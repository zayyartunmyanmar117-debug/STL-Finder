import time
import random

def stl_search():
    print("--- Starlink Login Code Searching ---")
    time.sleep(1)
    # 6-digit code တစ်ခုကို random ထုတ်ပေးခြင်း
    code = "".join([str(random.randint(0, 9)) for _ in range(6)])
    print(f"Checking Code: {code} ... [Status: Testing]")
    time.sleep(2)
    print(f"Result: Login Code Found -> {code}")

if __name__ == "__main__":
    stl_search()
