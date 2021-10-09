import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window
from kivy.properties import NumericProperty 
from kivy.uix.screenmanager import Screen
from veiculos import Pessoa, Aviao, Passagem
from controler import BancodeDadosAviao_KennyRossi

from kivy.config import Config
Config.set('graphics', 'multisamples', 0)

# # caso necessario
# import os
# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# import os
# os.environ ["KIVY_AUDIO"] ="sdl2"

Window.clearcolor = (0,210,173,1)

class MainWindow(Screen):
    def sair(self):
        App.get_running_app().stop()
        
class SecondWindow(BoxLayout, Screen):
    def sair(self):
        App.get_running_app().stop()

class ThirdWindow(BoxLayout, Screen):
    id = NumericProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.limpar()

    def limpar(self):
        self.ids.pp.text  = 'Propósito'
        self.ids.pf.text  = 'Prefixo'
        self.ids.c.text   = 'Combustível'
        self.ids.cor.text = 'Coloração'
        self.ids.mod.text = 'Modelo'
        self.ids.pa.text  = 'Há a Permissão de Animais?'
    
    def sair(self):
        App.get_running_app().stop()
    
    def criar(self):
        App.get_running_app().registro_atual = None
        db = BancodeDadosAviao_KennyRossi()
        if App.get_running_app().registro_atual == None: 
            aviao = Aviao(None, 
                            self.ids.pp.text, 
                            self.ids.pf.text, 
                            self.ids.c.text,
                            self.ids.cor.text,
                            self.ids.mod.text,
                            self.ids.pa.text,
                         )
            db.cadastrarAviao(aviao)
            self.ids.mensagem.text = '[b]Aviao CADASTRADO com SUCESSO!![/b]'
        else:
            self.ids.mensagem.text = '[b]Aviao NAO CADASTRADO!![/b]'

class FourthWindow(BoxLayout, Screen):
    id = NumericProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.limpar()
    
    def limpar(self):
        self.ids.nome.text  = 'Nome'
        self.ids.cpf.text   = 'CPF'
        self.ids.rg.text    = 'RG'
        self.ids.idade.text = 'Idade'
        self.ids.pp.text    = 'Passaporte'
        self.ids.bg.text    = 'Possui bagagem'

    def sair(self):
        App.get_running_app().stop()
        
    def criar(self):
        App.get_running_app().registro_atual = None
        db = BancodeDadosAviao_KennyRossi()
        if App.get_running_app().registro_atual == None:
            pessoa = Pessoa(None, 
                            self.ids.nome.text, 
                            self.ids.cpf.text, 
                            self.ids.rg.text,
                            self.ids.idade.text,
                            self.ids.pp.text,
                            self.ids.bg.text,
                         )
            db.cadastrarPessoa(pessoa)
            self.ids.mensagem.text = '[b]Pessoa CADASTRADA com SUCESSO!![/b]'
        else:
            self.ids.mensagem.text = '[b]Pessoa NAO CADASTRADA!![/b]'
        
class FifthWindow(BoxLayout, Screen):
    id = NumericProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.limpar()
    
    def limpar(self):
        self.ids.idA.text    = 'Identificação do Avião'
        self.ids.idPe.text   = 'Identificação do Passageiro'
        self.ids.dh.text     = 'Data e Hora'
        self.ids.emb.text    = 'Local de Embarque'
        self.ids.desemb.text = 'Local de Desembarque'
        self.ids.pol.text    = 'Número da Poltrona'
        self.ids.vp.text     = 'Valor da Passagem'

    def sair(self):
        App.get_running_app().stop()
        
    def criar(self):
        App.get_running_app().registro_atual = None
        db = BancodeDadosAviao_KennyRossi()
        if App.get_running_app().registro_atual == None:
            passagem = Passagem(None, 
                            self.ids.idA.text, 
                            self.ids.idPe.text, 
                            self.ids.dh.text,
                            self.ids.emb.text,
                            self.ids.desemb.text,
                            self.ids.pol.text,
                            self.ids.vp.text,
                         )
            db.cadastrarPassagem(passagem)
            self.ids.mensagem.text = '[b]Passagem CADASTRADA com SUCESSO!![/b]'
        else:
            self.ids.mensagem.text = '[b]Passagem NAO CADASTRADA!![/b]'
            
