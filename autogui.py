# 按键模拟
import pyautogui
import threading,time,signal,sys,random

def press_key(min,max,key):
    while True:
        random_interval = random.uniform(min, max)
        time.sleep(random_interval)
        pyautogui.press(key)
        print(f'key: {key},random: {random_interval}')

def quit(signum, frame):
    print('stop!')
    sys.exit(0)

def o1():
    press_key(60,70,'1')

def o2():
    press_key(2,3,'2')    

def o3():
    press_key(60,70,'3')    

def o4():
    press_key(60*20,60*30,'4')    
        
if __name__ == "__main__":
    time.sleep(10)
    t1 = threading.Thread(target=o1)
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=o2)
    t2.daemon = True
    t2.start()
    t3 = threading.Thread(target=o3)
    t3.daemon = True
    t3.start()
    t4 = threading.Thread(target=o4)
    t4.daemon = True
    t4.start()
    try:
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM,quit)
        while True:         
            pass      
    except KeyboardInterrupt:
        t1.join()
        t2.join()
        t3.join()
        t4.join()