import threading
from threading import Thread


def nanda():
    threads = [Thread(target=line2, args=(['Nanjing university'],)),
               Thread(target=taxi, args=(['Nanjing university'],))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def line2(route: [str]):
    threads = [Thread(target=line1, args=([*route, 'Metro line 2'],)),
               Thread(target=line3, args=([*route, 'Metro line 2'],))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def line3(route: [str]):
    nanjingnan([*route, 'Metro line 3'])


def line1(route: [str]):
    nanjingnan([*route, 'Metro line 1'])


def taxi(route: [str]):
    nanjingnan([*route, 'take by taxi'])


def nanjingnan(route: [str]):
    route.append('NanJingNan railway station !')
    print(*route, sep=' -> ')


if __name__ == '__main__':
    nanda()
