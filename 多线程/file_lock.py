from threading import Thread
import threading
import os
import time


def writeFile(s: str):
    with open('file.txt', 'a+') as fp:
        fp.write(s)


def readFile():
    with open('file.txt', 'r') as fp:
        lines = fp.readline()
        return lines


mu = threading.Lock()


def lock_file(s):
    if mu.acquire(True):
        writeFile(s)
        mu.release()

    if mu.acquire(True):
        print(readFile())
        mu.release()


if __name__ == '__main__':
    with open('file.txt', 'w') as fp:
        pass
    s = ['hello\n', 'world\n', 'Lee\n', 'come here!\n', 'hello\n', 'world\n', 'Lee\n', 'come here!\n', 'hello\n',
         'world\n', 'Lee\n', 'come here!\n']
    for i in range(len(s)):
        Thread(target=lock_file, args=(s[i],)).start()
