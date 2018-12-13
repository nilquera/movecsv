import os
import subprocess
from time import sleep
import sys

def main():
    if len(sys.argv) != 3:
        print('python3 move <ORIGIN_PATH> <FINAL_PATH> (full path)')
        return
    opath = sys.argv[1]
    fpath = sys.argv[2]
    files = os.listdir(opath)
    files.sort()
    while len(files) != 0:
        for i in range(4):
            filepath = opath + files[0]
            subprocess.call(['mv', filepath, fpath])
            files.pop(0)
            for f in files:
                print(f)
        sleep(4)

if __name__ == '__main__':
    main()
