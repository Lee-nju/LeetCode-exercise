from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
targetAddr = ("127.0.0.1", 8080)

udpSocket.bind(("", 3000))


def main():
    while True:
        msg = input("Enter message: ")
        udpSocket.sendto(msg.encode("utf-8"), targetAddr)


if __name__ == '__main__':
    # main()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j or i + j == 0:
                continue
            print(i, j)
