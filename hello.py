from kivy.app import App
from kivy.uix.button import Button
class MyApp (App):
    def build(self):
        return Button(Text="Olá mundo, Este é o meu primeiro progama no kivy \n Eu sou uma estudande do SESI e eu mo o professor")
    if __name__ == ' __main__':
     MyApp (). run()