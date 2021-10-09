'''
    Projeto Final:
        Concepção de Soluções Baseadas em Aplicativos (CSBA)
        Engenharia de Computação - 3° Periodo 
    Integrantes:
        Erick Lemmy dos Santos Oliveira
        Kenny Rossi Torres Teixeira
        Leandro Ricardo Guimaraes
'''
from AirplaneJorneyPass import *
from kivy.uix.screenmanager import ScreenManager, SlideTransition

class telaApp(App):
    def build(self):
        Window.size = (343,660)
        self.registro_atual = None
        self.title = 'Airplane JorneyPass'
        sm = ScreenManager(transition = SlideTransition(direction = "left"))
        sm.add_widget(MainWindow(name = 'main'))
        sm.add_widget(SecondWindow(name = 'second'))
        sm.add_widget(ThirdWindow(name = 'third'))
        sm.add_widget(FourthWindow(name = 'fourth'))
        sm.add_widget(FifthWindow(name = 'fifth'))
        return sm
    
if __name__ == "__main__":
    telaApp().run()