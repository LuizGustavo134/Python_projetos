#import time
#import os
#class Cronometro:
    #def __init__(self,segundos=0,minutos=0,horas=0):
       # self.segundos=segundos
      #  self.minutos=minutos
     #   self.horas=horas

        
    #def __repr__(self):
    #    return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}' 
        
   # def incremento(self):
       # self.segundos+=1
      #  if self.segundos>=60:
     #       self.segundos=0
    #        self.minutos+=1
   #     if self.minutos>=60:
  #          self.minutos=0
 #           self.horas+=1
    
#def start(self):
   # while True:
    #       time.sleep(1)
#cronometro1=Cronometro(
#cronometro1.start()
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(
            text='Fala galera!',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return label

# Esse bloco deve estar fora da classe
if __name__ == '__main__':
    app = MainApp()
    app.run()