class Cliente:
    def __init__(self,n,fone):
        self.nome= n
        self.telefone = fone

        #metodo get vai lê o valor interno do objeto e envia-lo como retorno da função
    def get_nome(self):
        return self.nome
    # o metodo set recebe o valor e muda ele com base nos paramêtros
    def set_nome(self,nome):
        self._nome = nome