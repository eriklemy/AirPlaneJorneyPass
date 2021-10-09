import sqlite3
from veiculos import Pessoa, Aviao, Passagem

class BancodeDadosAviao_KennyRossi:
    def cadastrarPessoa(self, novaPessoa):
        conn   = sqlite3.connect('db/BancodeDadosAviao_KennyRossi.db')
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO PESSOA(IdPessoa, Nome, CPF, RG, Idade, Passaporte, Bagagem)
                       VALUES (?,?,?,?,?,?,?)
                       """,
                       (novaPessoa.idPessoa, novaPessoa.nome, novaPessoa.cpf, novaPessoa.rg, novaPessoa.idade, novaPessoa.passaporte, novaPessoa.bagagem)
                )
        conn.commit()
        conn.close()

    def cadastrarAviao(self, novoAviao):
        conn = sqlite3.connect('db/BancodeDadosAviao_KennyRossi.db')
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO AVIAO(IdAviao, Proposito, Prefixo, Combustivel, Cor, Modelo, ProibeAnimal)
                       VALUES (?,?,?,?,?,?,?)
                       """,
                       (novoAviao.idAviao, novoAviao.proposito, novoAviao.prefixo, novoAviao.combustivel, novoAviao.cor, novoAviao.modelo, novoAviao.proibe_animal)
                )
        conn.commit()
        conn.close()
    
    def cadastrarPassagem(self, novaPassagem):
        conn = sqlite3.connect('db/BancodeDadosAviao_KennyRossi.db')
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO PASSAGEM(IdPassagem, IdAviao, IdPessoa, DataHora, Embarque, Desembarque, Poltrona, ValorPassagem)
                       VALUES (?,?,?,?,?,?,?,?)
                       """,
                       (novaPassagem.idPassagem, novaPassagem.idAviao, novaPassagem.idPessoa, novaPassagem.datahora, novaPassagem.embarque, novaPassagem.desembarque, novaPassagem.poltrona, novaPassagem.valor_passagem)
                )
        conn.commit()
        conn.close()
        
    def listarPessoaPorId(self, id):
        conn   = sqlite3.connect('db/BancodeDadosAviao_KennyRossi.db')
        cursor = conn.cursor()
        cursor.execute("""
                        SELECT *
                        FROM PESSOA
                        WHERE IdPessoa = ?""",(str(id))
                    )
        registro = cursor.fetchone()
        conn.close()
        if registro != None:
            return Pessoa(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
        else:
            return None
        
    def listarPassagemPorId(self, id):
        conn   = sqlite3.connect('db/BancodeDadosAviao_KennyRossi.db')
        cursor = conn.cursor()
        cursor.execute("""
                        SELECT *
                        FROM PASSAGEM
                        WHERE IdPassagem = ?""",(str(id))
                    )
        registro = cursor.fetchone()
        conn.close()
        if registro != None:
            return Passagem(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
        else:
            return None
    
    def listarAviaoPorId(self, id):
        conn   = sqlite3.connect('db/BancodeDadosAviao_KennyRossi.db')
        cursor = conn.cursor()
        cursor.execute("""
                        SELECT *
                        FROM AVIAO
                        WHERE IdAviao = ?""",(str(id))
                    )
        registro = cursor.fetchone()
        conn.close()
        if registro != None:
            return Aviao(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
        else:
            return None
        
    def Encerrar(self):
        input("Programa Encerrado.")
