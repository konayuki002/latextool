mport msvcrt
import time
import sys

while True:
    time.sleep(0.01)
    if msvcrt.kbhit(): # キーが押されているか
        kb = msvcrt.getch() # 押されていれば、キーを取得する
        print(kb)
        sys.exit()