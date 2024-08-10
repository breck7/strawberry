import os
import time

YELLOW = '\033[93m'
BROWN = '\033[38;5;52m'
RESET = '\033[0m'

def garden(sub_stage=0):
    frame = [
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        f"{BROWN}~~~~~~~~~~~~~~~~{RESET}",
        f"{BROWN}################{RESET}",
        f"{BROWN}################{RESET}",
        f"{BROWN}################{RESET}",
        f"{BROWN}################{RESET}",
        f"{BROWN}################{RESET}"
    ]
    
    if sub_stage < 4:
        frame[sub_stage] = f"      {YELLOW}(q*){RESET}          "
    elif sub_stage == 4:
        frame[4] = f"{BROWN}~~~~~~{YELLOW}(q*){BROWN}~~~~~~{RESET}"
    elif sub_stage == 5:
        frame[5] = f"{BROWN}######{YELLOW}(q*){BROWN}######{RESET}"
    elif sub_stage == 6:
        frame[6] = f"{BROWN}######{YELLOW}(q*){BROWN}######{RESET}"
    elif sub_stage == 7:
        frame[7] = f"{BROWN}######{YELLOW}(q*){BROWN}######{RESET}"
    
    return "\n".join(frame)

def delicious():
    while True:
        for i in range(8):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(garden(i))
            time.sleep(0.5)
        time.sleep(1)

if __name__ == "__main__":
    try:
        delicious()
    except KeyboardInterrupt:
        print("\nAnimation stopped.")
