class VeiculoMotorizado:
    def __init__(self, pp, pf, c):
        self.proposito = pp
        self.prefixo = pf
        self.combustivel = c
        
class Aviao(VeiculoMotorizado):
    def __init__(self, id, pp, pl, c, cor, mod, pa):
        super().__init__(pp, pl, c)
        self.idAviao = id
        self.cor = cor
        self.modelo = mod
        self.proibe_animal = pa
        
class Pessoa:
    def __init__(self, id, nome, cpf, rg, idade, pp, bg):
        self.idPessoa = id
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        self.passaporte = pp
        self.bagagem = bg
        
class Passagem:
    def __init__(self, id, idA, idPe, dh, emb, desemb, pol, vp):
        self.idPassagem = id
        self.idAviao = idA
        self.idPessoa = idPe
        self.datahora = dh
        self.embarque = emb
        self.desembarque = desemb
        self.poltrona = pol
        self.valor_passagem = vp
      