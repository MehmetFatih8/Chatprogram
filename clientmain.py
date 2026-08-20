import socket
import threading
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)



class Chat(App):
    def build(self):



        self.window = FloatLayout()
        #add widgets to window
        #self.window.cols = 1
        #self.window.size_hint = (0.6, 0.7)
        #self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        self.icon
        self.title = "Fatih Chat Programı"
        self.baglanbuton = Button(text="Bağlan", size_hint = (0.3 , 0.1), pos_hint = {'x': 0.65, 'top':0.95}, on_press=lambda a:sunucuya_baglan(self))
        self.window.add_widget(self.baglanbuton)
        self.buton = Button(text="Gönder!", size_hint = (0.4 ,0.1), pos_hint = {'x': 0.55, 'top':0.15},disabled = True, on_press=lambda a:mesajgonder(self) )
        self.window.add_widget(self.buton)
        self.chatgecmisi = TextInput(size_hint = (0.9 , 0.6), multiline = True , readonly = True , disabled = True, pos_hint = {'x': 0.05, 'top':0.80})
        self.window.add_widget(self.chatgecmisi)
        self.mesajgirisi = TextInput(size_hint = (0.48 , 0.15), multiline = True , disabled = True, pos_hint = {'x': 0.05, 'top':0.18}, font_size = 16)
        self.window.add_widget(self.mesajgirisi)

        def chatdegistirme(self, message):
            print("geldim bi ara")
            self.chatgecmisi.text += message + "\n"


        def mesajgonder(self):
            print(self.mesajgirisi.text)
            client.send(f"{kullaniciadi}: {self.mesajgirisi.text}".encode('utf-8'))



        def sunucuya_baglan(self):
            global kullaniciadi
            kullaniciadi = "uzgunMbappe"
            if kullaniciadi != "":
                client.connect(("127.0.0.1", 9999))
                message = client.recv(1024).decode('utf-8')
                if message == "NICK":
                    print("SUNUCUYA BAĞLANDIM")
                    client.send(kullaniciadi.encode('utf-8'))
                    self.buton.disabled = False
                    self.baglanbuton.disabled = True
                    self.mesajgirisi.disabled = False
                    self.chatgecmisi.disabled = False


                    chatdegistirme(self,message)
                    mesajal(self)

        def mesajal(self):
            dur = 0
            while dur == 0:
                try:
                    message = client.recv(1024).decode('utf-8')
                    dur = 1
                    chatdegistirme(self,message)
                    #mesajal(self)
                except:
                    pass






        return self.window




if __name__ == "__main__":
    Chat().run()