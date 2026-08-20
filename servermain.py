import socket
import threading

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

istemciler = []
kullaniciadlari = []

def duyuru(mesaj):
    for istemci in istemciler:
        istemci.send(mesaj)

def baglantidevamke(istemci):
    stop = False
    while not stop:
        try:
            mesaj = istemci.recv(1024)
            duyuru(mesaj)
        except:
            index = istemciler.index(istemci)
            istemciler.remove(istemci)
            kullaniciadi = kullaniciadlari[index]
            kullaniciadlari.remove(kullaniciadi)
            duyuru(f"{kullaniciadi} sohbetten ayrıldı!".encode('utf-8'))
            stop = True

def main():
    print("Server çalışıyorke...")
    while True:
        istemci, addr = server.accept()
        print(f"{addr}'e bağlanıldı...")
        istemci.send("NICK".encode('utf-8'))
        kullaniciadi = istemci.recv(1024).decode('utf-8')
        kullaniciadlari.append(kullaniciadi)
        istemciler.append(istemci)
        print(f"{addr} 'nin kullanıcı adı {kullaniciadi}")

        istemci.send("Sunucuya bağlandın!\n".encode('utf-8'))
        duyuru(f"{kullaniciadi} sohbete katıldı!".encode('utf-8'))
        thread = threading.Thread(target=baglantidevamke, args=(istemci,))
        thread.start()

if __name__ == '__main__':
    main()



